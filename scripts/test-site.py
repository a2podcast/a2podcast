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
import glob
import json
import os
import re
import subprocess
import sys
import time

import requests

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
EPISODES_DIR = os.path.join(PROJECT_ROOT, "content", "episodi")

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
        ["hugo", "--gc", "--minify"],
        cwd=PROJECT_ROOT,
        capture_output=True, text=True
    )
    return result.returncode == 0, result.stdout + result.stderr


def start_server(port: int) -> subprocess.Popen:
    proc = subprocess.Popen(
        ["hugo", "server", "--port", str(port), "--disableLiveReload"],
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
    section(1, 7, "Build Hugo")
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
        if n >= 500:
            ok(f"{n} pagine generate (≥ 500)")
        else:
            fail(f"pagine generate: {n} (attese ≥ 500)")
    else:
        fail("conteggio pagine non trovato nell'output")

    sitemap = os.path.join(PROJECT_ROOT, "public", "sitemap.xml")
    if os.path.exists(sitemap):
        ok("public/sitemap.xml presente")
    else:
        fail("public/sitemap.xml non trovata")


def test_homepage(base: str):
    section(2, 7, "Homepage")
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
    if m and m.group(1).strip() == "A2 Podcast":
        ok(f"<title> = 'A2 Podcast'")
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
    else:
        fail("JSON-LD PodcastSeries non trovato")

    # Canonical
    if 'rel="canonical"' in html:
        ok("canonical presente")
    else:
        fail("canonical mancante")


def test_episode_with_youtube(base: str):
    section(3, 7, "Episodio CON YouTube (Ep. 74 — Andrea Ciraolo)")
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

    if f'data-ytid="{YT_ID}"' in html:
        ok(f"data-ytid={YT_ID} corretto")
    else:
        fail("data-ytid mancante o errato")

    if f"i.ytimg.com/vi/{YT_ID}/hqdefault.jpg" in html:
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
        if video.get("@type") == "VideoObject" and YT_ID in video.get("url", ""):
            ok("JSON-LD VideoObject presente con ID corretto")
        else:
            fail("JSON-LD VideoObject mancante o errato", str(video))
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
    if re.search(r'og:image:width"\s+content="1200"', html):
        ok("og:image:width = 1200")
    else:
        fail("og:image:width mancante o errato")

    if re.search(r'og:image:height"\s+content="630"', html):
        ok("og:image:height = 630")
    else:
        fail("og:image:height mancante o errato")


def test_episode_without_youtube(base: str):
    section(4, 7, "Episodio SENZA YouTube (Ep. 40 — WWDC 2022)")
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
    section(5, 7, "Pagine ausiliarie")

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
    section(6, 7, "SEO — head.html")
    r = fetch(base, "/74/")
    html = r.text

    def has_meta(html, name_or_prop, value):
        pattern = rf'(?:name|property)="{re.escape(name_or_prop)}"\s+content="{re.escape(value)}"'
        return bool(re.search(pattern, html))

    checks = [
        (lambda h: 'rel="canonical"' in h,                          "canonical presente"),
        (lambda h: has_meta(h, "og:image:width",  "1200"),          "og:image:width = 1200"),
        (lambda h: has_meta(h, "og:image:height", "630"),           "og:image:height = 630"),
        (lambda h: has_meta(h, "og:locale",       "it_IT"),         "og:locale = it_IT"),
        (lambda h: has_meta(h, "twitter:card",    "summary"),       "twitter:card = summary"),
        (lambda h: has_meta(h, "twitter:site",    "@a2podcast"),    "twitter:site = @a2podcast"),
    ]
    for check_fn, label in checks:
        (ok if check_fn(html) else fail)(label)


def test_frontmatter():
    section(7, 7, "Integrità frontmatter")
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
