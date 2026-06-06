# Fase 4 — Merge nel file episodio (A2)

Obiettivo: aggiungere sinossi e link all'`index.md` **esistente** senza rompere nulla.

## Struttura attuale di un episodio A2 (riferimento)

```
+++
... front matter TOML (NON toccare, lo gestisce ingest.py) ...
tags = ["workflow", "produttivita", "task-manager"]
[params]
  hasTranscript = true
  youtubeId = "..."
  guest = "..."
+++

> Teaser di apertura (= description del front matter)

## Note dell’episodio
- [link esistente](...)
- ...
```

Dopo il merge la pagina avrà, nell'ordine:

```
+++ front matter +++
> teaser
## Sinossi                    ← NUOVO, subito dopo il teaser
[nota IA fissa]
### Capitolo 1 ...
### Capitolo 2 ...
## Note dell’episodio        ← ESISTENTE, preservato dopo la sinossi
- link esistenti...           ← + eventuali link nuovi della Fase 2 NON già presenti
```

Motivo: molte note storiche di A2 sono scalette grezze, research dump o elenchi di link. Se la
sinossi viene messa in fondo, il lettore incontra prima un tono non rifinito e solo dopo il testo
editoriale. La sinossi deve fare da introduzione strutturata; le note restano materiale di supporto.

## Regole di merge (tassative)

1. **Front matter**: non riscriverlo. Se proponi tag nuovi, modifica SOLO la riga `tags = [...]`
   aggiungendo voci in kebab-case (vedi `tags-a2.md`), e chiedi conferma. Tutto il resto invariato.
2. **Teaser `>` e `## Note dell’episodio`**: preservali esattamente come sono, ma la sezione
   Sinossi va inserita **tra teaser e Note**.
3. **Link**: i link della Fase 2 già presenti nelle Note NON si duplicano. Aggiungi solo quelli
   nuovi e pertinenti, in coda alla lista delle Note esistenti (stesso stile `- [Nome](url)`).
   Se non ci sono link nuovi sensati, non aggiungere nulla.
4. **Sezione Sinossi**: aggiungila subito dopo il teaser come `## Sinossi` (H2). Sotto, la nota
   fissa qui sotto, poi i blocchi numerati della Fase 3.
5. **Heading**: solo `##`, `###`, `####`. MAI `#` nel corpo.
6. **Numerazione**: i capitoli della sinossi devono restare numerati (`### 1. ...`,
   `### 2. ...`); eventuali sottosezioni usano `#### 1.1 ...`, `#### 1.2 ...`. Il numero di
   capitoli è proporzionale agli argomenti reali, non fisso.
7. **Citazioni**: preserva i blockquote con virgolette e timestamp prodotti in Fase 3. Non
   trasformarli in testo normale.
8. **Link ospite**: se `[params] guest = "slug"` esiste, verifica che la prima occorrenza
   dell'ospite nella sinossi punti a `https://a2podcast.it/ospiti/slug/`.
9. **Ultimo capitolo**: deve riassumere l'ultimo argomento sostanziale della trascrizione, non
   essere una sintesi, morale, bilancio o commento sulla puntata.
10. **Densità**: minimo normale 1000 parole. Ogni capitolo deve superare il test "cosa impara
   il lettore?": se contiene solo generalità, torna alla trascrizione e aggiungi dettagli.
11. **Accenti**: prima di mostrare il diff, correggi eventuali apostrofi usati al posto degli
   accenti (`e'`, `piu'`, `qualita'`, `perche'`, `puo'`).
12. **Non** aggiungere player, badge, "dove trovarci", newsletter (li gestisce il template).

## Nota fissa da inserire sotto `## Sinossi`

```markdown
## Sinossi

> Questa sinossi è generata con l'intelligenza artificiale a partire dalla trascrizione
> della puntata, per aiutarti a trovare gli argomenti che ti interessano.

### 1. [primo capitolo dalla Fase 3]
...
```

(Se l'utente preferisce una formula diversa per la nota, è facilmente modificabile qui.)

## Come applicare la modifica

- Usa un editor che **inserisce** testo, non che riscrive il file. Inserisci `## Sinossi` tra
  il teaser iniziale e la prima sezione di note/contenuti esistenti. Se il corpo non ha teaser,
  inseriscila subito dopo il front matter.
- Non rigenerare l'index.md con `ingest.py` dopo il merge: `ingest.py` ricostruisce il corpo
  dai file note e cancellerebbe la sinossi. La sinossi vive solo nell'index.md.
  - Se in futuro l'episodio venisse rigenerato, la sinossi andrebbe ri-aggiunta. (Alternativa
    avanzata, fuori scope: spostare la sinossi in un file dati separato — non farlo ora.)

## Checkpoint finale

Mostra all'utente il risultato (o il diff). Ricorda:
- `python3 scripts/test-site.py` o almeno `hugo --gc --minify` per validare la build.
- Commit: `ep: Ep. NN: arricchimento sinossi e link` + push (utente `a2podcast`).
- Verifica che la pagina abbia un solo `<h1>` (il titolo) dopo la build.
- Verifica che nel markdown non ci siano heading `# `, accenti scritti con apostrofo, link
  duplicati aggiunti dalla skill, chiusure retoriche/generiche o capitoli finali di morale.
- Verifica che la sinossi sia proporzionata alla densità della puntata, normalmente almeno 1000
  parole, e che non contenga capitoli composti da frasi generiche senza insight.
