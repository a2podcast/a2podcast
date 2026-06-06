+++
title = "14: Introduzione all’automazione"
date = "2021-06-14T05:00:00+01:00"
episodeNumber = 14
slug = "14"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336046/6a5b12ed_a519_41ca_b938_a19012f6dbf7.mp3"
spreakerEpisodeId = "64336046"
duration = "52:04"
description = "In questa puntata introduciamo un argomento molto caro a Filippo: l’automazione! Oggi non entreremo troppo nel dettaglio di come creare una automazione o degli specifici programmi per automatizzare con macOS e iOS / iPadOS ma ci soffermeremo sul perché è importante automatizzare e quali “trappole” d"
tags = ["automazione", "macos", "ios", "produttivita", "workflow"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "ViG_mL8rlJU"
+++

> In questa puntata introduciamo un argomento molto caro a Filippo: l’automazione! Oggi non entreremo troppo nel dettaglio di come creare una automazione o degli specifici programmi per automatizzare con macOS e iOS / iPadOS ma ci soffermeremo sul perché è importante automatizzare e quali “trappole” dobbiamo evitare.

## Note dell’episodio

- [Automazione — Wikipedia](https://it.wikipedia.org/wiki/Automazione): voce enciclopedica citata come riferimento di base per la definizione del concetto.
- [xkcd 1319 — Automation](https://xkcd.com/1319/): fumetto che illustra la trappola classica: il tempo speso a costruire l'automazione supera il tempo risparmiato.
- [xkcd 1205 — Is It Worth the Time?](https://xkcd.com/1205/): tabella pratica per valutare se automatizzare ha senso in base alla frequenza e al tempo risparmiato.
- [AppleScript — Documentazione Apple](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/AppleScriptX.html): riferimento tecnico ufficiale per il linguaggio di automazione introdotto nel 1993.
- [Script Editor — Manuale Utente Apple](https://support.apple.com/it-it/guide/script-editor/welcome/mac): guida ufficiale all'ambiente di sviluppo e test degli AppleScript.
- [macOS Automation — Sal Soghoian](http://macosautomation.com): sito del responsabile storico dell'automazione in Apple, con esempi pratici delle potenzialità di AppleScript e Automator.
- [Automator — Guida utente Apple](https://support.apple.com/it-it/guide/automator/welcome/mac): documentazione ufficiale di Automator, l'ambiente di automazione visuale introdotto con Mac OS X Tiger 10.4.
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/): potente applicazione di automazione per macOS con trigger avanzati, simulazione tastiera, loop e condizioni logiche.
- [Hazel — Noodlesoft](https://www.noodlesoft.com/): monitora cartelle e applica regole automatiche ai file al loro arrivo.
- [TextExpander](https://textexpander.com/): espansione del testo con supporto a snippet dinamici e piccole automazioni.
- [LaunchBar — Objective Development](https://www.obdev.at/launchbar): launcher per macOS con supporto ad automazioni, apertura cartelle e integrazione con Keyboard Maestro.
- [Alfred](https://www.alfredapp.com/): launcher alternativo a LaunchBar con sistema di workflow per automazioni più articolate.
- [Comandi Rapidi (Shortcuts) — Apple](https://support.apple.com/it-it/guide/shortcuts/welcome/ios): app ufficiale Apple per l'automazione su iOS e iPadOS, evoluzione dell'ex Workflow.
- [URL Schemes iOS/iPadOS — MacStories](https://www.macstories.net/ios/a-comprehensive-guide-to-all-120-settings-urls-supported-by-ios-and-ipados-13-1/): guida completa di Federico Viticci ai link di sistema per automatizzare azioni tra app prima dell'era Comandi Rapidi.
- [ToolboxPro](https://toolboxpro.app): estensione per Comandi Rapidi con azioni avanzate non disponibili nativamente.
- [Scriptable](https://scriptable.app/): app gratuita di Simon Støvring per automatizzare iOS tramite JavaScript.
- [Pythonista](http://omz-software.com/pythonista/): ambiente Python completo per iOS, utile per automazioni avanzate.
- [Zapier](https://zapier.com/): piattaforma cloud per connettere app web e automatizzare flussi di lavoro senza codice.
- [IFTTT](https://ifttt.com/): servizio cloud di automazione basato su trigger "se questo, allora quello".
- [n8n](https://n8n.io): piattaforma di automazione cloud self-hostable e open source, segnalata dall'ascoltatore Ale R.
- [Microsoft Power Automate](https://flow.microsoft.com): soluzione Microsoft per l'automazione di processi aziendali e integrazione tra servizi cloud.

---

## Sinossi[^sinossi-ai]

### 1. Cos'è l'automazione: la metafora della ricetta

Filippo apre la puntata introducendo l'automazione come uno degli argomenti a lui più cari. La definizione che propone è volutamente concreta: un'automazione è una ricetta che facciamo eseguire al computer. Così come una ricetta indica ingredienti e passi in sequenza — prendere la farina, le uova, il latte, mescolare — allo stesso modo un'automazione descrive al computer esattamente cosa fare, in che ordine, con quali elementi, per produrre un risultato.

L'obiettivo è fare lavorare il computer al posto nostro. Filippo sottolinea che usare il computer come uno strumento puramente manuale, ripetendo ogni volta le stesse operazioni, è come usare uno scalpello per fare un lavoro che una macchina potrebbe svolgere in millisecondi. Il collegamento con la puntata precedente è immediato: anche l'espansione del testo, già discussa in precedenza, è di fatto una piccola automazione.

Roberto integra con una riflessione sul tempo: ogni secondo risparmiato, sommato nel corso di una giornata e di un anno, si accumula in quantità significative. Il principio, attribuito ad Alex Raccuglia, è che il tempo è la risorsa più preziosa, e le automazioni sono uno degli strumenti principali per recuperarne.

> "Invece di svolgere noi il lavoro, diamo delle indicazioni passo passo. Pensate a una ricetta."
> — Filippo, 00:03:50

### 2. Perché automatizzare: uniformità, velocità e riduzione degli errori

Filippo illustra i quattro vantaggi principali dell'automazione attraverso esempi tratti dalla sua pratica quotidiana da avvocato.

Il primo vantaggio è l'**uniformità**: un'automazione garantisce che dalle stesse premesse si ottenga sempre lo stesso risultato. L'esempio concreto è la creazione automatica di sottocartelle per ogni nuova pratica legale: anziché cercare ogni volta un modello, copiarlo, incollarlo e rinominarlo, una singola scorciatoia di tastiera genera in automatico l'intera struttura di cartelle prevista. Il computer compie questa operazione in millisecondi contro i venti secondi o più che richiederebbe un umano.

Il secondo vantaggio è l'**eliminazione degli errori**: svolgere manualmente la stessa operazione decine di volte espone inevitabilmente al rischio di sbagliare — un numero datato male, una cifra digitata storta. Un'automazione ben progettata non commette errori che non siano stati introdotti in fase di progettazione.

Il terzo vantaggio è la **velocità**: i computer elaborano in millisecondi ciò che all'utente richiederebbe decine di secondi. Filippo porta come esempio avanzato un'automazione con Keyboard Maestro che copia dati da un foglio Excel e li incolla in Word, simulando fisicamente i movimenti del mouse e le operazioni di copia-incolla, ma a una velocità impossibile per un umano.

Il quarto vantaggio è **evitare le attività ripetitive banali**: Filippo cita un caso reale in cui si è trovato un elenco di cento persone con nome davanti al cognome, in ordine alfabetico per nome — inutile e tedioso da correggere manualmente. Con un'automazione, spostare il cognome in prima posizione e riordinare l'elenco richiede pochi secondi invece di dieci minuti.

> "Il computer lo fa in millisecondi. Quello che è un'operazione che per noi fisicamente richiede del tempo, al computer richiede un istante."
> — Filippo, 00:07:30

### 3. Quando ha senso automatizzare: la trappola del tempo speso

La puntata affronta apertamente il rischio opposto: investire più tempo a costruire un'automazione di quanto se ne risparmierebbe usandola. Roberto descrive il grafico xkcd 1319 come la rappresentazione perfetta di questa trappola: in teoria si perde tempo a scrivere il codice, poi si guadagna tempo libero; in pratica, tra testing, debugging, variabili impreviste e idee migliori emerse durante lo sviluppo, il tempo libero spesso svanisce.

Filippo riconosce di essersi trovato spesso in questa situazione: si parte con un'idea, si cerca su internet come altri hanno risolto problemi simili, si scopre che nessuno ha risolto esattamente quel problema, si assembla una soluzione ibrida da più fonti, e alla fine si è prodotto qualcosa di più complesso di quello che serviva. La consolazione è che le automazioni si riusano: una soluzione costruita per un problema tende a diventare il punto di partenza per il successivo.

La linea guida pratica che emerge è quella del grafico xkcd 1205: più spesso si svolge un'attività e più tempo richiede ogni volta, più automatizzarla ha senso. L'esempio è eloquente: se un problema richiede mezz'ora al giorno e si impiega un giorno intero a costruire l'automazione, nel giro di poche settimane il conto torna già in positivo.

> "Invece di aver risolto il problema originale, vi siete relativamente complicati la vita."
> — Filippo, 00:17:10

### 4. AppleScript: la colla tra le applicazioni macOS

La rassegna degli strumenti di automazione su macOS comincia con AppleScript, introdotto nel 1993 come successore di HyperCard. Filippo ne descrive il meccanismo fondamentale: ogni applicazione che supporta AppleScript espone un dizionario di comandi, e il linguaggio permette di fare dialogare applicazioni diverse, passando dati dall'una all'altra.

L'esempio che porta è dettagliato e autobiografico: volendo aprire file Markdown salvati in DEVONthink direttamente in Vim dentro iTerm, ha costruito un AppleScript che — selezionato un file in DEVONthink — estrae il percorso del file nelle sottocartelle interne del database, apre una nuova finestra di iTerm e le passa il comando completo per lanciare Vim puntando a quel file specifico. Un'operazione che richiede la comprensione del funzionamento interno di due applicazioni diverse e della loro interfaccia AppleScript.

Roberto ammette apertamente di essersi perso a metà spiegazione, ma Filippo sottolinea il valore storico e pratico del linguaggio: nel periodo difficile di Apple, AppleScript era il sistema che permetteva alle redazioni grafiche di far dialogare Excel, QuarkXPress e altri strumenti, generando cataloghi e listini in automatico. Era un unicum nel panorama dei sistemi operativi con interfaccia grafica, e ha contribuito a tenere Apple in vita durante gli anni più critici.

Il punto di ingresso consigliato è il sito macOS Automation di Sal Soghoian — già responsabile dell'automazione in Apple prima di essere licenziato quando il suo ruolo venne soppresso — dove sono documentati esempi pratici delle potenzialità di AppleScript, dalla generazione automatica di presentazioni Keynote alla creazione di link a email selezionate in Mail.

### 5. Automator: l'automazione visuale a blocchi

Automator, nato anch'esso da un'idea di Sal Soghoian e introdotto con Mac OS X Tiger 10.4, rappresenta l'approccio opposto ad AppleScript: nessun codice, tutto drag and drop. L'utente costruisce sequenze di azioni concatenandole visualmente — fai A, poi B, poi C — come blocchi Lego.

Filippo descrive in concreto l'automazione per la creazione di sottocartelle: un'azione prende la cartella selezionata nel Finder, le azioni successive creano ciascuna una sottocartella con il nome predefinito. Dieci azioni, dieci sottocartelle, zero codice.

Automator supporta anche le Quick Action, azioni rapide eseguibili direttamente dal Finder selezionando un file e scegliendo l'azione dal menu contestuale. Rimane tuttavia in uno stato di sviluppo fermo da quando Soghoian lasciò Apple: le funzionalità esistenti continuano a funzionare, ma non arrivano nuove azioni da parte degli sviluppatori terzi. La previsione di Filippo è che Comandi Rapidi, già acquisito con il suo team di sviluppo da Apple e portato su iOS come evoluzione dell'ex Workflow, possa arrivare su macOS creando un sistema unificato tra le piattaforme.

> "Automator è un sistema costruito a blocchi: ci sono tante piccole azioni che voi potete concatenare l'una all'altra per ottenere il risultato."
> — Filippo, 00:35:00

### 6. Keyboard Maestro, Hazel, TextExpander, LaunchBar e Alfred

Filippo raggruppa questi strumenti come un insieme di applicazioni di automazione avanzata per macOS, ognuna con una specializzazione.

**Keyboard Maestro** è il più potente del gruppo. Il suo punto di forza è la varietà di trigger: il Mac si connette al Wi-Fi di casa e monta automaticamente il disco di rete; si collega una tastiera USB con layout americano e il sistema passa automaticamente al layout corrispondente; si carica un URL specifico e parte un'azione sul Mac anche da remoto, via webhook. Supporta condizioni logiche (se/allora), loop e simulazione completa della tastiera e del mouse. Costa circa quaranta euro e Filippo lo raccomanda esplicitamente.

**Hazel** fa una cosa sola ma la fa molto bene: monitora una cartella e applica regole ai file in arrivo. Supporta AppleScript e altri linguaggi per estendere le sue capacità.

**TextExpander** è lo strumento di espansione del testo già discusso nella puntata precedente, qui citato come esempio di automazione semplice ma potente. Filippo menziona un'automazione di David Spark che, digitando una sequenza di caratteri, crea automaticamente un link URL scheme all'email selezionata in Mail.

**LaunchBar** e **Alfred** sono launcher: si invocano con una scorciatoia di tastiera, compare una barra simile a Spotlight, si digitano poche lettere e si lancia qualsiasi cosa — applicazioni, cartelle, automazioni, azioni di Keyboard Maestro. Alfred ha sviluppato nel tempo un sistema di workflow più ricco; LaunchBar rimane più essenziale. Filippo accenna di stare valutando di passare da LaunchBar ad Alfred per ragioni economiche.

Chiude la rassegna macOS con i linguaggi di programmazione tradizionali — shell, Python, JavaScript — che permettono di scrivere script veri e propri, spesso usati in combinazione con gli strumenti precedenti per automatizzare il lancio di sequenze complesse.

### 7. iOS e iPadOS: Comandi Rapidi e URL Scheme

Su iOS e iPadOS, l'ecosistema di automazione ruota attorno a due sistemi: Comandi Rapidi (ex Workflow, acquisito da Apple e integrato nel sistema operativo) e gli URL Scheme.

Gli **URL Scheme** sono link che puntano a un'applicazione invece che a una pagina web. `drafts://` è lo scheme per Drafts, `x-devonthink-item://` per DEVONthink. Funzionano sia su iOS che su macOS, rendendoli uno dei pochi meccanismi di automazione veramente cross-platform. Filippo descrive il suo uso pratico: da Toodledo, con il supporto Markdown per i link, crea riferimenti a specifiche email che si aprono correttamente sia su iPhone che su iPad che su Mac. Prima che Comandi Rapidi diventasse l'applicazione di riferimento, gli URL Scheme erano l'unico modo per passare dati tra app su iOS, ma richiedono la codifica degli spazi e dei caratteri speciali, rendendoli poco accessibili.

**Comandi Rapidi** ha superato questa complessità offrendo un'interfaccia visuale simile ad Automator ma più moderna e con un ecosistema di azioni molto più ampio. L'acquisizione di Workflow ha portato in Apple non solo l'applicazione ma l'intero team di sviluppo — un segnale, secondo Filippo, che la piattaforma è considerata strategica. Gli strumenti complementari citati per chi vuole estenderne le capacità sono ToolboxPro, Scriptable (JavaScript) e Pythonista (Python).

La previsione di Filippo è una futura convergenza: se Comandi Rapidi dovesse arrivare su macOS in forma nativa, un'automazione creata su iPhone potrebbe funzionare anche sul Mac, eliminando la frammentazione attuale tra i sistemi operativi. La convivenza con AppleScript e Automator è ritenuta probabile, visto che i linguaggi storici raramente scompaiono del tutto.

### 8. Automazione cloud: Zapier, IFTTT e alternative

La parte conclusiva — tagliata dall'episodio principale per ragioni di durata ma disponibile nella diretta YouTube — riguarda l'automazione cloud. Zapier e IFTTT permettono di collegare servizi web diversi senza codice, con un approccio accessibile anche ai principianti e il vantaggio della neutralità rispetto alla piattaforma. Filippo segnala anche n8n, alternativa open source e self-hostable suggerita dall'ascoltatore Ale R., e Microsoft Power Automate per contesti aziendali.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
