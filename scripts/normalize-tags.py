#!/usr/bin/env python3
"""
Normalizza i tag degli episodi verso una lista canonica.
Uso:
  python3 scripts/normalize-tags.py           # dry-run: mostra modifiche
  python3 scripts/normalize-tags.py --apply   # applica le modifiche
"""

import re
import sys
import glob
from pathlib import Path

# ── Lista canonica ──────────────────────────────────────────────────────────
# Questi sono i tag validi. Lo script normalizzerà i tag esistenti
# verso questi valori tramite la mappa TAG_MAP.
CANONICAL_TAGS = {
    # Apple & prodotti
    "apple", "mac", "macos", "ios", "ipad", "iphone", "ipados",
    "apple-silicon", "apple-pencil", "vision-pro",
    # Produttività & workflow
    "produttivita", "workflow", "automazione", "organizzazione",
    "task-manager", "gtd", "focus", "time-management", "planning", "brainstorming",
    # App & software
    "app", "shortcuts", "note", "email", "calendario", "backup",
    "password-manager", "markdown", "text-editor", "browser",
    # Argomenti
    "sicurezza", "privacy", "intelligenza-artificiale", "hardware",
    "storage", "podcast", "podcasting", "video", "audio", "fotografia",
    "scrittura", "gaming",
    # Nicchie
    "pkm", "minimalismo", "accessibilita", "cybersecurity",
    # Formato episodio
    "intervista", "ospite", "retrospettiva", "tema-annuale",
    "speciale", "conduttori",
}

# ── Mappa di normalizzazione ────────────────────────────────────────────────
# "tag-originale" → "tag-canonico"  (None = rimuovi il tag)
TAG_MAP = {
    # ── Accenti e varianti produttività ──
    "produttività": "produttivita",
    "productivity": "produttivita",
    "productivita": "produttivita",

    # ── Workflow / flusso ──
    "flusso di lavoro": "workflow",
    "flusso-di-lavoro": "workflow",
    "flusso-lavoro": "workflow",
    "automazioni": "automazione",

    # ── iOS versioni → ios ──
    "ios 15": "ios",
    "ios 16": "ios",
    "ios-15": "ios",
    "ios17": "ios",
    "ipados-15": "ipados",
    "ipados15": "ipados",
    "ipados17": "ipados",

    # ── macOS versioni → macos ──
    "macos": "macos",           # già ok ma gestisce case
    "macos ventura": "macos",
    "monterey": "macos",
    "sonoma": "macos",
    "big-sur": "macos",

    # ── Case fix ──
    "apple": "apple",
    "ios": "ios",
    "ipad": "ipad",
    "iphone": "iphone",
    "macos": "macos",

    # ── Shortcuts / comandi rapidi ──
    "comandi-rapidi": "shortcuts",
    "comandi rapidi": "shortcuts",

    # ── PKM / secondo cervello ──
    "secondo-cervello": "pkm",
    "knowledge-management": "pkm",
    "gestione-conoscenza": "pkm",
    "note-taking": "pkm",

    # ── Task manager ──
    "task manager": "task-manager",
    "gestione progetti": "task-manager",

    # ── Time management ──
    "gestione del tempo": "time-management",
    "gestione-tempo": "time-management",
    "time blocking": "time-management",
    "time tracking": "time-management",

    # ── Email ──
    "posta-elettronica": "email",
    "gestione posta": "email",
    "comunicazione digitale": "email",
    "imap": None,
    "pop3": None,
    "apple-mail": "email",

    # ── Apple Pencil ──
    "apple pencil": "apple-pencil",

    # ── Vision Pro ──
    "vision pro": "vision-pro",
    "spatial computing": "vision-pro",

    # ── Sicurezza ──
    "sicurezza dati": "sicurezza",
    "sicurezza iphone": "sicurezza",

    # ── Privacy ──
    "cybersecurity": "cybersecurity",  # già ok
    "password": "password-manager",
    "gestori-password": "password-manager",

    # ── Produttività ──
    "calendari": "calendario",
    "appuntamenti": "calendario",
    "applicazioni": "app",
    "software": "app",
    "strumenti": "app",
    "tools": "app",
    "utility": "app",

    # ── Organizzazione ──
    "organizzazione-documenti": "organizzazione",
    "archiviazione-digitale": "organizzazione",
    "digitalizzazione": "organizzazione",
    "documenti": "organizzazione",
    "paperless": "organizzazione",

    # ── Scrittura ──
    "editor-testo": "scrittura",
    "app-scrittura": "scrittura",
    "testo-semplice": "scrittura",
    "video-scrittura": "scrittura",
    "markdown": "markdown",  # tieni

    # ── Audio / Video ──
    "montaggio-video": "video",
    "video-editing": "video",
    "video-making": "video",
    "produzione audio": "audio",
    "mac-studio": "audio",
    "logic-pro": "audio",
    "garageband": "audio",
    "imovie": "video",

    # ── Minimalismo ──
    "minimalismo digitale": "minimalismo",

    # ── Podcast ──
    "podcasting-2.0": "podcasting",
    "podcast 2.0": "podcasting",
    "value4value": None,
    "bitcoin": None,
    "lightning": None,
    "cryptomonete": None,
    "crypto": None,

    # ── Tema annuale ──
    "tema dell'anno": "tema-annuale",
    "yearly-theme": "tema-annuale",
    "intenzionalità": "tema-annuale",
    "propositi": "tema-annuale",

    # ── Ospiti / formato ──
    "ospiti": "ospite",

    # ── Accessibilità ──
    "accessibilità": "accessibilita",
    "gesti touch": None,

    # ── Hardware / Mac specifici ──
    "processori-apple": "apple-silicon",
    "m1-pro": "apple-silicon",

    # ── Persone (già gestite da pagine ospiti) ──
    "alex-raccuglia": None,
    "lucio-bragagnolo": None,
    "daniele-borghi": None,
    "giuseppe-pugliese": None,
    "franco-solerio": None,
    "lorenzo-morandi": None,
    "matteo-scandolin": None,
    "nicola-losito": None,
    "valentina-de-poli": None,

    # ── Varie ──
    "novità": None,
    "novita-sistema": None,
    "wwdc 2023": "wwdc",
    "wwdc": "wwdc",  # tieni
    "scelta-mac": "mac",
    "transizione-pc": "mac",
    "principianti": None,
    "hackintosh": None,
    "boot camp": None,
    "windows": None,
    "migrazione": None,
    "migrazione android": None,
    "professionisti": None,
    "libera-professione": None,
    "benessere": None,
    "salute": None,
    "tecniche": None,
    "concentrazione": "focus",
    "tecnologia": None,
    "innovazione": None,
    "sviluppo": None,
    "sviluppatori": None,
    "machine-learning": "intelligenza-artificiale",
    "ai": "intelligenza-artificiale",
    "chatgpt": "intelligenza-artificiale",
    "assistente-vocale": "intelligenza-artificiale",
    "linguaggio-naturale": "intelligenza-artificiale",
    "filosofia": None,
    "riflessione personale": None,
    "riflessioni": None,
    "visualizzazione": None,
    "launch": None,
    "community": None,
    "runtime-radio": None,
    "a2podcast": None,
    "digitalia": None,
    "castamatic": "podcast",
    "franco-solerio": None,
    "accessi": None,
    "stage-manager": "ipados",
    "multitasking": None,
    "accessori": "hardware",
    "configurazione": None,
    "manutenzione": "mac",
    "antivirus": "sicurezza",
    "mappe-mentali": "pkm",
    "appunti": "note",
    "bullet-journal": "pkm",
    "brainstorming": "brainstorming",  # tieni
    "ideazione": "brainstorming",
    "craft": "note",
    "notion": "pkm",
    "appweb": "app",
    "database": None,
    "todoist": "task-manager",
    "planning": "planning",  # tieni
    "homebrew": "app",
    "keyboard-maestro": "automazione",
    "hazel": "automazione",
    "dettatura vocale": "shortcuts",
    "iwork": "app",
    "pages": "scrittura",
    "numbers": "app",
    "keynote": "app",
    "presentazioni": "app",
    "freeform": "app",
    "scrivener": "scrittura",
    "torino": None,
    "esport": "gaming",
    "speciale estivo": "speciale",
}


def normalize_tag(tag: str) -> str | None:
    """Normalizza un singolo tag. Ritorna None se va rimosso."""
    key = tag.lower().strip()
    if key in TAG_MAP:
        return TAG_MAP[key]
    # se il tag è già canonico, tienilo
    if key in CANONICAL_TAGS:
        return key
    # fallback: rimuovi tag sconosciuti non critici
    return key  # conservativo: tieni tag non mappati


def parse_toml_tags(line: str) -> list[str]:
    """Estrae la lista di tag da una riga TOML: tags = ["a", "b"]"""
    match = re.match(r'^tags\s*=\s*\[(.+)\]', line.strip())
    if not match:
        return []
    items = re.findall(r'"([^"]*)"', match.group(1))
    return items


def format_toml_tags(tags: list[str]) -> str:
    quoted = [f'"{t}"' for t in tags]
    return f'tags = [{", ".join(quoted)}]'


def process_file(path: Path, apply: bool) -> bool:
    """Processa un file episodio. Ritorna True se ci sono modifiche."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    new_lines = []
    changed = False

    for line in lines:
        if re.match(r'^tags\s*=\s*\[', line.strip()):
            original_tags = parse_toml_tags(line)
            new_tags_raw = [normalize_tag(t) for t in original_tags]
            # Rimuovi None, deduplica preservando ordine
            seen = set()
            new_tags = []
            for t in new_tags_raw:
                if t is not None and t not in seen:
                    seen.add(t)
                    new_tags.append(t)

            if new_tags != original_tags:
                changed = True
                removed = set(original_tags) - set(new_tags)
                added = set(new_tags) - set(original_tags)
                print(f"  [{path.parent.name}]")
                print(f"    prima:  {original_tags}")
                print(f"    dopo:   {new_tags}")
                if removed:
                    print(f"    rimossi: {sorted(removed)}")
                if added:
                    print(f"    aggiunti: {sorted(added)}")
                new_line = format_toml_tags(new_tags) + "\n"
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if changed and apply:
        path.write_text("".join(new_lines), encoding="utf-8")

    return changed


def main():
    apply = "--apply" in sys.argv
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"=== normalize-tags.py [{mode}] ===\n")

    content_dir = Path(__file__).parent.parent / "content" / "episodi"
    files = sorted(content_dir.glob("*/index.md"))

    changed_count = 0
    for f in files:
        if process_file(f, apply):
            changed_count += 1

    print(f"\n{'─' * 50}")
    print(f"Episodi con modifiche: {changed_count}/{len(files)}")
    if not apply:
        print("\nNessuna modifica applicata. Usa --apply per salvare.")
    else:
        print("\nModifiche salvate.")


if __name__ == "__main__":
    main()
