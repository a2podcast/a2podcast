# Fase 2 — Ricerca e verifica link delle cose citate

Obiettivo: raccogliere gli URL ufficiali di prodotti/app/persone/risorse citati nell'episodio,
fondendoli con i link già presenti nelle note, per costruire la sezione `## Note dell’episodio`
e i link inline della sinossi.

Questa fase è obbligatoria: la skill deve comportarsi come un ricercatore editoriale, non
limitarsi ai link già presenti. Cerca, verifica e segnala l'affidabilità dei link.

**Priorità delle fonti:**
1. Link **già presenti nelle note** dell'index.md (verificati dai conduttori) — massima priorità:
   NON duplicarli, ma normalizzali nel formato finale.
2. URL espliciti citati nell'SRT (anche detti a voce).
3. URL ufficiali verificati per prodotti/servizi/persone menzionati.
4. App Store/Mac App Store, GitHub ufficiale, documentazione ufficiale, canale YouTube ufficiale.
5. Articoli o fonti terze solo se sono la risorsa citata in puntata o se non esiste una fonte
   ufficiale.

## Verifica obbligatoria

- Se hai accesso web, apri o cerca l'URL e verifica che sia pertinente al nome citato.
- Se non hai accesso web, usa solo i link già presenti nelle note come "verificati"; tutti gli
  altri vanno marcati `DA_VERIFICARE`.
- Non inventare homepage plausibili. Un link non verificato è peggio di nessun link.
- Mantieni un elenco di lavoro con fonte e stato:
  - `NOTE_ESISTENTI` — già nelle note iniziali, da preservare e normalizzare.
  - `SRT` — emerso dalla trascrizione.
  - `RICERCA` — emerso dalla verifica web/editoriale.
  - `VERIFICATO` — trovato e controllato durante la ricerca.
  - `DA_VERIFICARE` — candidato non controllato o dubbio.

**Delega (se disponibile):** passa questo prompt a un sub-agente con accesso web
(Claude: Haiku + WebSearch; Codex: passo con ricerca). Altrimenti esegui tu la ricerca.

```
Sei un ricercatore. Dall'analisi di questa trascrizione del podcast A2 (tecnologia Apple,
produttività) sono stati citati i seguenti prodotti/app/servizi/persone/risorse:

[LISTA estratta dalla Fase 1]

Per ciascuno trova l'URL ufficiale più pertinente. Formato output, una riga per risorsa:
Nome | Descrizione contestuale breve | URL | FONTE | STATO

Se non trovi un URL affidabile: Nome | Descrizione | URL candidato o vuoto | FONTE | DA_VERIFICARE
Priorità: siti ufficiali > App Store/Mac App Store > GitHub > video YouTube > articoli.
Per le app Apple di sistema (Comandi Rapidi, Spotlight, Mail, ecc.) usa la pagina di
supporto Apple ufficiale, oppure ometti il link se è una funzione nativa ovvia.
```

**Regole per la sezione Note finale (Fase 4):**
- Heading: `## Note dell’episodio`, subito dopo il teaser/descrizione.
- Subito sotto la heading devono esserci i link alle cose trattate nell'episodio.
- Formato riga esatto: `- [Nome prodotto / software / pagina web di riferimento](https://url-completo): <breve descrizione>`
- Il nome nel link deve essere pulito e leggibile; la descrizione dopo i due punti deve spiegare
  in una frase breve perché quella risorsa è citata o utile per la puntata.
- La descrizione deve essere **specifica** e derivata dal contesto dell'episodio, dalla nota
  originaria o dalla pagina verificata. Deve dire cosa fa quella risorsa o perché entra nel tema.
- Per ricavare la descrizione usa, in quest'ordine:
  1. la frase subito prima/dopo il link nelle note originarie;
  2. le heading padre della sezione in cui appare il link;
  3. il blocco della trascrizione in cui la risorsa viene discussa;
  4. titolo/metadati della pagina verificata.
- Descrizioni generiche come `risorsa citata nelle note originali dell’episodio`, `risorsa Apple
  o Mac citata nelle note originali`, `episodio A2 collegato agli argomenti trattati` sono vietate:
  se stai per scriverle, non hai abbastanza contesto e devi tornare alla trascrizione/nota o
  segnalare il link come da validare.
- Non usare label vaghe come `link qui`, `podcast`, `lavoro`, `dove è partito`, `inutile` se non
  riesci a ricostruire il nome reale della pagina. In quel caso verifica l'URL, rinomina la risorsa
  con il titolo corretto oppure escludila e segnala il dubbio.
- Non usare URL nudi come testo del link (`https://...`). Se nelle note originarie il link è scritto
  come URL, ricostruisci un nome leggibile dalla pagina o dal contesto, ad esempio `Prezzi Notion`,
  `Profilo Instagram Soya`, `Backlink`.
- Il testo cliccabile del link deve essere, in questo ordine:
  1. il titolo reale della pagina verificata (`<title>`, H1, titolo YouTube o titolo App Store);
  2. il nome ufficiale del prodotto, app, servizio, persona o progetto;
  3. un titolo editoriale normalizzato dalla nota originaria, solo se già chiaro.
- Non usare come testo link frasi descrittive interne alle vecchie note, per esempio `Sistema
  trasparente di Apple` o `Guida Apple`. In quei casi sostituisci con il titolo reale della pagina
  o con un nome specifico, ad esempio `Eseguire il backup del Mac con Time Machine`.
- Normalizza maiuscole/minuscole dei titoli: non lasciare titoli interamente maiuscoli se non sono
  acronimi o nomi ufficiali. Esempio: `HOW I USE NOTION AS AN ARCHITECT` diventa
  `How I Use Notion as an Architect`.
- Se non puoi ricostruire un titolo affidabile, non pubblicare il link nelle note finali: mettilo
  nel checkpoint `DA_VALIDARE` con 2/3 opzioni per l'utente.
- Link ad **altri episodi A2**: sempre `https://a2podcast.it/NN/` (con slash finale).
  MAI `a2podcast.fireside.fm` (vecchio dominio).
- Escludi dalla sezione Note i link di servizio o di chiusura che non sono "cose trattate" nella
  puntata: homepage A2, canale YouTube A2, istruzioni per recensioni, contatti dei conduttori,
  siti personali dei conduttori, newsletter inesistenti, pagine "dove trovarci", feed/pagine
  podcast generiche. Possono restare solo se sono davvero oggetto sostanziale della conversazione.
- Per URL incerti: includi con commento `<!-- DA VERIFICARE -->` a fine riga, così l'utente
  li controlla prima del commit.
- Nella sinossi usa link inline solo per URL `NOTE_ESISTENTI` o `VERIFICATO`. Non linkare inline
  risorse `DA_VERIFICARE`; al massimo mettile nella sezione note con il commento.
- Se un link è già presente nelle note, usalo inline nella sinossi ma non aggiungerlo una
  seconda volta alla lista: normalizza la riga esistente nel formato finale.
- Se due link puntano alla stessa risorsa, conserva quello più ufficiale o quello già scelto dai
  conduttori nelle note, segnando eventuali dubbi nel checkpoint.
- Se le note originarie non contengono link, la ricerca dalla trascrizione è obbligatoria: non
  lasciare `## Note dell’episodio` vuota nel merge finale. Se non trovi nessun URL verificabile,
  fermati e segnala all'utente che la sezione link richiede una scelta editoriale.
- Non conservare liste link separate, titoli di link grezzi o sezioni `## Link`: tutto confluisce
  in `## Note dell’episodio`.
- Non inventare URL. Se non sei sicuro, marca DA_VERIFICARE.

## Esempi di descrizioni accettabili e non accettabili

Non accettabile:

```markdown
- [Backblaze](https://www.backblaze.com/home-1.html): risorsa citata nelle note originali dell’episodio.
- [Metodo BuJo](https://en.wikipedia.org/wiki/Bullet_journal): pagina di riferimento usata nelle note originali.
- [Eric 30x40 template](https://courses.thirtybyforty.com/p/30x40-s-notion-template): risorsa citata nelle note originali dell’episodio.
- [Sistema trasparente di Apple](https://support.apple.com/it-it/HT201250): guida Apple a Time Machine.
- [HOW I USE NOTION AS AN ARCHITECT](https://thirtybyforty.com/blog/how-i-use-notion-as-an-architect): articolo 30x40.
```

Accettabile:

```markdown
- [Backblaze](https://www.backblaze.com/home-1.html): servizio di backup cloud citato come esempio di copia remota/off-site, con costi e tempi di ripristino da valutare.
- [Metodo BuJo](https://en.wikipedia.org/wiki/Bullet_journal): metodo Bullet Journal usato come riferimento per organizzare attività, appuntamenti e note dentro Notion.
- [Eric 30x40 template](https://courses.thirtybyforty.com/p/30x40-s-notion-template): template Notion per architetti da cui Roberto prende spunto per roadmap settimanale, ToDo e note.
- [Eseguire il backup del Mac con Time Machine](https://support.apple.com/it-it/HT201250): guida Apple a Time Machine come backup automatico e incrementale di macOS.
- [How I Use Notion as an Architect](https://thirtybyforty.com/blog/how-i-use-notion-as-an-architect): articolo 30x40 sul workspace Notion per architetti, con agenda, task list, SOP e wiki.
```
