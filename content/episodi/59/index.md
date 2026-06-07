+++
title = "59: Velocizzare la scrittura con le espansioni del testo"
date = "2023-05-15T05:00:00+01:00"
episodeNumber = 59
slug = "59"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64335977/68214cb9_7f43_4b47_9bc2_530adf7baf53.mp3"
spreakerEpisodeId = "64335977"
duration = "1:04:41"
description = "In questa puntata Roberto e Filippo esaminano le c.d. sostituzioni del testo. Digitare una serie di lettere e, a queste, si sostituisce un testo differente, abitualmente più lungo. Esaminato come funziona il principio di base ed alcuni trucchi utili da conoscere, il magico duo esaminerà i software p"
tags = ["espansioni testo", "produttivita", "mac", "iphone", "automazione"]
draft = false

[params]
 hasTranscript = true
 youtubeId = "Fj1R_KxMlxU"
+++

> In questa puntata Roberto e Filippo esaminano le c.d. sostituzioni del testo. Digitare una serie di lettere e, a queste, si sostituisce un testo differente, abitualmente più lungo. Esaminato come funziona il principio di base ed alcuni trucchi utili da conoscere, il magico duo esaminerà i software per implementare le sostituzioni sul tuo Mac, iPhone e iPad.

## Note dell’episodio
- [Sostituzione testo](https://support.apple.com/it-it/guide/iphone/iph6d01d862/ios): funzione Apple usata per creare abbreviazioni che si espandono automaticamente su iPhone, iPad e Mac.
- [TextExpander](https://textexpander.com/): app specializzata per espansioni di testo, snippet condivisi e automazioni di scrittura.
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/): strumento di automazione per Mac usato anche per macro ed espansioni di testo.
- [A2 episodio 52](https://a2podcast.it/52/): episodio richiamato nel confronto su automazioni e scrittura assistita.
- [Dr. Drang: From TextExpander to Keyboard Maestro again](https://leancrew.com/all-this/2021/07/from-textexpander-to-keyboard-maestro-again/): articolo citato per il passaggio da TextExpander a Keyboard Maestro.
- [Script in Python](https://github.com/rjames86/textexpander_to_keyboardmaestro): utility per convertire snippet TextExpander in macro Keyboard Maestro.
- [Espanso](https://espanso.org): text expander open source e multipiattaforma discusso tra le alternative specialistiche.
- [Allo stato non c’è un sistema rapido di convertire le espansioni di testo da TextExpander ad Espanso](https://github.com/espanso/espanso/discussions/1232): discussione sul problema della migrazione degli snippet verso Espanso.
- [Typinator](https://www.ergonis.com/typinator): app per macOS dedicata a espansioni di testo, correzioni e automazioni nella scrittura.
- [Typinator aggiornata](https://www.macitynet.it/typinator-aggiornata-lapplicazione-mac-che-scrive-al-posto-vostro-2/): aggiornamento dell'app citata tra le alternative macOS.
- [Espanso problemi con alcune app](https://neilzone.co.uk/2023/04/fixing-espanso-incomplete-text-replacement): nota tecnica sui casi in cui Espanso non completa correttamente l'espansione.

## Sinossi[^sinossi-ai]

### 1. Che cosa sono le espansioni di testo

Filippo e Roberto partono dal nome: in inglese si parla di text expansion, mentre Apple usa l'espressione "sostituzione del testo". Il principio è semplice: si digita una stringa breve e il sistema la sostituisce con un testo più lungo o più preciso. Può essere una firma, un indirizzo, una formula ricorrente, una mail standard, un frammento di codice o anche una parola con accenti difficili da digitare.

> "la sostituzione del testo permette di risolvere senza pensarci"

La puntata distingue subito le espansioni dalle scorciatoie da tastiera. Le scorciatoie eseguono comandi; le sostituzioni producono testo. Roberto collega il tema al mondo CAD, dove ricordare abbreviazioni fa risparmiare tempo, ma Filippo porta il discorso sul lavoro quotidiano: se una frase viene scritta spesso, conviene smettere di riscriverla ogni volta.

### 2. Il sistema Apple e la scelta delle abbreviazioni

La funzione nativa Apple è dentro le impostazioni della tastiera e si sincronizza tra Mac, iPhone e iPad. Questo la rende comoda per chi usa più dispositivi: una sostituzione creata su Mac può servire anche mentre si scrive un messaggio su iPhone. Il vantaggio principale è l'assenza di configurazione complessa, ma il limite è che non offre tutte le funzioni avanzate delle app specialistiche.

> "la possibilità di sincronizzare i cosiddetti snippet"

Filippo e Roberto discutono anche il prefisso da usare. Molti utenti anglofoni usano il punto e virgola prima dell'abbreviazione, perché è raro all'inizio di una parola; su tastiere italiane e dispositivi mobili, però, può essere meno pratico. Per questo emerge l'idea di usare una X iniziale, più facile da digitare e abbastanza improbabile nelle parole comuni.

### 3. Usi pratici: errori, testi ricorrenti e lavoro professionale

Gli esempi sono concreti: correggere errori frequenti, inserire indirizzi, preparare intestazioni, rispondere a messaggi ripetitivi, scrivere formule legali o tecniche e produrre blocchi strutturati. Roberto richiama il problema della memoria: se lo snippet è troppo arbitrario, non verrà usato; se è breve ma riconoscibile, diventa parte naturale della scrittura.

Un buon sistema di espansioni richiede quindi ordine. Bisogna decidere convenzioni coerenti, evitare abbreviazioni che si attivano per errore e creare snippet solo quando il beneficio è reale. Il rischio non è avere troppe automazioni, ma costruire un archivio che non si ricorda più.

> "Ho, per esempio, degli snippet per l'intestazione YAML"

### 4. TextExpander, Keyboard Maestro e condivisione

La seconda parte passa alle app dedicate. TextExpander viene presentato come soluzione storica e potente, soprattutto quando servono snippet condivisi tra persone o gruppi di lavoro. Questo è il punto che la funzione Apple non copre bene: in uno studio, in un'azienda o in un team editoriale, poter distribuire testi standard e aggiornarli centralmente può valere più della singola abbreviazione personale.

Keyboard Maestro entra come alternativa per chi vuole unire espansioni e automazioni più ampie su Mac. L'articolo di Dr. Drang e lo script di conversione da TextExpander mostrano un problema tipico: quando si investe anni in snippet, migrare da uno strumento all'altro non è banale.

> "condividere questi snippet di testo"

### 5. Espanso, Typinator e il compromesso tra potenza e manutenzione

Filippo e Roberto chiudono con le alternative. Typinator resta una scelta macOS solida per chi vuole un'app dedicata. Espanso, invece, è interessante perché open source e multipiattaforma, ma richiede più confidenza con file di configurazione e YAML.

> "Espanso è una roba un po' più da smanettoni"

La conclusione operativa è pragmatica: per molti utenti bastano le sostituzioni Apple, soprattutto se il bisogno è personale e trasversale tra Mac, iPhone e iPad. Le app dedicate diventano utili quando servono logiche più complesse, snippet condivisi, compatibilità multipiattaforma o integrazione con automazioni già esistenti.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
