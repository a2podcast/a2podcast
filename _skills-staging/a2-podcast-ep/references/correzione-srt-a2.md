# Fase 1 — Correzione SRT (glossario A2)

L'SRT è generato da riconoscimento vocale e contiene errori tipici sull'italiano tecnico.
Applica le correzioni mentalmente mentre elabori l'SRT — non serve riscrivere il file.

Se l'ambiente consente la delega (Claude: sub-agente Haiku; Codex: passo separato), passa
questo prompt sostituendo `[PATH_SRT]` col percorso reale `static/trascrizioni/ep-NN.srt`.

```
Sei un correttore di trascrizioni del podcast italiano "A2" di Filippo Strozzi (avvocato) e
Roberto Marin (architetto). Temi: tecnologia Apple per professionisti — Mac, iPhone, iPad,
automazioni, workflow, produttività. La trascrizione contiene errori tipici di riconoscimento.

Leggi il file SRT: [PATH_SRT]

Produci una lista di TUTTE le correzioni nel formato:
"testo errato" → "testo corretto" — [motivazione]

== GLOSSARIO TERMINI A RISCHIO ==

CONDUTTORI E PERSONE:
- "Strazzi" / "Strozzo" / "Astrozzi" → "Filippo Strozzi" (conduttore, avvocato)
- "Roberto Marino" / "Marin" → "Roberto Marin" (conduttore, architetto)
- ospiti citati per nome: deduci la grafia dal contesto (es. "Andrea Ciraolo", "Matteo
  Scandolin", "Alex Raccuglia", "Lucio Bragagnolo", "Franco Solerio") — verifica in
  content/ospiti/ se serve.

APPLE — SISTEMI E HARDWARE:
- "Mac OS" / "macos" → "macOS"; "i OS" / "ios" → "iOS"; "iPad OS" → "iPadOS"; "watch OS" → "watchOS"
- "Em uno" / "M1" / "Em due" → "M1"/"M2"/"M3"/"M4" (Apple Silicon, deduci dal contesto)
- "MacBook Pro" / "Mac book" → "MacBook"; "Mac Studio" → "Mac Studio"; "Mac Mini" → "Mac mini"
- "i Phone" → "iPhone"; "i Pad" → "iPad"; "Apple Pencil" / "pencil" → "Apple Pencil"
- "Vision Pro" / "Vision-Pro" → "Vision Pro"; "Apple Silicon" / "Apple silicio" → "Apple Silicon"

APP E SOFTWARE APPLE/PRODUTTIVITÀ:
- "Comandi Rapidi" / "shortcuts" / "Short cuts" → "Comandi Rapidi" (o "Shortcuts" se citato in inglese)
- "Spotlight" / "Spot light" → "Spotlight"; "Time Machine" → "Time Machine"
- "Keynote" / "Key note" → "Keynote"; "Pages" / "Numbers" → "Pages"/"Numbers"; "iMovie" → "iMovie"
- "Final Cut" / "Logic Pro" / "Logic" → "Final Cut Pro"/"Logic Pro"
- "Good Notes" / "Goodnotes" → "GoodNotes"; "Notability" → "Notability"
- "Obsidian" / "Obsidiana" → "Obsidian"; "Drafts" → "Drafts"; "Things" → "Things"
- "Todoist" / "To do ist" → "Todoist"; "Omni Focus" → "OmniFocus"; "Bear" → "Bear"
- "Scrivener" / "Scrivner" → "Scrivener"; "Alfred" / "Launch Bar" → "Alfred"/"LaunchBar"
- "Raycast" / "Ray cast" → "Raycast"; "Bartender" → "Bartender"; "Homebrew" / "brew" → "Homebrew"

CONCETTI / ANGLICISMI TECH (spesso resi male a voce):
- "workflow" / "work flow" → "workflow"; "task manager" → "task manager"
- "PKM" / "pi chi emme" → "PKM" (Personal Knowledge Management)
- "GTD" / "gi ti di" → "GTD"; "markdown" / "mark down" → "markdown"
- "back up" → "backup"; "cloud" → "cloud"; "password manager" → "password manager"
- "automazione" / "automation" → "automazione"; "produttività" → "produttività"

EVENTI / META:
- "WWDC" / "doppia vu di ci" → "WWDC"; "Runtime Radio" / "Ran taim Radio" → "Runtime Radio"
- "Spreaker" / "Spriker" / "Spicker" → "Spreaker"; "podcast" → "podcast"

URL detti a voce ("acca ti ti pi due punti slash slash...") → identificali come URL spoken,
servono per la sezione Link (Fase 2). Cerca anche errori non in lista, deducibili dal contesto.

Riporta i timestamp SRT (HH:MM:SS) dei principali cambi argomento: servono per i capitoli
della sinossi (Fase 3).
```

> Il glossario non è esaustivo: ogni puntata cita app nuove. Deduci la grafia corretta dal
> contesto e, se utile, aggiungila qui.
