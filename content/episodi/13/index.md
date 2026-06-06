+++
title = "13: 10 utility per Mac"
date = "2021-05-31T05:00:00+01:00"
episodeNumber = 13
slug = "13"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64335987/1e5911d1_bb48_4948_969a_ae68cd6a06b0.mp3"
spreakerEpisodeId = "64335987"
duration = "59:33"
description = "In questa puntata Roberto e Filippo di 10 utility da avere sul vostro Mac."
tags = ["mac", "app", "produttivita"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "0uDG5H_jqcg"
+++

## Note dell’episodio

- [Homebrew](https://brew.sh): gestore di pacchetti open source per macOS che permette di installare applicazioni non disponibili sull'App Store tramite riga di comando; utile anche per reinstallare tutto su un nuovo Mac con `brew list` e `brew install`.
- [Articolo Homebrew Cask su Avvocati e Mac](https://www.avvocati-e-mac.it/blog/2019/8/14/scaricare-tutti-o-quasi-i-programmi-da-installare-fuori-dallappstore-con-homebrew-cask): guida di Filippo su come installare applicazioni fuori dall'App Store con Homebrew Cask.
- [TripMode](https://tripmode.ch): utility per controllare quali app accedono a Internet; versione 3 compatibile con Big Sur e M1, licenza singola da 14 €.
- [Hazel](https://www.noodlesoft.com): automazione per cartelle e file su Mac; rinomina documenti, sposta screenshot, archivia email in base a regole visive. Hazel 5 costa 42 $, Family Pack 65 $, upgrade 20 $.
- [Hidden Bar](https://apps.apple.com/us/app/hidden-bar/id1452453066?mt=12): nasconde le icone in eccesso nella menu bar; gratuito, disponibile sul Mac App Store, compatibile con Big Sur e M1.
- [Bartender](https://www.macbartender.com): alternativa a pagamento a Hidden Bar; aggiunge scorciatoie da tastiera per accedere alle icone della menu bar.
- [Amethyst](https://ianyh.com/amethyst/): tiling window manager open source per macOS; gestisce le finestre automaticamente e tramite scorciatoie da tastiera senza usare il mouse.
- [AlDente](https://github.com/davidwernhart/AlDente): limita la percentuale massima di carica della batteria quando il Mac è collegato alla corrente; gratuito, compatibile con Big Sur e M1.
- [Timing](https://timingapp.com/): tracciamento automatico del tempo passato su Mac, per applicazione e progetto; 79 €/anno, con sincronizzazione tra più Mac.
- [Toggl Track](https://toggl.com): alternativa gratuita citata da Roberto per tracciare manualmente il tempo con timer, app mobile e reportistica.
- [Amphetamine](https://apps.apple.com/it/app/amphetamine/id937984704?mt=12): impedisce al Mac di andare in sleep; gratuito, programmabile, disponibile sul Mac App Store.
- [TextExpander 5](https://textexpander.com/textexpander-standalone-apps/): versione standalone dell'espansore di testo, 44,95 $; consigliata rispetto alla versione 6 ad abbonamento per uso personale.
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/): automazione avanzata per Mac con funzione di espansione del testo inclusa; ~37 €, licenza permanente.
- [Sostituzione Testo di macOS](https://support.apple.com/it-it/guide/mac-help/mh27071/mac): espansione testo nativa di Apple, sincronizzata tra Mac e iOS/iPadOS; meno potente ma gratuita e immediata.
- [NightOwl](https://nightowl.kramser.xyz): cambia tra modalità chiara e scura con un clic; gratuito con donazioni, permette di escludere singole app dalla modalità notturna.
- [Time Machine Editor](https://tclementdev.com/timemachineeditor/): permette di programmare gli orari di backup di Time Machine; gratuito con donazioni, compatibile con Big Sur.

## Sinossi[^sinossi-ai]

### 1. Presentazione della puntata e contesto

Il tredicesimo episodio di A2 nasce da un'idea di Roberto, che ha proposto un formato volutamente leggero: una carrellata di dieci utility per Mac consigliate dai due conduttori, senza approfondimenti tecnici estremi ma con il taglio pratico del professionista che usa questi strumenti ogni giorno. Filippo avverte subito che alcune delle sue scelte hanno richiesto un certo coraggio nella selezione, e che eventuali approfondimenti su singole applicazioni potranno arrivare in puntate future, se il riscontro del pubblico lo giustificherà. Roberto ricorda che nella puntata 7 si era già parlato di utility per la manutenzione del Mac, ma precisa che le applicazioni di oggi sono tutte diverse, tranne una.

### 2. Homebrew: installare il Mac da riga di comando

Filippo apre con Homebrew, definendolo il suo primo consiglio per chiunque usi un Mac. Si tratta di un gestore di pacchetti open source che opera da terminale e permette di installare applicazioni non presenti sull'App Store con un singolo comando. Il valore principale, spiega Filippo, non è tanto la riga di comando in sé, quanto la possibilità di ricostruire l'intero ambiente software su un nuovo Mac in pochissimo tempo: basta digitare `brew list` per ottenere la lista di tutto ciò che è installato, copiare il risultato e rieseguirlo su una macchina nuova. Homebrew si occupa di scaricare, installare e in molti casi anche aggiornare le applicazioni. Il comando `brew upgrade` controlla il repository e aggiorna tutto ciò che ha una nuova versione disponibile.

Roberto chiede come funziona la gestione degli aggiornamenti rispetto all'App Store: Filippo chiarisce che il processo è in due fasi — prima `brew update` per sincronizzare il catalogo, poi `brew upgrade` per installare le nuove versioni. Le singole applicazioni di solito mostrano le novità al primo avvio, come avviene con Hazel, Keyboard Maestro o Timing. L'assenza di un'interfaccia uniforme è compensata dal fatto che molte applicazioni professionali non vogliono o non possono stare nell'App Store per via del sandboxing Apple, e Homebrew risolve elegantemente il problema.

> "Homebrew è un modo veloce di installare tutto. Nella beta di Big Sur ho installato tutto attraverso Homebrew e ci ho messo molto poco."
> — Filippo, 00:06:29

### 3. TripMode: tenere sotto controllo il traffico Internet

Roberto presenta TripMode, un'utility per la menu bar che mostra in tempo reale tutte le applicazioni e i servizi che cercano di comunicare con Internet e permette di bloccarli selettivamente. L'icona diventa rossa non appena un'app non autorizzata tenta di uscire dalla rete locale. Roberto descrive tre scenari pratici: durante una chiamata Skype, quando si vuole riservare tutta la banda a un solo programma; in mobilità con il tethering del cellulare, per evitare che aggiornamenti da gigabyte consumino i dati; e in montagna o in contesti con connettività limitata, dove anche applicazioni come Foto possono divorare la banda inosservate.

Filippo aggiunge di usare Little Snitch, uno strumento più avanzato che mostra anche su mappa geografica a quali server si collegano le applicazioni. Il risultato, ammette, è "un po' angosciante", perché molte app telefonano a casa anche quando non sono in esecuzione attiva.

> "Quando mettete un'applicazione di questo tipo, vedete quanta roba esce dal vostro computer e cominciate a spaventarvi."
> — Roberto, 00:13:15

TripMode 3 è compatibile con Big Sur e i chip M1; per sistemi precedenti va usata la versione 2. La licenza singola costa 14 €, con opzioni multi-utente fino a 49 €.

### 4. Hazel: automazione delle cartelle e archiviazione digitale

Filippo introduce Hazel come uno degli strumenti centrali del suo sistema paperless, già citato nelle puntate dedicate all'archiviazione digitale. Hazel monitora cartelle specifiche e, al verificarsi di determinate condizioni sui file in entrata, esegue azioni automatiche. L'interfaccia è visuale: non servono competenze di programmazione, perché le regole si costruiscono combinando condizioni come tipo di file, contenuto testuale, data di creazione o nome.

Gli esempi concreti che Filippo porta sono tre. Primo, la rinominazione automatica dei PDF scansionati: se il documento ha un testo riconoscibile via OCR e contiene una data, Hazel può estrarre quella data e rinominare il file nel formato `AAAA-MM-GG`. Secondo, lo spostamento degli screenshot: qualsiasi cattura schermo sul desktop viene automaticamente trasferita in una cartella apposita dopo 24 ore, e cancellata dopo un ulteriore periodo. Terzo, l'archiviazione delle email: una mail salvata come PDF nella cartella di input viene riconosciuta in base al numero di pratica e archiviata automaticamente nella sottocartella giusta, compresa quella del mittente — nell'esempio portato, tutte le email con "Roberto Marin" nel nome finiscono nella cartella corrispondente.

Roberto nel frattempo cerca il prezzo: Hazel 5 costa 42 $ la licenza singola, 65 $ per il Family Pack (fino a 5 membri dello stesso nucleo familiare), 20 $ per l'upgrade da versioni precedenti. Filippo precisa di essere ancora sulla versione 4, compatibile con Catalina, e di pianificare l'aggiornamento alla 5 contestualmente al passaggio a Big Sur, poiché la nuova versione del sistema operativo ha rimosso il pannello delle preferenze di sistema da cui Hazel operava in precedenza.

### 5. Hidden Bar e Bartender: ordine nella menu bar

Roberto passa a Hidden Bar, un'applicazione gratuita — suggerita proprio da lui a Filippo — che nasconde le icone in eccesso nella barra dei menu. Con il crescere delle utility installate, la menu bar può diventare affollata; Hidden Bar permette di spostare le icone meno usate oltre una linea separatrice invisibile, rendendole accessibili con un clic sulla freccia. L'applicazione è disponibile sul Mac App Store, pesa 7,4 MB, ed è compatibile con Big Sur e M1.

Filippo aggiunge che esiste anche Bartender, l'alternativa a pagamento, che ha un'ulteriore funzione: associare le icone della menu bar a scorciatoie da tastiera personalizzate, cosa altrimenti impossibile su macOS. Questo lo renderebbe interessante per chi vuole interagire con la barra senza usare il mouse. Roberto menziona anche Vanilla, un'altra alternativa, scartata però per un fastidioso glitch grafico che faceva ricomparire tutte le icone nascoste quando si cambiava schermo o si attivava la modalità a tutto schermo.

> "Ho abbandonato Bartender e sono passato alla versione gratuita. Dal Mac App Store quindi non avete nessun tipo di problema."
> — Filippo, 00:25:39

### 6. Amethyst: gestire le finestre con la tastiera

Filippo porta Amethyst, un tiling window manager open source per macOS. L'applicazione ridispone automaticamente le finestre ogni volta che se ne apre una nuova, mantenendo tutte le finestre aperte visibili sullo schermo senza sovrapposizioni, salvo le finestre di dialogo e configurazione che si sovrappongono comunque per natura. La struttura di base prevede un'applicazione principale in una metà dello schermo e le altre che si suddividono l'altra metà, con possibilità di configurare il layout.

La vera potenza, sottolinea Filippo, è la gestione via tastiera: spostare il focus da una finestra all'altra, ridimensionare le proporzioni tra le finestre, trasferire una finestra su un monitor diverso — tutto senza toccare il mouse. Utile soprattutto per chi scrive di professione e lavora contemporaneamente su un documento, una mappa mentale e una cartella di riferimento. L'unica eccezione sono alcune applicazioni come Firefox, che non rispettano le API di gestione delle finestre di macOS e causano comportamenti inattesi. Amethyst è alla versione 0.15, tecnicamente ancora in fase beta, ma stabile nell'uso quotidiano.

Roberto ammette che nel suo caso, dove si lavora principalmente con grafica e applicazioni a tutto schermo, l'utilità sarebbe limitata, ma riconosce il valore per chi ha un flusso di lavoro testuale intenso.

### 7. AlDente: preservare la batteria dei portatili

Roberto introduce AlDente, un'utility che limita la percentuale massima di carica della batteria quando il Mac è collegato alla corrente. Il razionale è semplice: le batterie agli ioni di litio si degradano più rapidamente quando rimangono a lungo al 100% di carica. Per chi usa il portatile quasi sempre collegato alla presa — come Roberto in ufficio — tenere la batteria ferma all'80% può contribuire a prolungarne la vita utile. La percentuale limite è configurabile dall'utente a piacere.

AlDente è gratuita, compatibile con Big Sur e M1, e si installa tramite Homebrew (nessuna distribuzione App Store). Roberto precisa di essere ancora in fase di test e che le ultime versioni di macOS (da Catalina in poi) includerebbero una funzione simile a livello di sistema, ma senza la granularità di un'applicazione dedicata.

### 8. Timing: tracciamento automatico del tempo

Filippo presenta Timing come la sua utility preferita per la rendicontazione professionale. A differenza dei tradizionali time tracker che richiedono di avviare e fermare manualmente un timer, Timing monitora in background tutto ciò che avviene sul Mac — quali applicazioni si usano, quali documenti si aprono, quali siti si visitano — e ricostruisce automaticamente come è stata spesa la giornata. Il costo è di 79 € all'anno, ma per un avvocato che fattura a ore, spiega Filippo, il ROI è immediato.

Il caso d'uso principale è la verifica della redditività: se su una pratica si sono incassati 1.000 € ma si sono lavorate 100 ore, il bilancio è negativo; se invece le ore sono state due, quella è stata una pratica eccellente. Timing supporta la sincronizzazione tra più Mac con lo stesso account, utile per chi divide il lavoro tra studio e casa. Il limite rilevante è l'assenza di un'applicazione nativa per iOS/iPadOS: esiste una versione web, ma richiede l'avvio manuale del timer.

Filippo confronta Timing con "Tempo di utilizzo" di Apple, che su macOS risulta impreciso — ad esempio conta come tempo attivo un'applicazione aperta in background — e non offre la granularità necessaria a un professionista. Come alternativa gratuita, Roberto suggerisce Toggl, che funziona con timer manuale ma ha un'app per iOS e una buona reportistica.

> "Se nella posizione 1 ho portato a casa 1000 euro ma ho lavorato 100 ore, ovvio che non ci ho guadagnato. Se invece ci ho lavorato 2 ore, è stata una posizione molto positiva."
> — Filippo, 00:35:48

### 9. Amphetamine: impedire il sonno del Mac

Roberto presenta Amphetamine come evoluzione di Caffeine, l'utility classica per impedire al Mac di entrare in sleep. La differenza è la programmabilità: si può specificare per quanto tempo tenere il Mac sveglio, in quali condizioni farlo, e associare il comportamento a eventi specifici. Gratuita, disponibile sul Mac App Store, occupa 6,6 MB. Roberto la usa principalmente durante i rendering e quando deve registrare lo schermo — ad esempio per catturare un webinar da rivedere in seguito.

### 10. Espansione del testo: tre livelli di investimento

Filippo dedica l'ultimo slot a una categoria invece che a un singolo prodotto, presentando tre soluzioni per l'espansione del testo in ordine crescente di complessità e costo. Il principio comune è digitare poche lettere di abbreviazione per ottenere in output un blocco di testo preimpostato — firma dell'email, intestazione di una pratica, data nel formato corretto, indirizzi, codice fiscale.

La prima opzione è **TextExpander 5**, la versione standalone a 44,95 $, che Filippo preferisce alla versione 6 ad abbonamento (3-4 €/mese): quest'ultima sincronizza i dati sui server di TextExpander in America, mentre la 5 gestisce la sincronizzazione autonomamente. TextExpander funziona anche su Windows e iOS, il che lo rende interessante per ambienti misti o team che condividono risposte standard.

La seconda è **Keyboard Maestro**, a circa 37 €, che include l'espansione del testo tra le molte funzioni di automazione. Filippo lo usa dalla versione 7 e lo aggiorna a ogni release; per chi ha già bisogno di automazioni più ampie, è l'opzione più conveniente.

La terza è la **Sostituzione Testo nativa di macOS e iOS**, gratuita e sincronizzata tra le due piattaforme via iCloud. Meno potente delle prime due, ma sufficiente per le abbreviazioni di base: email, numero di telefono, via di casa, firma semplice. Roberto la usa attivamente — doppia chiocciola per l'email, `_CF` per il codice fiscale, `pvirgola tel` per il cellulare.

Filippo consiglia di usare la `X` come prefisso delle abbreviazioni, ispirandosi al metodo di Merlin Mann: la X è rara nelle parole italiane comuni e non richiede il tasto shift, il che la rende ideale come marcatore. Un altro utilizzo pratico è la formattazione automatica: Filippo ha un'espansione che converte la parola "latex" scritta in minuscolo nel formato tipografico corretto (LaTeX), evitando errori di battitura.

> "Io digito XCS e automaticamente viene espansa tutta la firma, con numero di telefono, mail, PEC e qualifiche. Con tre lettere."
> — Filippo, 00:41:53

### 11. NightOwl e Time Machine Editor: gli extra di Roberto

Roberto chiude con NightOwl, un'applicazione gratuita che permette di passare con un clic dalla modalità chiara a quella scura di macOS. La funzione aggiuntiva rispetto all'impostazione di sistema è la possibilità di escludere singole applicazioni dalla modalità notturna: Roberto porta l'esempio di "Podcast Cleaner Pro", sviluppato senza supporto per il dark mode e quindi tenuto in modalità chiara anche quando il resto del sistema è in modalità scura.

Come bonus — giustificato dal fatto che è stato lui a proporre la puntata — Roberto aggiunge Time Machine Editor, un'utility gratuita per programmare gli orari di backup di Time Machine. Il backup automatico ogni ora può interferire con il lavoro in corso e sollecita inutilmente i dischi rigidi a piatti se non si è al computer. Time Machine Editor permette di spostare il backup a orari precisi: ad esempio, all'1:05 di notte e alle 18:35, lasciando la macchina libera durante le ore di lavoro. Roberto non l'ha ancora testata personalmente ma la considera molto promettente.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
