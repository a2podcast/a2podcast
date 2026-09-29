+++
title = "Dalla voce al testo: dettatura, trascrizione e IA"
date = 2026-10-26T07:00:00+01:00
episodeNumber = 83
slug = "83"
audioUrl = ""
spreakerEpisodeId = "75432009"
duration = "1:06:15"
description = "Filippo e Roberto confrontano dettatura e trascrizione: strumenti Apple, Whisper e Parakeet, app gratuite e a pagamento. Dai memo vocali ai podcast, discutono rielaborazione con IA, automazioni, qualità dell’audio e riservatezza."
tags = ["audio", "scrittura", "intelligenza-artificiale", "automazione", "privacy", "podcasting"]
draft = false

[params]
hasTranscript = true
guest = ""
youtubeId = "5g8cyEoCrxo"
+++

> Filippo e Roberto confrontano dettatura e trascrizione: strumenti Apple, Whisper e Parakeet, app gratuite e a pagamento. Dai memo vocali ai podcast, discutono rielaborazione con IA, automazioni, qualità dell’audio e riservatezza.

## Note dell’episodio

- [A2 47: Dettatura vocale con i dispositivi Apple](https://a2podcast.it/47/): precedente approfondimento richiamato all’inizio, dedicato soprattutto alla dettatura.
- [Dettare messaggi e documenti sul Mac](https://support.apple.com/it-it/guide/mac-help/mh40584/mac): documentazione Apple su attivazione, lingua, microfono e scorciatoia della dettatura.
- [Visualizzare le trascrizioni dei memo vocali su iPhone](https://support.apple.com/it-it/guide/iphone/iph00953a982/ios): guida alla consultazione e copia del testo associato alle registrazioni.
- [Registrare e trascrivere audio in Note su iPhone](https://support.apple.com/it-it/guide/iphone/iphbe11247b5/ios): funzioni di Note menzionate insieme a Memo Vocali e Comandi Rapidi.
- [Comandi Rapidi](https://support.apple.com/it-it/guide/shortcuts/welcome/ios): manuale dello strumento discusso per avviare dettatura o trascrizione e salvare il risultato nella destinazione scelta.
- [A2 24: Le basi di Comandi Rapidi](https://a2podcast.it/24/): prima puntata consigliata per costruire una propria automazione.
- [A2 26: Comandi Rapidi per Calendario](https://a2podcast.it/26/): ulteriore approfondimento richiamato nel passaggio sulle automazioni.
- [Whisper](https://github.com/openai/whisper): repository ufficiale del sistema di riconoscimento vocale OpenAI, uno dei motori discussi nella panoramica.
- [NVIDIA Parakeet TDT 0.6B v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3): modello multilingue della famiglia Parakeet, usata da Filippo nel proprio flusso locale di trascrizione.
- [FluidVoice](https://altic.dev/fluid): applicazione gratuita e open source per dettare su macOS con motori selezionabili; le funzioni opzionali di rielaborazione vanno distinte dalla trascrizione locale.
- [WhisperDictation](https://sam-pop.github.io/WhisperDictation/): alternativa gratuita menzionata da Filippo nella panoramica delle interfacce per dettare sul Mac.
- [Ferrite Recording Studio](https://www.wooji-juice.com/products/ferrite/): applicazione usata da Filippo per montare il podcast e citata come possibilità di registrazione su iPhone.
- [MacWhisper](https://www.macwhisper.com/): applicazione per trascrivere file, controllare il testo insieme all’audio e integrare la trascrizione in automazioni tramite CLI.
- [Wispr Flow](https://wisprflow.ai/): dettatura con rielaborazione del testo, discussa attraverso l’esempio di un commento orale trasformato in una restituzione scritta.
- [Superwhisper](https://superwhisper.com/): applicazione citata fra le alternative per dettatura e trasformazione del parlato.
- [Transcriber](https://ulti.media/transcriber/): software di Alex Raccuglia, utilizzato da Filippo e richiamato per il suo orientamento ai contenuti audio e video.
- [Transcriptionist](https://www.wooji-juice.com/products/transcriptionist/): applicazione di Wooji Juice discussa per l’integrazione con Ferrite e il lavoro su registrazioni con tracce separate.
- [Audio Hijack: blocco Transcribe](https://rogueamoeba.com/support/manuals/audiohijack/?page=transcribe): trascrizione delle sorgenti audio catturate, con identificazione degli interlocutori quando gli ingressi sono separati.
- [Skill audio-transcription](audio-transcription.zip): archivio con le istruzioni locali per scegliere lo strumento di trascrizione in base al computer e generare file TXT, SRT, VTT e JSON.

## Sinossi[^sinossi-ai]

### 1. Dettare mentre si scrive oppure trascrivere una registrazione

Filippo e Roberto riprendono il tema della [dettatura vocale](https://a2podcast.it/47/), già affrontato da A2, per distinguerlo dal lavoro su registrazioni audio. La dettatura inserisce testo mentre la persona parla, per esempio nel campo di un messaggio. La trascrizione parte invece da un audio già registrato e lo trasforma in materiale scritto da consultare e riutilizzare.

> “la trascrizione è una trasformazione in parole di un file audio di una registrazione”
> — Roberto, 00:03:01

La distinzione cambia le esigenze. Chi detta vuole restare nel punto in cui sta lavorando; chi trascrive può voler conservare il riferimento all’audio, correggere termini, cercare un passaggio o ricavare sottotitoli. I conduttori ricordano l’esperienza dei software di dettatura precedenti, come Dragon, che richiedevano familiarità con comandi, punteggiatura e addestramento sulla voce.

Roberto racconta di aver usato la dettatura per bozze di relazioni tecniche. Filippo, che scrive velocemente alla tastiera, spiega perché non l’ha adottata come strumento abituale di redazione: formulare a voce una frase già completa richiede un modo diverso di pensare. La voce può essere molto utile senza dover sostituire ogni attività di scrittura.

### 2. Whisper, Parakeet e le risorse del computer

I due ripercorrono l’evoluzione dei sistemi di riconoscimento attraverso [Whisper](https://github.com/openai/whisper) e la famiglia [Parakeet](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3). Filippo racconta di aver usato entrambi e di preferire attualmente Parakeet per il proprio flusso: sul suo hardware, una registrazione lunga può essere trascritta in pochi minuti. Sono tempi della sua esperienza, non una misura valida per ogni computer o modello.

La scelta riguarda dimensione e qualità del modello, spazio occupato, memoria e potenza della macchina. Filippo ricorda che ottenere buoni risultati con modelli più impegnativi poteva richiedere tempi vicini alla durata dell’audio. La trascrizione di un messaggio breve e quella di un intero archivio di podcast pongono quindi problemi diversi.

Roberto e Filippo discutono anche i sistemi Apple e le novità attese al momento della registrazione, comprese le beta degli OS 27. Filippo descrive una prova sul proprio MacBook Air e collega il buon risultato anche ai microfoni e alla riduzione del rumore. Non distingue con certezza quale versione del riconoscimento stia operando: la qualità dell’audio è un elemento osservabile, mentre funzioni annunciate, lingue e disponibilità restano da verificare sulle rispettive configurazioni.

### 3. Locale, cloud e secondo passaggio con un modello linguistico

Il riconoscimento può avvenire sul computer, con un modello disponibile localmente, oppure attraverso un servizio remoto a cui viene inviato l’audio. Nel primo caso contano hardware e spazio; nel secondo contano anche connessione e trasferimento dei dati. Roberto porta il limite concreto della propria connessione: la rapidità apparente di un servizio dipende dal percorso completo, non soltanto dalla capacità del server.

Filippo separa poi la trascrizione dalla rielaborazione. Un motore converte il parlato in testo; un modello linguistico può effettuare un secondo passaggio per correggere formulazioni, eliminare riempitivi o trasformare una bozza in un messaggio più ordinato. L’esempio è una mail dettata in modo colloquiale e riscritta con tono professionale, mantenendo i contenuti che si vogliono esprimere.

> “scrivere un pensiero è diverso che dirlo”
> — Roberto, 00:22:34

Roberto racconta anche una conversazione vocale con un assistente durante un viaggio: il dialogo gli lascia un testo riutilizzabile. Filippo chiarisce il rapporto tra audio, testo e risposta sintetizzata, poi richiama il flusso di A2: correggere i termini tecnici della trascrizione prima di ricavare una sinossi. Il passaggio da parlato a scritto comprende dunque operazioni diverse, che non vanno confuse con una semplice copia parola per parola.

### 4. La dettatura inclusa nei dispositivi Apple

La parte pratica comincia dalla [dettatura su Mac](https://support.apple.com/it-it/guide/mac-help/mh40584/mac). Filippo descrive l’attivazione nelle impostazioni della tastiera, la scelta della lingua, del microfono e della scorciatoia. Le tastiere Apple offrono tasti dedicati, mentre con altre tastiere si può impostare una combinazione personale. Su iPhone e iPad il microfono della tastiera permette di dettare nel campo di testo.

I conduttori apprezzano la possibilità di alternare voce e tastiera: se un nome non viene riconosciuto, si può correggere senza dover trattare dettatura e digitazione come due modalità del tutto separate. Un sistema già incluso nei dispositivi può essere sufficiente per messaggi e appunti brevi.

Filippo distingue esplicitamente dettatura e Controllo Vocale. Il fatto che entrambi usino la voce non rende equivalenti le loro funzioni: qui l’interesse è produrre testo. Le possibilità relative a lingue, elaborazione sul dispositivo e novità dei sistemi vengono discusse come dipendenti dalla versione e dalla macchina, senza promettere che ogni configurazione funzioni allo stesso modo.

### 5. Memo Vocali: catturare il pensiero e ritrovare il testo

Roberto chiede perché registrare un memo anziché aprire una nota e dettare. Filippo racconta il proprio uso di [Memo Vocali](https://support.apple.com/it-it/guide/iphone/iph00953a982/ios) per ragionare ad alta voce, anche mentre cammina sul tapis roulant. In quel caso non vuole comporre subito un testo finale: registra il pensiero e torna successivamente sulla trascrizione.

La registrazione mantiene anche l’audio originale e, con la sincronizzazione attiva, diventa disponibile sugli altri dispositivi. Dal computer Filippo può poi recuperare il testo e lavorarlo. Microfono, rumore ambientale e trattamento della voce incidono sulla leggibilità della trascrizione; auricolari e connessioni Bluetooth possono produrre risultati diversi dal microfono del telefono.

Roberto esplora l’ipotesi di usare Apple Watch durante un sopralluogo, con le mani impegnate in rilievi e appunti. La discussione resta una possibilità da provare: la risposta sul microfono e sul trasferimento della registrazione viene cercata durante la conversazione, ma non verificata direttamente dai conduttori. Filippo preferisce in generale l’iPhone per registrazioni lunghe e considera l’orologio più adatto a interventi brevi.

### 6. Note e Comandi Rapidi per sapere dove finisce la trascrizione

Filippo menziona le funzioni di [registrazione e trascrizione in Note](https://support.apple.com/it-it/guide/iphone/iphbe11247b5/ios), poi dedica più spazio a [Comandi Rapidi](https://support.apple.com/it-it/guide/shortcuts/welcome/ios). Distingue un’azione che riceve un file audio da trascrivere e una che consente di dettare testo nel corso dell’esecuzione.

Il vantaggio è collegare la cattura alla destinazione. Una scorciatoia può essere richiamata, ricevere il parlato e salvare il risultato nella cartella scelta. Filippo descrive modalità di conclusione della dettatura mediante un tocco o una pausa e ragiona sull’avvio da Siri, dalla schermata Home o da un comando disponibile sul dispositivo.

Per Roberto, un flusso simile potrebbe rendere più immediato catturare un appunto in cantiere. Non viene costruita una nuova automazione completa durante la puntata: il riferimento per partire sono gli episodi [24](https://a2podcast.it/24/) e [26](https://a2podcast.it/26/). La funzione pratica da valutare è evitare che il testo prodotto rimanga in un luogo provvisorio, da cercare e spostare manualmente in seguito.

### 7. FluidVoice e WhisperDictation come interfacce gratuite

Filippo presenta [FluidVoice](https://altic.dev/fluid), provata brevemente prima della registrazione. Gli interessa perché rende accessibili motori come Parakeet, Whisper e Apple Speech attraverso un’interfaccia grafica e permette di dettare nelle applicazioni mediante una scorciatoia. L’app richiede i permessi necessari per acquisire il microfono e interagire con il punto di inserimento del testo.

La scelta del modello rimane: un’interfaccia più semplice non elimina requisiti di memoria, spazio e supporto linguistico. Filippo distingue inoltre il nucleo dell’app dalle funzioni opzionali Fluid Intelligence e racconta di preferire il primo per le proprie prove. Eventuali passaggi aggiuntivi di rielaborazione vanno considerati separatamente dal riconoscimento della voce.

[WhisperDictation](https://sam-pop.github.io/WhisperDictation/) viene citata come alternativa emersa durante la preparazione, senza attribuirle un’esperienza d’uso approfondita. Il confronto con le app commerciali introduce il criterio economico: per un uso occasionale può bastare un’interfaccia gratuita; per un uso intenso contano anche continuità, integrazioni e lavoro risparmiato. I riferimenti ai vincoli della riga di comando riguardano i workflow e le implementazioni ricordati dai conduttori, senza diventare proprietà universali del modello Whisper.

### 8. Sopralluoghi, riunioni e riservatezza professionale

Roberto descrive applicazioni nel proprio lavoro di architetto. Chiede agli interlocutori prima di registrare; dopo un sopralluogo può produrre un memo che separa problemi, decisioni e attività. Per una riunione con la committenza, il testo può sostenere la preparazione di una mail di riepilogo e l’identificazione dei passaggi da seguire.

Per podcast e video, trascrivere rende possibili ricerche, capitoli, citazioni e sottotitoli. Roberto richiama però il controllo di termini architettonici e nomi dei prodotti: un riconoscimento plausibile ma errato può compromettere l’utilità del testo professionale.

Filippo descrive un approccio diverso alla registrazione dei colloqui con i clienti, legato alla riservatezza del proprio lavoro. Parla di conservazione, cifratura e destinazione dei dati come elementi che rendono meno immediato usare gli strumenti più comodi. Non propone una procedura normativa generale: spiega perché spesso preferisce prendere appunti durante o dopo la conversazione.

Cita [Ferrite](https://www.wooji-juice.com/products/ferrite/), che usa per il montaggio di A2, come strumento con cui può registrare sul dispositivo e gestire il file. Il suo uso più frequente resta però la registrazione di idee personali, dalle quali ricavare una sintesi o una scaletta per un intervento.

> “registrare il proprio pensiero, cioè pensare ad alta voce”
> — Filippo, 00:52:50

### 9. MacWhisper, CLI e il flusso locale di A2

[MacWhisper](https://www.macwhisper.com/) viene discusso per le funzioni che vanno oltre il riconoscimento grezzo: confronto tra testo e audio, correzione dei passaggi e distinzione degli interlocutori. Filippo specifica che il riconoscimento dei parlanti non è perfetto; i nomi possono essere assegnati ai soggetti individuati per rendere più utile il testo finale.

La funzione che lo interessa maggiormente è l’accesso tramite CLI. Un’applicazione richiamabile dal terminale può entrare in un flusso più ampio o essere utilizzata da un assistente che sa eseguire comandi. L’esempio è una cartella di registrazioni da trascrivere in serie, senza dover aprire manualmente ogni file nell’interfaccia grafica.

Filippo racconta anche una strada basata su strumenti locali e una skill: l’assistente sceglie e usa il motore di trascrizione secondo istruzioni ripetibili. È il sistema con cui ha lavorato all’archivio di A2. Ha scelto SRT perché i timestamp gli consentono di ritrovare dove una persona ha pronunciato una frase, oltre a produrre il testo per la pagina dell’episodio. La trascrizione diventa così un passaggio documentato del processo editoriale.

### 10. Rielaborazione del parlato e applicazioni per audio e video

[Wispr Flow](https://wisprflow.ai/) entra nel discorso per il passaggio dalla voce a un testo già rielaborato. Filippo racconta un video in cui un insegnante commentava oralmente i compiti e, tramite istruzioni dedicate, otteneva una restituzione scritta strutturata per lo studente. È un esempio di trasformazione del contenuto, non soltanto di riconoscimento delle parole. [Superwhisper](https://superwhisper.com/) viene menzionata tra le alternative, senza un confronto dettagliato delle singole funzioni.

Per il mondo dei contenuti, Filippo segnala [Transcriber](https://ulti.media/transcriber/) di Alex Raccuglia, che ha utilizzato e trova orientata ai flussi audio e video. Le possibilità di estrarre contenuti e applicare prompt possono essere interessanti per chi produce podcast professionalmente, mentre non coincidono necessariamente con le esigenze del suo lavoro legale.

[Transcriptionist](https://www.wooji-juice.com/products/transcriptionist/) viene richiamata per l’integrazione con Ferrite: lavorare su tracce separate permette di mantenere distinta la voce di ciascun partecipante. Anche [Audio Hijack](https://rogueamoeba.com/support/manuals/audiohijack/?page=transcribe), usata nella registrazione, può trascrivere sorgenti separate. In questo caso l’identificazione nasce dall’organizzazione degli ingressi; non equivale a riconoscere automaticamente tutti i parlanti dentro un unico audio già miscelato.

### 11. Scegliere secondo frequenza, hardware e lavoro da svolgere

Nell’ultima parte sostanziale Roberto distingue gli usi occasionali dai flussi più intensi. Se si cerca soprattutto dettatura o trascrizione e si prevede di rileggere il risultato, gli strumenti inclusi o gratuiti possono offrire un punto di partenza. Le applicazioni commerciali diventano più interessanti quando contano integrazioni, flessibilità e uso frequente della voce al posto della digitazione.

Filippo riporta la scelta del modello alle risorse disponibili e al risultato cercato. Una trascrizione di podcast, un appunto breve e una bozza da trasformare in un documento richiedono combinazioni diverse di cattura, riconoscimento e revisione. Anche nel confronto economico, i conduttori ragionano sul vantaggio concreto del flusso per chi lo usa, senza indicare un prodotto adatto indistintamente a tutte le esigenze.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
