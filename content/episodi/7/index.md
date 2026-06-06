+++
title = "7: Manutenzione del Mac: procedure ed utility"
date = "2021-03-15T06:00:00+01:00"
episodeNumber = 7
slug = "7"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336034/50020470_14b4_4ed1_9888_81ddff04d8d9.mp3"
spreakerEpisodeId = "64336034"
duration = "59:35"
description = "In questa puntata Roberto e Filippo vi parlano di come tenere il vostro Mac in perfetta forma. 1. Antivirus ? Ha senso installare un antivirus / anti-malware??? Sicurezza su macOS (https://www.apple.com/it/macos/security/) Gatekeeper supporto Apple (https://support.apple.com/it-it/guide/deployment-r"
tags = ["mac", "sicurezza", "app"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "lV14XbD_v1I"
+++

## Note dell’episodio

- [Sicurezza su macOS](https://www.apple.com/it/macos/security/): panoramica ufficiale Apple sui meccanismi di protezione integrati nel sistema operativo.
- [Gatekeeper — Riferimento deployment macOS](https://support.apple.com/it-it/guide/deployment-reference-macos/apd02b925e38/web): documentazione Apple su come Gatekeeper controlla l'installazione delle applicazioni.
- [Protezione da malware su macOS](https://support.apple.com/it-it/guide/mac-help/mh40596/mac): guida Apple sulle firme anti-malware aggiornate automaticamente da XProtect.
- [Pi-hole](https://pi-hole.net/): sistema di filtraggio DNS a livello di rete per bloccare pubblicità, tracker e domini malevoli noti.
- [Virus e probiviri](http://macintelligence.org/blog/2018/01/13/virus-e-probiviri/): articolo di Lucio Bragagnoli sulla sicurezza dei Mac, citato in puntata da Roberto.
- [Bitdefender Virus Scanner](https://www.bitdefender.com/solutions/virus-scanner-for-mac.html): scanner antivirus gratuito per Mac, usato da Roberto nella sua routine mensile.
- [BlockBlock](https://objective-see.com/products/blockblock.html): utility gratuita di Objective See che segnala in tempo reale l'esecuzione di servizi persistenti non autorizzati.
- [OverSight](https://objective-see.com/products/oversight.html): utility di Objective See che avvisa ogni volta che un'applicazione accede al microfono o alla fotocamera.
- [Objective See](https://objective-see.com/index.html): raccolta di utility gratuite per la sicurezza su Mac, curata da Patrick Wardle.
- [Gemini](https://macpaw.com/gemini): app per trovare ed eliminare file duplicati, anche immagini con nomi diversi ma contenuto identico.
- [Come liberare spazio di archiviazione sul Mac](https://support.apple.com/it-it/HT206996): guida ufficiale Apple allo strumento integrato di gestione dello spazio su disco.
- [DaisyDisk](https://daisydiskapp.com/): utility a pagamento con grafico a torta interattivo per analizzare l'occupazione dell'hard disk cartella per cartella.
- [AppCleaner](https://freemacsoft.net/appcleaner/): app gratuita per disinstallare applicazioni rimuovendo anche tutti i file di preferenze associati.
- [Hazel](https://www.noodlesoft.com): utility di automazione che, tra le altre funzioni, rileva e rimuove i file residui quando si disinstalla un'applicazione.
- [OnyX](https://titanium-software.fr/en/onyx.html): utility di manutenzione per macOS (disponibile in versione specifica per ogni sistema operativo) che libera cache e ottimizza il sistema; da usare con cautela.
- [Macs Fan Control](https://crystalidea.com/macs-fan-control): utility gratuita per controllare manualmente la velocità delle ventole e monitorare le temperature dei sensori interni.

---

## Sinossi[^sinossi-ai]

### 1. Benvenuti in famiglia: figli ospiti e DAD al tempo della pandemia

L'episodio si apre in modo insolito: insieme ai due conduttori Roberto Marin e Filippo Strozzi ci sono anche i loro figli, Bianca e Andrea, ospiti speciali della diretta del venerdì sera. È la prima settimana di didattica a distanza e la tecnologia Apple è già protagonista della vita quotidiana dei ragazzi: Bianca usa l'iPad con WeSchool, Andrea lavora su un iMac da 24 pollici. L'intervista ai due giovani è leggera e divertente — lista dei desideri inclusa (un iPhone, una Apple Pencil tutta sua, un iPad di ultima generazione) — ma serve anche da contrappunto pratico all'argomento principale della puntata: la manutenzione del Mac. Roberto introduce il tema ricordando che, a differenza di Windows, macOS non ha un registro di sistema e le applicazioni sono per lo più autocontenute in pacchetti `.app`, il che rende il sistema strutturalmente più stabile e pulito per sua natura.

### 2. Antivirus sì o no? La posizione di Filippo

Filippo prende la parola sul tema sicurezza e fa subito chiarezza: la domanda «devo installare un antivirus?» è tipicamente da utente Windows, e su Mac la risposta dipende dal comportamento dell'utente. La quota di mercato di macOS è storicamente più bassa rispetto a Windows, il che lo rende un bersaglio meno appetibile per gli hacker, e di conseguenza la quantità di malware circolante è significativamente inferiore.

Per un utente attento — che non apre allegati sospetti, non clicca su link nelle email, non scarica contenuti da siti di streaming pirata — la risposta è tendenzialmente no. I principali vettori di contagio restano le email di phishing e i siti discutibili, non il sistema operativo in sé. Filippo segnala però un rischio spesso trascurato: avere un virus per Windows sul proprio Mac senza saperlo, e rischiare di contagiare macchine Windows sulla stessa rete.

> "Se siete utenti relativamente attenti e consapevoli nell'utilizzo del proprio computer, la risposta a se installare o meno un antivirus è tendenzialmente no."
> — Filippo, 00:08:09

Per chi invece naviga senza particolari accortezze, l'antivirus rimane consigliato, con la consapevolezza che qualsiasi software residente che analizza continuamente il disco ha un costo in termini di prestazioni. Filippo racconta in prima persona di aver installato un antivirus su un Mac e di averlo poi rimosso perché il degrado delle performance era evidente.

### 3. Le difese integrate di Apple: Gatekeeper, XProtect e il volume di sola lettura

Apple ha progressivamente irrigidito la propria politica di sicurezza. Filippo illustra tre livelli di protezione che macOS offre nativamente. Il primo è **Gatekeeper**, che richiede all'utente con privilegi di amministratore di autorizzare esplicitamente l'installazione di software non firmato. Il secondo è **XProtect**, il sistema di firme anti-malware aggiornato silenziosamente da Apple, che opera in background senza bisogno di configurazione. Il terzo, introdotto con Big Sur, è il **volume di sistema in sola lettura**: la partizione che contiene il sistema operativo non può essere modificata nemmeno con i permessi di root, il che rende strutturalmente molto più difficile un'infezione profonda.

Filippo ricorda anche la politica di Apple sugli aggiornamenti di sicurezza: vengono garantiti tipicamente per le ultime due versioni di macOS. Al momento della registrazione (inizio 2021) il limite era Mojave (10.14); con l'uscita di Big Sur, Catalina sarebbe diventato presto il confine. Chi usa sistemi più vecchi di quel limite è esposto.

### 4. Pi-hole e la protezione della rete di casa

Filippo introduce brevemente un sistema che va oltre il singolo computer: **Pi-hole**, un filtro DNS a livello di rete. L'idea è semplice: invece di proteggere ogni dispositivo singolarmente, si filtra il traffico a monte, bloccando la risoluzione dei domini noti per distribuire pubblicità, tracker e malware — inclusi i domini usati dai ransomware più diffusi. È una protezione che vale per tutti i dispositivi connessi alla rete, Mac, iPhone, iPad e PC Windows compresi. Filippo riconosce che approfondire Pi-hole richiederebbe una puntata a sé, ma vuole che gli ascoltatori sappiano che questo livello di protezione esiste.

### 5. La routine mensile di Roberto: Bitdefender, BlockBlock e OverSight

Roberto descrive nel dettaglio la sua procedura di manutenzione, che esegue il primo di ogni mese. Non usa un antivirus residente, ma avvia una volta al mese **Bitdefender Virus Scanner** (gratuito), che scarica le firme aggiornate, esegue una scansione completa dell'hard disk da 128 GB in circa mezz'ora e segnala eventuali corrispondenze. È una scansione a chiamata, non un processo permanente in background, e quindi non incide sulle prestazioni quotidiane.

A presidio del sistema in tempo reale usa invece due utility di **Objective See**, entrambe leggerissime e gratuite. La prima è **BlockBlock**: rimane silenziosamente attiva nella barra dei menu, monitora i servizi che si avviano all'interno del sistema operativo e avvisa l'utente ogni volta che un processo tenta di installarsi in modo persistente. Roberto racconta un episodio divertente: aveva provato a bloccare un servizio di Spotify con BlockBlock e Spotify aveva smesso di funzionare. Nessun segnale di malware, ma la prova che lo strumento funziona davvero.

> "Nel momento in cui vede qualcosa di strano, te lo fa sapere."
> — Roberto, 00:21:13

La seconda utility è **OverSight**: monitora microfono e fotocamera e avvisa immediatamente quando un'applicazione tenta di accedervi senza che l'utente l'abbia richiesto esplicitamente. Per un professionista che tratta dati sensibili, è una protezione concreta contro accessi non autorizzati alla telecamera del Mac.

Roberto segnala che il sito di Objective See contiene molte altre utility, tra cui una per monitorare il traffico di rete, e consiglia di esplorarlo.

### 6. Liberare spazio: lo strumento integrato di Apple, Gemini e DaisyDisk

Roberto passa alla gestione dello spazio su disco, argomento particolarmente sentito per chi lavora con un SSD da 128 GB. Il primo strumento che consiglia è già integrato nel sistema: dal menu Apple → *Informazioni su questo Mac* → *Archiviazione* → *Gestisci*, si accede a una panoramica dell'occupazione suddivisa per categoria (applicazioni, documenti, foto, mail, musica, sistema). La tab *Browser file* permette di navigare le cartelle e individuare quelle più pesanti, in modo simile a DaisyDisk ma senza installare nulla.

> "Questa è una delle grandi novità dei sistemi operativi Apple che ha tagliato le gambe a molte utility."
> — Roberto, 00:28:24

Filippo aggiunge che DaisyDisk va oltre: il grafico a torta interattivo permette di scendere nella gerarchia delle cartelle e scoprire cache nascoste o file di sistema in posizioni non standard, come i backup di iPhone e iPad che possono occupare decine di gigabyte senza che l'utente se ne accorga. Il costo è intorno ai 15 euro.

Per la ricerca di duplicati, Roberto cita **Gemini**, che riesce a identificare file identici anche con nomi diversi, per esempio confrontando le immagini a livello di contenuto. Roberto precisa che lo ha usato in un periodo in cui era incluso in un bundle in abbonamento tipo Setapp.

Viene citata anche **GrandPerspective** (o Grand Perspective), utility gratuita che rappresenta graficamente l'hard disk con rettangoli proporzionali alle dimensioni dei file, raggruppati per tipo e colorati per categoria. Utile per individuare con un colpo d'occhio i file più pesanti.

Durante la diretta, Roberto scopre di avere ancora 12 GB occupati dall'installer di Big Sur — lo aveva installato su un disco esterno ma non aveva cancellato il file sorgente — e li elimina in diretta. Filippo, dal canto suo, nota 4 GB di film archiviabili e 55 GB occupati dalla libreria foto.

### 7. Disinstallare le applicazioni nel modo giusto

Roberto spiega la differenza tra la disinstallazione su Mac e su Windows. Su Mac, nella maggior parte dei casi, basta trascinare l'applicazione nel cestino: le app sono autocontenute nel pacchetto `.app` e non contaminano il registro di sistema. I file di preferenze (`.plist`) rimangono nella cartella Libreria, ma sono piccoli e non causano problemi.

Chi vuole una pulizia più completa può usare **AppCleaner**: si trascina l'applicazione nell'interfaccia di AppCleaner, che individua tutti i file associati sparsi nel sistema e li presenta all'utente prima di eliminarli. Filippo usa invece **Hazel**, che intercetta automaticamente l'eliminazione di un'app e propone di rimuovere anche tutti i file collegati.

La distinzione che Filippo tiene a fare riguarda i file `.pkg` (pacchetti di installazione tipici di driver e stampanti), che scrivono in profondità nel sistema operativo e richiedono un disinstaller dedicato. I normali file `.dmg` — dove basta trascinare l'icona nella cartella Applicazioni — non hanno questo problema.

### 8. OnyX: pulizia del sistema con i superpoteri (da usare con giudizio)

Roberto introduce **OnyX** come strumento di manutenzione avanzata del sistema: libera le cache di macOS, Safari e delle applicazioni, e permette di eseguire le script di manutenzione Unix che solitamente girano di notte. Avverte però con forza che OnyX è potente e richiede attenzione.

> "Come per Spider-Man, dai grandi poteri derivano grandi responsabilità."
> — Roberto, 00:44:41

Tre avvertenze pratiche: esiste una versione di OnyX per ogni versione di macOS e non sono intercambiabili; va avviato con tutte le altre applicazioni chiuse, perché richiede un riavvio al termine; le impostazioni di default sono sicure, ma avventurarsi nelle sezioni avanzate senza sapere cosa si fa può causare problemi seri. Il consiglio di Roberto è di limitarsi alla scheda *Manutenzione*, lasciare tutto su default ed eseguire — niente di più.

### 9. Manutenzione hardware: pulizia esterna e gestione delle ventole

La parte finale è dedicata all'hardware. Roberto descrive la sua routine di pulizia fisica, valida anche per iPad e iPhone. Per scocca e tastiera usa un panno inumidito di alcol: durante la pandemia è il minimo igienico, ma serve anche a rimuovere lo sporco che si accumula invisibilmente. Per lo schermo del Mac raccomanda invece il panno in microfibra da occhiali leggermente inumidito con acqua, per via del rivestimento più delicato rispetto ai display di iPhone e iPad.

La parte più originale riguarda le ventole. Roberto racconta che l'idea gli è venuta da un amico comune, Nicola Lossito, che aveva problemi di surriscaldamento con un iMac da 27 pollici e aveva risolto mandando le ventole al massimo con **Mac Fan Control** (evoluzione di SMC Fan Control, non compatibile con i chip T2 dei Mac più recenti). Con le ventole a piena velocità per circa venti minuti, la polvere accumulata all'interno viene espulsa senza dover aprire il computer.

> "Tutti i vari residui che ci sono all'interno di un portatile vengono espulsi. Per me lo è stato perché lo utilizzo praticamente dal 2014."
> — Roberto, 00:51:46

Roberto usa questa tecnica anche come precauzione prima di avviare rendering pesanti: mette le ventole al massimo prima di iniziare, in modo che il processore lavori subito in condizioni termiche ottimali anziché scaldarsi e aspettare che il sistema operativo reagisca con ritardo. La versione gratuita di Mac Fan Control è sufficiente per questo scopo: permette di salvare un preset automatico (sistema operativo) e uno al massimo, oltre a mostrare i valori di tutti i sensori di temperatura interni.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
