# Tag — A2 Podcast

## ⚠️ Convenzione reale (verificata sul repo del sito)

A2 usa i tag in **kebab-case minuscolo** (NON la forma con spazi/maiuscole). Esempi veri:
- `tags = ["workflow", "produttivita", "task-manager", "organizzazione", "ospite"]`
- `tags = ["apple-pencil", "ipad", "note"]`

Regole:
1. **Tutto minuscolo, parole separate da trattino**: `task-manager`, `time-management`,
   `apple-pencil`, `intelligenza-artificiale`, `password-manager`, `tema-annuale`.
2. **Senza accenti**: `produttivita` (non "produttività"), come nei tag esistenti.
3. **Sigle minuscole**: `pkm`, `gtd`, `wwdc` (il tema del sito normalizza per gli URL).
4. **3–6 tag per episodio**, solo i temi davvero centrali.
5. Se un ospite è presente, usa il tag `ospite` (e `intervista` se è un'intervista).

## Tag esistenti più usati (riusa questi quando calzano)

`produttivita` · `apple` · `app` · `mac` · `workflow` · `macos` · `ipad` · `organizzazione` ·
`ios` · `automazione` · `sicurezza` · `ospite` · `iphone` · `shortcuts` · `scrittura` ·
`podcast` · `pkm` · `note` · `wwdc` · `time-management` · `tema-annuale` · `task-manager` ·
`podcasting` · `ipados` · `hardware` · `email` · `apple-pencil` · `privacy` · `planning` ·
`password-manager` · `minimalismo` · `markdown` · `intelligenza-artificiale` · `gaming` ·
`focus` · `calendario` · `brainstorming` · `audio` · `intervista` · `gtd` · `backup` ·
`storage` · `cybersecurity` · `fotografia` · `vision-pro` · `apple-silicon`

## Come dedurre i tag

1. Leggi i titoli dei capitoli della sinossi (Fase 3) e le note esistenti.
2. Identifica i 3–6 argomenti centrali.
3. Riusa i tag esistenti sopra; se ne manca uno, creane uno nuovo **in kebab-case minuscolo**.

## Importante: come applicarli

I tag stanno nel **front matter TOML** (riga `tags = [...]`), generato da `ingest.py`.
- `ingest.py` **preserva i tag esistenti** dell'index.md. Quindi se l'episodio ha già tag,
  non serve fare nulla; per aggiungerne, modifica la riga `tags` nell'index.md (o nel note
  file e rilancia ingest).
- **Proponi** all'utente i tag mancanti come suggerimento; non sovrascrivere quelli esistenti
  senza conferma.

Le categorie Hugo (`categories`) NON si usano per gli episodi: A2 indicizza i podcast solo via `tags`.
