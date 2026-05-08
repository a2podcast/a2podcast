#!/usr/bin/env python3
"""
A2 Podcast — enrich.py
Arricchisce il frontmatter degli episodi con description SEO, tags e guest
usando Claude Haiku via CLI (claude -p ...).

Run from the project root (a2podcast/):
    python3 scripts/enrich.py

Prerequisiti: Claude CLI autenticato (claude login)
"""

import json
import os
import re
import subprocess
import sys
import time

EPISODES_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "episodi")

PROMPT_TEMPLATE = """Sei un assistente SEO per un podcast italiano su tecnologia Apple per professionisti.
Analizza questo episodio e rispondi SOLO con un oggetto JSON valido, senza markdown, senza spiegazioni.

Formato richiesto:
{{
  "description": "descrizione SEO in italiano, max 280 caratteri, concisa e informativa",
  "tags": ["tag1", "tag2", "tag3"],
  "guest": "nome-slug-ospite oppure null"
}}

Regole:
- description: massimo 280 caratteri, in italiano, senza virgolette doppie interne
- tags: 3-5 parole chiave pertinenti (es. "apple", "backup", "produttivita", "ospiti", nome tool trattato)
- guest: se c'è un ospite, lo slug in minuscolo con trattini (es. "andrea-ciraolo"), altrimenti null
- Rispondi SOLO con il JSON, nessun altro testo

Titolo episodio: {title}

Contenuto:
{body}"""


def read_frontmatter_and_body(filepath: str):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # TOML frontmatter delimited by +++
    m = re.match(r'^\+\+\+\n(.*?)\n\+\+\+\n?(.*)', content, re.DOTALL)
    if not m:
        return None, None, content
    return m.group(1), m.group(2).strip(), content


def get_frontmatter_value(fm: str, key: str) -> str:
    m = re.search(rf'^{key}\s*=\s*"(.*?)"', fm, re.MULTILINE)
    if m:
        return m.group(1)
    m = re.search(rf'^{key}\s*=\s*(\S+)', fm, re.MULTILINE)
    return m.group(1) if m else ""


def has_tags(fm: str) -> bool:
    return bool(re.search(r'^tags\s*=', fm, re.MULTILINE))


def needs_enrichment(fm: str) -> bool:
    if not has_tags(fm):
        return True
    desc = get_frontmatter_value(fm, "description")
    if len(desc) < 100:
        return True
    return False


def call_haiku(prompt: str) -> dict | None:
    try:
        result = subprocess.run(
            ["claude", "-p", prompt, "--model", "claude-haiku-4-5-20251001"],
            capture_output=True, text=True, timeout=30
        )
        output = result.stdout.strip()
        # Extract JSON from output (handles possible extra text)
        json_match = re.search(r'\{.*\}', output, re.DOTALL)
        if json_match:
            return json.loads(json_match.group(0))
    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception) as e:
        print(f"    ERROR calling claude: {e}", file=sys.stderr)
    return None


def update_frontmatter(fm: str, data: dict) -> str:
    # Add/replace description
    desc = data.get("description", "").replace('"', '\\"')[:280]
    if re.search(r'^description\s*=', fm, re.MULTILINE):
        fm = re.sub(r'^description\s*=\s*".*?"', f'description = "{desc}"', fm, flags=re.MULTILINE)
    else:
        fm += f'\ndescription = "{desc}"'

    # Add/replace tags
    tags = data.get("tags", [])
    if isinstance(tags, list) and tags:
        tags_toml = ", ".join(f'"{t}"' for t in tags[:5])
        if re.search(r'^tags\s*=', fm, re.MULTILINE):
            fm = re.sub(r'^tags\s*=\s*\[.*?\]', f'tags = [{tags_toml}]', fm, flags=re.MULTILINE)
        else:
            fm += f'\ntags = [{tags_toml}]'

    # Add/replace guest (only if not null)
    guest = data.get("guest")
    if guest and guest != "null":
        slug = re.sub(r'[^a-z0-9-]', '', guest.lower().replace(" ", "-"))
        if re.search(r'^guest\s*=', fm, re.MULTILINE):
            fm = re.sub(r'^guest\s*=\s*".*?"', f'guest = "{slug}"', fm, flags=re.MULTILINE)
        else:
            fm += f'\nguest = "{slug}"'

    return fm


def write_episode(filepath: str, fm: str, body: str):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"+++\n{fm}\n+++\n\n{body}\n")


def main():
    episodes_dir = os.path.abspath(EPISODES_DIR)
    ep_dirs = sorted(
        [d for d in os.listdir(episodes_dir) if os.path.isdir(os.path.join(episodes_dir, d))],
        key=lambda x: int(x) if x.isdigit() else 0
    )

    total = len(ep_dirs)
    enriched = 0
    skipped = 0

    print(f"Found {total} episodes. Checking which need enrichment...")

    for ep_slug in ep_dirs:
        filepath = os.path.join(episodes_dir, ep_slug, "index.md")
        if not os.path.exists(filepath):
            continue

        fm, body, _ = read_frontmatter_and_body(filepath)
        if fm is None:
            print(f"  EP {ep_slug}: SKIP (no frontmatter)")
            continue

        if not needs_enrichment(fm):
            skipped += 1
            continue

        title = get_frontmatter_value(fm, "title")
        # Truncate body to ~800 chars to keep prompt small
        body_excerpt = (body or "")[:800]

        print(f"  EP {ep_slug}: enriching... ", end="", flush=True)

        prompt = PROMPT_TEMPLATE.format(title=title, body=body_excerpt)
        data = call_haiku(prompt)

        if data is None:
            print("FAILED")
            continue

        fm_updated = update_frontmatter(fm, data)
        write_episode(filepath, fm_updated, body or "")
        enriched += 1
        print(f"OK — tags: {data.get('tags', [])}")

        # Small delay to avoid rate limiting
        time.sleep(0.5)

    print(f"\nDone. Enriched: {enriched}, Already complete: {skipped}, Total: {total}")


if __name__ == "__main__":
    main()
