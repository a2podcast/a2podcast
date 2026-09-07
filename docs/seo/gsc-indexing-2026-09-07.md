# Audit GSC e segnali di indicizzazione — 7 settembre 2026

## Scopo e contesto

Questo dossier conserva la fotografia Google Search Console disponibile durante l'audit del 7
settembre 2026 e le decisioni tecniche conseguenti. Il sito era stato ricostruito di recente: i
conteggi GSC includono quindi URL storici, redirect, risorse volontariamente escluse e segnali
raccolti prima dell'ultima scansione. Non sono un obiettivo da azzerare e non descrivono lo stato
live in tempo reale.

Le quattro schermate originali, aggiornate da GSC al **4 settembre 2026**, sono conservate fuori
dagli asset pubblici Hugo in [`docs/evidence/gsc/`](../evidence/gsc/):

| Report GSC | Conteggio storico | Evidenza |
|---|---:|---|
| Pagina scansionata, ma attualmente non indicizzata | 88 | `2026-09-04-crawled-not-indexed.png` |
| Non trovata (404) | 13 | `2026-09-04-not-found.png` |
| Pagina con reindirizzamento | 12 | `2026-09-04-page-with-redirect.png` |
| Esclusa in base al tag `noindex` | 46 | `2026-09-04-noindex.png` |

I file sono copie byte-identiche delle acquisizioni fornite, non ricostruzioni. I quattro numeri
`88 / 13 / 12 / 46` sono una fotografia storica: la suite non li codifica e non è stato creato
alcuno snapshot JSON destinato a diventare obsoleto.

## Classificazione degli URL

- **Canoniche episodio**: meritano controllo di canonical, qualità del titolo e della description,
  contenuto e presenza in sitemap. La decisione finale di indicizzazione resta di Google.
- **Redirect intenzionali**: `/feed[/]`, `/rss[/]`, `/index.xml` e `/episodi/index.xml` devono
  rispondere `301` verso l'unico feed ufficiale Spreaker. È corretto che GSC li classifichi come
  pagine con reindirizzamento.
- **404 intenzionali**: i vecchi feed di tag e ospiti e gli URL realmente inesistenti devono
  restituire `404`; non vanno trasformati in soft 404 o redirect generici.
- **`noindex` intenzionali**: tassonomie e termini tag restano HTML navigabili con `noindex,
  follow`, fuori dalla sitemap. Le trascrizioni SRT restano accessibili e ricevono
  `X-Robots-Tag: noindex`, senza blocco in `robots.txt`.
- **Varianti non canoniche**: HTTP, `www`, URL senza slash e vecchi link interni vanno risolti o
  corretti senza aggiungere una nuova regola Cloudflare che duplichi la canonicalizzazione già
  attiva.

## Campione storico delle 22 canoniche episodio

L'elenco seguente proviene dalla schermata GSC delle pagine scansionate ma non indicizzate. Va
letto come campione storico da monitorare, **non** come lista di pagine da riscrivere in blocco:

`/73/`, `/60/`, `/70/`, `/13/`, `/15/`, `/10/`, `/48/`, `/41/`, `/31/`, `/25/`, `/71/`,
`/74/`, `/54/`, `/26/`, `/56/`, `/27/`, `/72/`, `/37/`, `/3/`, `/76/`, `/2/`, `/57/`.

Durante il follow-up sono prioritarie `/60/`, perché aveva una description non pertinente, e
`/73/` e `/74/`, come controlli di confronto su pagine recenti e ricche.

## Revisioni delegate e decisione dell'orchestratore

L'intervento è stato scomposto in tre revisioni indipendenti, integrate e sottoposte a controllo
finale dall'agente principale:

1. **Interpretazione GSC**: i quattro gruppi non rappresentano 159 errori equivalenti. 404,
   redirect e `noindex` intenzionali sono esclusioni corrette; le 22 canoniche richiedono invece
   segnali coerenti e monitoraggio.
2. **Implementazione minima Hugo**: eliminare gli output RSS Hugo, mantenere l'autodiscovery e i
   link al feed Spreaker, correggere link/tag/titoli e aggiungere controlli automatici, senza
   introdurre nuove catene di redirect.
3. **Strategia `lastmod`**: attribuire una data di modifica soltanto alle 21 pagine il cui testo
   descrittivo è realmente cambiato; pubblicare `dateModified` e `article:modified_time` solo in
   presenza del campo esplicito, evitando date retroattive derivate da build o commit.

La decisione integrata è un intervento minimo e verificabile: migliorare segnali contraddittori o
contenuti realmente difettosi, preservando le esclusioni intenzionali. Non si tenta di manipolare
il conteggio GSC attraverso redirect o indicizzazione di pagine prive di valore autonomo.

## Interventi accettati

- Spreaker rimane l'unico feed ufficiale e l'unico feed in autodiscovery; gli output Hugo sono
  soltanto HTML per home, section, taxonomy, term e page.
- I vecchi endpoint feed noti reindirizzano a Spreaker; i feed storici di tag e ospiti restano 404.
- Gli SRT ricevono `X-Robots-Tag: noindex`; le pagine tag restano `noindex, follow` e fuori sitemap.
- Link ai tag generati con i termini Hugo e permalink relativi; link interni corretti alla forma
  canonica HTTPS apex con slash.
- Normalizzazione unica dei prefissi numerici, riutilizzata da title SEO, H1, card, navigazione e
  dati strutturati.
- Riscrittura mirata delle description degli episodi 1, 4, 5, 6, 7, 14, 23, 24, 29, 32, 43,
  45, 48, 49, 51, 52, 54, 56, 59 e 77, più la description non pertinente dell'episodio 60.
- `lastmod` esplicito sulle sole 21 pagine modificate e prevenzione dei futuri troncamenti ciechi
  nell'ingestione, senza eseguire `ingest.py` durante l'intervento.
- Suite locale derivata dal build e dai contenuti, più modalità live per verificare il
  comportamento effettivo di Cloudflare.

## Soluzioni scartate

- **Nuova regola Cloudflare 308**: duplicava la canonicalizzazione esistente senza risolvere la
  qualità o la scoperta delle canoniche.
- **Disattivare gli alias `/page/1/`**: intervento rivolto al conteggio delle escluse, non al
  problema delle pagine episodio.
- **Correlati automatici**: ampliamento editoriale non sostenuto dai dati del report.
- **Riscrivere tutti i 22 episodi del campione**: GSC non dimostra che ciascuno abbia contenuto
  inadeguato; si correggono soltanto description realmente troncate o non pertinenti.
- **`lastmod` retroattivi da rigenerazione o cronologia Git**: avrebbero dichiarato modifiche non
  editoriali e attribuito date nuove a pagine non cambiate.
- **Bloccare SRT o tag in `robots.txt`**: impedirebbe al crawler di osservare il `noindex` e
  ridurrebbe l'utilità dei link `follow`.
- **Modifiche tecniche estranee**: escluse per mantenere attribuibile l'effetto del rilascio.

Queste esclusioni sono decisioni durevoli: non vanno riproposte senza nuove evidenze.

## Prima e dopo tecnico

| Segnale | Prima dell'intervento | Contratto dopo l'intervento |
|---|---|---|
| Feed | Output RSS Hugo affiancati al feed ufficiale | Solo HTML Hugo; autodiscovery e footer puntano a Spreaker |
| Sitemap | Rischio di includere output non canonici | Solo HTTPS apex; niente tag, feed o SRT |
| Trascrizioni | Risorsa accessibile senza direttiva robot dedicata | Accessibile con `X-Robots-Tag: noindex` |
| Titoli | Rimozione prefissi duplicata in più template | Un'unica normalizzazione riusata ovunque |
| Description | 20 tagliate e una non pertinente | 21 frasi complete di 120–200 caratteri |
| Date modifica | Nessun contratto esplicito | Metadati di modifica solo con `lastmod` esplicito |
| Regressioni | Controlli parziali e valori storici hardcoded | Controlli derivati da contenuti/build e smoke test live |

L'“after” descrive il contratto di rilascio. La sua effettiva pubblicazione va confermata con build,
suite, dry-run Wrangler e test live annotati qui sotto.

## Verifiche tecniche del rilascio

Checklist da completare sul commit destinato alla pubblicazione:

- [x] `hugo --gc --minify --cleanDestinationDir` — build locale riuscita il 7 settembre 2026
- [x] `python3 -m py_compile scripts/test-site.py` — riuscito il 7 settembre 2026
- [x] `python3 -m unittest scripts/test_ingest.py` — 4/4 test riusciti il 7 settembre 2026
- [x] `python3 scripts/test-site.py` — 88/88 controlli locali riusciti il 7 settembre 2026
- [x] `npm run deploy:dry-run` — Wrangler 4.127.1 ha validato 617 asset il 7 settembre 2026
- [x] dopo il push: `python3 scripts/test-site.py --no-build --live-base-url https://a2podcast.it`
  — 98/98 controlli riusciti il 7 settembre 2026; `/60/`, `/73/` e `/74/` rispondono `200`
  con canonical HTTPS apex e slash corretta

La suite verifica: assenza dei feed Hugo; unico feed Spreaker in autodiscovery; sitemap priva di
tag/feed/SRT/HTTP/`www`; canonical con HTTPS apex e slash; link interni e tag risolti; titoli senza
numero duplicato; description senza tagli, URL o Markdown; coerenza `lastmod`/JSON-LD/Open Graph;
regola e header SRT; esclusione degli episodi futuri. Non usa i conteggi GSC come aspettative.

## Follow-up Search Console

| Scadenza | Data obiettivo | Operazioni e dati da registrare |
|---|---|---|
| Rilascio | da compilare | Reinviare sitemap; ispezionare `/60/`, `/73/`, `/74/`; richiedere indicizzazione solo se una canonica è ancora esclusa; usare “Convalida correzione” solo sul report pertinente. Non convalidare 404, redirect o `noindex` intenzionali. |
| +7 giorni | da compilare | Data rilevazione, esito ispezioni, ultima scansione delle tre URL, eventuale variazione dei quattro report rispetto alla fotografia (senza sovrascriverla). |
| +30 giorni | da compilare | Ripetere campione delle 22 canoniche, annotare quante risultano indicizzate e motivazioni GSC residue. |
| +60 giorni | da compilare | Valutare il trend, distinguere regressioni tecniche da decisioni di Google e decidere eventuali interventi soltanto su nuove evidenze. |

L'indicizzazione effettiva non è un esito garantibile dal deploy: rimane una decisione di Google.
