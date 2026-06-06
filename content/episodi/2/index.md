+++
title = "2: Passare a Mac nel 2021: da Windows a Mac"
date = "2021-02-23T17:00:00+01:00"
episodeNumber = 2
slug = "2"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336039/fb359288_5fe2_4a3a_9d65_9d5aed6b609a.mp3"
spreakerEpisodeId = "64336039"
duration = "1:05:34"
description = "In questa puntata vi parliamo di come passare da Windows a Mac, le accortezze da utilizzare, di Boot Camp, Macchine virtuali, installazione da zero e come installare tutte le vecchie applicazioni del vostro Mac con MAcAppStore e Homebrew."
tags = ["mac", "app"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "3bx_8i2jCPo"
+++

> In questa puntata vi parliamo di come passare da Windows a Mac, le accortezze da utilizzare, di Boot Camp, Macchine virtuali, installazione da zero e come installare tutte le vecchie applicazioni del vostro Mac con MAcAppStore e Homebrew.

## Note dell’episodio

- [Boot Camp](https://support.apple.com/it-it/boot-camp): guida ufficiale Apple per installare Windows su Mac Intel con partizione dedicata.
- [Lettore multifunzione per smartcard e SIM compatibile con macOS](https://amzn.to/3sr7GxJ): soluzione hardware consigliata per chi ha problemi con le chiavette di firma digitale Aruba su Mac.
- [MS-DOS su Wikipedia](https://it.wikipedia.org/wiki/MS-DOS): riferimento al filesystem DOS, leggibile nativamente da macOS.
- [FAT su Wikipedia](https://it.wikipedia.org/wiki/File_Allocation_Table): filesystem FAT, compatibile in lettura e scrittura con macOS.
- [ExFAT su Wikipedia](https://it.wikipedia.org/wiki/ExFAT): filesystem ExFAT, compatibile in lettura e scrittura con macOS.
- [NTFS su Wikipedia](https://it.wikipedia.org/wiki/NTFS): filesystem Windows leggibile da macOS ma non scrivibile nativamente; richiede software di terze parti per la scrittura.
- [Samba su Wikipedia](https://it.wikipedia.org/wiki/Samba_(software)): protocollo di rete Microsoft implementato anche su macOS, permette l'accesso a server Windows senza software aggiuntivi.
- [Installare applicazioni con Homebrew (avvocati-e-mac.it)](https://www.avvocati-e-mac.it/blog/2019/8/14/scaricare-tutti-o-quasi-i-programmi-da-installare-fuori-dallappstore-con-homebrew-cask): guida pratica all'uso di Homebrew Cask per installare software proprietario da riga di comando.
- [Video: installazione di Homebrew, Pandoc e MacTeX su macOS](https://www.avvocati-e-mac.it/blog/2020/6/19/youtube-installazione-homebrew-pandoc-e-mactex-su-macos): tutorial video che mostra l'installazione di Homebrew e alcuni pacchetti comuni.
- [Homebrew](https://brew.sh/index_it): gestore di pacchetti open source per macOS, alternativa gratuita a Parallels e VMware per chi vuole automatizzare l'installazione di software.
- [Mac App Store](https://www.apple.com/it/osx/apps/app-store/): store ufficiale Apple per scaricare e reinstallare le app acquistate su qualsiasi Mac collegato allo stesso Apple ID.

## Sinossi[^sinossi-ai]

### 1. Premessa: la scaletta improvvisata e il tono della puntata

Il secondo episodio di A2 inizia con una confessione scherzosa di Roberto Marin: non ha studiato la scaletta. Filippo Strozzi prende le redini e introduce il tema della puntata — come passare da Windows a Mac — precisando che, dopo quattordici anni da utente Apple, i suoi ricordi personali di quella transizione sono ormai lontani, ma la materia è ancora più che attuale per chi si avvicina per la prima volta all'ecosistema Apple.

### 2. Compatibilità delle periferiche: stampanti, scanner e macchine fotografiche

Il primo passo prima di acquistare un Mac, secondo Filippo, è verificare la compatibilità delle periferiche già in casa. Scanner, stampanti, dischi esterni e macchine fotografiche nell'80-90% dei casi funzionano senza problemi grazie al sistema CUPS integrato in macOS, che garantisce almeno una stampa di base anche senza driver dedicati. Il consiglio è visitare il sito del produttore hardware per scaricare i driver specifici, oppure acquistare direttamente periferiche certificate macOS. Roberto aggiunge che il Mac ha sempre avuto un vantaggio storico su Windows nel riconoscimento automatico dell'hardware: racconta di una stampante HP A3 riconosciuta immediatamente da macOS, che però stampava in modo scorretto finché non ha installato i driver ufficiali scaricati dal sito HP — pochi minuti di operazione.

### 3. Firma digitale e chiavette smart card

Filippo apre una parentesi dedicata ai professionisti: le chiavette di firma digitale sono state storicamente il tallone d'Achille del Mac. Quattro o cinque anni fa, farle funzionare era un'impresa. Oggi la situazione è migliorata sensibilmente, anche grazie a soluzioni software come SPID, che consente l'autenticazione ai siti istituzionali tramite app mobile senza necessità di hardware aggiuntivo.

> "Per riuscire a farli funzionare, era più facile mettere un coltello nel lettore CD del Mac e cercare di sentirci la musica."
> — Roberto, 00:07:17

Il consiglio attuale è evitare le chiavette Aruba, che hanno problemi sia con macOS Big Sur sia con i processori M1. InfoCert e Namirial risultano le più compatibili al momento della registrazione. Per chi possiede una chiavetta problematica, Filippo segnala nelle note dell'episodio un lettore USB multifunzione acquistato il giorno stesso della registrazione: permette di estrarre la SIM dalla chiavetta e inserirla in un lettore nativo ad alta compatibilità con Mac. Roberto chiude ricordando che la firma digitale della Camera di Commercio ha sempre funzionato bene anche in versione smart card, con un supporto tecnico affidabile.

### 4. Compatibilità software: verificare prima di comprare

Il secondo controllo preliminare riguarda il software professionale. Non sempre il programma che si usa su Windows esiste per Mac, e quando esiste non è detto che sia identico. L'esempio più citato è Microsoft Office: fino a poco tempo fa la versione Mac era una variante separata; oggi l'interfaccia è sostanzialmente allineata, tranne la versione iPad che rimane limitata.

Roberto porta il caso concreto di AutoCAD, che lo aveva trattenuto a lungo su Windows. Rivela che nel mondo dell'architettura non esiste Revit per Mac, ma esiste Archicad — un software BIM alternativo disponibile su entrambe le piattaforme. Il messaggio è non scoraggiarsi di fronte a una lacuna: il panorama dei software Mac offre spesso alternative valide, spesso con un'attenzione alla cura dell'interfaccia e ai dettagli grafici che nel mondo Windows viene talvolta trascurata. Filippo stima che nell'80-90% dei casi, esclusi software molto verticali o costruiti per versioni obsolete di Windows, non ci siano problemi reali.

### 5. Migration Assistant: trasbordare i dati da Windows a Mac

Per chi ha il PC Windows ancora operativo accanto al nuovo Mac, Apple mette a disposizione il Windows Migration Assistant, un software gratuito sviluppato da Apple stessa. Collega i due computer alla stessa rete Wi-Fi (o via cavo diretto) e trasferisce la struttura delle cartelle utente, i contatti, i calendari e gli account. L'interfaccia guida passo passo, con una piccola sezione che richiede l'uso del prompt dei comandi Windows — nulla di complesso, ma da non sottovalutare.

Filippo precisa due limiti importanti: il Migration Assistant funziona solo con Windows 7 e versioni successive (chi è ancora su XP dovrebbe prioritariamente aggiornare il sistema operativo), e OneDrive va disinstallato dal PC Windows prima di avviare la migrazione per evitare conflitti. Roberto aggiunge che lui non ha mai usato questa procedura, preferendo il percorso parallelo di Boot Camp per mantenere a lungo entrambi i sistemi.

### 6. Boot Camp: Windows e Mac sullo stesso hardware

Boot Camp è il sistema Apple che permette di installare Windows direttamente sull'hardware del Mac, dedicandogli una partizione separata dell'hard disk. All'avvio, un piccolo software intermedio chiede all'utente quale sistema operativo caricare. Il vantaggio principale è la piena potenza dell'hardware: Boot Camp non virtualizza nulla, Windows gira sul metallo come su qualsiasi PC. Chi fa rendering 3D, quindi, troverà Boot Camp molto più performante di qualsiasi macchina virtuale.

Lo svantaggio è l'interruzione del flusso di lavoro: per passare da macOS a Windows bisogna riavviare completamente il Mac, attendere lo spegnimento, la scelta della partizione e il caricamento di Windows. Ogni sessione di cambio sistema richiede qualche minuto. Roberto sottolinea che Boot Camp è stato per lui il paracadute ideale durante il periodo di transizione: quando non sapeva come fare qualcosa su Mac, riavviava su Windows e lavorava senza problemi, poi gradualmente spostava tutto sul lato Mac.

> "Nel momento in cui io utilizzo il Mac e non so che santo votarmi, ma dopo domani devo fare una consegna, se nel caso io con Windows sono ancora più operativo, allora Boot Camp aiuta moltissimo."
> — Roberto, 00:22:00

Filippo ricorda che sia Boot Camp sia le macchine virtuali richiedono una licenza Windows a pagamento. Il consiglio è acquistarla contestualmente al Mac, sfruttando le licenze OEM — quelle legate all'acquisto della macchina — che costano meno delle licenze retail.

### 7. Macchine virtuali: Parallels, VMware e VirtualBox

Le macchine virtuali sono l'alternativa software a Boot Camp: permettono di far girare Windows come un programma all'interno di macOS, senza riavviare. Il pregio è la flessibilità — si accende la VM quando serve e si spegne quando non serve più — ma si paga in prestazioni: la virtualizzazione consuma risorse della macchina host, e la grafica 3D in particolare soffre rispetto al bare metal di Boot Camp.

I due software commerciali principali sono Parallels e VMware Fusion. Entrambi richiedono un aggiornamento a pagamento (circa 50-70 euro) ad ogni nuovo major release di macOS, una politica che Roberto e Filippo trovano fastidiosa. Entrambi offrono però funzioni avanzate come la "coerenza" di Parallels (le finestre di Windows appaiono come normali app macOS) e la condivisione trasparente delle cartelle tra i due sistemi.

Roberto e Filippo convergono sulla stessa scelta: VirtualBox di Oracle. È gratuito, open source, meno rifinito graficamente ma completo nelle funzionalità essenziali. Roberto apprezza in particolare la semplicità del backup: la macchina virtuale è un singolo file (con estensione `.vdi` o simile) che si copia su un disco esterno. Lui conserva ancora i backup delle vecchie macchine virtuali degli anni passati. Filippo avverte che una VM di Windows occupa facilmente 20-30 GB e può crescere molto se si caricano file; 4 GB di RAM dedicati sono il minimo per un funzionamento accettabile.

> "Voi potete fare il backup della macchina virtuale semplicemente spostando un file."
> — Roberto, 00:40:00

Sul fronte M1, al momento della registrazione la situazione è in evoluzione: Parallels ha una versione beta per Apple Silicon, ma richiede Windows per ARM — una variante con meno software disponibili rispetto alla versione x86. Filippo conclude che per chi ha bisogno di Windows quotidianamente su M1 la soluzione più pratica rimane collegarsi in remoto al vecchio PC Windows.

### 8. Da Mac a Mac: Time Machine e installazione da zero

Per chi aggiorna il proprio Mac, ci sono due approcci opposti. Roberto è il difensore di Time Machine: collega il disco di backup al nuovo Mac, avvia l'Assistente Migrazione, sceglie "da un backup di Time Machine" e poi va a mangiare un panino. Quando torna, il nuovo Mac è identico all'ultimo backup — stesse app, stesse preferenze, stessi dati, tutto nello stesso posto.

> "Dal mio punto di vista ho sempre usato, invece di partire con un sistema pulito, di partire da un sistema che arriva da un Time Machine precedente. Non me ne sono mai pentito."
> — Roberto, 00:48:27

Filippo fa l'opposto: ogni due o tre anni parte da zero. Prima clona l'intero disco su un disco esterno (così il vecchio Mac è recuperabile in ogni momento attaccando il disco esterno e avviando da lì), poi copia manualmente le cartelle di lavoro, poi formatta e reinstalla macOS. I vantaggi: sistema più snello, nessun residuo software accumulato negli anni, nessun rischio di portarsi dietro instabilità pregresse. I tempi si recuperano grazie a due strumenti: il Mac App Store, che con un Apple ID permette di reinstallare in pochi clic tutte le app acquistate in precedenza, e Homebrew.

Filippo descrive Homebrew come la sua scoperta più importante per gestire i software fuori dallo store. Con il comando `brew list` si ottiene la lista di tutto ciò che è installato; su un nuovo Mac basta copiare quella lista e lanciare un unico comando per installare decine di applicazioni in sequenza automatica — dal sito ufficiale di ogni sviluppatore, senza cercare manualmente ogni programma. LibreOffice, Acrobat Reader, 1Password, Audacity: tutto si scarica e si installa senza aprire un browser.

### 9. Curiosità su Time Machine: avviare il Mac da backup

Filippo chiude con un dettaglio che in pochi conoscono: è possibile avviare un Mac direttamente da un disco di Time Machine. Se l'hard disk interno è danneggiato ma il Mac funziona, si può collegare il disco di backup e avviare da lì, ritrovandosi con la macchina operativa esattamente come era all'ultimo backup. Una soluzione di emergenza citata da un ascoltatore (Davide Gatti) che Roberto conferma.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
