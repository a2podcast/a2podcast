# A2 Podcast — CLAUDE.md

Sito Hugo statico per il podcast **A2** (a2podcast.it).  
Conduttori: Filippo Strozzi (avvocato) e Roberto Marin (architetto).  
Ospitato su Spreaker, network Runtime Radio da feb 2025.

→ Per l'architettura tecnica dettagliata vedi [ARCHITETTURA.md](./ARCHITETTURA.md).

---

## Quick Start

```bash
hugo server -D                  # dev server locale
python3 scripts/ingest.py       # sincronizza episodi da RSS + note
hugo --gc --minify              # build produzione
python3 scripts/test-site.py   # test automatici completi (build + HTTP + frontmatter)
```

---

## Regola Hugo: verifica sempre le funzionalità native

Prima di implementare qualsiasi soluzione custom (partial, CSS, JavaScript), verificare sempre:

1. **Hugo ha già questa funzione?** Consultare la documentazione ufficiale: https://gohugo.io/documentation/
2. **Esiste uno shortcode built-in?** Hugo include shortcode nativi per YouTube, Vimeo, figure, highlight, ecc.
3. **Esiste una funzione template?** Hugo ha centinaia di funzioni template built-in (format, transform, collections, ecc.)

**Esempi di funzionalità native Hugo da preferire sempre al codice custom:**
- Video YouTube/Vimeo → `{{< youtube ID >}}` / `{{< vimeo ID >}}`
- Evidenziazione codice → `{{< highlight >}}`
- Privacy (GDPR) → `[privacy]` in `hugo.toml`
- Paginazione → `{{ template "_internal/pagination.html" . }}`
- Sitemap, RSS, OpenGraph → template interni Hugo

**Riferimento:** https://gohugo.io/documentation/

---

## Workflow: nuovo episodio

1. Crea `../note episodi/NN - Titolo episodio.md` con le note in markdown
2. `python3 scripts/ingest.py` — genera/aggiorna `content/episodi/NN/index.md`
3. (Opzionale) Se esiste la diretta YouTube, aggiungi a `content/episodi/NN/index.md`:
   ```toml
   [params]
     youtubeId = "ID_VIDEO"   # 11 caratteri dall'URL youtube.com/watch?v=XXXXX
   ```
4. `git add content/episodi/NN/ && git commit -m "ep: Ep. NN: Titolo"`
5. `git push` → Cloudflare Pages rebuild automatico (~1 min)

## Workflow: aggiungere trascrizione

1. Carica il file SRT su Spreaker (dashboard episodio)
2. `python3 scripts/ingest.py` — scarica SRT in `static/trascrizioni/ep-NN.srt` e imposta `hasTranscript = true`
3. Commit + push

## Workflow: associare video YouTube agli episodi

```bash
python3 scripts/match-youtube.py            # recupera video dal canale, propone match interattivo
python3 scripts/match-youtube.py --apply    # applica tutti i match automaticamente
python3 scripts/match-youtube.py --ep 74   # solo episodio 74
python3 scripts/match-youtube.py --dry-run # mostra match senza scrivere
```

Richiede `yt-dlp` (`pip install yt-dlp`). Per titoli anomali usa Claude Haiku (richiede `ANTHROPIC_API_KEY`).  
In alternativa passa `--csv FILE` con un file CSV a due colonne: `ep_num,youtube_id`.

## Workflow: aggiungere/aggiornare tag episodi

```bash
python3 scripts/tag-episodes.py          # propone tag per episodi senza tag (usa Claude API)
python3 scripts/tag-episodes.py --apply  # applica automaticamente senza chiedere conferma
```

Richiede `ANTHROPIC_API_KEY` nell'ambiente. Installa con `pip3 install anthropic`.

---

## Struttura file (file critici)

| File | Ruolo |
|------|-------|
| `hugo.toml` | config Hugo, params podcast, permalink |
| `content/episodi/NN/index.md` | episodio (generato da ingest.py) |
| `content/ospiti/slug/index.md` | pagina ospite |
| `data/hosts.toml` | dati host (bio, link, foto) |
| `layouts/episodi/single.html` | template pagina episodio |
| `layouts/partials/head.html` | SEO, OG, meta tag |
| `layouts/partials/schema-episode.html` | JSON-LD PodcastEpisode |
| `static/css/style.css` | tutto il CSS (~1100 righe) |
| `static/_headers` | HTTP headers Cloudflare (CSP, HSTS) |
| `scripts/ingest.py` | ingestione episodi da RSS |

---

## Frontmatter episodio

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
tags = ["workflow", "ospite", "ipad", "produttivita", "intervista"]
draft = false

[params]
  hasTranscript = false
  guest = "andrea-ciraolo"   # slug della cartella in content/ospiti/
+++
```

`hasTranscript = true` quando il file SRT è in `static/trascrizioni/ep-NN.srt`.  
`guest` collegamento alla pagina ospite (opzionale).

---

## Deploy (Cloudflare Pages)

| Parametro | Valore |
|-----------|--------|
| Branch | `main` |
| Build command | `hugo --gc --minify` |
| Output directory | `public` |
| Env var | `HUGO_VERSION = 0.145.0` |

---

## Regole Git

**Prima di ogni commit:**
```bash
hugo --gc --minify   # la build deve completare senza errori
```

**Struttura commit:** `tipo: descrizione breve in italiano`

| Tipo | Quando usarlo |
|------|--------------|
| `ep` | nuovo episodio o aggiornamento contenuto |
| `fix` | correzione bug o errore |
| `seo` | meta tag, schema.org, Open Graph |
| `style` | modifiche CSS |
| `feat` | nuova funzionalità nel sito |
| `security` | header HTTP, CSP, permessi |
| `docs` | CLAUDE.md, ARCHITETTURA.md, commenti |
| `scripts` | ingest.py, tag-episodes.py e simili |

**Esempi:**
```
ep: Ep. 78: Titolo episodio
fix: correggi link ospite nella card
seo: aggiungi og:image per episodi
style: padding card mobile
feat: sezione newsletter in homepage
security: restringe img-src nella CSP
```

**Push → deploy automatico** su Cloudflare Pages (~1 min). Non serve altro.

**Regola:** quando l'utente chiede di fare commit, merge o "pubblica/deploya", eseguire sempre anche `git push` (con `gh auth switch --user a2podcast` se necessario) senza aspettare ulteriore conferma.

---

## Check di fine attività (suggerire sempre a fine sessione)

Al termine di ogni sessione di lavoro significativa, suggerire proattivamente:

```bash
hugo --gc --minify   # build senza errori prima del commit finale
```

E verificare che siano stati aggiornati:
- `SEO-ottimizzazione.md` — se sono state fatte modifiche SEO, UI o ai contenuti
- `ARCHITETTURA.md` — se sono stati aggiunti/modificati/rimossi file di sistema (template, script, CSS)
- Commit e push di tutti i file modificati inclusi i documenti

**Non aspettare che l'utente lo chieda.** Proporre il check al termine naturale di ogni attività.
