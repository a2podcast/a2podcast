# Fase 3 — Prompt sinossi A2

Ragiona passo passo e segui un filo logico.

Il tuo scopo è creare una sinossi della trascrizione di un episodio del podcast **A2**,
presentato da **Filippo Strozzi** e **Roberto Marin**. Se c'è un ospite, considera l'ospite
parte centrale della puntata e attribuisci chiaramente le sue idee.

La sinossi deve permettere agli ascoltatori di sapere con precisione gli argomenti trattati.
Deve essere un riassunto dettagliato della trascrizione, non un commento editoriale sulla
puntata.

## Prima di scrivere

1. Leggi la trascrizione SRT.
2. Ignora introduzione, saluti iniziali, saluti finali e parti di servizio non sostanziali.
3. Crea mentalmente una scaletta cronologica degli argomenti trattati, con timestamp indicativi.
4. Suddividi la puntata nelle sue parti fondamentali.
5. Cerca le "perle" dell'ospite, se presente; altrimenti cerca le migliori intuizioni di
   Filippo e Roberto.
6. Estrai 2-5 citazioni brevi dalla trascrizione, utili e dense, evitando battute vuote o saluti.

## Struttura

Scrivi in Markdown.

Usa capitoli numerati progressivamente:

```markdown
### 1. Titolo del capitolo

Testo del capitolo...

> "Citazione breve presa dalla trascrizione."
> — Nome, 00:12:34

- **Punto chiave:** spiegazione.
- **Altro punto:** spiegazione.

### 2. Titolo del capitolo
```

Regole di struttura:

- Usa solo `###` per i capitoli principali.
- Se servono sottosezioni, usa `#### 1.1 Titolo`, `#### 1.2 Titolo`.
- Non usare mai `#` o `##` dentro la sinossi: `## Sinossi` viene aggiunto dal merge.
- Crea 5-10 capitoli, in base alla durata e densità della puntata.
- I capitoli devono seguire l'ordine reale della trascrizione.
- Ogni capitolo deve corrispondere a un blocco reale della conversazione.
- Non creare un capitolo finale di sintesi, bilancio, morale o commento editoriale.
- L'ultimo capitolo deve riassumere l'ultimo argomento sostanziale trattato nella puntata.

## Stile

- Tono colloquiale, amichevole e concreto.
- Scrivi in italiano naturale, con lettere accentate vere: `è`, `é`, `à`, `ò`, `ù`, `ì`.
- Non scrivere mai `e'`, `piu'`, `qualita'`, `perche'`, `puo'`.
- Evita linguaggio da IA: "è importante notare", "in conclusione", "in sintesi",
  "approfondiamo".
- Evita commenti retorici o meta-commenti sulla puntata.
- Non scrivere frasi tipo:
  - "La puntata costruisce la base del podcast..."
  - "Il risultato operativo della puntata è..."
  - "Il valore della puntata sta..."
  - "Una fotografia del momento..."
  - "Un workflow da artigiano..."
  - "A2 propone di..."
- Non giudicare la puntata: riassumi cosa viene detto.

## Contenuto

La sinossi deve essere densa di contenuti.

Per ogni capitolo includi, quando presenti:

- strumenti, app, servizi e prodotti citati;
- problemi pratici affrontati;
- esempi concreti raccontati in puntata;
- differenze di opinione tra Filippo, Roberto e l'ospite;
- decisioni operative o consigli pratici;
- passaggi tecnici spiegati;
- limiti, dubbi e cautele;
- perle di saggezza dell'ospite o dei conduttori.

Formatta per punti quando aiuta la leggibilità:

```markdown
- **Risultati incoraggianti ma costosi:** spiegazione concreta.
- **La gestione delle risorse:** spiegazione concreta.
```

## Bilanciamento

La sinossi deve coprire in modo proporzionato tutta la puntata.

- Non dedicare più del 25% della sinossi a un solo macrotema, salvo che quel tema occupi davvero
  più del 25% della trascrizione.
- Se una puntata tratta molti argomenti, distribuisci i capitoli tra tutti i blocchi principali.
- Se un tema è solo una digressione breve, non trasformarlo in un capitolo dominante.
- Se ci sono note dell'episodio molto ricche, usale per riconoscere i temi, ma dai priorità alla
  trascrizione.

## Link

- Quando nomini per la prima volta un prodotto, app, servizio o risorsa con URL verificato,
  linkalo inline.
- Se il front matter contiene `guest = "slug"`, la prima occorrenza del nome ospite deve linkare:
  `https://a2podcast.it/ospiti/slug/`.
- I link ad altri episodi A2 devono usare sempre `https://a2podcast.it/NN/`.
- Non inventare link.
- Se un link non è verificato, non inserirlo inline.

## Citazioni

Inserisci 2-5 citazioni brevi in blockquote.

Regole:

- Devono venire dalla trascrizione.
- Puoi correggere solo errori evidenti di riconoscimento vocale.
- Devono essere brevi e utili.
- Devono distinguersi dal testo normale.
- Devono avere attribuzione e timestamp.

Formato:

```markdown
> "Svuotare il cervello è il primo pezzo del sistema."
> — Andrea Ciraolo, 00:42:18
```

## Lunghezza

- Obiettivo normale: 700-1000 parole.
- Episodi molto densi: fino a 1200 parole.
- Episodi brevi o poveri di contenuti: 500-700 parole.
- Non allungare con commenti generici: se mancano contenuti, resta più breve.

## Controllo finale

Prima di consegnare, verifica:

- nessun `#` o `##` nella sinossi;
- capitoli numerati progressivamente;
- niente capitolo finale di morale o commento;
- niente apostrofi al posto degli accenti;
- ospite linkato alla prima occorrenza, se presente;
- citazioni presenti e attribuite;
- nessun link inventato;
- copertura bilanciata della trascrizione;
- testo scritto come riassunto dettagliato, non come recensione della puntata.

> La sinossi confluisce nel file della Fase 4 — non è un file separato. Dopo averla scritta,
> procedi al merge.
