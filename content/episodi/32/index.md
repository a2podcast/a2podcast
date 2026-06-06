+++
title = "32: Email (parte II): gli aspetti tecnici"
date = "2022-04-11T05:00:00+01:00"
episodeNumber = 32
slug = "32"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336041/04862468_92b5_4038_89a5_8988cdb9f6a6.mp3"
spreakerEpisodeId = "64336041"
duration = "59:11"
description = "Oggi parleremo delle email ma con un taglio più tecnico rispetto alla puntata 29. Infatti approfondiremo il funzionamento sotto il cofano delle email (cos'è IMAP e POP3), alcune particolarità dei servizi di posta elettronica più famosi , come rendere più sicure le email, come salvare le email sul vo"
tags = ["email", "sicurezza"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "5OGvLz9ZDZY"
+++

> Oggi parleremo delle email ma con un taglio più tecnico rispetto alla puntata 29. Infatti approfondiremo il funzionamento sotto il cofano delle email (cos'è IMAP e POP3), alcune particolarità dei servizi di posta elettronica più famosi , come rendere più sicure le email, come salvare le email sul vostro computer.

## Note dell’episodio
- [POP3](https://it.wikipedia.org/wiki/Post_Office_Protocol): protocollo storico di ricezione della posta, spiegato in puntata con la metafora della cassetta postale e del messaggio scaricato sul computer.
- [IMAP](https://it.wikipedia.org/wiki/Internet_Message_Access_Protocol): protocollo oggi più comune per sincronizzare la stessa casella email tra Mac, iPhone, iPad e altri client.
- [Gmail](https://www.google.com/intl/it/gmail/about/): uno dei servizi di posta più diffusi, citato per la configurazione semplificata su Apple Mail, lo spazio cloud e le implicazioni privacy degli account gratuiti.
- [Gmail per Google Workspace](https://workspace.google.com/products/gmail/): versione professionale a pagamento di Gmail, richiamata nella distinzione tra caselle gratuite e servizi business.
- [Programmare l’invio delle email in Gmail](https://support.google.com/mail/answer/9214606?hl=it): funzione citata come buona pratica per scrivere quando si vuole ma spedire in orari lavorativi.
- [Mail di iCloud](https://support.apple.com/it-it/guide/icloud/mm6b1a0b80/icloud): servizio Apple discusso come alternativa a Gmail, soprattutto per chi vive nell’ecosistema iCloud.
- [Panoramica sulla sicurezza di iCloud](https://support.apple.com/it-it/HT202303): pagina Apple collegata al tema della protezione dei dati e dell’approccio più attento alla privacy rispetto ad altri provider gratuiti.
- [Protezione della privacy di Mail su iPhone](https://support.apple.com/it-it/guide/iphone/iphf084865c7/15.0/ios/15.0): funzione Apple citata nel contesto delle protezioni offerte da iCloud e Mail.
- [Kill the Newsletter!](https://kill-the-newsletter.com/): servizio open source citato da Filippo per trasformare le newsletter in feed RSS, evitando di intasare la casella email principale.
- [Airmail](https://airmailapp.com/): client email usato da Filippo, citato per funzioni come la sincronizzazione limitata agli ultimi mesi, il bounce e una gestione più avanzata delle caselle.
- [Sanebox](https://www.sanebox.com): servizio che filtra le email a monte analizzando almeno gli oggetti dei messaggi, discusso con attenzione per il tema dell’accesso alla casella.
- [DEVONthink](https://www.devontechnologies.com/apps/devonthink): applicazione citata per l’importazione massiva e la ricerca dentro archivi di email in formato EML.
- [Come salvare una mail sul PC](https://www.aranzulla.it/come-salvare-una-mail-sul-pc-1144680.html): guida pratica collegata al tema finale dell’archiviazione locale delle email.

## Sinossi[^sinossi-ai]

### 1. Client, server e protocolli: cosa succede sotto il cofano dell’email

Filippo e Roberto riprendono il tema delle email, già affrontato in una puntata precedente con un taglio più organizzativo, e questa volta lo spostano sul piano tecnico. L’obiettivo è capire che cosa succede quando un messaggio viene ricevuto, letto, sincronizzato o salvato. Filippo parte da un problema molto concreto: molte persone non hanno nemmeno configurato la propria posta su iPhone, non per scelta consapevole o per evitare distrazioni, ma perché non sanno quali parametri inserire.

Da qui introduce la distinzione essenziale tra client e server. Mail, l’app di Apple su macOS, iOS e iPadOS, è il client: il programma che permette di leggere e gestire i messaggi. Il server, invece, è il computer remoto che riceve, conserva e invia la posta. Per far comunicare questi due mondi servono protocolli, e i due principali al centro della puntata sono POP3 e IMAP.

POP3 viene descritto come il sistema più vecchio, simile alla posta tradizionale. Il messaggio arriva al server del destinatario e da lì viene scaricato sul computer dell’utente. Se non si lascia una copia sul server, quella mail vive solo sul dispositivo che l’ha scaricata. Filippo spiega che questo approccio aveva senso quando una persona usava un solo computer, ma diventa problematico appena entrano in gioco più macchine, per esempio un computer a casa e uno in ufficio. Se la posta viene scaricata da una parte, non è più disponibile dall’altra.

IMAP risolve proprio questo limite. I messaggi restano sul server e i vari dispositivi si sincronizzano con quella casella centrale. Una mail letta, cancellata o inviata da Mac risulta coerente anche su iPhone e iPad. Il vantaggio è l’ubiquità della posta elettronica; lo svantaggio è che tutta la corrispondenza resta nel cloud del provider e tende ad accumulare molto spazio, soprattutto quando si inviano e ricevono allegati pesanti.

> "Il vantaggio grosso dell’IMAP è che una volta che voi avete scaricato la posta sul vostro computer di casa, la potete scaricare anche contemporaneamente sull’iPhone o sull’iPad."
> — Filippo, 00:05:55

### 2. POP3 o IMAP: comodità, controllo e backup

Alla domanda su quale protocollo sia migliore, Filippo risponde con un classico “dipende”. Nella maggior parte dei casi, soprattutto per chi usa più dispositivi, IMAP è la scelta più pratica. Permette di avere tutto sincronizzato, di ritrovare la posta inviata ovunque e di lavorare senza preoccuparsi di quale dispositivo abbia scaricato per primo un messaggio.

La conversazione però non liquida POP3 come tecnologia morta. Filippo lo considera ancora interessante in scenari specifici: per esempio quando si vuole che un solo computer scarichi tutta la posta e la conservi localmente, riducendo il tempo in cui i messaggi rimangono sul server. Questo approccio richiede più disciplina, perché bisogna avere backup seri e magari sincronizzare i dati locali tra più computer, ma offre un maggiore controllo sul proprio archivio.

Roberto collega IMAP al tema della privacy: se tutto resta sincronizzato su server di grandi provider, in particolare Gmail, bisogna accettare che la propria posta sia custodita da un soggetto esterno. Filippo chiarisce che Gmail non usa un IMAP completamente standard e ricorda i problemi storici con Apple Mail. Poi sottolinea un punto netto: sugli account gratuiti, Google analizza la posta per costruire servizi e pubblicità, mentre le garanzie più forti sono riservate ai clienti business.

La puntata insiste anche sull’aspetto dello spazio. Gmail offre una quantità di archiviazione gratuita generosa, ma non infinita. Roberto racconta di aver trovato email vecchissime, risalenti anche al 2008, e di aver dovuto ripulire la casella. Filippo aggiunge che IMAP sincronizza tutto: non solo il server si riempie, ma anche Mac, iPhone e iPad possono ritrovarsi occupati da anni di corrispondenza. Per questo cita Airmail, che gli permette di sincronizzare solo gli ultimi mesi e non l’intero archivio.

> "Da buon avvocato, la risposta è dipende."
> — Filippo, 00:09:30

### 3. Gmail, iCloud, forward e servizi di posta

La parte sui servizi parte da Gmail, definito di fatto il servizio email più diffuso nel mondo occidentale. Roberto nota che la configurazione su iPhone e Mac è ormai molto semplice, quasi guidata. Filippo conferma, ma spiega che Google richiede ormai forme di autenticazione più moderne, come token e autenticazione a due fattori, rendendo più difficile usare il vecchio schema di configurazione IMAP con semplice server, utente e password.

Filippo ricorda che, in generale, per configurare una casella bisogna conoscere almeno due elementi: il server per ricevere e sincronizzare la posta, cioè IMAP o POP3, e il server SMTP per l’invio. Ogni provider pubblica di solito pagine con i parametri corretti per i vari client, anche se non sempre l’esperienza è lineare. Racconta un problema recente con una casella Aruba che non riusciva a configurare in Apple Mail nonostante le istruzioni.

Roberto propone il forward come soluzione pratica in alcuni casi: far inoltrare i messaggi da una casella problematica verso Gmail o un altro provider più gestibile. Filippo spiega che anche A2 usa un forward per l’indirizzo del podcast: il dominio riceve la posta e la gira verso una casella letta dai conduttori. Il forward è quindi presentato come un compromesso utile, non come una soluzione perfetta.

Il discorso si sposta poi su Libero e sui vecchi provider gratuiti. Filippo è molto critico verso Libero, soprattutto per la sicurezza e per la quantità di spam generata da caselle compromesse. Racconta che in passato la configurazione era complicata proprio perché il provider spingeva a usare i propri sistemi. Il tema non è solo tecnico: una casella vecchia, poco protetta o abbandonata può diventare una sorgente di spam, phishing e catene indesiderate.

### 4. iCloud, alias, newsletter e il problema dello spam

Dopo Gmail, Filippo introduce iCloud. Il servizio Apple viene presentato come particolare: non è semplicemente una casella a pagamento, ma è legato allo spazio e ai servizi iCloud. Con i piani più recenti Apple offre funzioni interessanti, tra cui la possibilità di usare domini personalizzati con alcune limitazioni e strumenti più orientati alla privacy. Filippo però distingue chiaramente l’uso personale dall’uso professionale: iCloud permette alcune personalizzazioni, ma non arriva a essere una piattaforma email professionale completa.

Il punto centrale resta la sicurezza. Filippo ripete che l’email non è un mezzo sicuro per scambiare informazioni riservate. Se bisogna inviare contenuti confidenziali, bisogna cifrarli o usare strumenti diversi. Non basta scegliere iCloud o Gmail: il mezzo email, per sua natura, nasce come comunicazione semplice e veloce, non come canale blindato.

Nel ragionamento entrano anche le email temporanee, gli alias e le newsletter. Filippo cita Kill the Newsletter!, un servizio open source che genera un indirizzo email dedicato per iscriversi alle newsletter e trasforma i messaggi ricevuti in un feed RSS. In questo modo le newsletter possono essere lette in un lettore di feed invece di entrare nella casella principale. Roberto gli chiede se abbia poi cancellato l’iscrizione con l’indirizzo originale; Filippo spiega che usa il sistema soprattutto per testare nuove newsletter, mentre per le vecchie ha una casella ormai di risulta.

Questo passaggio porta al tema dello spam e delle cancellazioni. Filippo osserva che il pulsante di annullamento iscrizione può essere comodo, ma anche rischioso: quando ci si cancella da una newsletter gestita male o da uno spammer, si può confermare che la casella è attiva. Airmail offre anche una funzione di bounce, cioè un finto avviso di errore che segnala al mittente che la casella non esiste o ha problemi, con l’obiettivo di generare un feedback negativo.

> "Se dovete gestire della corrispondenza sicura, l’email non lo è."
> — Filippo, 00:25:32

### 5. Phishing, ransomware e buone pratiche di sicurezza

La puntata entra poi nella sicurezza pratica. Filippo spiega che molte campagne email funzionano come pesca a strascico: si mandano messaggi a milioni di indirizzi e si punta su percentuali minime di risposta. Anche se solo una piccola parte dei destinatari compra qualcosa, inserisce credenziali o cade in una truffa, l’operazione può essere redditizia.

Gli esempi sono concreti. Filippo racconta il caso del suocero truffato tramite una falsa comunicazione sulla carta prepagata o sull’home banking: cliccando sul link, ha consegnato le credenziali ai truffatori, che hanno eseguito bonifici rapidi verso l’estero. Cita anche un cliente che ha ricevuto un finto avviso Aruba per il rinnovo del dominio, con richiesta di pagamento tramite carta di credito.

Da qui arrivano le raccomandazioni operative: non cliccare sui link nelle email, non aprire allegati strani, controllare sempre il mittente e diffidare anche quando il nome visualizzato sembra familiare. I client spesso mostrano “Avvocato Filippo Strozzi” invece dell’indirizzo reale, ma quel nome può essere falsificato. Per questo bisogna aprire i dettagli del mittente e guardare il dominio effettivo, soprattutto se il messaggio chiede denaro, credenziali, documenti o azioni urgenti.

Filippo parla anche di ransomware: email che portano a scaricare software capace di cifrare il contenuto del disco e chiedere un riscatto. Pagare non garantisce nulla, perché il sistema di decifrazione può non esistere più o non funzionare. L’unica difesa reale, oltre alla prevenzione, è una strategia di backup solida. Tornano così temi già trattati in puntate precedenti: password robuste, password manager, autenticazione a due fattori, firewall, antivirus e soprattutto attenzione umana.

> "Mai mai cliccare sui link all’interno dell’email o aprire gli allegati all’interno di una mail, soprattutto di gente sconosciuta."
> — Filippo, 00:33:09

### 6. Archiviare le email: PDF, EML, MSG e valore dei messaggi

Nella parte finale Filippo affronta l’archiviazione. Il primo motivo per archiviare è non lasciare troppa roba sui server altrui, soprattutto se la casella contiene anni di corrispondenza, allegati, documenti personali e informazioni sensibili. L’email non dovrebbe diventare un archivio documentale completo: può essere un archivio di corrispondenza, ma non il posto in cui conservare tutto senza criterio.

La modalità più semplice è salvare o stampare la mail in PDF. Filippo non ama questa soluzione, ma la riconosce come praticabile in molti casi. Sconsiglia invece la stampa su carta. Il PDF, però, è una fotografia della mail: può essere comodo per leggere e conservare, ma non mantiene tutti i dati tecnici del messaggio. Dal punto di vista giuridico, una mail conservata come EML o MSG è più interessante, perché mantiene struttura, intestazioni, allegati e metadati.

Filippo spiega che EML è il formato base delle email, mentre MSG è il formato proprietario di Outlook, ormai molto diffuso. Una mail semplice, se riconducibile a un soggetto tramite indirizzo, contesto e scambi precedenti, può avere un valore probatorio. Per questo il formato conta: se si conserva solo una stampa o un PDF, si perdono elementi che possono essere rilevanti.

Il passaggio più tecnico riguarda la natura stessa dei file EML. Aprendoli con un editor di testo si vede che l’email contiene mittente, destinatario, oggetto, data, server attraversati, versione testuale, versione HTML e allegati codificati. Gli allegati vengono inseriti come testo codificato, spesso in base64, e questo spiega perché le email con allegati pesano molto. Filippo racconta di usare questi dati anche per automazioni di archiviazione, per esempio estraendo la data di spedizione direttamente dal contenuto del file.

> "L’email è un semplice file di testo, essendo un file di testo, tutto è in chiaro."
> — Filippo, 00:44:05

### 7. Cifratura, SSL, Sanebox, invio programmato e ricerca negli archivi

Dalla struttura dei file EML Filippo passa al tema della cifratura. Oggi, configurando un account, è opportuno attivare SSL: in questo modo il traffico tra client e server viene cifrato durante il transito. Questo però non significa che la mail sia cifrata ovunque. Se qualcuno entra nel server, il messaggio può essere leggibile in chiaro. Per cifrare davvero il contenuto esistono sistemi basati su chiavi pubbliche e private: chi invia usa la chiave pubblica del destinatario, il destinatario decifra con la propria chiave privata. Filippo ne descrive il principio, ma sottolinea che nella pratica è una procedura complessa e poco compatibile con la comodità quotidiana dell’email.

Tra i servizi collaterali cita Sanebox, che filtra la posta a monte e aiuta a ridurre il rumore nella casella. Filippo segnala però il costo in termini di fiducia: per funzionare, il servizio deve avere accesso alla casella, anche se dichiara di leggere soprattutto gli oggetti dei messaggi. È uno strumento interessante, ma non neutro dal punto di vista della privacy.

Un’altra funzione utile è l’invio programmato. Filippo la considera una buona prassi: si possono scrivere email di notte, nel weekend o in momenti improbabili, ma farle partire il primo giorno lavorativo utile, magari alle 8:30 o alle 9. Gmail lo permette nativamente; Apple Mail, al momento della puntata, no. La funzione può essere gestita lato server oppure tramite automazioni locali, ma in ogni caso aiuta a non imporre i propri orari agli altri.

La chiusura reale dell’argomento riguarda l’archiviazione operativa degli allegati. Roberto osserva che il file EML si porta dietro gli allegati, quindi non è necessario salvarli separatamente solo per conservarli. Filippo distingue: se gli allegati servono nella pratica o devono essere modificati, li salva nella cartella corretta; poi conserva anche l’EML nella corrispondenza, così mantiene la prova che quei file sono arrivati con quella mail.

Infine discutono della ricerca. Su macOS, Finder non sempre cerca bene dentro i file EML; Filippo ha scoperto che per alcuni comportamenti servirebbe l’estensione EMLX o software dedicati. DEVONthink viene citato come strumento più adatto per importare caselle, indicizzare email, renderizzare i messaggi e cercare anche dentro archivi complessi. La puntata si chiude quindi non con una teoria astratta, ma con un criterio pratico: scegliere il formato di archiviazione in base a ciò che si dovrà ritrovare, provare o modificare in futuro.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
