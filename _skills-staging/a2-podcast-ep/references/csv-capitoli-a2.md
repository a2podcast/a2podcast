# Fase 3 — Formato CSV — Podcast Chapters

Il CSV per Podcast Chapters contiene **solo righe capitolo**: nessuna riga di metadata come
`PODCAST`, `AUTHOR`, `TITLE`, `DESCRIPTION` o `YEAR`.

## Struttura

```csv
Titolo capitolo,MM:SS,URL
```

- Titolo in italiano, descrittivo, normalmente 3-6 parole.
- Se la puntata dura meno di 1 ora usa `MM:SS`, per esempio `45:30`.
- Se la puntata dura 1 ora o più usa `HH:MM:SS`, per esempio `1:06:20`; il primo capitolo sarà
  `0:00:00`.
- Usa lo stesso formato timestamp per tutti i capitoli.
- Inserisci un URL solo se è direttamente pertinente a quel capitolo; altrimenti lascia la terza
  colonna vuota, mantenendo la virgola finale.
- Non usare homepage generiche quando esiste una pagina specifica del podcast, episodio, feed,
  risorsa o argomento. Se il link specifico non è verificabile, lascia il campo URL vuoto.
- Se un titolo contiene una virgola, racchiudilo tra virgolette doppie.

## Granularità

Target normale: 10-15 capitoli. Crea capitoli per intro, comunicazioni di servizio, annunci,
argomenti tecnici principali e conclusioni. Il primo capitolo parte sempre da `00:00` o
`0:00:00`.

## Marcatori utili nell'SRT

Usa cambi argomento reali e marcatori come "allora", "arriviamo a", "passiamo a", "detto questo",
"bando alle ciance", "veniamo ora a", pause narrative e frasi di transizione.

## Output

Il file va salvato come `NN/ep-NN-chapters.csv` nella cartella episodio grezza.
Non salvarlo nel repo Hugo: serve per inserirlo nell'MP3, non per il sito.
