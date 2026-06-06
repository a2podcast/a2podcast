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

## Fase 3 — Maggio 2026 (UI/UX e contenuto)

### Sezione "Dove ci potete trovare?" — link con icone
- Aggiunto `layouts/partials/host-icon.html`: SVG inline per 5 tipi di link (web/globo, twitter/X, linkedin, youtube, podcast/microfono)
- `hosts-contact.html` e `about/single.html`: link diventano pill con icona + span label (gap flexbox funzionante)
- `data/hosts.toml`: aggiunto link "Avvocati e Mac: Compendium" (`icon = "podcast"`) per Filippo
- Stile pill: sfondo rosso brand `#c13a0a`, testo e icona bianchi, hover scurisce a `brand-dark`

### Player YouTube nelle pagine episodio
- `.episode-youtube` portato da `max-width: 1100px` a `max-width: 640px` centrato — video a larghezza media (~60%), non più ristretto alla colonna testo

### Fix contenuto episodi
- Rimossi blockquote duplicati in ep. 75 e 76 (la descrizione appariva due volte sotto il video)
- 11 episodi: link `a2podcast.fireside.fm` sostituiti con `a2podcast.it` via script `fix-fireside-links.py`

### Testi
- Homepage hero: testo aggiornato con nuova formulazione
- Meta description globale sito aggiornata (più specifica, introduce professioni dei conduttori)

---

## Fase 4 — Maggio 2026 (tag, YouTube, pagina episodi)

### Normalizzazione tag
- Ridotti da 167 tag caotici a **60 tag canonici** tramite `scripts/normalize-tags.py`
- Eliminati: nomi propri ospiti (già gestiti da pagine `/ospiti/`), versioni OS specifiche (ios-15, monterey, sonoma → tag generico), tag irrilevanti o troppo specifici
- Normalizzati: maiuscolo → minuscolo, spazi → trattini, accenti rimossi (`produttività` → `produttivita`)
- Impatto SEO: pagine tag più dense e significative, meno pagine thin con 1–2 episodi

### Player YouTube riscritto
- Sostituito player click-to-load custom (CSS complesso, JavaScript) con iframe diretto `youtube-nocookie.com`
- Aggiunto `[privacy.youtube] privacyEnhanced = true` in `hugo.toml`
- Video centrato (`margin: auto`) e allargato a `max-width: 800px`
- Nessun cambiamento SEO diretto, ma migliore UX su tutti i browser (Safari, Chromium)

### Pagina /episodi/ — description SEO
- Rimosso conteggio hardcoded errato (`len .Site.RegularPages` = 89 invece di 77)
- Sostituito con description da `content/episodi/_index.md`:
  > "Ogni episodio di A2 Podcast è una conversazione pratica su Apple, produttività e tecnologia — pensata per professionisti italiani che vogliono lavorare meglio. Mac, iPhone, iPad, automazioni, workflow: scegli l'argomento e inizia ad ascoltare."
- Keyword: Apple, produttività, tecnologia, professionisti italiani, Mac, iPhone, iPad, automazioni, workflow

---

## Fase 5 — Giugno 2026 (warning GSC "noindex" + indicizzazione)

Avviato dal warning Google Search Console *"Esclusa in base al tag noindex"*. Diagnosi sui dati reali
della proprietà `a2podcast.it`: 156 pagine indicizzate, 200 no. Cause individuate e risolte:

### Sitemap senza pagine tassonomia
- Le pagine `/tags/*` hanno `noindex` (corretto) ma erano incluse nella sitemap → contraddizione = warning.
- Creato `layouts/sitemap.xml` custom che esclude i Kind `taxonomy`/`term`. Le pagine tag restano
  `noindex` ma non vengono più proposte a Google. 0 URL tag in sitemap, 92 URL reali.

### Trascrizioni inline su 76 episodi (era 10) — fix "Rilevata ma non indicizzata"
- Causa principale dei ~139 episodi non indicizzati: corpo "thin" (21–126 parole).
- Caricati gli SRT (76/77) e ri-eseguito `ingest.py`: `hasTranscript=true` su 76 episodi →
  `transcript-inline.html` inietta il testo nel DOM (indicizzabile). Es. ep. 70: da 68 a ~17.000 parole.

### VideoObject schema completo — fix "video non su pagina di visualizzazione" (18 video)
- `schema-episode.html`: aggiunti i campi obbligatori Google al `VideoObject` (`name`, `description`,
  `thumbnailUrl` da `i.ytimg.com`, `uploadDate`, `contentUrl`). Vale per i 73 episodi con `youtubeId`.

### Un solo H1 per pagina (era doppio su ~30 episodi)
- `ingest.py` (`clean_body`) ora declassa gli `# ` residui del corpo a `## `: la pagina ha un solo H1
  (titolo episodio dal template). Fix centralizzato e permanente.

### Link interni: vecchio dominio fireside.fm → a2podcast.it
- Corretti 16 link `a2podcast.fireside.fm/NN` → `a2podcast.it/NN/` nei file note sorgente (11 file).

### Da fare lato utente
- **Cloudflare**: redirect 301 `www.a2podcast.it` → `a2podcast.it` (oggi entrambi rispondono 200).
- **GSC**: *Convalida correzione* sui report noindex e video dopo il deploy.

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
- **Tag cleanup**: ✅ fatto (Fase 4) — 60 tag canonici
- **Immagine copertina**: aggiornare a 1400×1400 su Spreaker dashboard
- **Descrizioni episodi**: alcune sono troncate nel frontmatter — allungarle a 150–300 caratteri migliora CTR
