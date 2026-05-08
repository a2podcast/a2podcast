+++
title = "8: Backup, questo sconosciuto!"
date = "2021-03-22T06:00:00+01:00"
episodeNumber = 8
slug = "8"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336028/4c96f50f_d6a1_481b_9cbd_98b653fa7e5d.mp3"
spreakerEpisodeId = "64336028"
duration = "1:01:21"
description = "Backup, questo sconosciuto! Scopri cos'è un backup, perché è essenziale e quali sono le migliori strategie e soluzioni per proteggere i tuoi dati su Mac."
draft = false

[params]
  hasTranscript = false
tags = ["backup", "sicurezza dati", "macos", "storage", "produttivita"]
+++

> In questa puntata Bianca, Roberto e Filippo vi parlano di che cos'è un backup, perché è importante farlo e quali sono le strategie e soluzioni migliori.

È operativo anche il sito ufficiale con le note degli episodi

* [a2podcast.it](http://a2podcast.it)
* [a2podcast.it/youtube](http://www.a2podcast.it/youtube) per il canale dove trovate le nostre dirette del venerdì sera.

Se volete **supportare il podcast** vi chiediamo con il cuore di fare una **recensione su Apple Podcast.** In questo fase iniziale tante recensioni ci permetteranno di essere visti da più persone possibili.

Se volete sapere come fare una recensione trovate il [link qui](https://www.avvocati-e-mac.it/podcast/itunes).

# Note episodio

## 1. macOS

### Perché è importante un backup ?

* Rottura / compromissione disco fisso
* Furto
* Ransomware

Differenza tra:

* backup manuale = l'utente deve ricordarsi di farlo ed avviare il programma di backup
* backup automatico = il software si occupa automaticamente ad intervalli prestabiliti di fare un backup

Differenza tra:

* **backup completo** = copia dell'intero sistema o disco
* **backup incrementale** = Un repository incrementale mira a rendere minore l'occupazione dello spazio per la memorizzazione delle copie dei dati in base alle differenze che ci sono tra i dati in uso e quelli che sono già nel repository. Questo elimina la necessità di memorizzare copie duplicate di dati invariati
* **backup differenziale** = vengono salvati solo i dati che sono stati modificati dopo l'ultimo backup completo

Supporti di backup:

* **Nastro magnetico** (vecchio)
* **disco rigito** = soluzione più performanete Gb / costo, possibilità di rottura e smagnetizzazione
* **Supporti ottici** (obsoleti ormai, non si smagnetizzano ma possono venire danneggiati dal tempo ossidazione o rottura, dimensioni limitare rispetto disco rigido)
* **SSD** (dischi a stato solido) = come HD ma limitata capacità di riscrittura quindi non consigliati, minor rischio di rottura
* **backup remoto / offsite** spazio su un server esterno, solitamente affittato, non si ha sicurezza completa dei dati (salvo cifratura più oltre) si evita che un disastro possa far perdere i dati

Differenza backup:

* online: più efficienti e permettono automazione
* offline: più sicuri rispetto a ransomware non sono collegati a PC attivi, abitualmente da fare manualmente o comunque collegare il backup manualmente

### Cosa non è un backup ?

La **sincronizzazione** ≠ backup

Ad esempio iCloud o Dropbox non sono un backup ma un modo per sincronizzare i dati da un PC ad un altro. Alcune di queste soluzione hanno un sistema di versioning (vedi dopo) che di fatto è una sorta di backup (è possibile ripristinare documenti a versioni di salvataggio precedenti / documenti cancellati) MA sono spesso limitati nel tempo (30 giorni abitualmente).

Avere i dati in cloud meglio che non avere niente ma la sincronizzazione cloud non è un backup.

Dischi fissi ridondanti (**RAID**) non è in senso tecnico una forma di backup ma un sistema per garantire che i dati “operativi” non subiscano danni. È tuttavia una forma di protezione dei dati.

### La regola 3, 2, 1.

**3** backup complessivi, **2** on site su supporti differenti (ad esempio bakcup timemachine e backup offline in un cassetto su disco rigido), **1** backup conservato in un luogo geografico differente da dove sono i dati di cui si vuole fare il backup.

### Time Machine

[Sistema trasparente di Apple](https://support.apple.com/it-it/HT201250).

Backup, automatico ed incrementale su disco. Sisterma di versioning possibilità di “tornare indietro nel tempo” ad una versione precedente.

Possibilità di fare backup time-machine anche su dischi presenti in rete (non esiste più la time-capsule ma è possibile configurare NAS ed altri computer per un backup time-machine).

Time-machine fa anche una “fotografia del sistema operativo” è quindi possibile riavviare un mac con il disco fisso danneggiato direttamente dal backup di time machine.

### Clonazione del disco

Copia dell’intero disco fisso di un computer. Possibile fare una **copia a caldo** (con il computer acceso) o **a freddo** (con il disco fisso del computer non acceso). La prima è più agile ma il disco viene scritto nel mentre che viene fatto il backup e quindi ci sono rischi di modifiche dello stesso (pericoloso in caso di database ad esempio), il secondo è meno comodo (necessità per esempio di avviare il Mac da un disco esterno con un sistema operativo ulteriore) ma garantisce copie “sicure”.

### Backup cloud / remoto

* Lento (legato al collegamento internet)
* Meno sicuro (possibilità che l'hosting provider possa vedere i vostri dati – salvo che facciate backup cifrati)
* potenzialmente costoso ([Backblaze](https://www.backblaze.com/home-1.html) relativamente poco costoso 6$ mese e spazio illimitato ma legato a solo un computer)
* costoso recuperare i documenti (backblaze permette di scaricare i singoli file ma se necessario recuperare un intero disco allora i costi salgono e non è pensabile scaricare Gb o Tb di dati in breve tempo – salvo per Filippo che ha la FTTH 😆).

#### Versioning

Un file system di **controllo delle versioni** è qualsiasi file system di computer che consente a un file di computer di esistere in più versioni contemporaneamente. Quindi è una forma di controllo di revisione. I file system di controllo delle versioni più comuni mantengono un numero di vecchie copie del file. Alcuni limitano il numero di modifiche al minuto o all'ora per evitare di memorizzare un numero elevato di modifiche banali. Altri invece scattano istantanee periodiche ai cui contenuti è possibile accedere con una semantica simile al normale accesso ai file.

Questo in se e per se non è un backup.

## Backup iOS / iPadOS

[Guida Apple](https://support.apple.com/it-it/HT203977)

### Backup cloud: iCloud

Unico presente, bisogna fidarsi di Apple (Apple ha concesso accesso ai backup dei dispositivi su iCloud alle forze dell’ordine Americane quindi questa soluzione deve essere considerata non sicura a livello di riservatezza dei dati).

### Altre modalità di backup: iMazing

[iMazing](https://dev.imazing.com/it/backup-iphone-ipad): Garantisci la sicurezza dei tuoi dati sul tuo Mac o PC con la tecnologia di backup unica di iMazing. Wireless, privata e automatica: è la migliore soluzione di backup per il controllo dei dati dei tuoi iPhone e iPad.

## Dove ci possono trovare?

### Bianca:
Quando avrà quant'anni e dei figli potrete avere i suoi contatti 😜 (quantomeno così dice il padre Roberto).

### Roberto:

[Mac e architettura: mach - dot - net.wordpress.com](https://marchdotnet.wordpress.com/) [Podcast settimanale Snap - architettura imperfetta](https://www.spreaker.com/show/snap-archiettura-imperfetta)

### Filippo:

[Avvocati e Mac punto it](https://www.avvocati-e-mac.it/)
