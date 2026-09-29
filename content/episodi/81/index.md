+++
title = "Gestione della conoscenza e IA con Daniele Borghi"
date = 2026-09-30T07:00:00+02:00
episodeNumber = 81
slug = "81"
audioUrl = ""
spreakerEpisodeId = "75431972"
duration = "51:57"
description = "Filippo e Roberto aiutano Daniele Borghi a orientarsi tra documenti, note e archivi digitali: Apple Note, Forever Notes, Markdown, Hazel, assistenti IA e sincronizzazione con Syncthing. Il metodo PARA prosegue nella puntata 82."
tags = ["pkm", "note", "workflow", "intelligenza-artificiale", "ospite", "organizzazione"]
draft = false

[params]
hasTranscript = true
# Associazione alla pagina ospite da completare quando sarà creata nel sito.
guest = ""
youtubeId = "NS_LSMkSLwg"
+++

> Filippo e Roberto aiutano Daniele Borghi a orientarsi tra documenti, note e archivi digitali: Apple Note, Forever Notes, Markdown, Hazel, assistenti IA e sincronizzazione con Syncthing. Il metodo PARA prosegue nella puntata 82.

## Note dell’episodio

- [A2 80: Automazione Apple nell’era dell’IA generativa](https://a2podcast.it/80/): la conversazione da cui nasce la richiesta di Daniele di riorganizzare il proprio materiale digitale.
- [A2 42: Note di Apple: approfondimento](https://a2podcast.it/42/): episodio richiamato da Filippo mentre i tre discutono come usare Note per appunti e documenti.
- [Hazel](https://www.noodlesoft.com/): automazione delle cartelle sul Mac; Filippo porta l’esempio della data estratta dal contenuto di un documento per rinominarlo e archiviarlo.
- [Forever Notes](https://www.myforevernotes.com/category/get-started): metodo di Matthias Hilse adottato in parte da Daniele per collegare e organizzare le note nell’app Apple.
- [Obsidian](https://obsidian.md/): applicazione basata su file Markdown, utilizzata in precedenza da Daniele e preferita da Filippo per mantenere le note accessibili come file.
- [Notion](https://www.notion.com/): precedente ambiente di lavoro di Roberto, che ne confronta le integrazioni con IA e le possibilità rispetto alla scrittura a mano in Note.
- [Claude](https://claude.com/product/overview): assistente usato da Daniele per preparare testi, ricerche e materiali del podcast, che richiedono poi una collocazione stabile fuori dalla chat.
- [Model Context Protocol](https://modelcontextprotocol.io/): protocollo discusso per collegare assistenti IA a note, servizi e file, entro le possibilità e i permessi delle singole integrazioni.
- [Perplexity](https://www.perplexity.ai/): servizio di ricerca usato da Filippo, che descrive sperimentazioni di accesso alle conversazioni tramite un connettore esterno.
- [NotebookLM](https://notebooklm.google/): strumento menzionato nel passaggio sulle integrazioni tra assistenti e raccolte di fonti; il recupero dei materiali su disco resta una possibilità da verificare.
- [Syncthing](https://syncthing.net/): sincronizzazione tra computer di cartelle selezionate, proposta come alternativa all’uso di iCloud per il vault di Obsidian.
- [Möbius Sync](https://mobiussync.com/): applicazione per integrare iPhone e iPad in una sincronizzazione basata su Syncthing; Filippo distingue ciò che ha letto dalle funzioni provate direttamente.
- [Il metodo PARA](https://fortelabs.com/blog/para/): riferimento di Tiago Forte per l’organizzazione in Progetti, Aree, Risorse e Archivio, il cui approfondimento viene rinviato alla puntata successiva.

## Sinossi[^sinossi-ai]

### 1. Il problema di Daniele: conservare tutto e non sapere dove cercare

Filippo e Roberto invitano Daniele Borghi dopo le domande che aveva posto durante la diretta della puntata sull’automazione. Daniele parte da una situazione concreta: anni di documenti, immagini, video e registrazioni si sono sommati alle informazioni raccolte ogni giorno per interessi personali, formazione e podcast. Il sistema di cartelle che usava in passato non gli basta più. Vorrebbe una struttura più semplice, capace di distinguere subito documenti e note e di ridurre il tempo necessario per recuperare ciò che sa di avere.

Il problema attraversa più luoghi. Daniele sta concentrando il materiale di vecchi dischi in un DAS collegato direttamente al Mac mini, mentre mantiene copie su NAS. Restano anche archivi cloud e vecchi progetti del periodo in cui lavorava come libero professionista. Filippo separa subito due domande: quali informazioni devono rimanere disponibili e quali operazioni si vogliono automatizzare? Il backup viene riconosciuto come argomento distinto, da affrontare in un’altra occasione.

Daniele chiarisce inoltre che gran parte del materiale attuale è personale. Comprende documenti domestici, assicurazioni e informazioni finanziarie, oltre a contenuti per il podcast. Il lavoro svolto nell’azienda segue invece un sistema separato. Questa distinzione evita di immaginare un unico contenitore per dati con usi e contesti molto diversi.

### 2. Rinomina e archiviazione: che cosa può fare Hazel

L’idea iniziale di Daniele è affidare a un assistente IA l’esame, la rinomina e lo spostamento di molti documenti. La quantità gli fa pensare a un lavoro manuale di intere giornate. Ha già una convenzione con date nei nomi dei file e usa una piccola utility di Alex Raccuglia che aggiunge prefissi o suffissi e legge date di modifica o salvataggio. Il nome dell’applicazione non viene chiarito: la funzione utile è poter trattare rapidamente gruppi di file.

Filippo introduce [Hazel](https://www.noodlesoft.com/) per distinguere un problema di comprensione da un problema di regole. Se un documento contiene una data riconoscibile, una regola può estrarla dal testo e usarla nel nome. Se contiene un termine come “fattura” e un anno, altre regole possono indirizzarlo alla cartella corrispondente. Un PDF deve offrire testo leggibile, eventualmente attraverso OCR: l’estensione del file, da sola, non garantisce che il contenuto sia utilizzabile.

> “Probabilmente si può fare molto più velocemente e a minor spesa utilizzando strumenti come Hazel”
> — Filippo, 00:11:58

Il suggerimento nasce dal tipo di operazione, non da una preferenza assoluta per un’app. Quando la struttura dei documenti è nota, corrispondenze e regole possono risolvere il passaggio senza interrogare un modello generativo per ogni file. Prima di scegliere il sistema, occorre dunque capire quali caratteristiche permettono davvero di riconoscere e collocare il materiale.

### 3. Perché Roberto usa Note e torna a guardare Notion

Roberto racconta il passaggio da [Notion](https://www.notion.com/) a Note di Apple dopo aggiornamenti che avevano reso più interessante l’integrazione tra appunti, Promemoria e Calendario. Di Note apprezza la disponibilità sui propri dispositivi e soprattutto la possibilità di scrivere a mano e disegnare. Per un architetto queste funzioni incidono sulla scelta: un ambiente più ricco di integrazioni non sostituisce automaticamente un taccuino su cui annotare e tracciare uno schizzo.

Durante la registrazione, però, Roberto considera nuovamente Notion per le possibilità di collegamento con Claude tramite MCP. Il confronto riguarda il suo flusso di lavoro e la situazione osservata in quel momento: Note gli offre immediatezza e scrittura manuale; un altro sistema può offrire un accesso più diretto agli assistenti IA.

Roberto descrive anche la propria separazione tra documenti professionali e personali. I primi seguono una struttura legata al lavoro; i secondi possono essere organizzati secondo momenti della vita familiare, come il percorso scolastico dei figli. Chiede quindi a Daniele dove sente l’attrito maggiore: trovare le cose, scegliere dove metterle o mantenere il sistema. Daniele risponde che i problemi si alimentano a vicenda: un’organizzazione coerente aiuterebbe sia il recupero sia l’uso futuro dei materiali con un assistente.

### 4. L’IA produce nuovi materiali che devono essere archiviati

Daniele lega l’aumento del disordine all’uso più intenso dei progetti in [Claude](https://claude.com/product/overview). Dopo aver provato diversi servizi, lo preferisce per testi, script del podcast e articoli delle proprie newsletter, perché trova l’output più vicino al suo modo di esprimersi. È una valutazione della sua esperienza, non una classifica generale dei modelli.

Le chat, però, gli sembrano un luogo poco stabile per conservare il lavoro. Esporta quindi testi in Markdown, salva ricerche e prompt e raccoglie immagini per le copertine, generate anche con Nano Banana. L’assistente che dovrebbe semplificare il lavoro diventa così anche una fonte di nuovi file. Il problema si sposta dalla produzione alla conservazione: dove collocare ogni pezzo, come riconoscere un progetto concluso e quali materiali mantenere per usi successivi?

Il Markdown piace a Daniele perché gli permette di scrivere e mantenere testi semplici anche fuori dall’applicazione originaria. Ma la portabilità del formato non risolve da sola l’ordine delle cartelle. Avere i documenti sul disco resta utile soltanto se è chiaro il contesto in cui verranno cercati e riutilizzati.

### 5. Forever Notes e i documenti personali dentro Apple Note

Daniele spiega perché è passato da Obsidian a Note: sincronizzando il vault attraverso iCloud tra Mac e Windows aveva incontrato duplicati e file sincronizzati male. Non presenta questo come un difetto inevitabile di Obsidian; racconta il problema avuto nella propria configurazione. Note gli offre invece continuità tra Mac mini, iPad e iPhone senza dover gestire personalmente quel passaggio.

Adotta parte di [Forever Notes](https://www.myforevernotes.com/category/get-started), il metodo di Matthias Hilse. Gli interessano i collegamenti testuali tra note, che permettono di navigare il materiale senza affidarsi soltanto alle cartelle. Non usa però la sezione journal, perché la trova troppo elaborata per le proprie esigenze. Roberto aveva guardato lo stesso metodo con interesse, ma lo aveva abbandonato perché non si adattava alla sua struttura.

> “il mio second brain è Apple Note”
> — Daniele, 00:24:49

Per Daniele, Note contiene anche alcuni documenti: assicurazioni, informazioni sull’auto e sulla moto, materiali della casa e copertine del podcast. Tag e ricerca gli consentono di recuperarli rapidamente dall’iPhone. Precisa che non vi mette tutto: altri documenti rimangono nei file locali. In ufficio usa invece OneNote, secondo l’organizzazione dell’azienda. La scelta è quindi un insieme di ambienti con funzioni diverse, non un trasferimento completo della vita digitale in una sola applicazione.

### 6. Allegati, spazio e possibilità di esportazione

Roberto introduce il costo meno visibile di questa comodità. Allegati e appunti a mano possono aumentare lo spazio occupato dalle note e incidere sullo spazio iCloud. Racconta inoltre una difficoltà riscontrata dopo gli aggiornamenti: un’esportazione verso Pages che in precedenza gli permetteva di conservare immagini, PDF e annotazioni non restituisce più il risultato desiderato. Si tratta del comportamento osservato sul suo sistema, non di una verifica di tutte le versioni dell’app.

Filippo aggiunge il problema dell’accesso ai dati. Un insieme di note dentro un database è diverso da una cartella di file: può essere comodo da consultare nell’app, ma meno immediato da esportare o trattare in blocco. Dichiara di non conoscere un metodo semplice per salvare tutte le note in un’unica operazione e distingue quindi il dubbio dalla certezza tecnica.

La domanda pratica è cosa succede quando si vuole fare una copia indipendente o usare un’altra applicazione. Daniele cerca soprattutto velocità dal telefono; Filippo pone l’accento sull’accessibilità dei documenti sul disco. Le due esigenze non coincidono necessariamente e vanno considerate prima di aumentare la quantità di allegati nel sistema.

### 7. Assistenti desktop, MCP e materiali fuori dalle chat

Filippo suggerisce di valutare quanto il lavoro dipenda dall’IA. Se un assistente deve leggere, modificare e produrre molti documenti, una cartella di file offre un punto di accesso concreto e circoscrivibile. Le integrazioni basate su [MCP](https://modelcontextprotocol.io/) possono collegare servizi e note, ma le possibilità effettive dipendono dal connettore, dai permessi e dal sistema usato.

> “Il mio suggerimento è di andare su qualcosa di fisico.”
> — Filippo, 00:32:54

Per “fisico” intende materiale presente sull’hard disk, che possa essere letto e conservato fuori da una conversazione online. Porta l’esempio della preparazione di A2: scaletta e immagini realizzate con l’assistenza di Codex rimangono nella cartella della puntata, dove raccoglierà anche le tracce audio e i successivi materiali di pubblicazione.

Descrive poi un connettore esterno per [Perplexity](https://www.perplexity.ai/) e un’integrazione con [NotebookLM](https://notebooklm.google/). Li presenta come sperimentazioni e possibilità, specificando di non aver ancora provato direttamente alcuni passaggi di esportazione. Il punto comune è evitare che il lavoro rimanga disperso in chat separate e debba essere archiviato una seconda volta.

### 8. Syncthing, dischi esterni e sincronizzazione selettiva

Per i problemi del vault tra Mac e Windows, Filippo propone [Syncthing](https://syncthing.net/). Il sistema sincronizza cartelle tra computer: un file modificato su una macchina può arrivare alle altre quando sono disponibili. La scelta della singola cartella consente di trasferire le note senza replicare ogni archivio su tutti i dispositivi.

Daniele ricorda di avere poco spazio sul disco interno del Mac. Filippo spiega che una cartella sincronizzata può trovarsi anche su un disco esterno, purché sia collegato e visibile al sistema. Racconta la propria configurazione: un Mac mini sempre acceso mantiene i dati e riceve le modifiche dagli altri computer, propagandole quando le macchine si collegano. Se il disco viene scollegato, la cartella non è più disponibile per la sincronizzazione.

Su iPhone e iPad cita [Möbius Sync](https://mobiussync.com/), distinguendo le possibilità lette da quelle sperimentate personalmente. Il limite torna a essere lo spazio: un vault composto soprattutto da testo pesa poco, mentre replicare tutti i documenti dell’ufficio su un dispositivo mobile potrebbe saturarlo. Filippo mantiene quindi una separazione tra note e grandi archivi, scegliendo quali cartelle raggiungono ciascuna macchina. La sincronizzazione discussa qui riguarda la disponibilità dei file; il tema delle strategie di backup resta rinviato.

### 9. La scelta del metodo e il seguito su PARA

Prima della chiusura, i tre riconoscono che hanno affrontato soprattutto strumenti, formati e luoghi di conservazione. Rimane da decidere come organizzare il materiale nel tempo. Filippo spiega che conosce PARA ma, per le proprie pratiche professionali, utilizza una struttura di cartelle ripetuta per ogni posizione: il metodo va adattato alle esigenze effettive del lavoro.

Daniele ha iniziato a sperimentare la suddivisione dei vecchi archivi Dropbox e Box e vorrebbe capire meglio la differenza tra progetti, risorse e archivio. [PARA](https://fortelabs.com/blog/para/) viene quindi indicato come argomento della puntata successiva, non presentato qui come un percorso già svolto. Roberto osserva affinità con alcune idee di Forever Notes e torna alla distinzione tra ciò che possono fare regole come quelle di Hazel e ciò che richiede interpretazione.

Roberto aggiunge infine un pensiero personale sulla scrittura a mano e sul ritorno alla carta. L’interesse è recuperare uno spazio di riflessione, dopo una conversazione concentrata su sistemi digitali che raccolgono sempre più materiale. Daniele conferma la disponibilità a proseguire il confronto per passare dalla scelta degli strumenti all’organizzazione concreta dei propri archivi.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
