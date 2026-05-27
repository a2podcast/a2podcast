#!/usr/bin/env python3
"""
A2 Podcast — tag-episodes.py
Finds episodes without tags and suggests 5 tags per episode using Claude API.

Usage:
    python3 scripts/tag-episodes.py            # interactive: review and confirm each
    python3 scripts/tag-episodes.py --apply    # apply all tags automatically
    python3 scripts/tag-episodes.py --ep 74    # process only episode 74

Requirements:
    pip install anthropic
    export ANTHROPIC_API_KEY=sk-ant-...

Run from the project root (a2podcast/).
"""

import argparse
import os
import re
import sys

try:
    import anthropic
except ImportError:
    print("ERROR: anthropic package not found. Run: pip install anthropic", file=sys.stderr)
    sys.exit(1)

EPISODES_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "episodi")
MODEL = "claude-haiku-4-5-20251001"


def get_episode_files(ep_filter: int | None = None) -> list[tuple[int, str]]:
    """Return list of (ep_num, filepath) for episodes missing tags."""
    episodes_dir = os.path.abspath(EPISODES_DIR)
    results = []

    for name in sorted(os.listdir(episodes_dir), key=lambda x: int(x) if x.isdigit() else 0):
        if not name.isdigit():
            continue
        ep_num = int(name)
        if ep_filter is not None and ep_num != ep_filter:
            continue

        filepath = os.path.join(episodes_dir, name, "index.md")
        if not os.path.exists(filepath):
            continue

        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        has_tags = bool(re.search(r'^tags\s*=\s*\[', content, re.MULTILINE))
        if not has_tags:
            results.append((ep_num, filepath))

    return results


def extract_frontmatter_field(content: str, field: str) -> str:
    m = re.search(rf'^{field}\s*=\s*"([^"]*)"', content, re.MULTILINE)
    return m.group(1) if m else ""


def suggest_tags(ep_num: int, title: str, description: str, body_excerpt: str) -> list[str]:
    """Call Claude API to suggest 5 tags for an episode."""
    client = anthropic.Anthropic()

    prompt = f"""Sei un assistente SEO per un podcast italiano su tecnologia Apple per professionisti.

Episodio {ep_num}: {title}
Descrizione: {description}
Estratto note: {body_excerpt[:500] if body_excerpt else "(nessuna nota disponibile)"}

Suggerisci esattamente 5 tag SEO in italiano (minuscolo, senza spazi — usa il trattino se necessario).
I tag devono essere pertinenti all'episodio, utili per la ricerca, e adatti a un podcast tech italiano.
Esempi di tag: workflow, ipad, automazione, ospite, produttivita, apple-silicon, shortcuts, bim, legale

Rispondi SOLO con i 5 tag separati da virgola, senza altro testo. Esempio: tag1, tag2, tag3, tag4, tag5"""

    message = client.messages.create(
        model=MODEL,
        max_tokens=100,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()
    tags = [t.strip().lower().replace(" ", "-") for t in raw.split(",") if t.strip()]
    return tags[:5]


def apply_tags(filepath: str, tags: list[str]):
    """Insert tags field into episode frontmatter."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    tags_toml = f'tags = [{", ".join(f\'"{t}"\' for t in tags)}]'

    # Insert after description line, before draft = false
    new_content = re.sub(
        r'(^description\s*=\s*"[^"]*")',
        rf'\1\n{tags_toml}',
        content,
        count=1,
        flags=re.MULTILINE
    )

    if new_content == content:
        # fallback: insert before draft = false
        new_content = re.sub(
            r'(^draft\s*=)',
            rf'{tags_toml}\n\1',
            content,
            count=1,
            flags=re.MULTILINE
        )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    parser = argparse.ArgumentParser(description="Tag A2 Podcast episodes via Claude API")
    parser.add_argument("--apply", action="store_true", help="Apply tags without confirmation")
    parser.add_argument("--ep", type=int, default=None, help="Process only this episode number")
    args = parser.parse_args()

    episodes = get_episode_files(ep_filter=args.ep)

    if not episodes:
        print("Tutti gli episodi hanno già i tag.")
        return

    print(f"Trovati {len(episodes)} episodi senza tag.\n")

    updated = 0
    for ep_num, filepath in episodes:
        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        title = extract_frontmatter_field(content, "title")
        description = extract_frontmatter_field(content, "description")

        # Extract body (after frontmatter)
        body_match = re.search(r'^\+\+\+\n.*?\+\+\+\n(.*)', content, re.DOTALL)
        body_excerpt = body_match.group(1).strip() if body_match else ""

        print(f"Ep. {ep_num}: {title}")
        print(f"  Generating tags...", end=" ", flush=True)

        tags = suggest_tags(ep_num, title, description, body_excerpt)
        print(f"{', '.join(tags)}")

        if args.apply:
            apply_tags(filepath, tags)
            print(f"  ✓ Tags applied")
            updated += 1
        else:
            confirm = input(f"  Applicare questi tag? [s/N/custom]: ").strip().lower()
            if confirm == "s":
                apply_tags(filepath, tags)
                print(f"  ✓ Tags applied")
                updated += 1
            elif confirm not in ("", "n"):
                # Allow custom comma-separated tags
                custom = [t.strip() for t in confirm.split(",") if t.strip()]
                if custom:
                    apply_tags(filepath, custom)
                    print(f"  ✓ Custom tags applied: {', '.join(custom)}")
                    updated += 1
            else:
                print(f"  Skipped.")

        print()

    print(f"Done. {updated}/{len(episodes)} episodi aggiornati.")


if __name__ == "__main__":
    main()
