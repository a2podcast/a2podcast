# Fase 3 — Prompt sinossi A2

Ragiona passo passo e segui un filo logico.

Il tuo scopo è creare una sinossi della trascrizione di un episodio del podcast **A2**,
presentato da **Filippo Strozzi** e **Roberto Marin**. Se c'è un ospite, considera l'ospite
parte centrale della puntata e attribuisci chiaramente le sue idee.

La sinossi deve permettere agli ascoltatori di sapere con precisione gli argomenti trattati,
ma deve anche dare **insight e conoscenza** a chi legge. Non deve essere una recensione della
puntata e non deve limitarsi a invogliare l'ascolto: deve essere utile anche come contenuto
SEO autonomo, senza sostituire il valore della puntata.

## Prima di scrivere

1. Leggi la trascrizione SRT.
2. Leggi anche le note esistenti dell'episodio: link, mappe mentali, scalette convertite in
   Markdown, appunti o research dump.
3. Ignora introduzione, saluti iniziali, saluti finali e parti di servizio non sostanziali.
4. Crea una scaletta cronologica degli argomenti trattati, con timestamp indicativi.
5. Per ogni blocco della scaletta annota:
   - tema;
   - persone coinvolte;
   - app/prodotti/servizi citati;
   - esempi concreti;
   - insight o "perle";
   - eventuali link verificati disponibili.
6. Confronta le note esistenti con la trascrizione:
   - se una mappa/scaletta ripete temi già presenti, usala solo per migliorare struttura e dettagli;
   - se aggiunge informazioni utili coerenti, integrale nel capitolo pertinente;
   - se contiene informazioni non verificabili o incongruenti, segnala il problema in Fase 4 con
     2/3 opzioni per l'utente.
7. Decidi i capitoli in base agli argomenti reali, non a un numero fisso.
8. Estrai 3-6 citazioni brevi dalla trascrizione, utili e dense, evitando battute vuote o saluti.

## Struttura

Scrivi in Markdown.

Usa capitoli numerati progressivamente:

```markdown
### 1. Titolo del capitolo

Testo del capitolo...

> "Citazione breve presa dalla trascrizione."
> — Nome, 00:12:34

- **Punto chiave:** spiegazione concreta.
- **Conseguenza pratica:** spiegazione concreta.

### 2. Titolo del capitolo
```

Regole di struttura:

- Usa solo `###` per i capitoli principali.
- Se servono sottosezioni, usa `#### 1.1 Titolo`, `#### 1.2 Titolo`.
- Non usare mai `#` o `##` dentro la sinossi: `## Sinossi[^sinossi-ai]` viene aggiunto dal merge.
- Il numero di capitoli **non è fisso**: dipende dagli argomenti reali della trascrizione.
- Crea un capitolo per ogni macrotema sostanziale; se un macrotema contiene 2-3 sottoargomenti
  tecnici, usa sottosezioni o punti elenco.
- Per episodi oltre 60 minuti di solito servono almeno 7 capitoli; per episodi oltre 90 minuti
  o molto densi possono servire 9-12 capitoli.
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
- Non giudicare la puntata: riassumi cosa viene detto e spiega perché è utile o rilevante.

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
- perle di saggezza dell'ospite o dei conduttori;
- implicazioni pratiche per professionisti, creator, utenti Mac/iPhone/iPad.

Ogni capitolo deve superare il test "cosa impara il lettore?":

- Se nomini una funzione, spiega cosa fa e perché entra nel discorso.
- Se nomini un prodotto, spiega il criterio con cui viene valutato.
- Se nomini un metodo, spiega come viene applicato.
- Se riporti un'opinione, attribuiscila e spiega il ragionamento dietro.
- Se scrivi una frase generica, sostituiscila con dettagli dalla trascrizione.

Esempio di frase **non sufficiente**:

> Lucio osserva come Apple porti funzioni simili su piattaforme diverse, ma adattandole al contesto.

Esempio di trasformazione accettabile:

> Lucio collega widget, profili di Safari e gestione dei PDF a una strategia comune: Apple porta
> funzioni simili su Mac, iPad e iPhone, ma cambia l'interfaccia in base al dispositivo. Per chi
> lavora ogni giorno tra più schermi, questo significa poter usare lo stesso concetto operativo
> senza replicare identicamente la stessa UI.

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
- Non lasciare che le note dell'episodio creino un doppio tono: se una vecchia scaletta è utile,
  assorbila nella sinossi; se è ridondante, non ricopiarla.
- Se le note sono scarne, la scaletta cronologica dalla trascrizione diventa obbligatoria:
  non compensare con commenti generici.

## Link inline nella sinossi

- Quando nomini per la prima volta un prodotto, app, servizio o risorsa con URL verificato,
  linkalo inline.
- Se il front matter contiene `guest = "slug"`, la prima occorrenza del nome ospite deve linkare:
  `https://a2podcast.it/ospiti/slug/`.
- I link ad altri episodi A2 devono usare sempre `https://a2podcast.it/NN/`.
- Non inventare link.
- Se un link non è verificato, non inserirlo inline.

## Citazioni

Inserisci 3-6 citazioni brevi in blockquote.

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

- Minimo normale: **1000 parole**.
- Episodi densi o oltre 75 minuti: 1200-1800 parole.
- Episodi molto densi o oltre 90 minuti: 1600-2200 parole, se i contenuti lo giustificano.
- Episodi brevi o poveri di contenuti possono stare sotto le 1000 parole solo se la trascrizione
  non contiene abbastanza argomenti sostanziali.
- Non allungare con commenti generici: aumenta la lunghezza con esempi, spiegazioni, criteri,
  differenze tra posizioni e dettagli verificati dalla trascrizione.

## Controllo finale

Prima di consegnare, verifica:

- nessun `#` o `##` nella sinossi;
- capitoli numerati progressivamente;
- numero capitoli proporzionato agli argomenti reali, non scelto a priori;
- niente capitolo finale di morale o commento;
- niente apostrofi al posto degli accenti;
- ospite linkato alla prima occorrenza, se presente;
- citazioni presenti e attribuite;
- nessun link inventato;
- copertura bilanciata della trascrizione;
- almeno 1000 parole salvo episodio davvero breve o povero;
- ogni capitolo insegna qualcosa di specifico o chiarisce un passaggio concreto;
- testo scritto come riassunto dettagliato, non come recensione della puntata.

> La sinossi confluisce nel file della Fase 4 — non è un file separato. Dopo averla scritta,
> procedi al merge.
