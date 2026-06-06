# Fase 4 — Merge nel file episodio (A2)

Obiettivo: fondere note/link e sinossi nell'`index.md` **esistente** senza rompere front matter,
teaser, template o contenuti editoriali utili.

## Struttura finale richiesta

La pagina deve avere, nell'ordine:

```markdown
+++
... front matter TOML (NON riscrivere) ...
+++

> Teaser di apertura (= description del front matter)

## Note dell’episodio
- [Nome prodotto / software / pagina web di riferimento](https://link.com): breve descrizione.
- [Altro nome](https://link.com): breve descrizione.

## Sinossi

> Questa sinossi è generata con l'intelligenza artificiale a partire dalla trascrizione
> della puntata, per aiutarti a trovare gli argomenti che ti interessano.

### 1. Primo capitolo
...
```

`## Note dell’episodio` deve quindi stare **subito dopo il teaser/descrizione** e prima della
sinossi. I link alle cose trattate nell'episodio devono seguire immediatamente sotto quella
heading.

## Regole di merge tassative

1. **Front matter**: non riscriverlo. Se proponi tag nuovi, modifica SOLO la riga `tags = [...]`
   aggiungendo voci in kebab-case (vedi `tags-a2.md`) e chiedi conferma. Tutto il resto invariato.
2. **Teaser**: preserva il blockquote iniziale `>`. Se manca, inserisci le sezioni subito dopo
   il front matter.
3. **Heading note**: crea o normalizza la sezione come `## Note dell’episodio` subito dopo il
   teaser. Se nel file esiste `## Note episodio`, `## Note Episodio` o equivalente, trattala
   come la stessa sezione e normalizzala.
4. **Formato link note**: ogni link finale deve usare questo formato esatto:
   `- [Nome prodotto / software / pagina web di riferimento](https://link.com): <breve descrizione>`
5. **Merge dei link**: fondi i link già presenti nelle note iniziali con quelli emersi da
   trascrizione e ricerche. Non duplicare URL, varianti dello stesso prodotto o link già presenti.
   Se un link esistente non ha descrizione, aggiungi una descrizione breve e utile dal contesto.
6. **Priorità link**: i link già inseriti dai conduttori hanno priorità editoriale. I link nuovi
   devono essere verificati; se sono incerti, aggiungi `<!-- DA_VERIFICARE -->` a fine riga.
7. **Mappe mentali, scalette, note convertite in Markdown e research dump**: non devono rimanere
   come blocchi grezzi se la sinossi affronta già quegli argomenti.
   - Se il contenuto è già coperto dalla trascrizione/sinossi, rimuovilo dal corpo finale.
   - Se aggiunge dettagli utili non presenti nella trascrizione, integralo nel capitolo di
     sinossi più pertinente.
   - Se è ambiguo, contraddittorio o non riconciliabile con la trascrizione, non decidere in
     silenzio: segnala il problema all'utente.
8. **Sinossi**: inserisci `## Sinossi` dopo `## Note dell’episodio` e la lista link normalizzata.
   Poi aggiungi la nota fissa e i capitoli numerati prodotti in Fase 3.
9. **Heading**: nel corpo usa solo `##`, `###`, `####`. MAI `#`.
10. **Numerazione**: i capitoli della sinossi devono restare numerati (`### 1. ...`,
    `### 2. ...`); eventuali sottosezioni usano `#### 1.1 ...`, `#### 1.2 ...`.
11. **Citazioni**: preserva i blockquote con virgolette e timestamp prodotti in Fase 3.
12. **Link ospite**: se `[params] guest = "slug"` esiste, verifica che la prima occorrenza
    dell'ospite nella sinossi punti a `https://a2podcast.it/ospiti/slug/`.
13. **Ultimo capitolo**: deve riassumere l'ultimo argomento sostanziale della trascrizione, non
    essere una sintesi, morale, bilancio o commento sulla puntata.
14. **Densità**: minimo normale 1000 parole. Ogni capitolo deve superare il test "cosa impara
    il lettore?": se contiene solo generalità, torna alla trascrizione e aggiungi dettagli.
15. **Accenti**: prima di mostrare il diff, correggi eventuali apostrofi usati al posto degli
    accenti (`e'`, `piu'`, `qualita'`, `perche'`, `puo'`).
16. **Non** aggiungere player, badge, "dove trovarci", newsletter (li gestisce il template).

## Quando segnalare incongruenze

Segnala chiaramente all'utente, prima del merge definitivo, se trovi uno di questi casi:

- le note iniziali contengono un tema o una risorsa importante che non appare nella trascrizione;
- una mappa mentale contiene conclusioni o passaggi più forti di quelli effettivamente detti;
- un link esistente sembra sbagliato, rotto, non ufficiale o riferito a un oggetto diverso;
- la sinossi e le note rischiano di duplicare lo stesso contenuto in due toni diversi.

Formato della segnalazione:

```markdown
## Questioni da validare

1. [Problema concreto]
   - Opzione A: ...
   - Opzione B: ...
   - Opzione C: ...
```

Le opzioni devono essere 2 o 3, concrete e valutabili dall'utente. Non inserire questa sezione
nel file episodio salvo richiesta esplicita: è un checkpoint editoriale.

## Nota fissa sotto `## Sinossi`

```markdown
## Sinossi

> Questa sinossi è generata con l'intelligenza artificiale a partire dalla trascrizione
> della puntata, per aiutarti a trovare gli argomenti che ti interessano.

### 1. [primo capitolo dalla Fase 3]
...
```

## Come applicare la modifica

- Usa un editor che **inserisce e riordina** testo senza rigenerare l'intero file.
- Non rigenerare l'`index.md` con `ingest.py` dopo il merge: `ingest.py` ricostruisce il corpo
  dai file note e cancellerebbe la sinossi.
- Se la pagina contiene già una sinossi generata da una versione precedente della skill, sostituisci
  quella sinossi e riordina le sezioni secondo la struttura finale richiesta.
- Se la pagina contiene una sezione note grezza molto lunga, conserva nel corpo finale solo i link
  normalizzati; integra il resto nella sinossi o segnala le incongruenze.

## Checkpoint finale

Mostra all'utente il risultato (o il diff). Verifica:

- `## Note dell’episodio` è subito dopo il teaser/descrizione;
- i link seguono immediatamente `## Note dell’episodio`;
- ogni link usa il formato `- [Nome](https://url): descrizione`;
- `## Sinossi` arriva dopo i link, non prima;
- nel markdown non ci sono heading `# `;
- non ci sono accenti scritti con apostrofo;
- non ci sono link duplicati;
- non restano mappe/scalette grezze ridondanti;
- eventuali contenuti nota-only ambigui sono stati segnalati con 2/3 opzioni;
- non ci sono chiusure retoriche/generiche o capitoli finali di morale;
- la sinossi è proporzionata alla densità della puntata, normalmente almeno 1000 parole;
- ogni capitolo contiene dettagli concreti dalla trascrizione.

Poi valida con `python3 scripts/test-site.py` o almeno `hugo --gc --minify`, committa e pusha.
