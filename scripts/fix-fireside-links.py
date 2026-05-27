#!/usr/bin/env python3
"""Sostituisce link a2podcast.fireside.fm/<N> con a2podcast.it/<N>/ negli episodi."""

import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content" / "episodi"
PATTERN = re.compile(r'https://a2podcast\.fireside\.fm/(\d+)')
REPLACEMENT = r'https://a2podcast.it/\1/'

def main():
    files_with_matches = []
    for md_file in sorted(CONTENT_DIR.rglob("index.md")):
        text = md_file.read_text(encoding="utf-8")
        matches = PATTERN.findall(text)
        if matches:
            files_with_matches.append((md_file, text, matches))

    if not files_with_matches:
        print("Nessun link fireside.fm trovato.")
        return

    print(f"Trovati {len(files_with_matches)} file con link fireside.fm:\n")
    for md_file, _, matches in files_with_matches:
        ep = md_file.parent.name
        print(f"  episodio {ep}: {len(matches)} link → {', '.join(matches)}")

    print()
    if "--apply" not in sys.argv:
        print("Aggiungi --apply per sostituire i link.")
        return

    for md_file, text, _ in files_with_matches:
        new_text = PATTERN.sub(REPLACEMENT, text)
        md_file.write_text(new_text, encoding="utf-8")
        print(f"  ✓ {md_file.parent.name}/index.md aggiornato")

    print(f"\nDone: {len(files_with_matches)} file aggiornati.")

if __name__ == "__main__":
    main()
