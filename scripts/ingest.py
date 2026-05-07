#!/usr/bin/env python3
"""
A2 Podcast — ingest.py
Parses the Spreaker RSS feed + local episode note files and generates
Hugo-ready content/episodi/<slug>/index.md files with TOML frontmatter.

Run from the project root (a2podcast/):
    pip install feedparser python-slugify
    python3 scripts/ingest.py
"""

import os
import re
import sys
from datetime import datetime, timezone, timedelta

import feedparser
from slugify import slugify

FEED_URL   = "https://www.spreaker.com/show/6519470/episodes/feed"
NOTES_DIR  = os.path.join(os.path.dirname(__file__), "..", "..", "note episodi")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "content", "episodi")

ROME_TZ = timezone(timedelta(hours=1))


# ── helpers ──────────────────────────────────────────────────────────────────

def extract_ep_number(title: str) -> int | None:
    # Handles both "74 - Title" and "74: Title" and "Episode 74: Title"
    m = re.match(r'^(?:Episode\s+)?(\d+)\s*[-:]', title.strip(), re.IGNORECASE)
    return int(m.group(1)) if m else None


def parse_duration(raw: str) -> str:
    """Normalise Spreaker duration to HH:MM:SS or MM:SS string."""
    if not raw:
        return ""
    raw = str(raw).strip()
    if ":" in raw:
        return raw  # already formatted
    try:
        secs = int(raw)
        h, rem = divmod(secs, 3600)
        m, s = divmod(rem, 60)
        if h:
            return f"{h}:{m:02d}:{s:02d}"
        return f"{m}:{s:02d}"
    except ValueError:
        return raw


def extract_spreaker_id(entry) -> str:
    """Extract Spreaker episode ID from the entry id or link fields."""
    # entry.id = "https://api.spreaker.com/episode/64402537" — most reliable
    # entry.link = "https://www.spreaker.com/episode/77-...-64402537" — also works
    for field in (getattr(entry, "id", ""), getattr(entry, "link", "")):
        m = re.search(r'/episode/(?:[^/]*--)?(\d+)$', field)
        if m:
            return m.group(1)
        m = re.search(r'/episode/(\d+)', field)
        if m:
            return m.group(1)
    return ""


def clean_body(raw: str) -> str:
    """
    Strip the H1 title line, remove the 'Dove ci potete trovare' section,
    deduplicate adjacent identical blockquote lines, strip trailing whitespace.
    """
    lines = raw.splitlines()

    # 1. Drop the leading H1
    if lines and lines[0].startswith("# "):
        lines = lines[1:]

    # 2. Trim leading blank lines after the title
    while lines and not lines[0].strip():
        lines.pop(0)

    # 3. Find and drop 'Dove ci potete trovare' section to end of file
    cutoff = None
    for i, line in enumerate(lines):
        if re.search(r'dove ci potete trovare', line, re.IGNORECASE):
            cutoff = i
            break
    if cutoff is not None:
        lines = lines[:cutoff]

    # 4. Deduplicate consecutive identical blockquote lines
    cleaned = []
    prev = None
    for line in lines:
        if line == prev and line.startswith(">"):
            continue
        cleaned.append(line)
        prev = line

    # 5. Strip trailing blank lines
    while cleaned and not cleaned[-1].strip():
        cleaned.pop()

    return "\n".join(cleaned)


def extract_description(raw: str, fallback: str = "") -> str:
    """
    Return the first blockquote block as the episode description (≤ 300 chars).
    Falls back to the RSS description if no blockquote is found.
    """
    lines = raw.splitlines()
    bq_lines = []
    in_bq = False
    for line in lines:
        if line.startswith(">"):
            stripped = line.lstrip("> ").strip()
            if stripped:
                bq_lines.append(stripped)
            in_bq = True
        elif in_bq:
            break  # first non-blockquote line ends the block

    result = " ".join(bq_lines).strip()
    if not result:
        result = fallback

    # Collapse whitespace and cap length
    result = re.sub(r'\s+', ' ', result)[:300]
    return result


def toml_str(s: str) -> str:
    """Escape a string for use inside TOML double-quoted values."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


# ── RSS parsing ───────────────────────────────────────────────────────────────

def parse_rss() -> dict:
    print(f"Fetching RSS feed: {FEED_URL}")
    feed = feedparser.parse(FEED_URL)
    if feed.bozo and not feed.entries:
        print(f"ERROR: could not parse feed — {feed.bozo_exception}", file=sys.stderr)
        sys.exit(1)

    rss_data = {}
    for entry in feed.entries:
        title = entry.get("title", "").strip()
        ep_num = extract_ep_number(title)
        if ep_num is None:
            print(f"  SKIP (no episode number): {title}")
            continue

        # Audio URL
        audio_url = ""
        for enc in entry.get("enclosures", []):
            if enc.get("type", "").startswith("audio"):
                audio_url = enc.get("href", enc.get("url", ""))
                break

        # Publication date
        pub_date = entry.get("published_parsed")
        if pub_date:
            dt = datetime(*pub_date[:6], tzinfo=timezone.utc).astimezone(ROME_TZ)
        else:
            dt = datetime(2021, 1, 1, tzinfo=ROME_TZ)

        # Duration
        duration_raw = ""
        for ns in ("itunes_duration", "duration"):
            val = entry.get(ns)
            if val:
                duration_raw = str(val)
                break

        # Description (strip HTML tags for plain text)
        summary = re.sub(r'<[^>]+>', '', entry.get("summary", "")).strip()
        summary = re.sub(r'\s+', ' ', summary)[:300]

        rss_data[ep_num] = {
            "title":             title,
            "date":              dt.strftime("%Y-%m-%dT%H:%M:%S+01:00"),
            "audio_url":         audio_url,
            "spreaker_ep_id":    extract_spreaker_id(entry),
            "duration":          parse_duration(duration_raw),
            "rss_description":   summary,
        }

    print(f"  Found {len(rss_data)} episodes in RSS feed.")
    return rss_data


# ── Markdown file parsing ─────────────────────────────────────────────────────

def parse_notes() -> dict:
    notes_dir = os.path.abspath(NOTES_DIR)
    if not os.path.isdir(notes_dir):
        print(f"ERROR: notes directory not found: {notes_dir}", file=sys.stderr)
        sys.exit(1)

    md_data = {}
    for filename in os.listdir(notes_dir):
        if not filename.endswith(".md"):
            continue
        m = re.match(r'^(\d+)\s*-', filename)
        if not m:
            continue
        ep_num = int(m.group(1))
        filepath = os.path.join(notes_dir, filename)
        with open(filepath, encoding="utf-8") as f:
            md_data[ep_num] = f.read()

    print(f"  Found {len(md_data)} episode note files.")
    return md_data


# ── Episode generation ────────────────────────────────────────────────────────

def write_episode(ep_num: int, rss: dict, body: str, description: str, output_dir: str):
    # Slug is just the episode number (e.g. "74" → URL /74/)
    slug = str(ep_num)

    ep_dir = os.path.join(output_dir, slug)
    os.makedirs(ep_dir, exist_ok=True)
    out_path = os.path.join(ep_dir, "index.md")

    frontmatter = f"""+++
title = "{toml_str(rss['title'])}"
date = "{rss['date']}"
episodeNumber = {ep_num}
slug = "{slug}"
audioUrl = "{toml_str(rss['audio_url'])}"
spreakerEpisodeId = "{rss['spreaker_ep_id']}"
duration = "{rss['duration']}"
description = "{toml_str(description)}"
draft = false

[params]
  hasTranscript = false
+++

{body}
"""

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(frontmatter)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    rss_data = parse_rss()
    md_data  = parse_notes()
    output_dir = os.path.abspath(OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    generated = 0
    for ep_num in sorted(rss_data.keys()):
        rss  = rss_data[ep_num]
        raw  = md_data.get(ep_num)

        if raw is None:
            # No markdown file — use RSS description as placeholder body
            body        = f"> {rss['rss_description']}"
            description = rss["rss_description"]
            print(f"  EP {ep_num:02d}: no note file — using RSS description as placeholder")
        else:
            body        = clean_body(raw)
            description = extract_description(raw, fallback=rss["rss_description"])

        write_episode(ep_num, rss, body, description, output_dir)
        generated += 1

    print(f"\nDone. Generated {generated} episode files in {output_dir}")


if __name__ == "__main__":
    main()
