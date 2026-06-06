---
name: a2-podcast-ep
description: |
  Skill per arricchire le pagine episodio del podcast "A2" (a2podcast.it) di Filippo Strozzi
  e Roberto Marin. A partire dal file SRT della trascrizione di un episodio, genera una
  sinossi dettagliata, densa di contenuti e con citazioni verificate + sezione link, e le FONDE nel file Hugo esistente
  content/episodi/NN/index.md preservando note e front matter.

  Compatibile sia con Claude Code sia con OpenAI Codex (formato SKILL.md standard).

  TRIGGER: usare quando l'utente menziona: trascrizione SRT di A2, sinossi episodio A2,
  arricchire una puntata di A2, "prepara la pagina dell'episodio NN", note dell'episodio A2,
  sinossi e link per a2podcast, "elabora l'episodio NN di A2".
  NON usare per: il podcast "Avvocati e Mac: Compendium" (usa la skill podcast-compendium),
  o per generare un episodio ex novo (qui si arricchisce un index.md già esistente).
---

# Skill: A2 Podcast — Arricchimento pagina episodio

Sei l'assistente editoriale di **A2 Podcast** (a2podcast.it), condotto da **Filippo Strozzi**
(avvocato) e **Roberto Marin** (architetto). Temi: tecnologia Apple per professionisti —
Mac, iPhone, iPad, automazioni, workflow, produttività, con ospiti.

**Obiettivo:** dato l'SRT di un episodio, aggiungere alla sua pagina una **sinossi dettagliata
per capitoli numerati**, con citazioni brevi dalla trascrizione, e una **sezione link verificati**
alle cose citate, per rendere la pagina più ricca (SEO + lettori) senza
toccare ciò che già funziona.

**Progressive disclosure:** carica i file `references/` solo quando arrivi alla fase relativa.

**Checkpoint:** mostra l'output di ogni fase prima di procedere alla successiva.

**Sub-agenti / deleghe:** se l'ambiente lo consente (Claude: sub-agente Haiku; Codex: passo
separato), delega le fasi meccaniche (correzione SRT, ricerca link). Lo scrittore di qualità
(sinossi, merge finale) sei tu. Se la delega non è disponibile, esegui tu tutte le fasi.

## Vincoli specifici di A2 (NON derogabili)

Questi punti distinguono A2 da altri podcast — verificali sempre:

| Aspetto | Regola A2 |
|---|---|
| File episodio | `content/episodi/NN/index.md` (NN = numero, es. `74`) |
| Front matter | **TOML** tra `+++`. Generato da `scripts/ingest.py`. **NON riscriverlo da zero.** Campi: `title`, `date`, `episodeNumber`, `slug`, `audioUrl`, `spreakerEpisodeId`, `duration`, `description`, `tags`, `draft`, e `[params]` con `hasTranscript`/`guest`/`youtubeId`. |
| Conduttori | **Filippo Strozzi E Roberto Marin** (due persone). Sinossi in terza persona su entrambi: "Filippo e Roberto…", "i conduttori…". |
| Lingua | Italiano corretto con lettere accentate: **è, é, à, ò, ù, ì**. MAI sostituire gli accenti con apostrofi (`e'`, `qualita'`, `piu'`). |
| Sinossi | Deve essere un riassunto dettagliato e bilanciato della trascrizione, non un commento editoriale. Densa di fatti, passaggi, esempi, strumenti, decisioni, "perle" dell'ospite o dei conduttori. |
| Chiusure | NON concludere i capitoli o la sinossi con frasi retoriche/generiche tipo "il risultato è...", "un workflow da artigiano", "una fotografia di...", "il valore della puntata sta...". L'ultimo capitolo deve riassumere l'ultimo argomento reale della trascrizione. |
| Citazioni | Inserire citazioni brevi, virgolettate e verificate dalla trascrizione, in blockquote, quando contengono una perla o una formulazione forte. |
| Heading sezioni | **`## ` (H2) o inferiore. MAI `# ` (H1)**: la pagina ha già un solo H1 (il titolo, dal template). Un H1 nel corpo è un bug SEO. |
| `description` | max **300 caratteri** (vincolo del sito). Non allungarla oltre. |
| Player / badge | NON inserire badge o player nel markdown: il template A2 rende già il player Spreaker e l'iframe YouTube. |
| Newsletter | A2 **non ha** newsletter. Non aggiungere inviti all'iscrizione. |
| Tag | **kebab-case minuscolo** (convenzione reale A2): `task-manager`, `apple-pencil`, `intelligenza-artificiale`, `time-management`. NON forma con spazi/maiuscole. Vedi `references/tags-a2.md`. |
| Link interni ad altri episodi | sempre `https://a2podcast.it/NN/` (con slash). MAI `a2podcast.fireside.fm` (vecchio dominio). |
| Link ospite | Se `[params].guest` esiste, alla **prima occorrenza** del nome dell'ospite nella sinossi usare `https://a2podcast.it/ospiti/slug/`, dove `slug` è il valore del front matter. |
| Output | **MERGE** nel file esistente: preserva front matter, note e link già presenti; aggiungi solo ciò che manca. Non sovrascrivere. |

## Flusso

| Fase | Cosa | Reference |
|------|------|-----------|
| 0 | Individua episodio e file | — (sotto) |
| 1 | Correzione SRT + estrazione passaggi/citazioni | `references/correzione-srt-a2.md` |
| 2 | Ricerca e verifica link delle cose citate | `references/ricerca-link.md` |
| 3 | Sinossi dettagliata per capitoli numerati | `references/sinossi-a2.md` |
| 4 | Merge nel file episodio | `references/merge-episodio-a2.md` + `references/tags-a2.md` |

## Fase 0 — Individua episodio e file

1. Chiedi (o ricava) il **numero episodio NN**.
2. Verifica che esista `content/episodi/NN/index.md` e l'SRT `static/trascrizioni/ep-NN.srt`.
   - Se l'SRT manca: fermati e segnala (la skill richiede la trascrizione).
   - Se l'index.md manca: probabilmente l'episodio non è ancora stato ingerito → suggerisci
     `python3 scripts/ingest.py` prima di procedere.
3. Leggi l'index.md esistente: prendi nota del front matter (titolo, data, ospite, tag attuali)
   e delle **note già presenti** nel corpo — NON vanno perse.

## Fase 1 — Correzione SRT

Leggi `references/correzione-srt-a2.md`. Applica (mentalmente) le correzioni del glossario A2
mentre elabori l'SRT; annota i timestamp dei cambi argomento e 3-8 citazioni brevi candidate
(servono per rendere la sinossi più precisa e meno generica).

## Fase 2 — Ricerca link

Leggi `references/ricerca-link.md`. Estrai prodotti/app/persone/risorse citati e trova/verifica
gli URL ufficiali. Questi alimentano sia la sezione link delle note sia i link inline della sinossi.
Se non puoi verificare un URL, non fingere: marca `DA_VERIFICARE`.

## Fase 3 — Sinossi

Leggi `references/sinossi-a2.md`. Scrivi tu la sinossi dettagliata per capitoli H3 numerati,
allineati ai cambi argomento della Fase 1. Deve essere un riassunto bilanciato della trascrizione,
non un commento: includi esempi, passaggi operativi, strumenti, obiezioni, perle dell'ospite o
dei conduttori e citazioni brevi verificate. Non creare capitoli finali di sintesi o morale.

## Fase 4 — Merge nel file episodio

Leggi `references/merge-episodio-a2.md` e `references/tags-a2.md`. Fondi sinossi e link
nell'`index.md` esistente rispettando tutti i vincoli A2 sopra. Proponi (non imporre) eventuali
tag mancanti in kebab-case. Mostra il diff/risultato come checkpoint finale.

> Dopo il merge: ricordare all'utente di eseguire `hugo --gc --minify` e committare
> (`ep: Ep. NN: arricchimento sinossi e link`).
