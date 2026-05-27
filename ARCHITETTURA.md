# A2 Podcast — Architettura tecnica

Documentazione di riferimento per capire come è costruito e come funziona il sito.  
Per i comandi operativi quotidiani vedi [CLAUDE.md](./CLAUDE.md).

---

## Stack e infrastruttura

| Strato | Tecnologia |
|--------|-----------|
| Generatore statico | Hugo v0.145+ |
| Audio hosting | Spreaker (show `6519470`) |
| Deploy | Cloudflare Pages (build automatico su push a `main`) |
| Analytics | Matomo self-hosted (`matomo.studiolegalestrozzi.it`) |
| Network | Runtime Radio (da feb 2025) |
| Dominio | `a2podcast.it` su Cloudflare DNS |

---

## Flow di rendering Hugo

```
baseof.html
├── head.html          ← SEO, OG, meta, RSS, CSS
├── header.html        ← nav sticky
├── [block "main"]     ← contenuto specifico per tipo di pagina
│   ├── index.html              → homepage
│   ├── episodi/single.html     → pagina episodio
│   ├── episodi/list.html       → lista /episodi/
│   ├── ospiti/single.html      → pagina ospite
│   ├── ospiti/list.html        → lista /ospiti/
│   └── about/single.html       → pagina chi siamo
├── footer.html
├── schema-podcast.html  ← JSON-LD PodcastSeries (ogni pagina)
└── matomo.html          ← analytics
```

Ogni pagina episodio include anche `schema-episode.html` (JSON-LD PodcastEpisode) e i partial `audio-player.html`, `hosts-contact.html`, `transcript-inline.html`.

---

## Come funziona `ingest.py`

Lo script è l'unico punto di ingestion dei dati. Va eseguito da `a2podcast/`:

```
RSS Spreaker → parse_rss()
                  ↓
         rss_data[ep_num] = { title, date, audio_url, spreaker_ep_id, duration, rss_description }

../note episodi/NN - Titolo.md → parse_notes()
                  ↓
         md_data[ep_num] = raw markdown

Per ogni episodio:
  se ha file markdown → clean_body() + extract_description()
  altrimenti          → corpo = RSS description come blockquote placeholder

→ write_episode() → content/episodi/NN/index.md
```

**`clean_body()`**: rimuove H1 iniziale, taglia sezione "Dove ci potete trovare", deduplica blockquote adiacenti identici, normalizza whitespace.

**`extract_description()`**: estrae il primo blockquote (`>`) come meta description (max 300 chars). Fallback: RSS description.

Lo script è idempotente — ri-eseguirlo sovrascrive i file esistenti senza problemi. I campi `tags`, `guest` e `hasTranscript` vengono preservati solo se presenti nel file markdown delle note, perché ingest.py non li genera automaticamente.

---

## Struttura file completa

```
a2podcast/
├── hugo.toml                        # config Hugo (baseURL, permalink, params podcast)
├── CLAUDE.md                        # istruzioni operative (comandi, workflow)
├── ARCHITETTURA.md                  # questo file
├── content/
│   ├── _index.md                    # home (title + description)
│   ├── episodi/                     # 77 episodi, uno per cartella
│   │   └── NN/index.md              # frontmatter TOML + corpo markdown
│   ├── ospiti/                      # 11 ospiti (page bundle con foto)
│   │   └── nome-slug/
│   │       ├── index.md             # frontmatter + bio
│   │       └── foto.jpg             # foto ospite come page resource
│   └── about/
│       ├── index.md                 # bio conduttori
│       ├── filippo.jpg              # foto Filippo (page resource)
│       └── roberto.jpg              # foto Roberto (page resource)
├── data/
│   └── hosts.toml                   # dati strutturati host (nome, bio, link, foto)
├── layouts/
│   ├── _default/baseof.html         # shell HTML comune
│   ├── _default/single.html         # fallback pagine generiche
│   ├── _default/list.html           # fallback liste
│   ├── index.html                   # homepage
│   ├── about/single.html            # pagina chi siamo
│   ├── episodi/single.html          # pagina singolo episodio
│   ├── episodi/list.html            # lista /episodi/
│   ├── ospiti/single.html           # pagina singolo ospite
│   ├── ospiti/list.html             # lista /ospiti/
│   └── partials/
│       ├── head.html                # SEO, OG, meta, RSS autodiscovery
│       ├── header.html              # nav con brand color
│       ├── footer.html
│       ├── episode-card.html        # card riusabile (home + lista)
│       ├── audio-player.html        # embed Spreaker iframe
│       ├── hosts-contact.html       # "Dove ci potete trovare" da data/hosts.toml
│       ├── host-icon.html           # SVG inline per icone link host (web/twitter/linkedin/youtube/podcast)
│       ├── schema-podcast.html      # JSON-LD PodcastSeries (ogni pagina)
│       ├── schema-episode.html      # JSON-LD PodcastEpisode (solo episodi)
│       ├── transcript-inline.html   # trascrizione SRT inline con <details>
│       └── matomo.html              # snippet analytics Matomo
├── static/
│   ├── css/style.css                # CSS (~1270 righe, no framework, mobile-first)
│   ├── js/matomo.js                 # snippet Matomo estratto (richiesto da CSP)
│   ├── img/logo.jpg                 # logo podcast (usato in OG e JSON-LD)
│   ├── _headers                     # Cloudflare Pages: HTTP headers, CSP, cache
│   ├── _redirects                   # /feed e /rss → Spreaker RSS
│   └── trascrizioni/                # file SRT trascrizioni (ep-NN.srt)
└── scripts/
    ├── ingest.py                    # genera content/episodi/ da RSS + note MD
    ├── tag-episodes.py              # aggiunge tag agli episodi via Claude API
    ├── match-youtube.py             # associa video YouTube agli episodi (interattivo o --apply)
    ├── normalize-tags.py            # normalizza tag esistenti verso lista canonica (dry-run / --apply)
    ├── fix-fireside-links.py        # sostituisce link a2podcast.fireside.fm → a2podcast.it
    └── requirements.txt             # feedparser, python-slugify
```

---

## Sistema di permalink

```toml
# hugo.toml
[permalinks]
  episodi = "/:slug/"
  ospiti  = "/ospiti/:slug/"
```

Il campo `slug` nel frontmatter di ogni episodio è il numero come stringa (`"74"`, non `74`) — TOML richiede le quoted strings per i campi stringa. Il risultato è `a2podcast.it/74/`.

---

## Ospiti: come funzionano

Ogni ospite ha una cartella in `content/ospiti/nome-slug/` con:
- `index.md`: frontmatter con `title`, `role`, `photo`, `website`, `twitter`, `youtube`, `episodes = [40, 54, 57]`
- foto JPEG: page bundle resource (non in `static/`)

Per collegare un episodio all'ospite, nel frontmatter dell'episodio:
```toml
[params]
  guest = "nome-slug"   # deve corrispondere allo slug della cartella ospiti
```

Il template `episodi/single.html` legge `guest`, risolve la pagina ospite con `Site.GetPage "/ospiti/nome-slug"` e mostra il link.

---

## Foto come page bundle resource

Le foto degli host (`content/about/filippo.jpg`, `roberto.jpg`) e degli ospiti (`content/ospiti/nome/foto.jpg`) sono **page bundle resources**, non file in `static/`. Hugo le elabora e genera gli URL corretti con `.Resources.GetMatch`. Questo permette elaborazione immagini futura (resize, WebP).

---

## Design tokens CSS

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

Layout: `--content-width: 70ch`, `--wide-width: 1100px`. Nessun framework CSS. Font: system stack (Apple System, Segoe UI, ecc.). Tipografia responsive via `clamp()`.

---

## SEO e structured data

Ogni pagina riceve:
- `<title>`, `<meta description>`, `<link rel="canonical">` → `head.html`
- Open Graph (`og:*`) e Twitter Card (`twitter:*`) → `head.html`
- JSON-LD `PodcastSeries` → `schema-podcast.html` (incluso in ogni pagina via `baseof.html`)
- JSON-LD `PodcastEpisode` (con `BreadcrumbList`) → `schema-episode.html` (incluso in `episodi/single.html`)

La sitemap è generata automaticamente da Hugo (`/sitemap.xml`). Il `robots.txt` è generato da Hugo con `enableRobotsTXT = true` + direttiva `Sitemap:` nel template.

---

## Trascrizioni

Il template è già pronto. Workflow completo:

1. Caricare il file SRT su Spreaker (dashboard episodio) — Spreaker lo espone via API
2. Eseguire `python3 scripts/ingest.py` → scarica automaticamente l'SRT in `static/trascrizioni/ep-NN.srt` e imposta `hasTranscript = true`
3. Commit + push → la pagina episodio mostra i link download/lettura
4. (Opzionale) inserire `https://a2podcast.it/trascrizioni/ep-NN.srt` nel campo "URL di trascrizione" su Spreaker

`Content-Type: text/plain; charset=utf-8` per i file SRT è già configurato in `static/_headers`.

---

## Sicurezza: header HTTP (`static/_headers`)

Headers applicati da Cloudflare Pages a tutte le risposte:
- `X-Frame-Options: SAMEORIGIN` — previene clickjacking
- `X-Content-Type-Options: nosniff` — previene MIME sniffing
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload` — forza HTTPS
- `Permissions-Policy` — disabilita camera, microfono, geolocalizzazione
- `Content-Security-Policy` — whitelist di sorgenti permesse (no `unsafe-inline`)

Lo script Matomo vive in `static/js/matomo.js` (file esterno) per evitare `'unsafe-inline'` nella CSP.

---

## Deploy — Cloudflare Pages

| Parametro | Valore |
|-----------|--------|
| Repository | `github.com/a2podcast` |
| Branch | `main` |
| Build command | `hugo --gc --minify` |
| Output directory | `public` |
| Env var | `HUGO_VERSION = 0.145.0` |

Push su `main` → build automatico in ~1 minuto.

---

## Player YouTube

Le pagine episodio con `youtubeId` nel frontmatter mostrano un iframe YouTube diretto:

```html
<!-- layouts/episodi/single.html -->
<div class="episode-youtube-embed">
  <iframe src="https://www.youtube-nocookie.com/embed/{{ .Params.youtubeId }}" ...></iframe>
</div>
```

Configurazione privacy in `hugo.toml`:
```toml
[privacy]
  [privacy.youtube]
    privacyEnhanced = true
```

Il CSS `.episode-youtube` ha `max-width: 800px; margin: auto` (centrato, più largo della colonna testo). Non viene usato lo shortcode `{{< youtube >}}` (funziona solo nel content markdown, non nei template layout).

---

## Sistema tag

Tag normalizzati verso una lista canonica di ~60 tag (da 167 originali caotici). Script di normalizzazione: `scripts/normalize-tags.py` — modalità dry-run di default, `--apply` per scrivere.

Lista canonica: apple, mac, macos, ios, ipad, iphone, ipados, apple-silicon, apple-pencil, vision-pro, produttivita, workflow, automazione, organizzazione, task-manager, gtd, focus, time-management, planning, brainstorming, app, shortcuts, note, email, calendario, backup, password-manager, markdown, sicurezza, privacy, intelligenza-artificiale, hardware, storage, podcast, podcasting, video, audio, fotografia, scrittura, gaming, pkm, minimalismo, accessibilita, cybersecurity, intervista, ospite, retrospettiva, tema-annuale, speciale, conduttori.

---

## Note tecniche

- Hugo v0.160+ richiede `hugo.Data` invece di `.Site.Data` — già corretto in tutti i template
- `unsafe = false` in goldmark: le note episodio sono markdown puro, nessun HTML inline
- Le foto dei conduttori sono in `content/about/` come page bundle resources (non in `static/`)
- Il `slug` nel frontmatter è il numero come stringa (`"74"`, non `74`) perché TOML lo richiede quoted
- `ingest.py` non genera `tags`, `guest` né modifica `hasTranscript` se già impostato — questi campi si aggiungono ai file markdown delle note o manualmente
