+++
title = "Automazione Apple nell’era dell’IA generativa"
date = 2026-09-14T07:00:00+02:00
episodeNumber = 80
slug = "80"
audioUrl = ""
spreakerEpisodeId = "74923293"
duration = "50:58"
description = "Filippo e Roberto confrontano automazioni classiche e IA generativa: Comandi Rapidi, Hazel, Keyboard Maestro, AppleScript, servizi cloud e agenti, con esempi reali e criteri per scegliere lo strumento giusto."
tags = ["automazione", "intelligenza-artificiale", "shortcuts", "workflow", "privacy", "sicurezza"]
draft = false

[params]
hasTranscript = true
guest = ""
youtubeId = "JDSL52az0ko"
+++

> Filippo e Roberto confrontano automazioni classiche e IA generativa: Comandi Rapidi, Hazel, Keyboard Maestro, AppleScript, servizi cloud e agenti, con esempi reali e criteri per scegliere lo strumento giusto.

## Note dell’episodio

- [A2 14: Introduzione all’automazione](https://a2podcast.it/14/): la prima puntata richiamata da Filippo per ricostruire il percorso di A2 tra automazioni, script e strumenti Apple.
- [A2 22: Introduzione a Comandi Rapidi e focus sull’app Craft](https://a2podcast.it/22/): uno degli episodi dedicati alle basi di Comandi Rapidi e all’integrazione tra applicazioni.
- [A2 24: Le basi di Comandi Rapidi](https://a2podcast.it/24/): puntata in cui Filippo e Roberto avevano costruito una prima automazione passo dopo passo.
- [A2 26: Comandi Rapidi per Calendario](https://a2podcast.it/26/): episodio citato nel riepilogo iniziale delle automazioni già affrontate dal podcast.
- [A2 52: Introduzione a Keyboard Maestro](https://a2podcast.it/52/): approfondimento sullo strumento che Roberto descrive come uno dei suoi punti di ingresso nell’automazione su Mac.
- [A2 56: Automazione dell’archiviazione digitale con Hazel](https://a2podcast.it/56/): puntata dedicata all’organizzazione automatica di file e documenti.
- [A2 59: Velocizzare la scrittura con le espansioni del testo](https://a2podcast.it/59/): riferimento per il passaggio sulle automazioni che riducono digitazione ripetitiva ed errori.
- [Comandi Rapidi](https://support.apple.com/it-it/guide/shortcuts/apda2b83d0e0/ios): manuale Apple dello strumento disponibile su iPhone, iPad e Mac.
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/): applicazione per creare macro e concatenare azioni sul Mac, spesso citata da Roberto.
- [Hazel](https://www.noodlesoft.com/): utility per organizzare e trasformare file in base a regole, al centro degli esempi di Filippo sull’automazione documentale.
- [Automator](https://support.apple.com/it-it/guide/automator/ensm2690/mac): strumento Apple con cui Roberto aveva costruito un’app per raccogliere, cifrare e salvare nel cloud i file modificati.
- [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/): linguaggio di automazione di macOS richiamato come collante tra applicazioni, oggi più accessibile grazie all’assistenza dell’IA nella scrittura del codice.
- [Zapier](https://zapier.com/), [Make](https://www.make.com/en), [n8n](https://n8n.io/) e [IFTTT](https://ifttt.com/): servizi citati per collegare applicazioni online e trasferire dati tra sistemi diversi.
- [Model Context Protocol](https://modelcontextprotocol.io/): protocollo discusso per collegare assistenti basati su IA a servizi e strumenti esterni.
- [Claude Code](https://claude.com/product/claude-code): assistente da riga di comando usato da Filippo nell’esempio di analisi del server domestico.
- [Proxmox Virtual Environment](https://proxmox.com/en/products/proxmox-virtual-environment/overview): piattaforma del server su cui Filippo ha analizzato i log e sperimentato una regolazione automatica delle ventole.

## Sinossi[^sinossi-ai]

### 1. Le automazioni Apple servono ancora?

Filippo e Roberto partono da una domanda molto concreta: nel 2026, dopo l’arrivo dell’intelligenza artificiale generativa e degli agenti capaci di interagire con computer e servizi, ha ancora senso imparare a usare gli strumenti tradizionali di automazione? La risposta anticipata dalla puntata è sì, ma con una distinzione importante. Le automazioni classiche e l’IA non sono concorrenti che si escludono a vicenda; risolvono problemi differenti e, quando vengono combinate con criterio, possono rafforzarsi.

Per ricostruire il quadro, i due conduttori ripercorrono alcuni temi già affrontati da A2: [Comandi Rapidi](https://support.apple.com/it-it/guide/shortcuts/apda2b83d0e0/ios), [Keyboard Maestro](https://www.keyboardmaestro.com/main/), [Hazel](https://www.noodlesoft.com/), espansioni del testo, [AppleScript](https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/) e Automator. Ciascuno occupa uno spazio diverso. Comandi Rapidi attraversa l’ecosistema Apple; Keyboard Maestro permette di costruire macro articolate sul Mac; Hazel osserva cartelle e documenti applicando regole; AppleScript può far comunicare applicazioni diverse. Proprio AppleScript mostra già il primo effetto dell’IA: non occorre necessariamente conoscere bene il linguaggio per farsi aiutare a produrre uno script, ma resta necessario capire cosa si vuole ottenere e controllare il risultato.

### 2. Dal backup con Automator ai servizi cloud

Roberto racconta un’automazione costruita anni fa con [Automator](https://support.apple.com/it-it/guide/automator/ensm2690/mac). Una piccola applicazione individuava i file modificati, li copiava, li cifrava e li salvava nel cloud. L’avvio restava manuale, perché dipendeva dalla qualità della connessione disponibile, ma la sequenza interna era automatica e ripetibile. L’esempio chiarisce che automatizzare non significa necessariamente eliminare ogni intervento umano: può bastare trasformare una procedura lunga e fragile in un comando avviato nel momento opportuno.

La stessa logica si è poi spostata sul web. Filippo cita [Zapier](https://zapier.com/), [Make](https://www.make.com/en), [IFTTT](https://ifttt.com/) e soprattutto [n8n](https://n8n.io/), sperimentato anche in self-hosting. Questi strumenti permettono di ricevere dati da un servizio, trasformarli e passarli a un altro: per esempio, elaborare le risposte di un modulo e inserirle nella struttura usata per gestire un cliente. Non viene proposto un confronto sistematico tra le piattaforme; il punto è mostrare come l’automazione abbia superato i confini del singolo Mac.

Nel quadro entra anche il [Model Context Protocol](https://modelcontextprotocol.io/), che consente a un assistente basato su IA di accedere, entro i permessi concessi, a strumenti e servizi esterni. La differenza è significativa: non si programma soltanto una catena prestabilita, ma si dà a un sistema linguistico la possibilità di scegliere e usare gli strumenti necessari per raggiungere un obiettivo.

### 3. Automatizzare significa rendere ripetibile un processo

Roberto propone una definizione essenziale, che diventa il centro della puntata:

> “Automatizzare significa delegare a un sistema una sequenza ripetibile di azioni.”
> — Roberto, 00:13:46

Da questa definizione nasce una serie di esempi quotidiani. Rinominare molti file secondo una convenzione; applicare codici coerenti agli elementi di un progetto BIM; preparare note o email ricorrenti; usare template nei flussi CAD e BIM; archiviare screenshot; trasformare una registrazione in materiale editoriale. Sono attività molto diverse, ma condividono una struttura: una parte del lavoro si ripete, segue regole descrivibili e può essere affidata a un sistema.

Il vantaggio non è soltanto risparmiare minuti. Un’automazione evita di ricostruire ogni volta la procedura, riduce il carico mentale e rende più uniforme il risultato. È particolarmente utile nei passaggi poco creativi ma necessari, quelli che interrompono il lavoro principale e moltiplicano le occasioni di dimenticanza. La condizione è che la regola sia sufficientemente precisa: una procedura deterministica non è infallibile, esegue con coerenza ciò che le è stato chiesto, compresi eventuali errori nella progettazione.

### 4. Meno errori, ma anche manutenzione

Filippo porta un esempio legato al processo civile telematico. Aveva bisogno di ordinare gli allegati secondo una sequenza visiva e rinominarli in modo coerente come “doc 1”, “doc 2” e così via. Il flusso che ha costruito permette di trascinare i documenti, disporli nell’ordine desiderato e ottenere i nomi corretti senza ripetere manualmente ogni operazione.

> “Automatizzare vuol dire anche ridurre gli errori.”
> — Filippo, 00:20:11

L’aspetto più interessante emerge subito dopo: per automatizzare, Filippo ha dovuto descrivere con chiarezza l’ordine delle operazioni. Il risultato non è soltanto uno strumento più veloce, ma un processo professionale esplicito, controllabile e riproducibile.

> “L’automazione spesso vuol dire anche formalizzare il flusso di lavoro.”
> — Filippo, 00:20:44

Questo investimento, però, ha un limite. Roberto ricorda che una soluzione fragile, dipendente da troppi componenti o soggetta a continue modifiche può richiedere più tempo di quanto ne faccia risparmiare.

> “L’automazione può diventare dannosa quando richiede decisamente più manutenzione del lavoro che dovrebbe risparmiare.”
> — Roberto, 00:18:12

Non tutte le azioni ripetute meritano quindi un sistema complesso: contano frequenza, stabilità della procedura, rischio di errore e costo della manutenzione.

### 5. L’IA abbassa la soglia d’ingresso, non elimina il controllo

L’intelligenza artificiale generativa cambia soprattutto il modo in cui si costruiscono le automazioni. Prima era necessario conoscere un linguaggio, cercare la sintassi corretta o affidarsi a chi sapeva programmare; oggi si può spiegare il problema in linguaggio naturale e chiedere una prima versione di uno script o di un workflow. Per Roberto è un passaggio paragonabile, con le dovute proporzioni, a quello dal tecnigrafo al CAD: lo strumento accelera il lavoro, ma non sostituisce la competenza necessaria per descrivere il problema e giudicare la soluzione.

> “L’intelligenza artificiale è un acceleratore. Non pensiate che vi risolva i problemi: ve ne può anche creare.”
> — Roberto, 00:21:54

La qualità della richiesta diventa parte della progettazione. Occorre chiarire input, trasformazioni, eccezioni e risultato atteso; poi bisogna verificare ciò che il modello ha prodotto. La facilità con cui si genera codice può infatti nascondere errori o concedere a un agente un accesso eccessivo. Per questo Roberto insiste sul confinamento: cartelle limitate, copie di sicurezza, permessi minimi e un ambiente nel quale un tentativo sbagliato non possa danneggiare dati importanti.

Filippo osserva che questa accessibilità amplia enormemente il numero delle persone capaci di costruire strumenti su misura. Il vincolo non è più soltanto la conoscenza tecnica: è anche sapere che una certa possibilità esiste e riuscire a immaginare una procedura utile.

> “Il vero limite […] è la fantasia dell’utente e sapere che si possono utilizzare questi strumenti.”
> — Filippo, 00:28:56

### 6. Tre livelli: chat, riga di comando e applicazioni desktop

Filippo distingue tre modalità di utilizzo. La prima è una normale chat, a cui chiedere istruzioni, formule o porzioni di codice da copiare nel proprio strumento. La seconda è rappresentata dagli assistenti a riga di comando, che possono leggere file, eseguire comandi e lavorare direttamente in un progetto. La terza comprende applicazioni desktop capaci, con le autorizzazioni appropriate, di interagire in modo più esteso con il computer.

Il caso più concreto riguarda un server [Proxmox](https://proxmox.com/en/products/proxmox-virtual-environment/overview) che manifestava blocchi periodici. Collegandosi via SSH e usando [Claude Code](https://claude.com/product/claude-code), Filippo ha fatto analizzare i log, formulare l’ipotesi di un surriscaldamento e preparare uno script per regolare le ventole. Al momento della registrazione, tuttavia, la modifica era attiva soltanto da circa un’ora: la causa e l’efficacia della soluzione richiedevano ancora settimane di osservazione.

> “Io non sarei riuscito a fare nulla di tutto questo senza dare le chiavi di casa all’intelligenza artificiale.”
> — Filippo, 00:34:10

La frase contiene sia la potenza sia il rischio dell’esperimento. L’assistente ha reso possibile un’indagine altrimenti fuori dalla portata di Filippo, ma ha ottenuto accesso a una macchina importante. Il risultato non è un invito a concedere permessi indiscriminati: è la dimostrazione del compromesso tra capacità operative, controllo e fiducia.

### 7. Deterministico e generativo non sono la stessa cosa

Un secondo esempio aiuta a separare i due mondi. Filippo ha usato l’IA per costruire l’interfaccia della diretta video: un compito progettuale, composto da molti elementi e ancora soggetto a piccoli problemi. Qui la capacità generativa di proporre una soluzione completa è preziosa. Per rinominare e spostare file secondo una regola stabile, invece, un sistema classico come Hazel o uno script resta spesso più semplice, controllabile ed efficiente.

> “L’intelligenza artificiale è un sistema non deterministico e tutte le automazioni di cui abbiamo parlato […] sono deterministiche.”
> — Filippo, 00:38:06

Un’automazione tradizionale, a parità di condizioni, segue sempre gli stessi passaggi. Un modello generativo può produrre risposte diverse e va usato proprio quando serve interpretare contenuto, affrontare variabilità o costruire qualcosa che non si lascia ridurre facilmente a regole rigide. Impiegare un LLM per ogni operazione non rende automaticamente il workflow migliore: può aggiungere latenza, costo, imprevedibilità e dipendenza da un servizio esterno.

### 8. Il workflow ibrido con cui A2 costruisce il proprio archivio

La lavorazione delle vecchie puntate di A2 offre un esempio di architettura ibrida. Il file MP3 viene trascritto localmente sul Mac Studio attraverso strumenti basati su MLX. Questa prima fase è ripetibile e può essere avviata con uno script; produce una trascrizione che conserva inevitabilmente errori nei nomi propri e nei termini tecnici. A quel punto interviene l’IA, non per sostituire il processo di trascrizione, ma per interpretare il testo, correggere mentalmente gli errori più evidenti e trasformarlo in una sinossi strutturata.

La divisione del lavoro segue la natura delle attività. Acquisizione del file e generazione dei formati sono passaggi tecnici; organizzare gli argomenti, scegliere citazioni e scrivere una pagina leggibile richiede comprensione linguistica. La procedura viene formalizzata in una skill, così l’IA riceve istruzioni, vincoli editoriali e controlli coerenti a ogni episodio. In questo modo il modello diventa un componente di un workflow più ampio, non un sostituto indistinto di tutti gli altri strumenti.

Il lavoro locale apre anche il tema della riservatezza. Per un professionista tenuto al segreto, inviare online il contenuto di documenti o registrazioni non è una scelta neutra. L’elaborazione sul proprio computer riduce l’esposizione verso servizi esterni, ma non equivale da sola a una garanzia generale di conformità: vanno comunque considerate tipologia dei dati, permessi, conservazione e misure organizzative.

### 9. Una regola pratica per scegliere lo strumento

Nella parte finale Filippo e Roberto guardano agli sviluppi possibili: una puntata specifica sugli MCP, un ritorno su Comandi Rapidi e una verifica delle nuove integrazioni dei sistemi Apple dopo un periodo di utilizzo reale. Evitano però di presentare funzioni ancora da provare come soluzioni consolidate. Il criterio utile non dipende dalla novità dello strumento, ma dal tipo di problema.

Per un’attività unica e ben circoscritta può bastare una chat che aiuti a trovare la soluzione. Se il compito è ripetuto, stabile e descrivibile con regole precise, conviene un’automazione deterministica. Se invece la struttura resta uguale ma cambia il contenuto — come nel passaggio da una trascrizione grezza alla sinossi di un episodio — l’IA può essere inserita dentro una procedura automatizzata, con verifiche e limiti definiti.

Resta infine un criterio di proporzionalità. Usare un grande modello per rinominare un file o compiere un’operazione banale può consumare più risorse del necessario, oltre a introdurre variabilità e possibili problemi di privacy. L’automazione migliore non è quella che usa la tecnologia più recente: è quella che riduce davvero attrito ed errori, rimane comprensibile e costa meno da mantenere rispetto al lavoro che sostituisce.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
