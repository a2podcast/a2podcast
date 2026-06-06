+++
title = "24: Le basi di Comandi rapidi: Creiamo la nostra prima automazione"
date = "2021-12-20T06:00:00+01:00"
episodeNumber = 24
slug = "24"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336025/143be723_2cbb_411e_9e03_42d5d4a12694.mp3"
spreakerEpisodeId = "64336025"
duration = "1:12:00"
description = "Per la tua gioia di Filippo facciamo un ulteriore approfondimento su Comandi Rapidi. Ne abbiamo già parlato nella precedente puntata 22 che, se non avete ascoltato, vi consigliamo di recuperare prima di ascoltare questa. Infatti daremo per scontato l’introduzione già fatta in quella puntata. In ques"
tags = ["shortcuts", "automazione", "ios", "mac", "produttivita"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "ObNc3_33C4U"
+++

> Per la tua gioia di Filippo facciamo un ulteriore approfondimento su Comandi Rapidi. Ne abbiamo già parlato nella precedente puntata 22 che, se non avete ascoltato, vi consigliamo di recuperare prima di ascoltare questa. Infatti daremo per scontato l’introduzione già fatta in quella puntata. In questa puntata creeremo il nostro primo Comando Rapido

## Note dell’episodio
- [A2 episodio 22: “Craft, Comandi Rapidi e note con Daniele Borghi”](https://a2podcast.it/22/): puntata da recuperare prima di questa, perché introduce Comandi Rapidi e Craft, temi dati per acquisiti nell’episodio 24.
- [Shortcuts in Limbo, di David Sparks](https://www.macsparky.com/blog/2021/12/shortcuts-in-limbo): articolo citato da Filippo per spiegare perché, a fine 2021, Comandi Rapidi su macOS Monterey era ancora da considerare sperimentale.
- [Craft](https://www.craft.do): applicazione di scrittura e gestione dei contenuti discussa nella puntata 22 e richiamata qui per il premio ricevuto da Apple.
- [App Store Awards 2021 di Apple](https://www.apple.com/it/newsroom/2021/12/app-store-awards-honor-the-best-apps-and-games-of-2021/): comunicato Apple in cui Craft viene premiata tra le migliori app del 2021.
- [Craft X](https://www.craft.do/s/OhmDYXrBwI2wZS): programma beta citato da Filippo per estendere Craft e collegarla ad altri strumenti di lavoro.
- [Knowledge management software](https://en.wikipedia.org/wiki/Knowledge_management_software): categoria di strumenti citata parlando di Obsidian, DEVONthink, Notion, Roam e della possibile puntata futura sulla gestione della conoscenza.
- [Esempio Comandi Rapidi: numerazione documenti per PCT](https://www.icloud.com/shortcuts/b91888e61d62480db15b5ec781e7dda9): comando rapido di Filippo usato per spiegare azioni condizionali, numerazione progressiva e loop.
- [Esempio Comandi Rapidi: Normattiva](https://www.icloud.com/shortcuts/4f80efc6ec4242049b9b7afd1e16d2f8): comando rapido citato per mostrare l’uso di “Scegli dal menu” come piccolo launcher di risorse normative.
- [Schermata iPhone dell’editor di Comandi Rapidi](https://images.squarespace-cdn.com/content/v1/55b2626fe4b0bfab95304b93/a7afd96d-4d95-40f3-bd6f-fcc85d7ddfc0/iPhone+interfaccia+editor+Comandi+rapidi.jpeg?format=500w): immagine citata durante la spiegazione dell’interfaccia su iPhone.
- [Schermata iPad dell’editor di Comandi Rapidi](https://images.squarespace-cdn.com/content/v1/55b2626fe4b0bfab95304b93/6abc75c9-bd6c-4064-9451-01c10da88ad4/iPad+interfaccia+editor+Comandi+Rapidi.jpeg?format=750w): immagine usata per seguire la struttura dell’editor su iPad.
- [Pannello opzioni di Comandi Rapidi](https://images.squarespace-cdn.com/content/v1/55b2626fe4b0bfab95304b93/b33ddd1d-947f-4570-9103-5581407cbd95/Pannello+opzioni.jpeg?format=750w): schermata richiamata per distinguere dettagli, privacy e configurazione del comando.

## Sinossi[^sinossi-ai]

### 1. Ripresa dalla puntata 22 e contesto dell’episodio
Filippo e Roberto aprono l’episodio spiegando che questa puntata riprende il tema di Comandi Rapidi già affrontato nell’episodio 22 con Daniele Borghi. La puntata precedente aveva dato una prima infarinatura: come orientarsi nella Galleria, che cosa sono i comandi rapidi, perché possono entrare nella vita quotidiana e professionale degli utenti Apple. Qui, invece, l’obiettivo è più operativo: creare un comando rapido personalizzato, seguendo passo passo l’interfaccia di iOS e iPadOS 15.

Roberto chiarisce subito che non si tratta di ripetere l’introduzione già fatta, ma di costruire qualcosa. Il tono è quello del tutorial guidato: Filippo prepara un esempio pratico, Roberto lo segue da utente meno esperto e interviene quando un passaggio rischia di essere dato per scontato. Questa dinamica diventa importante per tutta la puntata, perché permette di spiegare sia la logica generale sia i piccoli ostacoli dell’interfaccia.

Prima di entrare nel vivo, i conduttori fanno gli auguri di Natale agli ascoltatori, perché la puntata esce il 20 dicembre ed è stata registrata in anticipo. Roberto spiega anche che le pubblicazioni continueranno durante il periodo festivo, grazie a una programmazione anticipata. La parte iniziale contiene poi alcuni richiami di servizio e di scenario: il podcast procede con una cadenza regolare, i conduttori ringraziano chi ascolta e ricordano l’importanza delle recensioni per i podcast italiani.

> "Questa volta parliamo di nuovo di comandi rapidi."
> — Roberto, 00:00:18

### 2. Perché non parlare ancora di Comandi Rapidi su Mac
La prima comunicazione tecnica riguarda macOS Monterey. Filippo spiega che, pur essendo arrivati anche su Mac, i Comandi Rapidi non saranno trattati in questa puntata e probabilmente nemmeno nelle successive immediate. La ragione è prudenziale: secondo Filippo, e anche secondo David Sparks nell’articolo citato nelle note, la versione Mac è ancora in una condizione instabile, quasi da beta.

Il punto non è sconsigliare del tutto la sperimentazione. Chi usa Monterey può provare Comandi Rapidi su Mac, ma deve sapere che eventuali malfunzionamenti non dipendono necessariamente da errori dell’utente. Alcuni comandi potrebbero non funzionare perché il sistema è ancora immaturo. Filippo sottolinea anche che Comandi Rapidi su Mac andrà affrontato con un’impostazione diversa rispetto a iOS e iPadOS: il Mac ha caratteristiche proprie, più possibilità di scripting e un rapporto diverso con file, automazioni e sistema operativo.

Questa distinzione serve a delimitare il campo dell’episodio. La puntata è dedicata all’interfaccia mobile, soprattutto iPad, con riferimenti anche a iPhone. Il Mac resta sullo sfondo come evoluzione interessante, ma non ancora abbastanza stabile da diventare il centro di una guida affidabile.

> "La situazione di comandi rapidi su Mac è ancora abbastanza complicata."
> — Filippo, 00:04:45

### 3. Craft, Craft X e gli strumenti di gestione della conoscenza
Prima del tutorial, Roberto e Filippo riprendono anche Craft, applicazione discussa nell’episodio 22. Roberto segnala che Craft ha ricevuto da Apple un riconoscimento tra le migliori app del 2021. La notizia li colpisce perché, prima della puntata con Daniele Borghi, non conoscevano direttamente l’applicazione: grazie a quell’episodio, il podcast era arrivato sul tema poco prima della consacrazione pubblica da parte di Apple.

Filippo aggiunge due elementi. Il primo è il finanziamento ricevuto da Craft, segnale che l’app potrebbe avere un futuro solido. Il secondo è Craft X, un programma beta per sviluppatori pensato per collegare Craft ad altri strumenti. L’idea è che Craft non debba essere necessariamente “lo strumento unico”, ma possa diventare un nodo dentro un flusso più ampio: scrittura, pubblicazione, gestione dei contenuti, interfacce verso WordPress o altre piattaforme.

Da qui nasce una possibile direzione futura per A2: una puntata sui knowledge management software. Filippo cita Obsidian e DEVONthink, Roberto è interessato a Notion, e vengono nominati anche Roam e Craft. La prospettiva non è solo la scrittura, già trattata in altri episodi, ma la gestione delle informazioni, delle note e delle relazioni tra contenuti. I conduttori chiedono agli ascoltatori di condividere esperienze specifiche, soprattutto con strumenti che loro non hanno ancora esplorato a fondo.

### 4. Orientarsi nell’interfaccia di Comandi Rapidi
La parte centrale della puntata inizia con un richiamo a quanto visto nell’episodio 22: Galleria, Automazioni e I miei comandi rapidi. Roberto interviene subito per ricordare una cosa apparentemente banale ma decisiva: quando si apre l’app Comandi Rapidi non ci si trova già davanti all’editor di un comando nuovo. Bisogna andare nella sezione dei propri comandi e premere il pulsante “+”. Filippo aveva dato questo passaggio per scontato, ma Roberto lo recupera per chi sta seguendo il tutorial in tempo reale.

Su iPad, Filippo descrive l’editor come diviso in due colonne. A sinistra c’è il comando vero e proprio: il nome, i pulsanti annulla e rifai, la condivisione, il tasto play e lo spazio in cui vengono inserite le azioni. A destra c’è il pannello con la ricerca delle azioni, i suggerimenti e le opzioni disponibili. Premendo l’icona con le manopole si accede invece ai dettagli del comando: aggiunta alla schermata Home, visibilità nel menu di condivisione, privacy e configurazione.

Il tasto play ha una funzione pratica essenziale: permette di testare il comando mentre lo si costruisce. Filippo insiste sul fatto che un comando rapido difficilmente nasce perfetto al primo tentativo. Si prova, si vede dove si blocca, si corregge. L’editor diventa quindi non solo uno spazio di composizione, ma anche di verifica progressiva.

Su iPhone l’interfaccia è più compressa: una sola finestra, nome in alto, opzioni, chiusura, pulsante “Aggiungi azione”, suggerimenti e ricerca in basso. Filippo consiglia, quando possibile, di costruire i comandi su iPad perché lo spazio aiuta, lasciando poi che la sincronizzazione li renda disponibili anche su iPhone.

### 5. Dettagli, condivisione, input e uso vocale
Filippo dedica molto spazio alle impostazioni del comando, perché determinano come verrà usato. “Aggiungi alla schermata Home” permette di creare un’icona che avvia direttamente il comando. Roberto precisa che, nell’esperienza utente, quell’icona si comporta quasi come una piccola applicazione: si tocca e parte la procedura prevista.

L’opzione “Mostra in condivisione” è altrettanto importante. Permette di rendere un comando disponibile dal menu di condivisione di iOS e iPadOS. Filippo fa l’esempio di un comando che unisce più screenshot verticalmente: seleziona tre immagini da Foto, apre la condivisione, sceglie il comando rapido e ottiene un’unica immagine finale. In questo caso è fondamentale limitare il tipo di input accettato, per esempio solo immagini. Se il comando accettasse qualunque cosa, potrebbe comparire anche quando si condivide testo o PDF, pur non essendo in grado di elaborarli.

Filippo segnala anche un problema pratico: nel menu di condivisione i comandi rapidi appaiono tutti in grigio, senza i colori assegnati nell’app. Per distinguerli meglio, lui spesso aggiunge un’emoji significativa al nome del comando. È un espediente semplice, ma utile quando i comandi diventano molti.

Si parla poi di Apple Watch e Siri. Mostrare un comando sull’orologio può servire, ma Filippo trova ancora più interessante l’avvio vocale. Il nome del comando diventa rilevante perché è la frase che Siri dovrà riconoscere. Filippo racconta l’esempio domestico dell’albero di Natale acceso e spento con un comando vocale. Il punto tecnico è che Comandi Rapidi permette di programmare cosa Siri deve fare: non rende Siri davvero “intelligente”, ma consente all’utente di costruire risposte e percorsi che sembrano intelligenti perché sono stati pensati prima.

> "Il nome che date al comando rapido è importante, soprattutto se volete invocarlo a voce."
> — Filippo, 00:31:36

### 6. Il primo comando: scegliere una foto e preparare un messaggio
Il comando costruito nell’episodio ha uno scopo semplice: scegliere una foto, associare un testo precompilato e inviare tutto a un contatto tramite Messaggi. Filippo ammette però che l’esempio, scelto perché apparentemente banale, rivela subito alcuni limiti dell’automazione con Messaggi. Con Mail sarebbe possibile selezionare il destinatario più liberamente; con Messaggi, invece, il contatto deve essere impostato nel comando durante la creazione. Non si può passare dinamicamente un contatto scelto prima, almeno nel flusso che Filippo aveva immaginato.

Il primo passaggio è cercare l’azione “Seleziona foto”. Prima di inserirla, Filippo mostra come leggere la scheda informativa dell’azione: descrizione, risultato e compatibilità. Il risultato di questa azione sono le foto o i video selezionati. Una volta aggiunta, il comando può essere configurato per includere solo immagini, solo foto, video o più elementi. Roberto consiglia di togliere i video, visto che il comando si chiama “invia foto con commento”. Si abilita anche la selezione multipla, così l’utente può scegliere più immagini dal rullino.

Poi si aggiunge l’azione “Testo”. Questa serve a preparare la frase da inviare, per esempio “Guarda questa foto bellissima”. Filippo fa notare che questa azione non riceve automaticamente l’output della precedente, perché non c’è un passaggio diretto tra foto e testo: il testo viene scritto dall’utente e prodotto come risultato autonomo. Subito dopo si cerca e si inserisce “Invia messaggio”. Qui l’azione si collega al testo, perché il testo diventa il contenuto del messaggio.

Il destinatario viene scelto direttamente nell’azione. Filippo seleziona Roberto e spiega che si possono aggiungere più contatti, ma sempre in fase di progettazione del comando. L’opzione “Mostra quando viene eseguito” può essere lasciata o rimossa; Filippo di solito la disattiva per ridurre i passaggi manuali, ma nel caso delle foto Apple può comunque richiedere conferme aggiuntive.

### 7. Variabili, variabili magiche e metadati della foto
La parte più formativa arriva quando Filippo introduce le variabili. L’azione “Invia messaggio” viene duplicata: il primo messaggio invierà il testo, il secondo servirà a inviare la foto. Tenendo premuta l’icona dell’azione si apre il menu con “Duplica”. Dopo la duplicazione, però, il secondo messaggio contiene ancora la variabile “Testo”. Filippo la cancella e la sostituisce con la variabile “Foto”.

Qui entra in gioco il concetto centrale: ogni azione può avere un input e produce un output. L’output di “Seleziona foto” non è solo l’immagine in senso visivo, ma un oggetto ricco di informazioni. Una foto contiene anche nome, estensione, data di creazione, posizione, dimensioni, metadati e altre proprietà. Comandi Rapidi permette di accedere a queste informazioni senza dover scrivere codice tradizionale.

Filippo spiega le variabili con l’immagine del cassetto: una variabile è un contenitore in cui viene messo un oggetto, che può essere testo, immagine, data, file o altro. La particolarità di Comandi Rapidi è che spesso l’oggetto contiene molte proprietà estraibili. Per rendere questa gestione più accessibile, Workflow prima e Comandi Rapidi poi hanno introdotto le “variabili magiche”. Premendo “Seleziona variabile”, l’editor cambia modalità e mostra sotto ogni azione la variabile prodotta. L’utente può quindi scegliere visivamente quale risultato riutilizzare.

Filippo rende l’esempio più sofisticato: nel testo del messaggio inserisce “Guarda questa foto del” e poi aggiunge la data di creazione della foto. Imposta il formato della data come esteso e rimuove l’orario. Il messaggio risultante sarà quindi qualcosa come “Guarda questa foto del 5 dicembre 2021”. La variabile viene rinominata “data foto”, per rendere più chiaro che cosa contiene. È un dettaglio di buona prassi: quando i comandi crescono, i nomi comprensibili evitano confusione.

> "La variabile è un cassetto all’interno della quale viene messo un oggetto."
> — Filippo, 00:48:15

### 8. Test, limiti di Messaggi e necessità di sperimentare
Quando il comando viene testato con il tasto play, emergono i limiti concreti dell’automazione. Filippo seleziona per errore un video, poi invia il contenuto a Roberto. Il testo arriva subito, mentre la foto richiede una conferma ulteriore. I due conduttori osservano che Apple tratta l’invio di immagini come un’azione più sensibile: il comando può preparare il messaggio, ma l’utente deve comunque confermare l’invio della foto.

Il test dimostra anche che il comando non produce esattamente l’idea iniziale di Filippo. Lui avrebbe voluto inviare in un unico messaggio testo e immagine. Invece il risultato pratico è composto da due messaggi: uno con il testo e uno con la foto. Dal punto di vista dell’uso quotidiano può cambiare poco, ma dal punto di vista dell’automazione è importante: il comando si adatta ai limiti delle azioni disponibili.

Roberto nota che, per usare bene Comandi Rapidi, bisogna prima avere chiaro che cosa si vuole automatizzare. Filippo conferma: il primo lavoro non è inserire azioni nell’editor, ma descrivere il flusso. Nel caso dell’esempio: selezionare una foto, preparare un testo, mandare testo e foto a un destinatario. Solo dopo si cercano le azioni disponibili. Il secondo passaggio, spesso più difficile, è verificare se quelle azioni esistono davvero e se accettano gli input desiderati. Se non esistono, bisogna trovare un giro alternativo.

> "Il primo step non è scrivere il comando rapido."
> — Filippo, 01:07:00

### 9. Comandi intelligenti: condizioni, menu, launcher e loop
Nella parte finale Filippo allarga la prospettiva oltre il comando appena costruito. I Comandi Rapidi non devono essere per forza flussi lineari: possono diventare “intelligenti” inserendo logica, scelte e ripetizioni. La prima azione citata è “Se”, cioè una condizione. Se una certa cosa è vera, il comando esegue un ramo; se è falsa, ne esegue un altro. Filippo usa come esempio il suo comando per la numerazione dei documenti nel Processo Civile Telematico: il comando conta i file, li rinomina in ordine e decide quanti zeri anteporre in base al numero complessivo di documenti. Se i documenti sono più di cento, serve una numerazione a tre cifre; se sono meno, ne bastano due.

Questo esempio introduce anche il tema dei loop, cioè delle azioni “Ripeti”. Invece di scrivere un’azione per ogni file, il comando ripete la stessa operazione su tutti gli elementi selezionati: prende il file, calcola il numero, antepone la cifra formattata, passa al successivo e incrementa la variabile. Filippo lo spiega come un modo per fare molte volte la stessa cosa senza duplicare manualmente il lavoro.

Si parla poi di “Elenco” e “Scegli dal menu”. L’elenco può essere generato da un’azione precedente, per esempio filtrando le ultime foto di una persona e permettendo all’utente di sceglierne alcune. “Scegli dal menu” è ancora più immediato: crea opzioni A, B, C e sotto ciascuna permette di inserire azioni diverse. Filippo cita il suo comando rapido per Normattiva, che apre diverse pagine normative a seconda della scelta, e lo descrive anche come esempio di launcher. Un comando può infatti lanciarne altri: si può creare un unico pulsante sulla Home che apre un menu, dal quale scegliere spese di casa, spese dell’ufficio, stazione meteo, normativa o altri flussi.

L’episodio si chiude con Roberto che riporta il discorso a un punto pratico: per immaginare un’automazione bisogna osservare ciò che si fa spesso. Filippo ribadisce che usare Comandi Rapidi significa già programmare, anche nella forma più semplice. Non serve partire da comandi enormi: si parte da operazioni piccole, si verifica quali azioni sono disponibili, si prova, si scoprono i limiti e si adatta il flusso.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
