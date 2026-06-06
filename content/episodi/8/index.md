+++
title = "8: Backup, questo sconosciuto!"
date = "2021-03-22T06:00:00+01:00"
episodeNumber = 8
slug = "8"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336028/4c96f50f_d6a1_481b_9cbd_98b653fa7e5d.mp3"
spreakerEpisodeId = "64336028"
duration = "1:01:21"
description = "In questa puntata Bianca, Roberto e Filippo vi parlano di che cos'è un backup, perché è importante farlo e quali sono le strategie e soluzioni migliori."
tags = ["backup", "sicurezza", "macos", "storage", "produttivita"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "9L5K_jdat34"
+++

> In questa puntata Bianca, Roberto e Filippo vi parlano di che cos'è un backup, perché è importante farlo e quali sono le strategie e soluzioni migliori.

## Note dell’episodio

- [Eseguire il backup del Mac con Time Machine](https://support.apple.com/it-it/HT201250): guida Apple a Time Machine, usata nella puntata per spiegare backup automatici, incrementali e ripristino delle versioni precedenti su macOS.
- [Backblaze](https://www.backblaze.com/home-1.html): servizio di backup cloud citato come esempio di copia remota/off-site, con attenzione a costi, tempi di recupero e cifratura dei dati.
- [Come eseguire il backup del tuo iPhone, iPad e iPod touch](https://support.apple.com/it-it/HT203977): documentazione Apple sui metodi di backup tramite iCloud, Mac o PC per dispositivi iOS e iPadOS.
- [iMazing](https://dev.imazing.com/it/backup-iphone-ipad): app di terze parti citata per backup locali, wireless e più controllabili di iPhone e iPad.

## Sinossi[^sinossi-ai]

### 1. Perché il backup viene prima dello strumento

La puntata apre con una definizione molto concreta: un backup è la possibilità di non perdere i dati quando il dispositivo principale smette di essere disponibile. Filippo, Roberto e Bianca partono da esempi familiari, come fotografie, video, documenti personali e file di lavoro, per spostare subito il discorso sul punto più importante: i dati non sono solo “file”, ma spesso sono ricordi, pratiche professionali, anni di lavoro o materiali che non possono essere ricostruiti in tempi ragionevoli.

Filippo insiste sul concetto di disaster recovery: non basta chiedersi dove siano i dati oggi, bisogna chiedersi cosa succede se il Mac, l’iPhone o l’iPad vengono distrutti, rubati, cifrati da un ransomware o semplicemente smettono di funzionare. Da qui deriva una priorità editoriale chiara: prima si fa almeno una copia, poi si discute quanto sofisticata debba essere la strategia.

> "L'importante è fare almeno un backup."
> — Filippo, 00:03:17

La conversazione distingue anche tra dati personali e professionali. Le foto possono avere un valore affettivo enorme; i documenti di lavoro, invece, possono incidere direttamente sulla continuità di uno studio o di un’attività. Per questo la domanda non è soltanto “quanto spazio mi serve?”, ma anche “quanto tempo posso permettermi di perdere prima di tornare operativo?”.

### 2. Manuale, automatico, completo, incrementale: le parole base del backup

La prima distinzione operativa è tra backup manuale e backup automatico. Il backup manuale richiede memoria, disciplina e un gesto volontario: collegare un disco, avviare una procedura, copiare i file. Il backup automatico sposta invece il peso sull’applicazione o sul sistema operativo, che interviene a intervalli prestabiliti. La puntata non demonizza il manuale, ma evidenzia il limite più comune: se una procedura dipende dalla buona volontà dell’utente, prima o poi verrà saltata.

I conduttori passano poi ai tipi di copia. Il backup completo duplica l’intero disco o l’intero insieme di dati; è semplice da capire, ma può richiedere molto spazio. Il backup incrementale salva solo ciò che è cambiato rispetto all’ultimo backup, riducendo occupazione e tempi. Il backup differenziale conserva invece le modifiche rispetto all’ultimo backup completo. Roberto e Filippo usano esempi quotidiani per far capire che queste differenze non sono astratte: incidono sullo spazio necessario, sulla velocità e sul modo in cui si recuperano i file.

Anche i supporti vengono valutati in modo pratico. Il nastro magnetico viene citato come tecnologia storica ancora vista in alcuni ambienti; i dischi rigidi restano convenienti nel rapporto euro/gigabyte, ma possono rompersi; i supporti ottici sono ormai poco adatti per capacità e affidabilità; gli SSD sono resistenti agli urti, ma non sempre ideali per copie ripetute nel tempo. Il backup remoto aggiunge resilienza geografica, ma porta con sé dipendenza dalla connessione, costi e tema della riservatezza.

### 3. Sincronizzazione, versioning e RAID non sono la stessa cosa

Uno dei passaggi più utili della puntata è la distinzione tra backup e sincronizzazione. iCloud, Dropbox, OneDrive e servizi simili permettono di avere gli stessi file su più dispositivi, ma non garantiscono automaticamente una vera strategia di recupero. Se un file viene cancellato o danneggiato e la modifica si propaga su tutti i dispositivi, la sincronizzazione può replicare il problema invece di risolverlo.

> "La sincronizzazione non vuol dire backup."
> — Filippo, 00:26:40

Il versioning attenua il problema, perché consente di tornare a versioni precedenti di un documento o recuperare file cancellati entro un certo periodo. Ma anche qui i conduttori invitano a non confondere una funzione utile con una strategia completa. Se il periodo di recupero è limitato, o se il servizio non conserva abbastanza storia, il versioning aiuta solo entro una finestra temporale precisa.

Il RAID viene trattato nello stesso modo: utile per la continuità operativa, non sufficiente come backup. Avere più dischi che replicano i dati può proteggere da un guasto fisico, ma non protegge necessariamente da cancellazioni, errori dell’utente, furti, incendi o malware. La ridondanza mantiene il sistema in piedi; il backup deve permettere di tornare indietro quando il sistema o i dati non sono più affidabili.

### 4. La regola 3-2-1 come criterio minimo

Filippo introduce la regola 3-2-1 come base da cui partire: tre copie complessive, due copie on-site su supporti differenti e una copia off-site, conservata in un luogo diverso. L’esempio è quello dello studio: un backup Time Machine collegato al Mac, una seconda copia locale su supporto separato e una copia conservata altrove, per esempio a casa. Il senso non è accumulare dischi, ma coprire rischi diversi con copie diverse.

> "La regola è quella del 321."
> — Filippo, 00:29:21

La puntata chiarisce anche il problema dei backup sempre collegati. Una copia online, cioè un disco sempre connesso al computer, è comoda e favorisce l’automazione, ma se il Mac viene colpito da un ransomware può finire per salvare dati già cifrati. Una copia offline, scollegata dopo l’uso, è meno comoda ma più resistente a questo tipo di rischio. Per professionisti e studi, il punto pratico è bilanciare comodità e separazione: un backup che non viene mai fatto non serve, ma un backup sempre esposto può non bastare.

La regola 3-2-1 viene quindi presentata come una mappa dei rischi. Rottura del disco, furto, errore umano, ransomware e disastro fisico richiedono risposte differenti. Nessuna singola soluzione copre tutto; una strategia ragionevole combina più copie con ruoli diversi.

### 5. Time Machine, versioni precedenti e clonazione del disco

La parte su [Time Machine](https://support.apple.com/it-it/HT201250) entra nel funzionamento più familiare agli utenti Mac. Time Machine è descritta come una soluzione trasparente, automatica e incrementale: una volta configurata, copia periodicamente i dati e consente di recuperare versioni precedenti di file e cartelle. Filippo usa l’esempio di un documento modificato e poi rimpianto: se il capo chiede la versione del giorno prima, il versioning permette di recuperarla senza riscriverla.

> "Time Machine salva dati sull'hard disk finché c'è spazio sull'hard disk."
> — Roberto, 00:33:37

Il vantaggio è particolarmente forte per documenti di testo e file piccoli: con un disco capiente, Time Machine può conservare anni di storia. Quando lo spazio finisce, elimina progressivamente i backup più vecchi. La puntata ricorda anche che Time Machine può lavorare con dischi di rete: la vecchia Time Capsule non esiste più, ma NAS e altri Mac possono essere configurati per diventare destinazioni di backup, riducendo l’attrito del cavo fisico.

Accanto a Time Machine viene citata la clonazione del disco. Qui la logica cambia: non si recupera solo un file, ma si crea una copia dell’intero disco. La copia “a caldo”, fatta con il computer acceso, è più comoda ma può essere meno pulita se durante la procedura i dati cambiano; la copia “a freddo”, con il disco non in uso, richiede più passaggi ma riduce il rischio di incoerenze. Per database e sistemi complessi, questa distinzione è importante.

### 6. Backup remoto, iCloud, iMazing e dispositivi mobili

Nel backup remoto entra in gioco [Backblaze](https://www.backblaze.com/home-1.html), citato come servizio cloud relativamente economico per singolo computer e spazio ampio. La puntata però evita l’entusiasmo automatico: il backup remoto dipende dalla velocità della connessione, può essere lento in fase di primo caricamento e soprattutto può diventare scomodo quando bisogna recuperare grandi quantità di dati. Scaricare terabyte in emergenza non è la stessa cosa che ripristinare un singolo file.

Sul piano della riservatezza, Filippo sottolinea che un backup cloud richiede fiducia nel fornitore, salvo usare cifratura lato utente. Il servizio remoto è ottimo come copia off-site, ma va valutato con domande precise: chi può leggere i dati, quanto costa il ripristino, quanto tempo serve per tornare operativi e se la copia copre davvero tutti i file importanti.

La chiusura tecnica riguarda iPhone e iPad. Apple offre backup tramite iCloud oppure tramite Mac/PC, come riepilogato nella [guida ufficiale per iPhone, iPad e iPod touch](https://support.apple.com/it-it/HT203977). iCloud è comodo perché avviene in modo automatico quando il dispositivo è in carica e sotto Wi-Fi; il backup locale richiede più disciplina, ma può essere cifrato e conservato sotto controllo diretto. Per chi vuole più granularità viene citato [iMazing](https://dev.imazing.com/it/backup-iphone-ipad), che permette backup incrementali e recupero più mirato di contenuti come messaggi e chat.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
