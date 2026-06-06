+++
title = "50: Apple Mail"
date = "2023-01-09T06:00:00+01:00"
episodeNumber = 50
slug = "50"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64335978/fedb7b19_6f44_4d22_a619_19b1f903d369.mp3"
spreakerEpisodeId = "64335978"
duration = "1:26:31"
description = "In questa puntata Roberto e Filippo faranno un approfondimento sul programma di posta elettronica montato sui dispositivi Apple: Mail."
tags = ["email", "mac", "iphone", "ipad"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "DaZ8H7_ATRo"
+++

> In questa puntata Roberto e Filippo faranno un approfondimento sul programma di posta elettronica montato sui dispositivi Apple: Mail.

## Note dell’episodio
- [29: Email (Introduzione): il problema delle email e come cercare di risolverlo](https://a2podcast.it/29/): puntata precedente dedicata al sovraccarico da email e ai criteri generali per gestirle meglio.
- [32: Email (parte II): gli aspetti tecnici](https://a2podcast.it/32/): approfondimento sui protocolli e sugli aspetti tecnici della posta elettronica richiamati nella discussione su IMAP e POP.
- [Mail - Supporto Apple](https://support.apple.com/it-it/mail): pagina Apple che raccoglie le guide ufficiali per Mail su Mac, iPhone, iPad e iCloud.
- [Manuale utente di Mail per Mac](https://support.apple.com/it-it/guide/mail/welcome/mac): documentazione Apple sulle funzioni di Mail in macOS, incluse caselle, ricerca, regole e gestione dei messaggi.
- [Usare Mail su iPhone, iPad o iPod touch](https://support.apple.com/it-it/ht201419): guida Apple per configurare e usare Mail su dispositivi iOS e iPadOS.
- [Usare Mail di iCloud](https://support.apple.com/it-it/ht203528): guida Apple sulla casella iCloud Mail e sulle sue impostazioni.
- [Utilizzare Mail di iCloud su iCloud.com](https://support.apple.com/it-it/guide/icloud/mm6b1a17e3/icloud): guida all’interfaccia web di Mail di iCloud, distinta dal client Mail installato sui dispositivi Apple.
- [Cercare le email in Mail sul Mac](https://support.apple.com/it-it/guide/mail/mlhlp1003/15.0/mac/13.0): guida Apple alla ricerca in Mail, funzione discussa in puntata per filtri, mittenti, allegati e query concatenate.
- [Le novità di Mail sul Mac](https://support.apple.com/it-it/guide/mail/cpmlwn/mac): pagina Apple sulle funzioni recenti di Mail in macOS Ventura, tra cui invio programmato, annulla invio e promemoria.
- [Manuale utente di Comandi Rapidi per Mac](https://support.apple.com/it-it/guide/shortcuts-mac/welcome/mac): riferimento Apple per creare automazioni, richiamato nel confronto tra Mac, iPhone e iPad.
- [AppleScript Language Guide](https://help.apple.com/applescript/mac/10.9/): guida AppleScript, citata per le automazioni avanzate di Mail e l’integrazione tra applicazioni macOS.
- [Manuale utente di Automator per Mac](https://support.apple.com/it-it/guide/automator/welcome/mac): documentazione Apple su Automator, ancora utile per alcune azioni legate a Mail.
- [AppleScript rules in Mail](https://stackoverflow.com/questions/27952360/applescript-rules-in-mail): discussione tecnica su come scrivere AppleScript compatibili con le regole di Mail.
- [Utilizzo delle regole di filtro in Apple Mail](https://clean.email/create-email-rules/apple-mail-rules): panoramica pratica sulle regole di Mail, utile per capire condizioni e azioni automatiche.
- [Apple Mail rules you should be using](https://www.makeuseof.com/tag/apple-mail-rules/): articolo con esempi di regole per filtrare mittenti sconosciuti, spam, domini importanti e messaggi con allegati.
- [SpamSieve](https://c-command.com/spamsieve/): estensione antispam citata come esempio di componente esterno per Mail.
- [Free-GPGMail](https://github.com/Free-GPGMail/Free-GPGMail): progetto open source per integrare GPG e crittografia email in Mail.
- [GPG Mail](https://gpgtools.org/gpgmail/index.html): componente di GPG Suite per cifrare e firmare email in Mail su macOS.
- [Come usare PGP su Mac](https://proprivacy.com/email/guides/pgp-mac): guida introduttiva all’uso di PGP su Mac, collegata alla parte sulla cifratura della posta.
- [I miei nove plug-in indispensabili per Apple Mail](https://www.macworld.com/article/223159/my-nine-must-have-plug-ins-for-apple-mail.html): articolo storico sui plug-in per Apple Mail, utile per contestualizzare un ecosistema oggi molto cambiato.
- [MailMate](https://freron.com): client email per Mac citato da Filippo come alternativa avanzata, in particolare per chi vuole scrivere messaggi in Markdown.

## Sinossi[^sinossi-ai]

### 1. Perché tornare su Mail alla puntata 50
Filippo e Roberto aprono l’episodio 50 tornando al tema da cui era partita una parte importante del percorso del podcast: la gestione della posta elettronica. Non riprendono l’argomento in senso generale, già affrontato nell’episodio 29, né gli aspetti tecnici trattati nell’episodio 32, ma si concentrano sul client Mail di Apple: l’app installata su Mac, iPhone e iPad e collegata, in parte, anche al mondo iCloud.

Roberto ricorda che la posta resta uno degli strumenti più invasivi nella vita quotidiana: i client sono pieni di messaggi, newsletter, comunicazioni di lavoro e notifiche, e Mail è spesso il programma che gli utenti Apple si trovano davanti senza averlo scelto consapevolmente. Da qui nasce l’obiettivo della puntata: capire che cosa fa bene, che cosa fa meno bene e quali funzioni meno evidenti possono renderlo più utile.

Filippo distingue subito due piani che spesso vengono confusi. Da un lato c’è Mail come applicazione: il client per macOS, iOS e iPadOS, sempre più coerente tra le piattaforme pur con differenze operative. Dall’altro lato c’è iCloud Mail, cioè sia la casella `@icloud.com` sia l’interfaccia web disponibile su iCloud.com. Quest’ultima non è un duplicato universale di tutte le caselle configurate nell’app Mail, ma riguarda la posta iCloud e il relativo servizio.

> "Abbiamo le vere e proprie applicazioni, cioè abbiamo un'applicazione per macOS, per iOS e per iPadOS."
> — Filippo, 00:02:17

Il discorso su iCloud porta anche a una considerazione pratica sullo spazio. Filippo nota che la casella iCloud è legata allo spazio iCloud disponibile: chi ha il piano da 2 TB vede quello spazio riflettersi anche sulla posta. È una scoperta quasi laterale, ma rilevante per chi usa davvero iCloud Mail come archivio. Viene citata anche la possibilità di collegare un dominio personalizzato alla posta iCloud, funzione pensata più per un uso familiare che per una gestione professionale strutturata.

### 2. Interfaccia, caselle, colonne e personalizzazione
La parte centrale dell’episodio entra nell’interfaccia di Mail. Filippo descrive soprattutto iPadOS, perché durante la registrazione mostra l’app nella diretta video: la struttura tipica è a tre colonne. A sinistra ci sono caselle e account, al centro l’elenco dei messaggi della casella selezionata, a destra l’anteprima del messaggio. Su iPad con schermi grandi la tripartizione è visibile e stabile; su iPad più piccoli la colonna sinistra può scomparire e si richiama con il pulsante in alto a sinistra. Su iPhone la stessa logica esiste, ma diventa sequenziale: si entra nelle caselle, poi nell’elenco dei messaggi, poi nel singolo messaggio, tornando indietro con la freccia.

Roberto sottolinea che sugli iPad più piccoli questa semplificazione può essere persino più pulita. Anche su macOS lui tende a chiudere la colonna delle caselle quando non serve, perché l’interfaccia a due colonne lascia più spazio all’elenco e alla lettura. Filippo osserva che questo schema è ormai tipico delle applicazioni Apple più articolate e delle app professionali che cercano di adattarsi bene tra Mac e iPad.

Un elemento importante è la personalizzazione della barra laterale. Mail permette di decidere quali caselle o viste speciali mostrare: posta ricevuta oggi, bozze, contrassegnate, messaggi da ricordare, invio programmato e altre raccolte. È una funzione che Filippo ammette di aver scoperto tardi, anche perché non usa Mail come client principale, ma che considera molto utile per adattare l’app al proprio modo di lavorare.

La puntata dedica spazio anche ai flag, o contrassegni. Mail permette di usare più colori di bandierina, sincronizzati tra le app Mail dei vari dispositivi Apple. Il punto è che questa ricchezza resta interna all’ecosistema Mail: altri client possono vedere che un messaggio è contrassegnato, ma non necessariamente distinguere il colore. Per chi lavora dentro Mail, però, i contrassegni diventano un sistema semplice per attribuire importanza, contesto o priorità ai messaggi.

Roberto aggiunge una funzione piccola ma molto utile: il filtro che mostra solo le mail non lette, rappresentato da un’icona rotonda con tre linee. Secondo lui è un modo rapido per alleggerire la vista e ridurre il rumore mentale dentro una casella molto piena.

> "Nasconde di default le mail che avete già letto e quindi riesce anche a liberarvi mentalmente."
> — Roberto, 00:27:43

### 3. Cartelle smart, ricerca e configurazione degli account
Filippo introduce le cartelle smart, disponibili su macOS ma non su iOS e iPadOS. Le paragona alle cartelle smart del Finder: non sono vere cartelle della casella di posta, ma viste dinamiche costruite su criteri. Una cartella smart può raccogliere tutte le mail di Roberto, indipendentemente dall’account in cui sono arrivate, oppure tutti i messaggi relativi a un progetto, magari individuati da un numero di riferimento nell’oggetto o dalla presenza di allegati.

Roberto chiede se si tratti più di un filtro che di una cartella reale, e Filippo conferma. Per lui sono utili soprattutto a chi usa la posta come database documentale, cercando spesso allegati o conversazioni per progetto. Roberto racconta invece un approccio diverso: sposta le comunicazioni nelle cartelle del lavoro corrispondente, salva gli allegati dove gli servono e poi alleggerisce Mail, così da non appesantire troppo il database dell’applicazione e lo spazio locale.

La ricerca viene presentata come una funzione migliorata nelle versioni recenti. Filippo mostra che Mail evidenzia i termini trovati nel corpo o nell’oggetto del messaggio e consente ricerche più mirate: per mittente, periodo, nome dell’allegato e combinazioni di criteri. È possibile concatenare più elementi, per esempio cercare messaggi inviati da una persona specifica con un allegato dal nome determinato. Pur non usandola quotidianamente, perché lavora con un altro client, Filippo riconosce che la ricerca è diventata più strutturata.

La configurazione degli account viene trattata senza entrare nei passaggi puntuali, perché Mail offre procedure guidate per i provider più comuni: Microsoft Exchange, Google, Yahoo e AOL. Per gli account meno standard, come molte caselle italiane o PEC, serve configurazione manuale. Filippo e Roberto notano che le PEC degli ordini professionali possono funzionare in Mail e che spesso i fornitori italiani pubblicano guide specifiche per configurare i parametri corretti.

A questo punto torna la distinzione tra IMAP e POP. Filippo sintetizza IMAP come il protocollo adatto a chi usa più dispositivi, perché mantiene la casella sul server e sincronizza lettura, cancellazioni e archiviazioni. POP, invece, scarica i messaggi e, a seconda delle impostazioni, può rimuoverli dal server, rendendo più difficile una gestione coerente tra Mac, iPhone e iPad.

> "L'IMAP mi permette, cioè, per esempio, se ho letto un'email e voglio vederla come ho letto."
> — Filippo, 00:34:07

### 4. Le novità recenti: annulla invio, invio programmato e promemoria
Filippo passa poi alle funzioni introdotte con iOS e iPadOS 16 e con macOS Ventura. La prima è “Annulla invio”, che però viene spiegata come un artificio più che come un vero richiamo del messaggio: Mail non invia immediatamente l’email, ma aspetta un breve intervallo configurabile. In quel margine di tempo l’utente può bloccare l’invio, correggere il testo o aggiungere un allegato dimenticato.

La seconda funzione è l’invio programmato, che Filippo considera molto più importante. Mail permette di scegliere opzioni rapide, come inviare la sera o la mattina seguente, oppure una data e un’ora precise. Il caso d’uso è concreto: scrivere una mail in orari poco opportuni e farla partire alle 8 del giorno dopo. Il limite è tecnico e operativo. A differenza di altri client, come Airmail, Mail non usa un server esterno per spedire il messaggio programmato: l’invio avviene dal dispositivo. Di conseguenza, il dispositivo deve essere acceso, funzionante e collegato a internet.

Questo porta Filippo a suggerire, per chi voglia usare seriamente queste funzioni insieme alle regole, l’idea di un Mac sempre acceso, magari un Mac mini usato come piccolo server domestico o professionale. In quel caso Mail può restare aperto e gestire invii programmati e automazioni in modo più affidabile.

La terza funzione è “Ricordamelo”, che permette di far riemergere una mail in un momento scelto. I conduttori ragionano su come raggiungerla nell’interfaccia: su iPad e iPhone si può arrivare tramite swipe e menu “Altro”, facendo attenzione a non eseguire lo swipe completo che attiva l’azione predefinita. È una funzione utile, ma non sempre immediata da trovare.

> "Quello che invece, secondo me, è la funzione che non era possibile non avere su Mail, e invece adesso finalmente c'è il send later."
> — Filippo, 00:37:51

### 5. Automazioni tra Comandi Rapidi, AppleScript, Automator e regole
La parte più tecnica dell’episodio riguarda le automazioni. Filippo mette in evidenza una differenza netta: su macOS Mail può sfruttare strumenti storici e potenti come AppleScript e Automator; su iOS e iPadOS le possibilità passano soprattutto da Comandi Rapidi. Il risultato è paradossale: su iPhone e iPad ci sono più azioni Mail disponibili in Comandi Rapidi rispetto al Mac, mentre su macOS rimangono molto più forti gli strumenti tradizionali.

Filippo racconta un esempio concreto di automazione su Mac: la generazione di attestati per circa quaranta persone. Partendo da dati in Numbers e da un modello in Pages, lo script ha creato PDF personalizzati, generato email separate con destinatario, testo e allegato corretti, e inviato i messaggi. È un esempio di cosa significa far dialogare applicazioni diverse tramite AppleScript.

Su iOS e iPadOS, invece, Filippo cita automazioni più semplici ma comunque utili: aprire una casella specifica di Mail, cercare messaggi, inviare email o mostrare la casella VIP. Aprire direttamente una casella può aiutare a mantenere il focus: nel weekend si può entrare solo nella posta personale, mentre durante il lavoro si può evitare la casella privata o le newsletter. Questo si collega anche alla gestione delle notifiche. Filippo consiglia di disattivare le notifiche di Mail e, se necessario, usare aggiornamenti manuali, così da non subire continuamente l’arrivo dei messaggi.

La casella VIP viene citata come eccezione ragionata: si possono indicare persone importanti, come un familiare, e ricevere notifiche anche quando il resto della posta è silenziato. Non è quindi una questione di chiudere completamente Mail, ma di scegliere quali messaggi meritano davvero attenzione immediata.

Le regole di Mail su macOS vengono descritte come uno strumento potente. Si basano su condizioni e azioni: se un messaggio arriva da un mittente, contiene un certo oggetto, è indirizzato a un account specifico, ha allegati o proviene da qualcuno fuori dai contatti, allora Mail può spostarlo, copiarlo, colorarlo, eliminarlo, inoltrarlo, rispondere automaticamente o eseguire un AppleScript. Filippo sottolinea che combinando più condizioni si possono costruire filtri molto precisi, ma serve progettazione: una regola troppo aggressiva rischia di archiviare messaggi importanti.

### 6. Plugin, cifratura, PEC, Markdown e alternative a Mail
Nella parte finale Filippo affronta i limiti di Mail e le alternative. Ricorda che in passato esisteva un ecosistema più ricco di plug-in per Apple Mail, soprattutto su macOS, ma Apple ha cambiato il sistema delle estensioni e molti vecchi plug-in non sono più compatibili con le versioni moderne. Vengono citati SpamSieve per il filtro antispam e Free-GPGMail o GPG Mail per la cifratura con GPG.

La cifratura viene spiegata nei suoi principi essenziali: una mail normale è sostanzialmente testo leggibile; per renderla riservata occorre usare una chiave pubblica del destinatario per cifrarla e una chiave privata per decifrarla. Roberto collega il tema alla logica delle chiavi pubbliche e private usata anche in altri contesti moderni di autenticazione.

Filippo spiega poi perché non usa Mail come client principale. Utilizza Airmail, anche per alcune funzioni che per lui sono decisive. Una riguarda la PEC: in Mail spesso bisogna aprire un messaggio EML dentro il messaggio PEC, con un doppio passaggio fastidioso; Airmail, invece, gli consente di leggere la PEC in modo più diretto, anche se non controlla il certificato come farebbe un sistema specifico. Un altro limite di Mail è l’impossibilità di colorare in modo evidente le diverse caselle dentro una inbox unificata. Roberto ipotizza che si possa risolvere con automazioni e flag, ma Filippo osserva che sarebbe meglio avere questa funzione integrata nel programma.

C’è poi il tema dello spazio. Con IMAP, Mail tende a sincronizzare tutta la posta disponibile sul server, e chi ha anni di corrispondenza può ritrovarsi con molti gigabyte occupati sul disco. Si può ridurre il problema evitando di scaricare gli allegati, ma per Filippo resta un limite rispetto a client che permettono di sincronizzare solo gli ultimi trenta giorni.

Infine, Filippo cita l’impossibilità di scrivere direttamente email in Markdown. Il suo trucco è usare un Comando Rapido che converte Markdown in testo ricco, da incollare poi in Mail. Per chi vuole una soluzione più nativa su Mac, segnala MailMate, client avanzato che supporta Markdown e molte automazioni.

Roberto chiude con due osservazioni pratiche. La prima è la mancanza di una funzione comoda per i modelli di messaggio: lui invia spesso email simili per struttura e vorrebbe salvarle come template modificabili. Filippo suggerisce Comandi Rapidi, Automator o strumenti come TextExpander, ma Roberto nota che il suo Mac fermo a Big Sur non ha ancora Comandi Rapidi. La seconda riguarda allegati problematici, in particolare PDF e file P7M ricevuti da ambienti Windows o via Gmail. In alcuni casi Mail non mostra correttamente il contenuto o l’allegato, e la soluzione più pragmatica resta accedere al client web della casella per scaricare i file.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
