+++
title = "52: Introduzione a Keyboard Maestro"
date = "2023-02-06T08:00:00+01:00"
episodeNumber = 52
slug = "52"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64335998/45a7a928_8347_4683_8d48_48407381cfdf.mp3"
spreakerEpisodeId = "64335998"
duration = "1:14:50"
description = "In questa puntata di inizio anno Roberto e Filippo approfondiscono una delle applicazioni (a pagamento) più utili per automatizzare e velocizzare lo svolgimento di attività su macOS: Keyboard Maestro Comunicazioni di servizio Libro su come fare podcast dell’amico Matteo Scandolin (https://amzn.to/3i"
tags = ["automazione", "macos", "produttivita", "apple"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "Ad5CPa8KFUA"
+++

## Note dell’episodio
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/): applicazione per macOS al centro della puntata, usata per creare macro con trigger e azioni.
- [Libro su come fare podcast di Matteo Scandolin](https://amzn.to/3iBKbC6): libro citato nelle comunicazioni iniziali, dedicato alla progettazione e produzione di un podcast.
- [Video-corso di David Sparks su Keyboard Maestro](https://learn.macsparky.com/p/km): corso in inglese consigliato da Filippo per imparare l’app dalle basi fino ad automazioni più complesse.
- [Forum di Keyboard Maestro](https://forum.keyboardmaestro.com): comunità ufficiale citata come luogo dove trovare esempi, soluzioni e macro condivise.
- [Wiki di Keyboard Maestro](https://wiki.keyboardmaestro.com/doku.php): documentazione tecnica ufficiale dell’app, utile per approfondire trigger, azioni e variabili.
- [Moom](https://manytricks.com/moom/): alternativa citata per il posizionamento e il ridimensionamento delle finestre su macOS.
- [Magnet](https://magnet.crowdcafe.com): utility citata per agganciare le finestre ai bordi dello schermo, in stile Windows.
- [Amethyst](https://ianyh.com/amethyst/): window manager citato da Filippo come soluzione diversa per gestire automaticamente le finestre.
- [Playlist YouTube su Keyboard Maestro](https://www.youtube.com/watch?v=C-M2ECt9gIc&list=PLa0EpEatE4TIUSob_dkMuDP7MpPceth30): serie di video citata da Filippo come risorsa pratica per vedere automazioni costruite passo passo.
- [Ultimate Hacking Keyboard](https://www.avvocati-e-mac.it/blog/2020/8/20/come-configurare-il-mac-per-usare-il-formato-americano-della-tastiera-e-non-solo): articolo di Filippo sull’uso di una tastiera con layout americano e sul cambio automatico dell’input da macOS.
- [Keyboard Maestro e la nomenclatura dei documenti](https://www.avvocati-e-mac.it/blog/2016/10/20/keyboard-maestro-e-la-nomenclatura-dei-documenti): automazione documentata da Filippo per standardizzare i nomi dei file.
- [OCR gratuito con Tesseract e Keyboard Maestro](https://www.avvocati-e-mac.it/blog/2020/5/27/ocr-gratuito-con-tesseract-e-keyboard-maestro): esempio di automazione OCR usando Keyboard Maestro e Tesseract.
- [Salvare automaticamente le email in formato EML con Airmail e Keyboard Maestro](https://www.avvocati-e-mac.it/blog/2017/11/26/salvare-automaticamente-le-email-in-formato-eml-con-airmail-e-keyboard-maestro): automazione per archiviare messaggi email in formato EML.
- [Usare Keyboard Maestro per automatizzare la creazione di PDF avanzati da testi in Markdown usando Pandoc e LaTeX](https://www.avvocati-e-mac.it/blog/2018/11/16/usare-keyboard-maestro-per-automattizzare-la-creare-pdf-avanzati-da-testi-in-markdown-usando-pandoc-e-latex): esempio citato in puntata per trasformare file Markdown in PDF tramite script.
- [TextExpander e Keyboard Maestro: i due programmi a confronto](https://www.avvocati-e-mac.it/blog/2016/10/3/textexpander-e-keyboard-maestro-i-due-programmi-a-confronto): confronto utile per capire quando usare Keyboard Maestro anche come espansore di testo.
- [Come scegliere il miglior strumento per automatizzare le operazioni sul Mac](https://www.avvocati-e-mac.it/blog/2016/2/9/come-scegliere-il-miglior-strumento-per-automatizzare-le-operazioni-sul-mac): panoramica sugli strumenti di automazione citati nel ragionamento generale della puntata.
- [Comprimere i PDF con Ghostscript ed un’automazione di Keyboard Maestro](https://www.avvocati-e-mac.it/blog/2020/5/17/comprimere-i-pdf-con-ghostscript-ed-unautomazione-di-keyboard-maestro): esempio di automazione per comprimere PDF.
- [Automatizzare le operazioni sul browser con Keyboard Maestro](https://tixx.it/automatizzare-operazioni-browser-keyboard-maestro): risorsa in italiano citata per l’automazione di moduli e pagine web.

## Sinossi[^sinossi-ai]

### 1. Due anni di podcast e il libro di Matteo Scandolin

La puntata si apre con una piccola novità per A2: al cinquantaduesimo episodio arriva una sigla, realizzata da Alex Raccuglia, già ringraziato anche per il contributo alla copertina e all’organizzazione del podcast. Filippo e Roberto usano l’occasione per guardare brevemente ai primi due anni del progetto, sottolineando quanto il podcast abbia permesso loro di conoscere persone interessanti e di costruire una rete di relazioni attorno alla tecnologia Apple, ai flussi di lavoro e alle esperienze professionali degli ospiti.

Roberto introduce poi una comunicazione di servizio: Matteo Scandolin, già amico del podcast, ha pubblicato un libro dedicato a come fare podcast dall’inizio alla fine. Roberto lo segnala come una risorsa utile per chi vuole capire il lavoro che sta dietro a una produzione audio, aggiungendo di aver contribuito in una piccola parte al progetto. Da qui nasce anche un breve scambio sul lavoro dietro le quinte di A2: stare al microfono è la parte più visibile, ma l’editing resta una delle attività più impegnative.

Filippo racconta che l’uso di Ferrite, soprattutto nella versione 3 di cui è stato beta tester, gli ha reso più sostenibile il montaggio degli episodi. La possibilità di editare su iPad con Apple Pencil gli consente di lavorare in modo più rilassato e di continuare a produrre il podcast senza percepire l’editing come un peso eccessivo.

> "È stata una bellissima esperienza che, almeno dal mio punto di vista, ha cresciuto molto."
> — Filippo, 00:02:19

### 2. Che cos’è Keyboard Maestro e perché interessa a chi lavora su Mac

Il tema centrale della puntata è Keyboard Maestro, applicazione per macOS che Roberto non usa e che Filippo presenta come uno degli strumenti più potenti per automatizzare il Mac. Roberto parte dal proprio caso: usa soprattutto abbreviazioni da tastiera e si accontenta di funzioni più semplici, mentre Filippo chiarisce subito che Keyboard Maestro va molto oltre. L’app permette di automatizzare applicazioni, siti web, testo, immagini e procedure, sia tramite comandi manuali sia tramite esecuzioni pianificate.

Filippo spiega che Keyboard Maestro può anche coprire alcune funzioni tipiche di TextExpander, quindi espandere testo, usare variabili e modelli, ma può anche interagire con menu e applicazioni come Mail. Questo lo rende potenzialmente utile anche per modelli di comunicazione o procedure ripetitive, con il limite importante che funziona solo su Mac: non esiste una controparte per iOS o iPadOS.

La logica di base viene descritta attraverso il rapporto tra trigger e azioni. Un trigger è l’evento che fa partire una macro: una scorciatoia da tastiera, un orario, una rete Wi-Fi, una periferica collegata o un altro evento. Le azioni sono invece ciò che Keyboard Maestro esegue dopo l’attivazione: aprire app, premere tasti, manipolare testo, muovere finestre, cliccare elementi dell’interfaccia, lanciare script o interagire con pagine web. Filippo paragona il principio a Comandi Rapidi e Automator, ma sottolinea che Keyboard Maestro ha una storia lunga e una profondità molto ampia.

> "Permette di automatizzare le applicazioni, siti web, testo, immagini semplici o complesse su comandi, o pianificare."
> — Filippo, 00:05:29

### 3. Prezzo, comunità, documentazione e barriera d’ingresso

Roberto introduce il costo dell’applicazione, indicandolo attorno ai 44 dollari, circa 42 euro al cambio del momento. Filippo aggiunge che gli aggiornamenti hanno un prezzo ridotto e non seguono sempre una cadenza annuale rigida. Per lui è un acquisto che continua a valere la pena sostenere, anche perché dietro l’app c’è un singolo sviluppatore che mantiene uno strumento estremamente ricco.

Una parte importante della presentazione riguarda la comunità. Filippo racconta di aver imparato molte soluzioni dal forum ufficiale, spesso prendendo spunto da macro e discussioni condivise da altri utenti. Oltre al forum, esiste una wiki molto curata, che funziona quasi come un manuale completo. Questo ecosistema è rilevante perché Keyboard Maestro può diventare complesso: le funzioni semplici sono accessibili, ma quando si entra in variabili, passaggi di dati e automazioni più articolate la curva di apprendimento si alza.

Il limite principale, per il pubblico italiano, è la lingua. L’applicazione, la documentazione principale e molte risorse formative sono in inglese. Filippo è netto: chi non conosce almeno un po’ l’inglese rischia di trovare l’acquisto poco consigliabile, perché l’interfaccia e i materiali di supporto aumentano la barriera d’ingresso. Per compensare, nelle note vengono raccolti anche articoli in italiano, soprattutto quelli scritti da Filippo su Avvocati e Mac.

### 4. L’interfaccia: gruppi, macro, editor e menu bar

Filippo passa poi a descrivere l’interfaccia. Keyboard Maestro vive in parte nella barra dei menu, da cui si accede ad alcune funzioni rapide, tra cui la cronologia degli appunti. L’app infatti può funzionare anche come clipboard manager: conserva una storia degli elementi copiati e permette di recuperarli in seguito. Nella barra dei menu possono comparire anche macro selezionate e palette, cioè pannelli richiamabili per avviare automazioni, anche se Filippo sceglie di non approfondirle in questa puntata introduttiva.

L’editor vero e proprio è organizzato in tre aree. A sinistra ci sono i gruppi, usati per organizzare le macro per contesto, applicazione o tipologia. Una macro è la singola automazione, concettualmente simile alle macro di Office. I gruppi non servono solo a fare ordine: possono essere messi in pausa, così da disattivare in blocco più automazioni quando non servono, quando manca un’applicazione o quando potrebbero entrare in conflitto con altro.

Al centro si trovano le macro del gruppo selezionato. A destra, nella parte più grande dell’interfaccia, Keyboard Maestro mostra il contenuto della macro: in modalità lettura spiega cosa fa, mentre in modalità modifica permette di costruirla, scegliendo prima il trigger e poi la sequenza di azioni. Roberto nota una somiglianza con Automator, e Filippo conferma che l’archetipo è simile, anche se Keyboard Maestro ha una propria logica e molte funzioni specifiche.

### 5. Scorciatoie da tastiera e automazioni di contesto

Il primo tipo di trigger approfondito è quello più naturale per molti utenti Mac: la scorciatoia da tastiera. Filippo spiega che il vantaggio è mantenere le mani sulla tastiera senza passare al mouse o al trackpad. macOS consente già di assegnare scorciatoie ad alcuni comandi, ma Keyboard Maestro amplia molto il concetto: una combinazione di tasti non deve corrispondere per forza a un singolo comando di un’applicazione, può invece far partire una catena di azioni che coinvolge più app e più finestre.

Un esempio concreto riguarda l’avvio di un contesto di lavoro. Se una persona usa sempre tre applicazioni per scrivere un atto, consultare PDF e accedere a una cartella di pratiche, Keyboard Maestro può aprirle tutte insieme e disporle nello schermo con dimensioni e posizioni predefinite. La scorciatoia non richiama quindi solo un’app, ma prepara un ambiente di lavoro completo.

Filippo collega questo anche alle espansioni di testo: digitando una sequenza breve, Keyboard Maestro può sostituirla con un testo più lungo, come una formula professionale o un modello. In questo modo l’app entra in un territorio vicino a TextExpander, ma resta più generale, perché la stessa infrastruttura può comandare menu, finestre, script e applicazioni.

> "La scorciatoia a tastiera non è a un comando specifico di un’applicazione, ma di fatto può scatenare una serie di azioni differenti."
> — Filippo, 00:22:04

### 6. Trigger programmati, reti Wi-Fi, cartelle, periferiche e volumi

Il secondo gruppo di esempi riguarda i trigger legati al tempo e all’ambiente. Keyboard Maestro può eseguire una macro ogni cinque minuti, ogni ora, ogni giorno o a un orario preciso. Filippo immagina procedure come avviare un backup quotidiano, inviare un report, aprire applicazioni all’inizio della giornata lavorativa o chiuderle alla sera. Roberto chiede cosa succeda se un’applicazione ha un file non salvato: Filippo spiega che dipende dall’app, ma Keyboard Maestro può anche interagire con finestre di dialogo, menu e pulsanti, quindi in teoria può essere programmato per gestire alcuni casi.

Un trigger molto utile è la rete Wi-Fi. Filippo fa l’esempio di un Mac che, collegandosi alla rete di casa o dell’ufficio, monta automaticamente dischi di rete o esegue azioni specifiche. Al contrario, quando il computer si collega a una rete non conosciuta, si può far partire una VPN. Il contesto di rete diventa quindi una condizione per cambiare comportamento senza intervento manuale.

Altri trigger riguardano file e cartelle: Keyboard Maestro può monitorare una cartella e reagire quando viene creato o aggiunto un file. Può anche rispondere al collegamento di periferiche USB. Filippo racconta il proprio uso con la Ultimate Hacking Keyboard, una tastiera meccanica con layout americano: quando la collega, Keyboard Maestro cambia automaticamente l’input di macOS da italiano ad americano. Questo apre una digressione sulle tastiere meccaniche, sull’ergonomia, sul rumore degli switch e sulla memoria muscolare, ma il punto operativo resta chiaro: il collegamento fisico di una periferica può trasformarsi in un segnale per configurare il Mac.

Anche i volumi collegati al computer possono far partire automazioni. Se si attacca un disco esterno dedicato al backup, Keyboard Maestro può avviare l’applicazione o lo script di backup. Filippo precisa però che l’app non è un sistema di backup: serve a lanciare o coordinare strumenti specifici, non a sostituirli.

### 7. Web hook, MIDI e automazioni da remoto

Filippo cita anche trigger più particolari. Uno riguarda i comandi MIDI: chi usa tastiere elettroniche o controller musicali può impiegare quei tasti per lanciare automazioni, quando non li sta usando per suonare o comporre. È una possibilità di nicchia, ma mostra quanto ampio sia il modello di Keyboard Maestro.

L’altro caso sono i web hook. L’app consente di far partire una macro da remoto tramite un URL specifico, passando attraverso un servizio esterno legato a Keyboard Maestro. Filippo ne evidenzia subito i limiti: il Mac deve essere acceso e raggiungibile, il servizio esterno deve funzionare, e dal punto di vista della sicurezza non è una funzione da usare con leggerezza. Non è una modalità che lui adotterebbe abitualmente, ma la considera interessante per scenari specifici in cui si vuole comandare un Mac a distanza, anche da iPhone o iPad, pur sapendo che l’esecuzione reale avviene sul computer su cui Keyboard Maestro è installato.

### 8. Le azioni: testo, tasti, applicazioni, finestre e browser

La seconda metà della puntata passa dalle condizioni di avvio alle azioni. Filippo chiarisce che sono troppe per essere esaminate una per una, e che la vera potenza nasce dal metterle in sequenza. Le più immediate sono quelle di manipolazione del testo: leggere dagli appunti, riscrivere negli appunti, espandere abbreviazioni, trasformare contenuti o inserirli dove serve.

Un esempio delicato riguarda i siti che impediscono di incollare password. Filippo sconsiglia di trattare le password in modo disinvolto, ma spiega che Keyboard Maestro può simulare la digitazione dei caratteri invece del copia-incolla. In questo modo il sito riceve una sequenza di tasti come se fosse digitata dall’utente, ma con una velocità molto superiore.

Le azioni di pressione dei tasti permettono di manipolare interfacce ripetitive. Filippo immagina il trasferimento di testo in una tabella Numbers: non un semplice CSV, ma un caso in cui occorre copiare porzioni specifiche, spostarsi tra celle e ripetere un modello. Keyboard Maestro può tenere traccia del punto di inserimento e proseguire in modo meccanico. Può inoltre attivare applicazioni, accedere ai menu e richiamare comandi anche quando non hanno scorciatoie native.

Per le finestre, Keyboard Maestro può ridimensionare e posizionare applicazioni in modo preciso, sovrapponendosi in parte a strumenti come Moom, Magnet o Amethyst. Filippo cita il proprio uso negli screencast: una scorciatoia centra una finestra e la imposta a una dimensione predefinita, evitando regolazioni manuali.

L’automazione dei browser è un altro punto forte. Keyboard Maestro può inserire dati in moduli web, leggere elementi di una pagina e compilare campi, soprattutto se l’HTML è strutturato correttamente. Filippo cita limiti con Firefox e con alcune interfacce del Processo Civile Telematico, ma Roberto riconosce subito l’utilità per gli architetti: se i dati anagrafici di un proprietario sono già raccolti in un formato coerente, una macro può distribuirli nei campi di un portale senza doverli copiare uno per uno.

### 9. Mouse, OCR, script e il problema della velocità

Quando non ci sono menu, scorciatoie o elementi web facilmente controllabili, Keyboard Maestro può anche muovere il mouse e cliccare. Filippo lo considera una soluzione estrema ma utile per interfacce grafiche difficili da automatizzare, come alcune app Electron o finestre prive di comandi da tastiera. L’app può perfino cercare un’immagine sullo schermo e cliccarla, anche se questo approccio non è sempre affidabile.

Filippo racconta un esempio personale: dal Finder vuole aprire iTerm direttamente nella cartella selezionata, passando da un servizio del menu contestuale. Manualmente servono diversi clic e sottomenu; con Keyboard Maestro, una scorciatoia esegue la sequenza molto più rapidamente, a patto di calibrare tempi e posizioni.

> "Fatto con Kybo Maestro, quando funziona, è un’operazione di nanosecondi."
> — Filippo, 00:53:19

La puntata tocca poi l’OCR. Keyboard Maestro ha funzioni di riconoscimento del testo, ma Filippo non le approfondisce perché oggi usa altri strumenti. Roberto osserva però che le funzioni recenti di riconoscimento testo integrate nei sistemi Apple sono diventate molto affidabili quando si tratta di copiare testo da immagini.

Un capitolo importante è quello degli script. Filippo racconta il proprio vecchio flusso con Markdown, Pandoc e LaTeX: per creare un PDF doveva aprire il terminale, raggiungere la cartella corretta, scrivere un comando lungo, generare il file e poi aprirlo per controllarlo. Con Keyboard Maestro selezionava il file nel Finder, lanciava una scorciatoia e l’app passava il file allo script già predisposto, generando e aprendo il PDF. Oggi Filippo fa una cosa simile direttamente da Vim, ma l’esempio serve a mostrare come Keyboard Maestro possa rendere accessibili procedure da terminale anche quando l’utente non vuole interagire ogni volta con la riga di comando.

Prima di chiudere la parte tecnica, Filippo sottolinea un trucco fondamentale: inserire pause. Il Mac e Keyboard Maestro sono spesso più veloci delle interfacce che comandano. Se una macro clicca un menu prima che il menu sia apparso, l’automazione fallisce non perché la logica sia sbagliata, ma perché manca ancora l’elemento da premere. A volte bastano 0,5 o 1 secondo di attesa per rendere stabile una macro.

### 10. Risorse, launcher, Hyper Key e memoria muscolare

Nell’ultima parte Filippo e Roberto raccolgono le risorse per approfondire: il corso di David Sparks, il forum, la wiki, una playlist video in inglese e gli articoli in italiano pubblicati da Filippo. La puntata si allarga poi al tema dei launcher e delle scorciatoie. Filippo cita LaunchBar, che usa da anni per aprire cartelle e navigare strutture di file digitando poche lettere; menziona anche Alfred e Raycast come alternative note. L’esempio serve a chiarire che molti strumenti si sovrappongono parzialmente: launcher, Keyboard Maestro, Comandi Rapidi e utility dedicate possono risolvere problemi simili con approcci diversi.

Filippo introduce anche il concetto di Hyper Key, attribuendolo alla tradizione di utenti avanzati come Brett Terpstra e David Sparks. L’idea è usare una combinazione molto rara, composta da Shift, Command, Option e Control, più una lettera, così da avere molte scorciatoie disponibili senza entrare in conflitto con quelle già usate dalle app. Chi non ha una tastiera programmabile può simulare questa combinazione con strumenti come Karabiner-Elements, spesso mappandola sul tasto Caps Lock.

Roberto solleva il problema pratico: più scorciatoie si creano, più bisogna ricordarsele. Filippo conferma che le automazioni devono entrare nella memoria muscolare e nella quotidianità. Non conviene creare diciotto scorciatoie tutte insieme: è meglio introdurle gradualmente, associarle a bisogni reali e usarle abbastanza spesso da renderle automatiche. Come esempio personale cita anche PopClip, richiamabile con una scorciatoia quando il menu contestuale non appare come previsto, per trasformare testo selezionato in maiuscolo, minuscolo o con altre azioni.

La chiusura reale della puntata, prima dei saluti e dei riferimenti personali, riguarda due comunicazioni di servizio interne ad A2: l’invito a lasciare recensioni e il ringraziamento a Simone, ascoltatore che ha segnalato un problema con l’icona del podcast. Filippo spiega di aver corretto i bordi dell’immagine e che dalla puntata 52 dovrebbero essere disponibili sia la nuova icona sia la nuova sigla.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
