#!/usr/bin/env python3
"""
A2 Podcast — match-youtube.py
Recupera i video live dal canale YouTube, li associa agli episodi per numero
e scrive youtubeId nel frontmatter [params] di ogni episodio corrispondente.

Utilizzo:
    python3 scripts/match-youtube.py              # interattivo: mostra match e chiede conferma
    python3 scripts/match-youtube.py --apply      # applica tutti i match automaticamente
    python3 scripts/match-youtube.py --ep 74      # processa solo l'episodio 74
    python3 scripts/match-youtube.py --csv FILE   # usa CSV manuale (ep_num,youtube_id)
    python3 scripts/match-youtube.py --dry-run    # mostra match senza scrivere nulla

Requisiti:
    pip install yt-dlp anthropic
    export ANTHROPIC_API_KEY=sk-ant-...   # solo per titoli anomali senza numero esplicito

Eseguire dalla cartella a2podcast/.
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys

CHANNEL_URL  = "https://www.youtube.com/@a2podcast688/streams"
EPISODES_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "episodi")
MODEL        = "claude-haiku-4-5-20251001"


# ── Fetch video list ──────────────────────────────────────────────────────────

def fetch_videos() -> list[dict]:
    """Fetch video list from YouTube channel using yt-dlp."""
    print(f"Recupero video da {CHANNEL_URL} ...")
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "-J", CHANNEL_URL],
            capture_output=True, text=True, timeout=60
        )
    except FileNotFoundError:
        print("ERRORE: yt-dlp non trovato. Installa con: pip install yt-dlp", file=sys.stderr)
        sys.exit(1)
    except subprocess.TimeoutExpired:
        print("ERRORE: timeout nel recupero video da YouTube.", file=sys.stderr)
        sys.exit(1)

    if result.returncode != 0:
        print(f"ERRORE yt-dlp: {result.stderr[:200]}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(result.stdout)
    entries = data.get("entries", [])
    print(f"  Trovati {len(entries)} video.")
    return [{"id": e.get("id", ""), "title": e.get("title", "")} for e in entries if e.get("id")]


def load_csv(path: str) -> list[dict]:
    """Load video list from a CSV file with columns: ep_num,youtube_id."""
    videos = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ep = row.get("ep_num") or row.get("episodio") or row.get("episode")
            yt  = row.get("youtube_id") or row.get("youtubeId") or row.get("id")
            if ep and yt:
                videos.append({"ep_num": int(ep), "youtube_id": yt.strip(), "title": ""})
    print(f"  Caricati {len(videos)} record da {path}.")
    return videos


# ── Episode number extraction ─────────────────────────────────────────────────

def extract_ep_number_regex(title: str) -> int | None:
    """Fast regex extraction: matches '76. Titolo', '76 - Titolo', 'Ep. 76', '#76'."""
    patterns = [
        r'^(\d{1,3})\s*[.\-:]',       # "76. Titolo" or "76 - Titolo"
        r'\bEp\.?\s*(\d{1,3})\b',      # "Ep. 76" or "Ep76"
        r'#(\d{1,3})\b',               # "#76"
        r'\b(\d{1,3})\b',              # any standalone number (last resort)
    ]
    for pat in patterns:
        m = re.search(pat, title, re.IGNORECASE)
        if m:
            n = int(m.group(1))
            if 1 <= n <= 999:
                return n
    return None


def extract_ep_number_llm(title: str) -> int | None:
    """Use Claude Haiku to extract episode number from ambiguous titles."""
    try:
        import anthropic
    except ImportError:
        return None

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)
    msg = client.messages.create(
        model=MODEL,
        max_tokens=10,
        messages=[{
            "role": "user",
            "content": (
                f'Questo è il titolo di un video di un podcast: "{title}"\n'
                "Rispondi SOLO con il numero dell'episodio (intero) se riesci a identificarlo, "
                "oppure con la parola null se non c'è un numero episodio riconoscibile."
            )
        }]
    )
    raw = msg.content[0].text.strip()
    if raw.lower() == "null" or not raw.isdigit():
        return None
    return int(raw)


def get_ep_number(title: str) -> int | None:
    n = extract_ep_number_regex(title)
    if n is not None:
        return n
    return extract_ep_number_llm(title)


# ── Frontmatter read/write ────────────────────────────────────────────────────

def get_episode_path(ep_num: int) -> str | None:
    path = os.path.join(os.path.abspath(EPISODES_DIR), str(ep_num), "index.md")
    return path if os.path.exists(path) else None


def read_existing_youtube_id(content: str) -> str | None:
    m = re.search(r'^\s*youtubeId\s*=\s*"([^"]+)"', content, re.MULTILINE)
    return m.group(1) if m else None


def write_youtube_id(filepath: str, youtube_id: str) -> bool:
    """Write youtubeId into [params] section of the frontmatter. Returns True on success."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    existing = read_existing_youtube_id(content)

    if existing == youtube_id:
        return False  # already set, nothing to do

    if existing:
        # Update existing youtubeId value
        new_content = re.sub(
            r'(\s*youtubeId\s*=\s*)"[^"]*"',
            rf'\1"{youtube_id}"',
            content
        )
    else:
        # Insert youtubeId after hasTranscript line inside [params]
        new_content = re.sub(
            r'(^\s*hasTranscript\s*=\s*\S+)',
            rf'\1\n  youtubeId = "{youtube_id}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
        if new_content == content:
            # Fallback: insert before closing +++ if [params] pattern not found
            new_content = content.replace(
                "\n+++\n",
                f'\n  youtubeId = "{youtube_id}"\n+++\n',
                1
            )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Match YouTube video agli episodi A2 Podcast")
    parser.add_argument("--apply",   action="store_true", help="Applica tutti i match senza conferma")
    parser.add_argument("--dry-run", action="store_true", help="Mostra match senza scrivere nulla")
    parser.add_argument("--ep",      type=int, default=None, help="Processa solo l'episodio N")
    parser.add_argument("--csv",     type=str, default=None, help="CSV manuale (ep_num,youtube_id)")
    args = parser.parse_args()

    # Load video list
    if args.csv:
        csv_entries = load_csv(args.csv)
        matches = [(e["ep_num"], e["youtube_id"], "") for e in csv_entries
                   if args.ep is None or e["ep_num"] == args.ep]
    else:
        videos = fetch_videos()
        matches = []
        skipped = []
        for v in videos:
            ep_num = get_ep_number(v["title"])
            if ep_num is None:
                skipped.append(v["title"])
                continue
            if args.ep is not None and ep_num != args.ep:
                continue
            if get_episode_path(ep_num) is None:
                skipped.append(f"Ep. {ep_num} non trovato sul sito: {v['title']}")
                continue
            matches.append((ep_num, v["id"], v["title"]))

        matches.sort(key=lambda x: x[0])

        if skipped:
            print(f"\n⚠ Video non abbinati ({len(skipped)}):")
            for s in skipped:
                print(f"   - {s}")

    if not matches:
        print("\nNessun match trovato.")
        return

    # Show matches table
    print(f"\n{'Ep':>4}  {'YouTube ID':<13}  Titolo video")
    print("-" * 70)
    for ep_num, yt_id, title in matches:
        filepath = get_episode_path(ep_num)
        with open(filepath, encoding="utf-8") as f:
            existing = read_existing_youtube_id(f.read())
        status = " [già presente]" if existing == yt_id else (" [aggiorna]" if existing else "")
        display_title = (title[:40] + "…") if len(title) > 41 else title
        print(f"  {ep_num:>3}  {yt_id:<13}  {display_title}{status}")

    if args.dry_run:
        print("\n[dry-run] Nessuna modifica scritta.")
        return

    print()
    updated = 0
    for ep_num, yt_id, title in matches:
        filepath = get_episode_path(ep_num)

        if args.apply:
            changed = write_youtube_id(filepath, yt_id)
            if changed:
                print(f"  ✓ Ep. {ep_num}: youtubeId scritto")
                updated += 1
        else:
            filepath_display = os.path.relpath(filepath)
            with open(filepath, encoding="utf-8") as f:
                existing = read_existing_youtube_id(f.read())
            if existing == yt_id:
                print(f"  Ep. {ep_num}: già aggiornato, salto.")
                continue
            prompt_label = f"Ep. {ep_num}"
            if title:
                prompt_label += f" ({title[:35]})"
            ans = input(f"  Scrivi youtubeId per {prompt_label}? [S/n]: ").strip().lower()
            if ans in ("", "s", "y"):
                write_youtube_id(filepath, yt_id)
                print(f"    ✓ Scritto in {filepath_display}")
                updated += 1
            else:
                print(f"    Saltato.")

    print(f"\nDone. {updated}/{len(matches)} episodi aggiornati.")


if __name__ == "__main__":
    main()
