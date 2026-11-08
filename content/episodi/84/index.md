+++
title = "iOS, iPadOS e macOS 27 con Lucio Bragagnolo"
date = 2026-11-09T07:00:00+01:00
episodeNumber = 84
slug = "84"
audioUrl = ""
spreakerEpisodeId = "76244298"
duration = "1:04:14"
description = "Con Lucio Bragagnolo, Filippo e Roberto discutono iOS 27, iPadOS 27 e macOS Golden Gate. Dall’interfaccia di iPhone Duo alle prove sul Mac, parlano di spazio su disco, fine delle app Intel, disponibilità di Siri AI in Europa e uso del contesto dello schermo."
tags = ["ios", "ipados", "macos", "apple-silicon", "intelligenza-artificiale", "ospite"]
draft = false

[params]
hasTranscript = true
guest = "lucio-bragagnolo"
youtubeId = "sXTntrbjuXY"
+++

> Con Lucio Bragagnolo, Filippo e Roberto discutono iOS 27, iPadOS 27 e macOS Golden Gate. Dall’interfaccia di iPhone Duo alle prove sul Mac, parlano di spazio su disco, fine delle app Intel, disponibilità di Siri AI in Europa e uso del contesto dello schermo.

## Note dell’episodio

- Il keynote e le sessioni in cui Apple presenta le novità comuni ai suoi sistemi. [WWDC26](https://developer.apple.com/videos/wwdc2026/)
- La raccolta di piccoli cambiamenti annunciati alla WWDC, organizzati a partire da una schermata della presentazione. [WWDC26: The Small Things](https://blog.oneberri.com/posts/wwdc26-the-small-things)
- Le osservazioni di Jason Snell sui ritocchi di sistema e su come il lavoro per Siri AI abbia dato impulso a miglioramenti di Spotlight e Comandi Rapidi. [WWDC 2026: Emptying the notebook about AI, bug fixes, and more](https://sixcolors.com/post/2026/06/wwdc-2026-emptying-the-notebook-about-ai-bug-fixes-and-more/)
- Il pieghevole Apple con due schermi, usato in puntata per discutere come iOS cambi con il formato del dispositivo. [iPhone Duo](https://www.apple.com/it/iphone-duo/)
- Le novità di interfaccia, ricerca e prestazioni per i tre sistemi discussi in puntata. [iOS 27](https://www.apple.com/it/os/ios/), [iPadOS 27](https://www.apple.com/it/os/ipados/), [macOS 27 Golden Gate](https://www.apple.com/it/os/macos/)
- L’utility usata da Filippo per controllare come è occupato l’SSD e distinguere lo spazio libero da quello recuperabile. [DaisyDisk – Purgeable space](https://daisydiskapp.com/guide/4/en/PurgeableSpace/)
- Come macOS conserva e libera le istantanee locali di Time Machine su APFS. [Informazioni sulle istantanee locali di Time Machine sul Mac](https://support.apple.com/it-it/guide/mac-help/mh35933/27/mac/27)
- Le segnalazioni di spazio occupato dai modelli di Apple Intelligence su alcune configurazioni Mac all’uscita di Golden Gate. [Apple Intelligence Taking Up 30GB+ on Some Macs Running macOS 27](https://www.macrumors.com/2026/09/23/apple-intelligence-30gb-some-macs-macos-27/)
- Il calendario della fine del supporto generale alle app Intel tramite Rosetta e le indicazioni di Apple agli sviluppatori. [Upcoming changes to Rosetta support for Intel-based macOS apps](https://developer.apple.com/news/?id=w5ngl9k2)
- Requisiti di Siri AI per dispositivo, lingua e area geografica. [Requirements for Siri AI (Beta)](https://support.apple.com/en-mide/148218)
- I limiti di utilizzo previsti per alcune funzioni di Apple Intelligence. [Learn about Apple Intelligence usage limits](https://support.apple.com/en-us/127901)
- I modelli di Apple e il trattamento delle richieste tra Mac e infrastruttura cloud. [Foundation Models updates](https://developer.apple.com/documentation/updates/foundationmodels), [Apple Intelligence and privacy on Mac](https://support.apple.com/en-ie/guide/mac-help/mchlfc0d4779/mac)
- La sessione Apple su come le app espongono azioni e forniscono a Siri informazioni su ciò che è visibile sullo schermo. [Explore advanced App Intents features for Siri and Apple Intelligence](https://developer.apple.com/videos/play/wwdc2026/343/)
- Il server MCP locale usato da Filippo per collegare un modello alle app del Mac, tra cui Note, Promemoria e Calendario. [Macuse](https://macuse.app/)
- La guida alle funzioni di modifica delle immagini in Foto, compresa la Reinquadratura spaziale che ha colpito Roberto. [Ripulire, estendere e reinquadrare le foto su iPhone](https://support.apple.com/it-it/guide/iphone/xy0grrlxue5w/ios)
- Il racconto di Lucio sulla registrazione, con il collegamento alla diretta. [Risentirsi senza risentirsi](https://macintelligence.org/post/2026-09-24-risentirsi-senza-risentirsi/)

## Sinossi[^sinossi-ai]

### 1. Un keynote per tutti i sistemi

Filippo e Roberto invitano [Lucio Bragagnolo](https://a2podcast.it/ospiti/lucio-bragagnolo/) a discutere gli aggiornamenti Apple pochi giorni dopo il loro arrivo. Lucio propone di giudicare l’intelligenza artificiale integrata nei dispositivi dalla facilità con cui si usa ogni giorno. Roberto parte da una scelta del keynote della WWDC26. Apple ha presentato molte novità trasversalmente, passando con meno enfasi del solito da un sistema operativo all’altro. Per lui la regia della presentazione suggerisce una possibile convergenza e riapre la domanda su un futuro Apple OS.

Lucio ricorda da quanto tempo circola quella previsione. Una funzione può avere le stesse basi su iPhone, iPad e Mac e assumere forme diverse quando cambiano lo schermo, i comandi e il modo in cui si tiene il dispositivo. Richiama anche il precedente di «Windows Everywhere» per distinguere la possibilità tecnica di estendere una piattaforma dalla qualità dell’esperienza sui singoli dispositivi. Legge il keynote soprattutto come un modo per rendere visibili i miglioramenti comuni. [WWDC26](https://developer.apple.com/videos/wwdc2026/)

### 2. iPhone Duo, Liquid Glass e app che si ridimensionano

Filippo usa iPhone Duo come esempio. A telefono chiuso nota il dock laterale e una diversa disposizione dei controlli. Aprendolo, il dispositivo si avvicina all’iPad per lo spazio a disposizione e per il modo in cui può mostrare le app. Roberto è colpito persino dall’animazione di apertura, che gli ricorda un libro, e rivede nel pieghevole una distanza rispetto all’iOS rigido delle origini. [iPhone Duo](https://www.apple.com/it/iphone-duo/)

> «hardware e software viaggiano insieme»
> — Filippo, 00:08:04

La conversazione su Liquid Glass parte dalle preferenze di trasparenza e leggibilità. Lucio racconta che il grado di trasparenza è diventato persino argomento di conversazione tra utenti. Roberto, che lavora con modelli tridimensionali, preferisce ridurre l’effetto e dare priorità alle risorse disponibili per il proprio lavoro. Su iPad, Lucio nota un altro effetto della maggiore flessibilità di iOS. Le app nate per iPhone possono adattarsi meglio a una finestra ridimensionata o a un iPad tenuto in orizzontale con la tastiera. L’ipotesi è che il lavoro richiesto dagli schermi del Duo finisca per migliorare anche l’uso delle app su altri dispositivi. [iPadOS 27](https://www.apple.com/it/os/ipados/)

### 3. Apple Silicon tra grafica e modelli locali

La discussione sull’hardware nasce da due interessi diversi. Filippo segue i Mac per eseguire modelli in locale e guarda anche al costo della memoria. Roberto è interessato alla grafica e prende spunto da un titolo sui futuri chip M6 per chiedersi quanto una GPU integrata nello stesso sistema del processore possa avvicinarsi alle prestazioni di una scheda dedicata. Presenta il titolo come uno spunto e ragiona sulle implicazioni per chi usa la grafica nel proprio lavoro, mentre gran parte dell’attenzione del settore è rivolta alla velocità con cui i chip eseguono i modelli di IA.

### 4. Le prove di Golden Gate e i dati di sistema

Filippo racconta di avere iniziato con le beta per sviluppatori su un MacBook Air M4. L’interfaccia gli è sembrata più reattiva fin dalle prime versioni. La sua è un’impressione d’uso, senza misure comparative. Sul Mac Studio la differenza gli è parsa meno evidente e passando a un iPad Pro M5 ha fatto fatica a isolare l’effetto dell’aggiornamento, anche perché il precedente iPad Pro del 2018 gli sembrava già adeguato. Roberto, che di solito aspetta il primo aggiornamento successivo al rilascio, ascolta le prove prima di decidere se fare il salto. [macOS 27 Golden Gate](https://www.apple.com/it/os/macos/)

Il problema più tangibile per Filippo rimane l’archiviazione. Mostra il caso del MacBook Air con SSD da 256 GB in cui vede circa 131 GB sotto «Dati di sistema». In quella categoria possono rientrare file diversi, fra cui cache, modelli e spazio associato alle istantanee locali. Filippo usa DaisyDisk per controllare come è occupato il disco e racconta che alcune app gli hanno segnalato spazio insufficiente anche quando una parte risultava recuperabile per macOS. [DaisyDisk – Purgeable space](https://daisydiskapp.com/guide/4/en/PurgeableSpace/), [Istantanee locali di Time Machine](https://support.apple.com/it-it/guide/mac-help/mh35933/27/mac/27)

Lucio usa ancora un M1 con un SSD da 1 TB. Riconosce il comportamento, ma sulla sua macchina ha più margine e nota meno le conseguenze. Chiede che la gestione delle cache tenga conto della capacità effettiva del disco e che sistema e app concordino meglio su quanto spazio sia disponibile quando bisogna salvare un file.

> «la pulizia dovrebbe avvenire più spesso sulle macchine meno capaci»
> — Lucio, 00:26:28

### 5. Il peso dei modelli e il passaggio dalle app Intel

Roberto aveva avuto una buona esperienza con iPadOS 26 su un iPad di nona generazione e pensava di aggiornare subito il Mac. Lo fanno esitare le segnalazioni uscite al lancio di Golden Gate. Alcuni utenti vedevano diversi gigabyte occupati dai modelli di Apple Intelligence, con casi discussi nell’ordine di 14–30 GB. Le cifre citate riguardano configurazioni differenti. Il punto per Roberto è poter decidere se dedicare quella parte dell’SSD a funzioni che potrebbe usare poco, soprattutto su un Mac con capacità ridotta. [Segnalazioni sullo spazio usato da Apple Intelligence](https://www.macrumors.com/2026/09/23/apple-intelligence-30gb-some-macs-macos-27/)

Il passaggio dai Mac Intel riporta la discussione a un vantaggio quotidiano. Roberto usa un MacBook Air M2 senza ventola e apprezza poter lavorare più velocemente, al fresco e in silenzio. Sul piano della compatibilità, Golden Gate è l’ultima versione di macOS con supporto generale di Rosetta per le applicazioni solo Intel. Il passaggio interessa anche chi usa già Apple Silicon, se nel suo flusso di lavoro restano app o componenti privi di una versione nativa. [Upcoming changes to Rosetta support for Intel-based macOS apps](https://developer.apple.com/news/?id=w5ngl9k2)

### 6. Siri AI in Europa e il valore dell’integrazione

Roberto chiede a Filippo come sia andata la prova di Siri AI. Filippo spiega che lingua e disponibilità gli hanno impedito di farne una prova approfondita e che si è fatto un’idea iniziale dalle esperienze riportate da altri. Apple distingue le piattaforme nella propria documentazione. Nell’Unione Europea Siri AI in beta è disponibile su Mac compatibili e su Vision Pro con dispositivo e Siri impostati in inglese. Per iOS, iPadOS e watchOS Apple indica ancora l’esclusione iniziale dell’UE. Le altre funzioni di Apple Intelligence possono avere requisiti propri. [Requirements for Siri AI (Beta)](https://support.apple.com/en-mide/148218)

Lucio guarda alla situazione anche dal punto di vista di chi ha comprato più dispositivi per usarli insieme. Cita iPhone Mirroring, già assente nell’UE al momento della registrazione, come esempio di integrazione il cui valore per l’utente dipende proprio dall’abbinamento tra telefono e computer. Roberto riprende più avanti il confronto con Windows. Ricorda i pochi Mac isolati nella sua facoltà di architettura e racconta di avere trovato, tornando a Windows per lavoro, una situazione più aperta anche nel collegamento con l’iPhone. Entrambi auspicano un’intesa che renda disponibili più funzioni.

### 7. Modelli locali e Private Cloud Compute

Filippo osserva che i modelli Apple, sviluppati con il contributo delle tecnologie Gemini, sono progettati per lavorare con il sistema e le applicazioni. Per le sue prove su Mac trova interessanti anche modelli aperti più capaci in compiti generali. Lucio distingue l’app Siri dall’insieme delle funzioni integrate, come Intelligenza visiva e gli strumenti di scrittura. L’elaborazione avviene sul dispositivo quando possibile e le richieste più complesse possono ricorrere a Private Cloud Compute. [Foundation Models updates](https://developer.apple.com/documentation/updates/foundationmodels), [Apple Intelligence and privacy on Mac](https://support.apple.com/en-ie/guide/mac-help/mchlfc0d4779/mac)

Per Lucio conta anche il tempo che passa tra la domanda e la risposta. Per un dubbio semplice, come chiedere se il pipistrello sia un mammifero, poter interrogare il sistema sul posto gli sembra più proporzionato che aprire una chat dedicata. In cambio i modelli occupano spazio sul disco. Il giudizio è più prudente se l’uso previsto è quello di un agente capace di svolgere attività articolate sul Mac.

> «azioniamo il bazooka per sparare la formica»
> — Lucio, 00:44:52

### 8. App Intents, Macuse e fotoritocco

Filippo si concentra sulle operazioni che le applicazioni possono esporre attraverso App Intents e sui dati di cui l’assistente ha bisogno per svolgerle. Le confronta con un esperimento che sta facendo sul Mac Studio. Con il server MCP Macuse, un modello locale può raggiungere Note, Promemoria e Calendario attraverso strumenti dedicati. Roberto immagina invece una possibile evoluzione di Comandi Rapidi, che gli piacerebbe usare come punto di collegamento tra le automazioni di sistema e strumenti esterni. Sono due modi di ragionare sulle azioni che si possono affidare a un assistente e sulle informazioni che gli si rendono accessibili. [App Intents e Siri](https://developer.apple.com/videos/play/wwdc2026/343/), [Macuse](https://macuse.app/)

Roberto racconta anche quale dimostrazione lo ha colpito di più da utente che lavora spesso con le immagini. È la possibilità di cambiare l’inquadratura dopo lo scatto, modificando la composizione della foto. La funzione Reinquadra entra nella conversazione come esempio concreto di intelligenza artificiale collocata dentro uno strumento già usato nel lavoro di tutti i giorni. [Ripulire, estendere e reinquadrare le foto su iPhone](https://support.apple.com/it-it/guide/iphone/xy0grrlxue5w/ios)

### 9. Da Steve Jobs a John Ternus

Roberto chiede a Lucio come Steve Jobs avrebbe potuto accogliere l’idea di un sistema operativo comune. Lucio immagina che Jobs avrebbe preferito esperienze su misura. Ricorda la sua opposizione allo stilo sul primo iPhone e la accosta al supporto per Apple Pencil su iPhone Duo. Per lui il paragone mostra quanto cambi il senso di un accessorio quando cambiano le dimensioni e gli usi di un dispositivo.

Nel passaggio da Jobs a Cook e poi a Ternus, Lucio vede continuità nell’idea di un computer personale che dia alle persone strumenti per lavorare e che metta l’accessibilità al centro. A questa storia collega la sua preferenza per un’IA a portata di mano, integrata con l’hardware e capace di risolvere domande semplici nel punto in cui si presentano.

> «una bicicletta della mente potenziata»
> — Lucio, 00:56:54

### 10. Chiedere a Siri di ciò che si ha sullo schermo

Lucio torna infine sul contesto personale e su come Siri possa interpretare riferimenti a ciò che l’utente sta guardando. L’idea è poter fare una domanda nella situazione in cui nasce. Quando un’app espone al sistema il contesto della schermata, l’assistente può collegare la richiesta all’elemento visibile. Roberto sottolinea quanto questa possibilità conti su smartphone e tablet, dove la maggior parte dell’interazione passa dallo schermo. Per entrambi, poter indicare a voce ciò che si ha già davanti cambia il modo in cui si formula una richiesta. [Explore advanced App Intents features for Siri and Apple Intelligence](https://developer.apple.com/videos/play/wwdc2026/343/)

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
