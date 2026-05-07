# A2 Podcast — CLAUDE.md

Sito Hugo statico per il podcast **A2** (a2podcast.it).
Due conduttori: Filippo Strozzi (avvocato) e Roberto Marin (architetto).
Il podcast è ospitato su Spreaker, parte del network Runtime Radio da feb 2025.

---

## Struttura del progetto

```
a2podcast/
├── hugo.toml                        # config Hugo
├── content/
│   ├── _index.md                    # home
│   ├── episodi/NN/index.md          # 77 episodi (generati da ingest.py)
│   └── about/index.md               # bio conduttori + filippo.jpg + roberto.jpg
├── data/
│   └── hosts.toml                   # link e bio dei due host (usato da footer e about)
├── layouts/
│   ├── _default/baseof.html         # shell HTML
│   ├── _default/single.html         # fallback pagine generiche
│   ├── _default/list.html           # fallback liste
│   ├── index.html                   # home page
│   ├── about/single.html            # pagina about con foto host
│   ├── episodi/single.html          # pagina singolo episodio (critica)
│   ├── episodi/list.html            # lista episodi /episodi/
│   └── partials/
│       ├── head.html                # SEO, OG, meta, RSS autodiscovery
│       ├── header.html              # nav con brand color
│       ├── footer.html
│       ├── episode-card.html        # card riusabile (home + lista)
│       ├── audio-player.html        # embed Spreaker iframe
│       ├── hosts-contact.html       # "Dove ci potete trovare" da data/hosts.toml
│       ├── schema-podcast.html      # JSON-LD PodcastSeries (ogni pagina)
│       └── schema-episode.html      # JSON-LD PodcastEpisode (solo episodi)
├── static/
│   ├── css/style.css                # ~300 righe, no framework, mobile-first
│   ├── _headers                     # Cloudflare Pages response headers
│   ├── _redirects                   # /feed e /rss → Spreaker RSS
│   └── trascrizioni/.gitkeep        # slot SRT per trascrizioni future
└── scripts/
    ├── ingest.py                    # genera content/episodi/ da RSS + note MD
    └── requirements.txt             # feedparser, python-slugify
```

---

## Comandi principali

```bash
# Dev server
hugo server -D

# Build produzione
hugo --gc --minify

# Aggiungere/aggiornare episodi (dopo aver aggiunto/modificato file in "../note episodi/")
python3 scripts/ingest.py

# Installare dipendenze Python (una tantum)
pip3 install feedparser python-slugify
```

---

## URL e permalinks

- **Episodi:** `a2podcast.it/NN/` — slug = solo numero episodio (es. `/74/`)
- **Lista episodi:** `a2podcast.it/episodi/`
- **About:** `a2podcast.it/about/`
- **RSS redirect:** `a2podcast.it/feed` → feed Spreaker (via `static/_redirects`)
- **Trascrizioni SRT:** `a2podcast.it/trascrizioni/ep-NN.srt` (file in `static/trascrizioni/`)

Il permalink è configurato in `hugo.toml`:
```toml
[permalinks]
  episodi = "/:slug/"
```
Il campo `slug` nel frontmatter di ogni episodio contiene solo il numero (es. `slug = "74"`).

---

## Frontmatter episodi (generato da ingest.py)

```toml
+++
title = "74: Flusso di lavoro con Andrea Ciraolo"
date = "2023-12-11T06:00:00+01:00"
episodeNumber = 74
slug = "74"
audioUrl = "https://...spreaker.mp3"
spreakerEpisodeId = "64335973"
duration = "1:12:41"
description = "Descrizione breve per SEO (max 300 char)"
draft = false

[params]
  hasTranscript = false
+++
```

**`hasTranscript`**: impostare a `true` quando si aggiunge un file SRT in `static/trascrizioni/ep-NN.srt`. La pagina episodio mostrerà automaticamente i link download e lettura trascrizione.

---

## Script di ingestione (scripts/ingest.py)

Eseguire dalla cartella `a2podcast/` (non da `scripts/`).

- Legge il feed RSS: `https://www.spreaker.com/show/6519470/episodes/feed`
- Legge i file markdown da `../note episodi/NN - Titolo.md`
- Fa il match RSS ↔ file per numero episodio
- Pulisce il corpo: strip H1 iniziale, strip sezione "Dove ci potete trovare", deduplicazione blockquote
- Genera `content/episodi/NN/index.md` con frontmatter TOML completo
- È **idempotente**: ri-eseguirlo sovrascrive i file esistenti senza problemi
- L'ep. 77 non ha file markdown → usa la descrizione RSS come placeholder

---

## Design tokens (CSS)

```css
--color-brand:       #c13a0a;   /* brick red dal logo A2 */
--color-brand-dark:  #8f2a07;
--color-brand-light: #e8521a;
--color-bg:          #fafaf8;
--color-bg-alt:      #f5f0eb;
--color-text:        #1a1a1a;
--color-text-muted:  #666;
--color-border:      #e0d8d0;
```

Nessun framework CSS. Layout: `--content-width: 70ch`, `--wide-width: 1100px`.

---

## SEO e structured data

- Ogni episodio ha JSON-LD `PodcastEpisode` (via `partials/schema-episode.html`)
- Ogni pagina ha JSON-LD `PodcastSeries` (via `partials/schema-podcast.html`)
- `head.html` gestisce `<title>`, `<meta description>`, Open Graph, Twitter Card
- Sitemap generata automaticamente da Hugo (`/sitemap.xml`)
- `enableRobotsTXT = true` in `hugo.toml`

---

## Trascrizioni (future)

Spreaker permette di collegare un URL di trascrizione SRT per episodio.

**Workflow per aggiungere una trascrizione:**
1. Salvare il file: `static/trascrizioni/ep-NN.srt`
2. Nel frontmatter dell'episodio: `hasTranscript = true`
3. Commit + push → la pagina episodio mostrerà il link download SRT
4. Inserire `https://a2podcast.it/trascrizioni/ep-NN.srt` nel campo "URL di trascrizione" su Spreaker

Il `Content-Type: text/plain; charset=utf-8` per i file SRT è già configurato in `static/_headers`.

---

## Deploy — Cloudflare Pages

**Impostazioni nel dashboard CF Pages:**
| Parametro | Valore |
|---|---|
| Repository | `github.com/a2podcast` |
| Branch | `main` |
| Build command | `hugo --gc --minify` |
| Output directory | `public` |
| Env var | `HUGO_VERSION = 0.145.0` |

Il dominio `a2podcast.it` è già su Cloudflare → aggiungere un CNAME al deployment CF Pages dalla sezione Custom Domains del progetto.

---

## Aggiungere un nuovo episodio

1. Creare `../note episodi/NN - Titolo episodio.md` con le note in markdown
2. `python3 scripts/ingest.py` — genera/aggiorna `content/episodi/NN/index.md`
3. `git add content/episodi/NN/ && git commit -m "Ep. NN: Titolo"`
4. `git push` → Cloudflare Pages rebuild automatico (~1 min)

---

## Note tecniche

- Hugo v0.160+ richiede `hugo.Data` invece di `.Site.Data` — già corretto in tutti i template
- `unsafe = false` in goldmark: le note episodio sono markdown puro, nessun HTML inline
- Le foto dei conduttori sono in `content/about/` come page bundle resources (non in `static/`)
- Il `slug` nel frontmatter è il numero come stringa (`"74"`, non `74`) perché TOML lo richiede quoted
