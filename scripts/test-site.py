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
import io
import json
import os
import re
import subprocess
import sys
import time
from urllib.parse import unquote, urlparse

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
    """Run hugo --gc --minify and return True on success."""
    print(f"  Esecuzione: hugo --gc --minify ...")
    result = subprocess.run(
        [HUGO_BIN, "--gc", "--minify"],
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


def start_server(port: int) -> subprocess.Popen:
    proc = subprocess.Popen(
        [HUGO_BIN, "server", "--port", str(port), "--disableLiveReload"],
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


def parse_jsonld(html: str) -> list[dict]:
    """Extract and parse all JSON-LD script blocks from HTML."""
    blocks = []
    for match in re.finditer(
        r'<script\s+type="application/ld\+json"[^>]*>(.*?)</script>',
        html, re.DOTALL
    ):
        try:
            blocks.append(json.loads(match.group(1)))
        except json.JSONDecodeError:
            pass
    return blocks


def find_jsonld(blocks: list[dict], type_: str) -> dict | None:
    return next((b for b in blocks if b.get("@type") == type_), None)


# ── Test groups ───────────────────────────────────────────────────────────────

def test_build(build: bool) -> int:
    section(1, 10, "Build Hugo")
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

    # Count pages from output
    m = re.search(r'Pages\s+│\s+(\d+)', output)
    if m:
        n = int(m.group(1))
        if n >= 200:
            ok(f"{n} pagine generate (≥ 200)")
        else:
            fail(f"pagine generate: {n} (attese ≥ 200)")
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
    section(2, 10, "Homepage")
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


def test_episode_with_youtube(base: str):
    section(3, 10, "Episodio CON YouTube (Ep. 74 — Andrea Ciraolo)")
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
    section(4, 10, "Episodio SENZA YouTube (Ep. 40 — WWDC 2022)")
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
    section(5, 10, "Pagine ausiliarie")

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
    section(6, 10, "SEO — head.html")
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
    section(7, 10, "Integrità frontmatter")
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
    section(8, 10, "Markup generato")
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
    section(9, 10, "Sitemap — video sitemap")
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


def test_404(base: str):
    section(10, 10, "Pagina 404")

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
