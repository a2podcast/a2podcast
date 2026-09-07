#!/usr/bin/env python3
"""
A2 Podcast — test-site.py
Suite di test automatici per verificare che tutte le modifiche al sito
siano corrette: YouTube player, SEO, schema.org, meta tag, CSP.

Utilizzo:
    python3 scripts/test-site.py          # build + test completi
    python3 scripts/test-site.py --no-build  # salta la build Hugo, usa public/ esistente
    python3 scripts/test-site.py --port 1315 # usa una porta specifica

Eseguire dalla cartella a2podcast/.
"""

import argparse
import csv
import glob
import html as html_module
import io
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Hugo richiede oggi Python moderno nel progetto
    tomllib = None

import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EPISODES_DIR = os.path.join(PROJECT_ROOT, "content", "episodi")
HUGO_BIN = os.environ.get("HUGO_BIN", "hugo")

# Episodi noti senza live YouTube
NO_YOUTUBE = {40, 44, 66, 77}

# ── Colori ANSI ──────────────────────────────────────────────────────────────
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ── Stato globale ─────────────────────────────────────────────────────────────
results = []


def ok(label: str):
    results.append(True)
    print(f"  {GREEN}✓{RESET} {label}")


def fail(label: str, detail: str = ""):
    results.append(False)
    msg = f"  {RED}✗{RESET} {label}"
    if detail:
        msg += f"\n    {YELLOW}→ {detail}{RESET}"
    print(msg)


def section(n: int, total: int, title: str):
    print(f"\n{BOLD}[{n}/{total}] {title}{RESET}")


# ── Hugo helpers ──────────────────────────────────────────────────────────────

def run_build() -> bool:
    """Run a clean production-equivalent Hugo build and return its output."""
    print("  Esecuzione: hugo --gc --minify --cleanDestinationDir ...")
    result = subprocess.run(
        [HUGO_BIN, "--gc", "--minify", "--cleanDestinationDir"],
        cwd=PROJECT_ROOT,
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stdout + result.stderr


def list_future_publish_targets() -> tuple[list[tuple[str, str]], str]:
    """Return Hugo future pages and their expected files below public/."""
    result = subprocess.run(
        [HUGO_BIN, "list", "future"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return [], result.stdout + result.stderr

    targets = []
    for row in csv.DictReader(io.StringIO(result.stdout)):
        permalink = row.get("permalink", "")
        path = unquote(urlparse(permalink).path)
        if not path:
            continue

        relative_path = path.lstrip("/")
        if path.endswith("/"):
            relative_path = os.path.join(relative_path, "index.html")

        targets.append(
            (
                row.get("path", permalink),
                os.path.join(PROJECT_ROOT, "public", relative_path),
            )
        )

    return targets, ""


def latest_published_episode_number() -> tuple[int | None, str]:
    """Return the episode number with the newest published date according to Hugo."""
    result = subprocess.run(
        [HUGO_BIN, "list", "published"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None, result.stdout + result.stderr

    episodes = [
        row
        for row in csv.DictReader(io.StringIO(result.stdout))
        if row.get("kind") == "page" and row.get("section") == "episodi"
    ]
    if not episodes:
        return None, "nessun episodio pubblicato restituito da Hugo"

    latest = max(episodes, key=lambda row: datetime.fromisoformat(row["date"]))
    try:
        return int(latest["slug"]), ""
    except (KeyError, TypeError, ValueError):
        return None, f"slug episodio non valido: {latest.get('slug')!r}"


def start_server(port: int) -> subprocess.Popen:
    proc = subprocess.Popen(
        [HUGO_BIN, "server", "--port", str(port), "--disableLiveReload", "--renderToMemory"],
        cwd=PROJECT_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    # Wait for server to be ready
    base = f"http://localhost:{port}"
    for _ in range(20):
        try:
            r = requests.get(base, timeout=1)
            if r.status_code < 500:
                return proc
        except requests.ConnectionError:
            pass
        time.sleep(0.5)
    proc.terminate()
    print(f"{RED}ERRORE: hugo server non si è avviato sulla porta {port}{RESET}", file=sys.stderr)
    sys.exit(1)


# ── HTTP helpers ──────────────────────────────────────────────────────────────

def fetch(base_url: str, path: str) -> requests.Response:
    return requests.get(base_url + path, timeout=10, allow_redirects=True)


def fetch_direct(base_url: str, path: str) -> requests.Response:
    """Fetch without following redirects (needed to test their actual status/target)."""
    return requests.get(base_url + path, timeout=15, allow_redirects=False)


def tag_attributes(tag: str) -> dict[str, str]:
    """Parse the simple quoted or unquoted attributes emitted by minified Hugo."""
    attrs = {}
    pattern = r"([:\w-]+)(?:\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+)))?"
    for match in re.finditer(pattern, tag):
        key = match.group(1).lower()
        attrs[key] = next((value for value in match.groups()[1:] if value is not None), "")
    return attrs


def attribute_values(html: str, attribute: str) -> list[str]:
    """Return quoted and unquoted values for an HTML attribute."""
    values = []
    pattern = rf"\b{re.escape(attribute)}\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+))"
    for match in re.finditer(pattern, html, re.I):
        values.append(next(value for value in match.groups() if value is not None))
    return values


def meta_content(html: str, key: str) -> str | None:
    """Return a meta value regardless of name/property and attribute order."""
    for tag in re.findall(r"<meta\b[^>]*>", html, re.IGNORECASE):
        attrs = tag_attributes(tag)
        if attrs.get("name") == key or attrs.get("property") == key:
            return html_module.unescape(attrs.get("content", ""))
    return None


def canonical_url(html: str) -> str | None:
    for tag in re.findall(r"<link\b[^>]*>", html, re.IGNORECASE):
        attrs = tag_attributes(tag)
        if "canonical" in attrs.get("rel", "").lower().split():
            return html_module.unescape(attrs.get("href", ""))
    return None


def rss_autodiscovery_urls(html: str) -> list[str]:
    urls = []
    for tag in re.findall(r"<link\b[^>]*>", html, re.IGNORECASE):
        attrs = tag_attributes(tag)
        if (
            "alternate" in attrs.get("rel", "").lower().split()
            and attrs.get("type", "").lower() == "application/rss+xml"
        ):
            urls.append(html_module.unescape(attrs.get("href", "")))
    return urls


def generated_path_for_url(path: str) -> Path:
    """Map a canonical site URL path to its expected file below public/."""
    clean = unquote(path).split("?", 1)[0]
    relative = clean.lstrip("/")
    if not relative or clean.endswith("/"):
        relative = os.path.join(relative, "index.html")
    return Path(PROJECT_ROOT, "public", relative)


def load_episode_frontmatter(path: str) -> dict:
    """Read TOML front matter without interpreting the Markdown body."""
    if tomllib is None:
        raise RuntimeError("tomllib non disponibile")
    text = Path(path).read_text(encoding="utf-8")
    match = re.match(r"\+\+\+\s*\n(.*?)\n\+\+\+", text, re.DOTALL)
    if not match:
        raise ValueError(f"front matter TOML non trovato in {path}")
    return tomllib.loads(match.group(1))


def normalized_episode_title(title: str) -> str:
    """Mirror the repository-wide title-prefix normalization contract."""
    return re.sub(r"^(?:(?:ep(?:isode)?\.?\s*)?\d+\s*[:.-]\s*)", "", title, flags=re.I).strip()


def html_unescape_all(value: str) -> str:
    """Decode nested HTML entities defensively for text comparisons."""
    previous = value
    for _ in range(3):
        decoded = html_module.unescape(previous)
        if decoded == previous:
            break
        previous = decoded
    return previous


def parse_jsonld(html: str) -> list[dict]:
    """Extract and parse all JSON-LD script blocks from HTML."""
    blocks = []
    for match in re.finditer(r'<script\b([^>]*)>(.*?)</script>', html, re.DOTALL | re.I):
        if tag_attributes(match.group(1)).get("type", "").lower() != "application/ld+json":
            continue
        try:
            blocks.append(json.loads(match.group(2)))
        except json.JSONDecodeError:
            pass
    return blocks


def find_jsonld(blocks: list[dict], type_: str) -> dict | None:
    return next((b for b in blocks if b.get("@type") == type_), None)


# ── Test groups ───────────────────────────────────────────────────────────────

def test_build(build: bool) -> int:
    section(1, 12, "Build Hugo")
    if not build:
        print(f"  {YELLOW}(build saltata, uso public/ esistente){RESET}")
        pub = os.path.join(PROJECT_ROOT, "public")
        if os.path.isdir(pub):
            ok("cartella public/ presente")
        else:
            fail("cartella public/ non trovata — esegui senza --no-build")
        return

    success, output = run_build()
    if success:
        ok("hugo build completato senza errori")
    else:
        fail("hugo build fallita", output[-300:])
        return

    # Il numero dipende dai contenuti pubblicati e dagli output configurati: non
    # codifichiamo soglie storiche GSC o conteggi precedenti del repository.
    m = re.search(r'Pages\s+│\s+(\d+)', output)
    if m:
        n = int(m.group(1))
        if n > 0:
            ok(f"{n} pagine generate")
        else:
            fail("Hugo non ha generato pagine")
    else:
        fail("conteggio pagine non trovato nell'output")

    sitemap = os.path.join(PROJECT_ROOT, "public", "sitemap.xml")
    if os.path.exists(sitemap):
        ok("public/sitemap.xml presente")
    else:
        fail("public/sitemap.xml non trovata")

    future_targets, future_error = list_future_publish_targets()
    if future_error:
        fail("impossibile elencare le pagine future con Hugo", future_error[-300:])
    else:
        published_early = [source for source, target in future_targets if os.path.exists(target)]
        if published_early:
            fail(
                "pagine future pubblicate prima della data prevista",
                ", ".join(published_early),
            )
        elif future_targets:
            ok(f"{len(future_targets)} pagine future escluse dalla build corrente")
        else:
            ok("nessuna pagina futura indicata da Hugo")


def test_homepage(base: str):
    section(2, 12, "Homepage")
    r = fetch(base, "/")
    if r.status_code == 200:
        ok("HTTP 200 /")
    else:
        fail(f"HTTP {r.status_code} /")
        return

    html = r.text

    # Buttons
    if 'btn-yt' in html and 'youtube.com/@a2podcast688' in html:
        ok("bottone ▶ YouTube presente con URL canale")
    else:
        fail("bottone YouTube mancante o URL errato")

    if 'applePodcastsUrl' in html or 'podcasts.apple.com' in html:
        ok("link Apple Podcasts presente")
    else:
        fail("link Apple Podcasts non trovato")

    # Title
    m = re.search(r'<title>(.*?)</title>', html)
    if m and m.group(1).strip() == "A2 Podcast — Tecnologia Apple per professionisti":
        ok("<title> homepage corretto")
    else:
        fail("<title> non corrisponde", m.group(1) if m else "non trovato")

    # Meta description
    m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', html)
    if m and len(m.group(1)) > 20:
        ok("meta description presente")
    else:
        fail("meta description mancante o troppo corta")

    # JSON-LD PodcastSeries
    blocks = parse_jsonld(html)
    series = find_jsonld(blocks, "PodcastSeries")
    if series:
        ok("JSON-LD PodcastSeries presente e valido")
        n = series.get("numberOfEpisodes")
        if isinstance(n, int) and n > 0:
            ok(f"numberOfEpisodes = {n}")
        else:
            fail("numberOfEpisodes mancante o non intero", str(n))
            n = None

        # Confronto con il numero reale di episodi pubblicati: contiamo i <loc> della
        # sitemap che puntano a un URL episodio (permalink numerico "/NN/"), perché
        # la sitemap riflette la build già filtrata (draft/data futura) esattamente
        # come .Site.RegularPages usato dal template — più affidabile di riparsare
        # a mano il frontmatter (draft, data futura, fuso orario) in questo script.
        sitemap_path = os.path.join(PROJECT_ROOT, "public", "sitemap.xml")
        if n is not None and os.path.exists(sitemap_path):
            with open(sitemap_path, encoding="utf-8") as f:
                sitemap_xml = f.read()
            episode_locs = re.findall(r'<loc>https?://[^<]+/(\d+)/</loc>', sitemap_xml)
            if len(episode_locs) == n:
                ok(f"numberOfEpisodes coerente con la sitemap ({len(episode_locs)} episodi)")
            else:
                fail(
                    "numberOfEpisodes non coerente con la sitemap",
                    f"schema={n}, sitemap={len(episode_locs)}"
                )
        else:
            fail("impossibile verificare numberOfEpisodes: sitemap.xml non trovata")
    else:
        fail("JSON-LD PodcastSeries non trovato")

    # Canonical
    if 'rel="canonical"' in html:
        ok("canonical presente")
    else:
        fail("canonical mancante")

    # Ultimo episodio: Hugo deve scegliere la pagina pubblicata più recente e
    # riusare lo stesso player Spreaker della relativa pagina episodio. La
    # lista published di Hugo applica lo stesso filtro per draft e date future.
    featured = re.search(
        r'<section class="featured-episode" data-episode-number="(\d+)".*?</section>',
        html,
        re.DOTALL,
    )
    if not featured:
        fail("sezione ultimo episodio con player non trovata in homepage")
        return

    featured_html = featured.group(0)
    expected_number, latest_error = latest_published_episode_number()
    if expected_number is None:
        fail("impossibile determinare l'ultimo episodio pubblicato", latest_error)
        return
    actual_number = int(featured.group(1))
    if actual_number == expected_number:
        ok(f"ultimo episodio pubblicato selezionato dinamicamente: Ep. {actual_number}")
    else:
        fail(
            "episodio in evidenza non è l'ultimo pubblicato",
            f"homepage={actual_number}, atteso={expected_number}",
        )

    episode_response = fetch(base, f"/{expected_number}/")
    episode_player = re.search(
        r'widget\.spreaker\.com/player\?episode_id=(\d+)', episode_response.text
    )
    featured_player = re.search(
        r'widget\.spreaker\.com/player\?episode_id=(\d+)', featured_html
    )
    if (
        episode_player
        and featured_player
        and featured_player.group(1) == episode_player.group(1)
    ):
        ok(f"player homepage usa l'ID Spreaker dell'Ep. {expected_number}")
    else:
        fail("player homepage non coincide con il player dell'ultimo episodio")

    if 'title="Ascolta ' in featured_html and 'loading="lazy"' in featured_html:
        ok("iframe dell'ultimo episodio ha titolo accessibile e caricamento lazy")
    else:
        fail("iframe homepage privo di titolo accessibile o loading lazy")

    if 'class="featured-episode-card"' in featured_html:
        ok("ultimo episodio racchiuso nella card in evidenza")
    else:
        fail("card dell'ultimo episodio mancante")

    if "hide-logo=true" in featured_html:
        ok("player homepage senza branding Spreaker duplicato")
    else:
        fail("player homepage ripete il branding Spreaker")

    if "Il podcast è attualmente in pausa" not in html:
        ok("avviso obsoleto sulla pausa rimosso dalla homepage")
    else:
        fail("avviso obsoleto sulla pausa ancora presente in homepage")

    if html.find('class="featured-episode"') < html.find('class="pause-notice"'):
        ok("player dell'ultimo episodio precede il carosello evergreen")
    else:
        fail("player dell'ultimo episodio non precede il carosello evergreen")

    css = fetch(base, "/css/style.css").text
    featured_css = re.search(r'\.featured-episode\s*\{(.*?)\}', css, re.DOTALL)
    if featured_css and re.search(
        r'border-top:\s*3px\s+solid\s+var\(--color-brand\)', featured_css.group(1)
    ):
        ok("linea rossa sopra il player presente")
    else:
        fail("linea rossa sopra il player non trovata nel CSS")

    if ".featured-episode-card" in css and "grid-template-columns" in css:
        ok("card in evidenza con layout desktop a due colonne presente")
    else:
        fail("layout desktop a due colonne della card mancante")


def test_episode_with_youtube(base: str):
    section(3, 12, "Episodio CON YouTube (Ep. 74 — Andrea Ciraolo)")
    r = fetch(base, "/74/")
    if r.status_code == 200:
        ok("HTTP 200 /74/")
    else:
        fail(f"HTTP {r.status_code} /74/")
        return

    html = r.text
    YT_ID = "KFNWIq5vjTc"

    # YouTube player section
    if 'class="episode-youtube"' in html:
        ok('sezione <div class="episode-youtube"> presente')
    else:
        fail('sezione episode-youtube non trovata')

    if f"youtube-nocookie.com/embed/{YT_ID}" in html:
        ok(f"embed YouTube con ID {YT_ID} corretto")
    else:
        fail("embed YouTube mancante o errato")

    if f"i.ytimg.com/vi/{YT_ID}/maxresdefault.jpg" in html:
        ok("thumbnail YouTube presente")
    else:
        fail("thumbnail YouTube non trovata")

    if f"youtube-nocookie.com/embed/{YT_ID}" in html:
        ok("iframe youtube-nocookie.com presente")
    else:
        fail("iframe youtube-nocookie.com non trovato")

    # Spreaker player still present
    if 'class="audio-player"' in html:
        ok("player Spreaker ancora presente")
    else:
        fail("player Spreaker scomparso")

    # JSON-LD
    blocks = parse_jsonld(html)
    ep = find_jsonld(blocks, "PodcastEpisode")
    if ep:
        ok("JSON-LD PodcastEpisode presente")

        # duration ISO 8601
        media = ep.get("associatedMedia", {})
        dur = media.get("duration", "")
        if re.match(r'^PT\d+H\d+M\d+S$|^PT\d+M\d+S$', dur):
            ok(f"duration ISO 8601: {dur}")
        else:
            fail("duration non in formato ISO 8601", dur)

        # VideoObject
        video = ep.get("video", {})
        video_urls = " ".join(str(video.get(key, "")) for key in ("url", "contentUrl", "embedUrl"))
        if video.get("@type") == "VideoObject" and YT_ID in video_urls:
            ok("JSON-LD VideoObject presente con ID corretto")
        else:
            fail("JSON-LD VideoObject mancante o errato", str(video))

        # datePublished / uploadDate in ISO 8601 con fuso orario
        ISO_TZ = r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}$'
        date_published = ep.get("datePublished", "")
        if re.match(ISO_TZ, date_published):
            ok(f"datePublished ISO 8601 con fuso: {date_published}")
        else:
            fail("datePublished non in formato ISO 8601 con fuso", date_published)

        upload_date = video.get("uploadDate", "")
        if re.match(ISO_TZ, upload_date):
            ok(f"VideoObject.uploadDate ISO 8601 con fuso: {upload_date}")
        else:
            fail("VideoObject.uploadDate non in formato ISO 8601 con fuso", upload_date)

        # VideoObject.name senza prefisso numerico "NN: "
        video_name = video.get("name", "")
        if video_name and not re.match(r'^\d+:\s*', video_name):
            ok(f"VideoObject.name senza prefisso numerico: {video_name!r}")
        else:
            fail("VideoObject.name contiene ancora il prefisso numerico", video_name)

        # nessun residuo di htmlEscape (&#...) nei campi stringa del JSON-LD
        def find_html_escape_residue(obj, path=""):
            if isinstance(obj, str):
                return [path] if "&#" in obj else []
            if isinstance(obj, dict):
                found = []
                for k, v in obj.items():
                    found += find_html_escape_residue(v, f"{path}.{k}")
                return found
            if isinstance(obj, list):
                found = []
                for i, v in enumerate(obj):
                    found += find_html_escape_residue(v, f"{path}[{i}]")
                return found
            return []

        residue = find_html_escape_residue(ep)
        if not residue:
            ok("nessun residuo &# (htmlEscape) nel JSON-LD PodcastEpisode")
        else:
            fail("trovato residuo &# nel JSON-LD (atteso jsonify)", ", ".join(residue[:10]))
    else:
        fail("JSON-LD PodcastEpisode non trovato")

    # BreadcrumbList
    bc = find_jsonld(blocks, "BreadcrumbList")
    if bc and len(bc.get("itemListElement", [])) == 3:
        ok("BreadcrumbList con 3 livelli presente")
    else:
        fail("BreadcrumbList mancante o incompleto")

    # Meta tags SEO
    if 'property="article:published_time"' in html:
        ok("article:published_time presente")
    else:
        fail("article:published_time mancante")

    m = re.search(r'twitter:creator.*?content="([^"]+)"', html)
    if m and "@StrozziFilippo" in m.group(1):
        ok("twitter:creator = @StrozziFilippo")
    else:
        fail("twitter:creator mancante o errato", m.group(1) if m else "non trovato")

    if 'preconnect" href="https://widget.spreaker.com"' in html:
        ok("preconnect Spreaker presente")
    else:
        fail("preconnect Spreaker mancante")

    # OG image dimensions (use flexible pattern: attribute order may vary + extra spaces)
    if re.search(r'og:image:width"\s+content="1400"', html):
        ok("og:image:width = 1400")
    else:
        fail("og:image:width mancante o errato")

    if re.search(r'og:image:height"\s+content="1400"', html):
        ok("og:image:height = 1400")
    else:
        fail("og:image:height mancante o errato")


def test_episode_without_youtube(base: str):
    section(4, 12, "Episodio SENZA YouTube (Ep. 40 — WWDC 2022)")
    r = fetch(base, "/40/")
    if r.status_code == 200:
        ok("HTTP 200 /40/")
    else:
        fail(f"HTTP {r.status_code} /40/")
        return

    html = r.text

    if 'class="episode-youtube"' not in html:
        ok("sezione YouTube assente (corretto)")
    else:
        fail("sezione YouTube presente ma non dovrebbe esserci")

    if "data-ytid" not in html:
        ok("data-ytid assente (corretto)")
    else:
        fail("data-ytid presente ma non dovrebbe esserci")

    if 'class="audio-player"' in html:
        ok("player Spreaker presente")
    else:
        fail("player Spreaker non trovato")

    blocks = parse_jsonld(html)
    ep = find_jsonld(blocks, "PodcastEpisode")
    if ep:
        if "video" not in ep:
            ok("JSON-LD senza VideoObject (corretto)")
        else:
            fail("JSON-LD ha VideoObject ma non dovrebbe")
    else:
        fail("JSON-LD PodcastEpisode non trovato")


def test_aux_pages(base: str):
    section(5, 12, "Pagine ausiliarie")

    for path, expected_status, check_text in [
        ("/episodi/", 200, "Episodi"),
        ("/about/",   200, "Filippo"),
        ("/ospiti/",  200, None),
    ]:
        r = fetch(base, path)
        if r.status_code == expected_status:
            ok(f"HTTP {expected_status} {path}")
        else:
            fail(f"HTTP {r.status_code} {path} (atteso {expected_status})")
        if check_text and check_text not in r.text:
            fail(f"testo '{check_text}' non trovato in {path}")
        elif check_text:
            ok(f"contenuto '{check_text}' trovato in {path}")

    # 404
    r = fetch(base, "/pagina-inesistente-xyz-abc/")
    if r.status_code == 404:
        ok("HTTP 404 per pagina inesistente")
    else:
        fail(f"pagina inesistente ritorna HTTP {r.status_code} invece di 404")

    # RSS autodiscovery su homepage
    r = fetch(base, "/")
    if 'application/rss+xml' in r.text:
        ok("RSS autodiscovery presente in homepage")
    else:
        fail("RSS autodiscovery mancante")


def test_seo_head(base: str):
    section(6, 12, "SEO — head.html")
    r = fetch(base, "/74/")
    html = r.text

    def has_meta(html, name_or_prop, value):
        pattern = rf'(?:name|property)="{re.escape(name_or_prop)}"\s+content="{re.escape(value)}"'
        return bool(re.search(pattern, html))

    checks = [
        (lambda h: 'rel="canonical"' in h,                          "canonical presente"),
        (lambda h: has_meta(h, "og:image:width",  "1400"),          "og:image:width = 1400"),
        (lambda h: has_meta(h, "og:image:height", "1400"),          "og:image:height = 1400"),
        (lambda h: has_meta(h, "og:locale",       "it_IT"),         "og:locale = it_IT"),
        (lambda h: has_meta(h, "twitter:card",    "summary_large_image"), "twitter:card = summary_large_image"),
        (lambda h: has_meta(h, "twitter:site",    "@a2podcast"),    "twitter:site = @a2podcast"),
    ]
    for check_fn, label in checks:
        (ok if check_fn(html) else fail)(label)


def test_frontmatter():
    section(7, 12, "Integrità frontmatter")
    ep_dirs = sorted(
        d for d in glob.glob(os.path.join(EPISODES_DIR, "*"))
        if os.path.isdir(d) and os.path.basename(d).isdigit()
    )

    with_yt = []
    without_yt = []
    missing_tags = []
    missing_transcript = []

    for d in ep_dirs:
        ep_num = int(os.path.basename(d))
        path = os.path.join(d, "index.md")
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()

        if re.search(r'youtubeId\s*=\s*"[^"]+"', content):
            with_yt.append(ep_num)
        else:
            without_yt.append(ep_num)

        if not re.search(r'^tags\s*=\s*\[', content, re.MULTILINE):
            missing_tags.append(ep_num)

        if not re.search(r'hasTranscript\s*=', content):
            missing_transcript.append(ep_num)

    # youtubeId count
    if len(with_yt) >= 70:
        ok(f"{len(with_yt)} episodi con youtubeId (≥ 70)")
    else:
        fail(f"solo {len(with_yt)} episodi con youtubeId (attesi ≥ 70)")

    # episodi senza YouTube attesi
    unexpected_yt = [n for n in NO_YOUTUBE if n in with_yt]
    missing_no_yt  = [n for n in NO_YOUTUBE if n not in without_yt]
    if not unexpected_yt:
        ok(f"ep. {sorted(NO_YOUTUBE)} correttamente senza youtubeId")
    else:
        fail(f"episodi {unexpected_yt} hanno youtubeId ma non dovrebbero")

    # tags
    if not missing_tags:
        ok("tutti gli episodi hanno tags")
    else:
        fail(f"episodi senza tags: {missing_tags[:10]}")

    # hasTranscript
    if not missing_transcript:
        ok("tutti gli episodi hanno hasTranscript")
    else:
        fail(f"episodi senza hasTranscript: {missing_transcript[:10]}")


def test_generated_markup():
    section(8, 12, "Markup generato")
    html_paths = glob.glob(os.path.join(PROJECT_ROOT, "public", "**", "*.html"), recursive=True)
    bad_href = []
    bad_content_url = []

    for path in html_paths:
        with open(path, encoding="utf-8") as f:
            html = f.read()
        rel = os.path.relpath(path, PROJECT_ROOT)
        if re.search(r'href\s*=\s*""', html):
            bad_href.append(rel)
        if re.search(r'"contentUrl"\s*:\s*""', html):
            bad_content_url.append(rel)

    if not bad_href:
        ok('nessun href="" nelle pagine generate')
    else:
        fail('trovati href="" nelle pagine generate', ", ".join(bad_href[:10]))

    if not bad_content_url:
        ok('nessun "contentUrl": "" nelle pagine generate')
    else:
        fail('trovati "contentUrl": "" nelle pagine generate', ", ".join(bad_content_url[:10]))


def test_sitemap_video():
    section(9, 12, "Sitemap — video sitemap")
    sitemap_path = os.path.join(PROJECT_ROOT, "public", "sitemap.xml")
    if not os.path.exists(sitemap_path):
        fail("public/sitemap.xml non trovata")
        return

    with open(sitemap_path, encoding="utf-8") as f:
        xml = f.read()

    if 'xmlns:video="http://www.google.com/schemas/sitemap-video/1.1"' in xml:
        ok("namespace xmlns:video presente")
    else:
        fail("namespace xmlns:video mancante")

    video_blocks = re.findall(r'<video:video>(.*?)</video:video>', xml, re.DOTALL)
    if video_blocks:
        ok(f"{len(video_blocks)} blocchi <video:video> trovati")
    else:
        fail("nessun blocco <video:video> trovato")
        return

    if any("KFNWIq5vjTc" in b for b in video_blocks):
        ok("blocco video per episodio 74 con video:player_loc corretto")
    else:
        fail("nessun blocco <video:video> con l'ID YouTube dell'episodio 74")

    required_tags = (
        "video:thumbnail_loc", "video:title", "video:description",
        "video:player_loc", "video:publication_date",
    )
    incomplete = [
        i for i, b in enumerate(video_blocks)
        if not all(f"<{tag}" in b for tag in required_tags)
    ]
    if not incomplete:
        ok("ogni <video:video> ha thumbnail_loc, title, description, player_loc, publication_date")
    else:
        fail(f"blocchi <video:video> incompleti (indici): {incomplete[:10]}")


def test_indexing_contract(base: str):
    """Verify indexation signals from the current build and source content."""
    section(10, 12, "SEO — contratto di indicizzazione")
    public = Path(PROJECT_ROOT, "public")

    # Spreaker is the only feed advertised or generated by Hugo.
    hugo_feeds = sorted(
        str(path.relative_to(public))
        for path in public.rglob("index.xml")
        if path.is_file()
    )
    if not hugo_feeds:
        ok("nessun feed index.xml generato da Hugo")
    else:
        fail("feed Hugo inattesi nel build", ", ".join(hugo_feeds[:20]))

    home = fetch(base, "/").text
    feed_urls = rss_autodiscovery_urls(home)
    spreaker_feeds = [url for url in feed_urls if urlparse(url).hostname == "www.spreaker.com"]
    if len(feed_urls) == 1 and feed_urls == spreaker_feeds:
        ok(f"autodiscovery RSS esclusivamente Spreaker: {feed_urls[0]}")
    else:
        fail("autodiscovery RSS non esclusivamente Spreaker", repr(feed_urls))

    expected_feed = spreaker_feeds[0] if len(spreaker_feeds) == 1 else None
    footer_match = re.search(r"<footer\b.*?</footer>", home, re.DOTALL | re.I)
    footer_hrefs = attribute_values(footer_match.group(0), "href") if footer_match else []
    if expected_feed and expected_feed in footer_hrefs:
        ok("footer collegato direttamente al feed Spreaker")
    else:
        fail("footer senza link diretto al feed Spreaker")

    redirect_text = Path(PROJECT_ROOT, "static", "_redirects").read_text(encoding="utf-8")
    redirect_rules = {}
    for line in redirect_text.splitlines():
        fields = line.split()
        if len(fields) == 3 and not fields[0].startswith("#"):
            redirect_rules[fields[0]] = (fields[1], fields[2])
    required_redirects = ("/feed", "/feed/", "/rss", "/rss/", "/index.xml", "/episodi/index.xml")
    bad_redirects = [
        path for path in required_redirects
        if not expected_feed or redirect_rules.get(path) != (expected_feed, "301")
    ]
    if not bad_redirects:
        ok("endpoint feed storici configurati come 301 verso Spreaker")
    else:
        fail("redirect feed locali mancanti o errati", ", ".join(bad_redirects))

    sitemap_path = public / "sitemap.xml"
    if sitemap_path.exists():
        sitemap = sitemap_path.read_text(encoding="utf-8")
        locs = [html_module.unescape(value.strip()) for value in re.findall(r"<loc>(.*?)</loc>", sitemap)]
        forbidden = [
            url for url in locs
            if urlparse(url).scheme != "https"
            or urlparse(url).hostname != "a2podcast.it"
            or urlparse(url).path.startswith("/tags/")
            or urlparse(url).path.startswith("/trascrizioni/")
            or urlparse(url).path.endswith(".xml")
        ]
        if not forbidden:
            ok("sitemap solo HTTPS apex, senza tag, feed o SRT")
        else:
            fail("URL vietati nella sitemap", ", ".join(forbidden[:20]))
    else:
        locs = []
        fail("public/sitemap.xml non trovata")

    primary_canonical_errors = []
    for loc in locs:
        parsed = urlparse(loc)
        html_path = generated_path_for_url(parsed.path)
        if html_path.exists() and html_path.suffix == ".html":
            actual = canonical_url(html_path.read_text(encoding="utf-8"))
            if actual != loc:
                primary_canonical_errors.append(f"{parsed.path} → {actual!r}")
    for html_path in sorted((public / "tags").rglob("index.html")):
        relative = html_path.relative_to(public).parent.as_posix()
        if "/page/" in f"/{relative}/":
            # Pagination aliases intentionally canonicalize to the owning term.
            continue
        expected = f"https://a2podcast.it/{relative}/"
        actual = canonical_url(html_path.read_text(encoding="utf-8"))
        if actual != expected:
            primary_canonical_errors.append(f"/{relative}/ → {actual!r}")
    if not primary_canonical_errors:
        ok("canonical HTTPS apex con slash su pagine primarie e tag")
    else:
        fail("canonical primaria non conforme", "; ".join(primary_canonical_errors[:20]))

    tag_index = public / "tags" / "index.html"
    if tag_index.exists() and "noindex" in (meta_content(tag_index.read_text(encoding="utf-8"), "robots") or "").lower():
        ok("pagine tag HTML in noindex, follow")
    else:
        fail("pagina /tags/ priva di noindex")

    # Every generated HTML page must self-canonicalize to HTTPS/apex/trailing slash.
    canonical_errors = []
    title_errors = []
    description_errors = []
    modified_errors = []
    episode_pages = []
    for md_path in sorted(Path(EPISODES_DIR).glob("[0-9]*/index.md")):
        try:
            front = load_episode_frontmatter(str(md_path))
        except (RuntimeError, ValueError, tomllib.TOMLDecodeError if tomllib else ValueError) as exc:
            description_errors.append(f"{md_path}: {exc}")
            continue
        slug = str(front.get("slug", md_path.parent.name))
        html_path = public / slug / "index.html"
        if not html_path.exists():
            # Drafts and future pages are deliberately absent and checked elsewhere.
            continue
        episode_pages.append((slug, front, html_path))
        page_html = html_path.read_text(encoding="utf-8")
        expected_url = f"https://a2podcast.it/{slug}/"
        if canonical_url(page_html) != expected_url:
            canonical_errors.append(f"/{slug}/ → {canonical_url(page_html)!r}")

        normalized = normalized_episode_title(str(front.get("title", "")))
        h1_match = re.search(r"<h1[^>]*>(.*?)</h1>", page_html, re.DOTALL | re.I)
        h1 = re.sub(r"<[^>]+>", "", h1_match.group(1)).strip() if h1_match else ""
        h1 = html_unescape_all(h1)
        page_title = html_unescape_all((re.search(r"<title>(.*?)</title>", page_html, re.DOTALL | re.I) or [None, ""])[1])
        schema = find_jsonld(parse_jsonld(page_html), "PodcastEpisode") or {}
        schema_name = html_unescape_all(str(schema.get("name", "")))
        if "&amp;#" in page_html:
            title_errors.append(f"/{slug}/ contiene entità HTML doppio-escaped")
        if "&#" in str(schema.get("name", "")):
            title_errors.append(f"/{slug}/ JSON-LD name contiene entità HTML residue")
        if h1 != normalized or re.match(r"^(?:ep(?:isode)?\.?\s*)?\d+\s*[:.-]", h1, re.I):
            title_errors.append(f"/{slug}/ H1={h1!r}, atteso={normalized!r}")
        if f"— {normalized} | A2 Podcast" not in page_title:
            title_errors.append(f"/{slug}/ title={page_title!r}")
        if schema_name != normalized:
            title_errors.append(f"/{slug}/ JSON-LD name={schema.get('name')!r}")

        description = str(front.get("description", "")).strip()
        if re.search(r"https?://|\[[^]]+\]\(|^[#>*+-]\s", description, re.I):
            description_errors.append(f"/{slug}/ contiene URL o Markdown")
        explicit_lastmod = "lastmod" in front
        json_modified = schema.get("dateModified")
        og_modified = meta_content(page_html, "article:modified_time")
        if explicit_lastmod:
            if not (120 <= len(description) <= 200):
                modified_errors.append(f"/{slug}/ description {len(description)} caratteri")
            if not description or description[-1] not in ".!?…\"”’":
                modified_errors.append(f"/{slug}/ description non è una frase completa")
            if not json_modified or not og_modified:
                modified_errors.append(f"/{slug}/ lastmod senza JSON-LD/OG")
            elif json_modified != og_modified:
                modified_errors.append(f"/{slug}/ dateModified != article:modified_time")
        elif json_modified or og_modified:
            modified_errors.append(f"/{slug}/ data modificata pubblicata senza lastmod esplicito")

    if not canonical_errors:
        ok(f"canonical HTTPS apex con slash su {len(episode_pages)} episodi pubblicati")
    else:
        fail("canonical episodio non conforme", "; ".join(canonical_errors[:20]))
    if not title_errors:
        ok("titoli episodio normalizzati in H1, title e JSON-LD")
    else:
        fail("titoli episodio non normalizzati", "; ".join(title_errors[:20]))

    reused_title_errors = []
    for html_path in public.rglob("*.html"):
        page_html = html_path.read_text(encoding="utf-8")
        for class_name in ("episode-card-title", "episode-nav-title"):
            pattern = rf"class=(?:[\"'][^\"']*\b{class_name}\b[^\"']*[\"']|{class_name})[^>]*>(.*?)</"
            for match in re.finditer(pattern, page_html, re.DOTALL | re.I):
                text_value = html_unescape_all(re.sub(r"<[^>]+>", "", match.group(1)).strip())
                if re.match(r"^(?:ep(?:isode)?\.?\s*)?\d+\s*[:.-]", text_value, re.I):
                    reused_title_errors.append(f"{html_path.relative_to(public)}: {text_value!r}")
    if not reused_title_errors:
        ok("card e navigazione senza prefissi numerici duplicati")
    else:
        fail("prefissi duplicati in card/navigazione", "; ".join(reused_title_errors[:20]))
    if not description_errors:
        ok("descrizioni complete e prive di URL/Markdown")
    else:
        fail("descrizioni non conformi", "; ".join(description_errors[:20]))
    if not modified_errors:
        ok("lastmod coerente con JSON-LD e Open Graph")
    else:
        fail("lastmod non coerente", "; ".join(modified_errors[:20]))

    # Resolve internal page links against the build, and reject non-canonical
    # absolute variants (HTTP/www) or missing trailing slashes for HTML pages.
    link_errors = []
    for html_path in public.rglob("*.html"):
        page_html = html_path.read_text(encoding="utf-8")
        for raw_href in attribute_values(page_html, "href"):
            href = html_module.unescape(raw_href.strip())
            parsed = urlparse(href)
            if parsed.scheme in {"mailto", "tel", "javascript", "data"} or href.startswith("#"):
                continue
            if parsed.netloc and parsed.hostname not in {"a2podcast.it", "www.a2podcast.it"}:
                continue
            if parsed.hostname == "www.a2podcast.it" or parsed.scheme == "http":
                link_errors.append(f"{html_path.relative_to(public)}: {href}")
                continue
            if parsed.netloc:
                path = parsed.path
            else:
                current_url = "/" + str(html_path.relative_to(public)).replace("index.html", "")
                path = urlparse(urljoin(f"https://a2podcast.it{current_url}", href)).path
            suffix = Path(path).suffix.lower()
            if suffix or path in {"", "/"}:
                continue
            target = generated_path_for_url(path)
            if target.exists() and not path.endswith("/"):
                link_errors.append(f"{html_path.relative_to(public)}: manca slash in {href}")
            elif not target.exists():
                link_errors.append(f"{html_path.relative_to(public)}: destinazione assente {href}")
    if not link_errors:
        ok("zero link interni HTML non canonici o inesistenti")
    else:
        fail("link interni non canonici o inesistenti", "; ".join(link_errors[:25]))

    # Every source tag must resolve through the rendered episode link generated
    # by .GetTerms, without reproducing Hugo's slugification in Python.
    tag_errors = []
    for slug, front, html_path in episode_pages:
        page_html = html_path.read_text(encoding="utf-8")
        rendered_tag_hrefs = [href for href in attribute_values(page_html, "href") if "/tags/" in href]
        source_tags = front.get("tags", [])
        if len(set(rendered_tag_hrefs)) != len(set(source_tags)):
            tag_errors.append(f"/{slug}/: source={len(set(source_tags))}, link={len(set(rendered_tag_hrefs))}")
        for href in rendered_tag_hrefs:
            path = urlparse(href).path
            if not generated_path_for_url(path).exists():
                tag_errors.append(f"/{slug}/: {href} non risolve")
    if not tag_errors:
        ok("tag risolti dai link renderizzati e presenti nel build")
    else:
        fail("risoluzione tag non coerente", "; ".join(tag_errors[:20]))

    headers = Path(PROJECT_ROOT, "static", "_headers").read_text(encoding="utf-8")
    srt_block = re.search(r"(?ms)^/trascrizioni/\*\.srt\s*$\n((?:^[ \t]+.*\n?)*)", headers)
    if srt_block and re.search(r"(?im)^\s*X-Robots-Tag:\s*noindex\s*$", srt_block.group(1)):
        ok("_headers applica X-Robots-Tag: noindex agli SRT")
    else:
        fail("regola X-Robots-Tag: noindex mancante per gli SRT")
    robots_path = public / "robots.txt"
    robots = robots_path.read_text(encoding="utf-8") if robots_path.exists() else ""
    if not re.search(r"(?im)^\s*Disallow:\s*/trascrizioni/", robots):
        ok("robots.txt non blocca le trascrizioni SRT")
    else:
        fail("robots.txt blocca gli SRT e impedisce di leggere X-Robots-Tag")


def test_live(base: str):
    """Smoke-test the deployed Cloudflare behavior, without GSC count assumptions."""
    section(11, 12, f"Deploy live — {base}")
    local_home = Path(PROJECT_ROOT, "public", "index.html").read_text(encoding="utf-8")
    local_feeds = rss_autodiscovery_urls(local_home)
    if len(local_feeds) != 1:
        fail("impossibile derivare l'unico feed atteso dal build locale", repr(local_feeds))
        return
    expected_feed = local_feeds[0]
    for path in ("/feed", "/feed/", "/rss", "/rss/", "/index.xml", "/episodi/index.xml"):
        response = fetch_direct(base, path)
        location = response.headers.get("Location", "")
        if response.status_code == 301 and location == expected_feed:
            ok(f"{path} → 301 Spreaker")
        else:
            fail(f"redirect live errato per {path}", f"{response.status_code}, Location={location!r}")

    for path in ("/tags/index.xml", "/ospiti/index.xml", "/pagina-inesistente-seo-test/"):
        response = fetch_direct(base, path)
        if response.status_code == 404:
            ok(f"HTTP 404 live {path}")
        else:
            fail(f"HTTP {response.status_code} live {path} (atteso 404)")

    home = fetch(base, "/")
    feed_urls = rss_autodiscovery_urls(home.text)
    if home.status_code == 200 and feed_urls == [expected_feed]:
        ok("homepage live 200 con unico feed Spreaker")
    else:
        fail("homepage/feed live non conforme", f"HTTP {home.status_code}; feed={feed_urls!r}")

    episode_paths = re.findall(r'<loc>https://a2podcast\.it/(\d+)/</loc>', fetch(base, "/sitemap.xml").text)
    sample_path = f"/{episode_paths[-1]}/" if episode_paths else "/74/"
    episode = fetch(base, sample_path)
    if episode.status_code == 200 and canonical_url(episode.text) == f"https://a2podcast.it{sample_path}":
        ok(f"canonical live corretta su {sample_path}")
    else:
        fail(f"canonical live errata su {sample_path}", canonical_url(episode.text) or "assente")

    tag = fetch(base, "/tags/")
    if tag.status_code == 200 and "noindex" in (meta_content(tag.text, "robots") or "").lower():
        ok("pagina tag live in noindex, follow")
    else:
        fail("pagina tag live senza noindex effettivo", f"HTTP {tag.status_code}")

    srt_files = sorted(Path(PROJECT_ROOT, "static", "trascrizioni").glob("*.srt"))
    if srt_files:
        srt = fetch_direct(base, f"/trascrizioni/{srt_files[0].name}")
        if srt.status_code == 200 and "noindex" in srt.headers.get("X-Robots-Tag", "").lower():
            ok(f"SRT live con X-Robots-Tag noindex ({srt_files[0].name})")
        else:
            fail("header live SRT non conforme", f"HTTP {srt.status_code}; X-Robots-Tag={srt.headers.get('X-Robots-Tag')!r}")
    else:
        fail("nessun SRT sorgente disponibile per il test live")


def test_404(base: str):
    section(12, 12, "Pagina 404")

    # Test HTTP: hugo server risponde ai path inesistenti con la propria pagina 404
    # e status 404 (a differenza della modalità SPA di Cloudflare Pages, non
    # riproducibile con hugo server: quella si verifica solo sul deploy live).
    r = fetch(base, "/questo-url-non-esiste-12345/")
    if r.status_code == 404:
        ok("HTTP 404 per URL inesistente (hugo server)")
    else:
        fail(f"URL inesistente ritorna HTTP {r.status_code} invece di 404")

    page_404 = os.path.join(PROJECT_ROOT, "public", "404.html")
    if os.path.exists(page_404):
        ok("public/404.html presente (404-page in Workers Static Assets)")
        with open(page_404, encoding="utf-8") as f:
            html_404 = f.read()
        if 'noindex' in html_404:
            ok("public/404.html contiene noindex")
        else:
            fail("public/404.html non contiene noindex")
    else:
        fail("public/404.html non trovata")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Test suite A2 Podcast")
    parser.add_argument("--no-build", action="store_true", help="Salta la build Hugo")
    parser.add_argument("--port", type=int, default=1314, help="Porta del server Hugo (default: 1314)")
    parser.add_argument(
        "--live-base-url",
        metavar="URL",
        help="Esegue anche gli smoke test sul deploy (es. https://a2podcast.it)",
    )
    args = parser.parse_args()

    width = 56
    print(f"\n{BOLD}{'═' * width}")
    print(f"  A2 Podcast — Test Suite")
    print(f"{'═' * width}{RESET}")

    # Group 1: build (offline)
    test_build(not args.no_build)

    # Groups 2–6: HTTP tests
    test_frontmatter()  # Group 7 first (offline, while server starts)

    print(f"\n  Avvio hugo server sulla porta {args.port}...")
    server = start_server(args.port)
    base = f"http://localhost:{args.port}"

    try:
        test_homepage(base)
        test_episode_with_youtube(base)
        test_episode_without_youtube(base)
        test_aux_pages(base)
        test_seo_head(base)
        test_generated_markup()
        test_sitemap_video()
        test_indexing_contract(base)
        if args.live_base_url:
            test_live(args.live_base_url.rstrip("/"))
        test_404(base)
    finally:
        server.terminate()
        server.wait()

    # Final report
    passed = sum(results)
    total  = len(results)
    print(f"\n{BOLD}{'═' * width}{RESET}")
    if passed == total:
        print(f"{BOLD}{GREEN}  Risultato: {passed}/{total} test passati ✓{RESET}")
    else:
        failed = total - passed
        print(f"{BOLD}{RED}  Risultato: {failed} falliti, {passed}/{total} passati{RESET}")
    print(f"{BOLD}{'═' * width}{RESET}\n")

    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
