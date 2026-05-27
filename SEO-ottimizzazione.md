# SEO — Percorso di ottimizzazione A2 Podcast

Documento cronologico degli interventi SEO sul sito a2podcast.it.

---

## Fase 1 — Aprile/Maggio 2026 (batch iniziale)

### Struttura base
- **Meta description** aggiunta su tutte le pagine (homepage, episodi, ospiti, about, listing)
- **Canonical URL** su tutte le pagine
- **robots.txt** con sitemap dichiarata e permessi espliciti per AI crawler (GPTBot, ClaudeBot, PerplexityBot, Google-Extended)
- **llms.txt** aggiunto per AI discovery

### Open Graph e Twitter Card
- `og:type`, `og:title`, `og:description`, `og:url`, `og:site_name`, `og:locale` su tutte le pagine
- `og:image` con dimensioni 1400×1400 (logo podcast)
- `og:type = "article"` sulle pagine episodio con `article:published_time` e `article:author`
- `twitter:card = "summary_large_image"` + title + description + image + site/creator

### Structured Data (JSON-LD)
- **PodcastSeries** globale su tutte le pagine (via `schema-podcast.html` in `baseof.html`)
- **PodcastEpisode** su ogni pagina episodio con: name, url, datePublished, description, episodeNumber, inLanguage, author, keywords, performer (ospite), associatedMedia (audio MP3), partOfSeries, transcript (se disponibile), video (YouTube se disponibile)
- **BreadcrumbList** su ogni pagina episodio
- Durata in formato ISO 8601 (`PT1H12M41S`) con parsing da stringa HH:MM:SS

### Microdata HTML5
- `itemscope itemtype="https://schema.org/PodcastEpisode"` sul template episodio
- `itemprop` per name, description, datePublished

### Performance e sicurezza
- CSP rafforzata senza `unsafe-inline` per script
- HSTS con preload
- Cache immutable per CSS/JS (1 anno), 24h per trascrizioni SRT
- Preconnect/dns-prefetch per widget Spreaker sulle pagine episodio

### Trascrizioni
- Download automatico SRT da Spreaker API via `ingest.py`
- Rendering inline HTML della trascrizione sulle pagine episodio
- Campo `hasTranscript` nel frontmatter + riferimento nel JSON-LD

### YouTube
- Embed player `youtube-nocookie.com` sulle pagine episodio con `youtubeId`
- Riferimento video nel JSON-LD PodcastEpisode
- Script `match-youtube.py` per associazione automatica episodi ↔ video

---

## Fase 2 — Maggio 2026 (seconda analisi)

### noindex su pagine tag
- Aggiunto `<meta name="robots" content="noindex, follow">` in `head.html` per `.Kind == "taxonomy"` e `.Kind == "term"`
- Copre `/tags/<tag>/` (lista episodi per tag) e `/tags/` (lista tutti i tag)
- Le pagine tag hanno contenuto thin (1–5 episodi) e nessun valore SEO autonomo

### Title homepage con keyword
- Aggiunto `tagline = "Tecnologia Apple per professionisti"` in `hugo.toml`
- `head.html` ora genera: `A2 Podcast — Tecnologia Apple per professionisti` per la homepage

### Pulizia link fireside.fm
- 11 file episodio contenevano link `https://a2podcast.fireside.fm/<N>` (vecchio hosting Fireside, non più attivo)
- Sostituiti con `https://a2podcast.it/<N>/` via script `scripts/fix-fireside-links.py`
- Episodi coinvolti: 35, 36, 43, 44, 50, 51, 55, 61, 73, 75, 76

---

## Cosa è stato valutato e scartato

| Intervento | Motivo del no |
|---|---|
| Cambio URL episodi (`/8/` → `/episodi/backup-mac/`) | Romperebbe link inbound, RSS feed e bookmark. Rischio >> beneficio, specie con sito in pausa |
| Slug SEO-friendly per episodi esistenti | Stessa motivazione |
| Immagine podcast 1400×1400 | Richiede aggiornamento manuale su Spreaker dashboard — nessun impatto sul sito Hugo |

---

## Prossimi step suggeriti (se il podcast riprende)

- **Google Search Console**: richiedere re-crawl dopo ogni batch di modifiche
- **Tag cleanup**: valutare se ridurre il numero di tag per episodio (molti hanno 1 sola occorrenza)
- **Immagine copertina**: aggiornare a 1400×1400 su Spreaker dashboard
- **Descrizioni episodi**: alcune sono troncate nel frontmatter — allungarle a 150–300 caratteri migliora CTR
