+++
title = "56: Automazione dell'archiviazione digitale con Hazel"
date = "2023-04-03T05:00:00+01:00"
episodeNumber = 56
slug = "56"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64335997/ce677938_b1e5_4320_80ec_d066bd87012c.mp3"
spreakerEpisodeId = "64335997"
duration = "1:01:35"
description = "Scopri Hazel, l'applicazione macOS per automatizzare l'archiviazione digitale dei file. Roberto e Filippo ti spiegano come controllare le cartelle e organizzare i documenti in modo intelligente."
draft = false

[params]
  hasTranscript = false
tags = ["hazel", "automazione", "macos", "archiviazione-digitale", "produttivita"]
+++

In questa puntata Roberto e Filippo ti parlano dell'applicazione per macOS Hazel. Hazel permette di controllare il contenuto di una cartella e automatizzare l'archiviazione digitale dei file in essa contenuti.

# Note episodio 
## [Sito Hazel](https://www.noodlesoft.com/)

Applicazione creata e sviluppata da una sola persona

### Costo

- 42 $ solo
- 65 $ family pack 5 persone
- Aggiornamento 20 $

### [Versione 5](https://www.noodlesoft.com/whats-new-in-hazel-5/)

- Interfaccia
- Possibilità di rilevare modelli all’interno di liste e tabelle
	- Ad esempio, puoi abbinare una colonna di una tabella e rinominare con i valori di un'altra. Gli elenchi e le tabelle possono essere creati in Hazel o caricati da un file esterno.
- Editor distaccatile dall’interfaccia principale
- Integrazione dei Comandi Rapidi
	- Tra le azioni di Hazel c’è anche Comandi Rapidi

### [Forum di Hazel](https://www.noodlesoft.com/forums/)

## Che cos’è?
Organizzazione automatizzata per il tuo Mac.
> Hazel sorveglia qualsiasi cartella tu gli dica, organizzando automaticamente i tuoi file in base alle regole che gli hai dato. Chiedi a Hazel di spostare i file in base a nome, data, tipo, da quale sito proviene e molto altro. Ordina automaticamente i tuoi film o archivia le tue bollette. Tieni i tuoi file fuori dal desktop e mettili dove appartengono.
>  Hazel può aprire, archiviare, taggare e persino caricare. Puoi fare in modo che Hazel rinomini i tuoi file o li ordini in sottocartelle in base al nome, alla data o a qualsiasi combinazione di attributi tu scelga. Accoppiato con la potente corrispondenza dei modelli di Hazel, puoi creare flussi di lavoro per elaborare i tuoi file, a modo tuo.

## Come funziona?

### Se …
- Le condizioni
 Fai questo ai documenti o cartelle che corrispondono al modello

## Cosa è possibile farci?
- Archiviazione digitale
- Rinomina file
- Rielaborare secondo modelli il nome di documenti
- Estrapolare dati da PDF ed altri documenti
- Spostamento
- Datazione documenti
- Gestione musica, foto e film
- 
## Utilizzo dei modelli di corrispondenza nelle condizioni
A volte potresti aver bisogno di una regola per verificare una condizione che corrisponda a un modello rispetto a uno che corrisponde semplicemente a un attributo fisso (ad esempio, "corrispondere a qualsiasi file con un numero a tre cifre nel suo nome", anziché "corrispondere qualsiasi file con il numero 372 nel suo nome"). Hazel offre un'ampia interfaccia di pattern-building per situazioni del genere.

### Corrispondenze token

- Singolo
	- Lettera
	- Numero
	- Simbolo
	- Carattere (tutti e 3) tranne  gli spazi
	- Numero o lettera
- Composito
	- Parola
	- Numeri
	- Simboli
	- Caratteri
- Qualsiasi cosa

I 4 attributi personalizzati sono ancora più potenti, in quanto ti consentono di creare **modelli denominati propri** che sono quindi disponibili per altre condizioni e azioni in questa regola:

- "Testo personalizzato (●)": questo token ti consente di creare il tuo attributo personalizzato basato sul testo. Vedere Attributi di testo personalizzati .  
- "Data personalizzata ( □ )": questo token ti consente di creare il tuo attributo di data personalizzato (cioè un particolare formato di data). Vedere Attributi Data personalizzati .
- "Articola dell'elenco personalizzato (—)": questo token ti consente di creare un elenco, in modo che la tua condizione possa corrispondere a uno qualsiasi degli elementi dell'elenco. Vedere Attributi elenco personalizzati .
-  "Tabella personalizzata ( ☷ )": questo token ti consente di creare una tabella, in modo tale che la tua condizione possa corrispondere a uno qualsiasi degli elementi in una particolare colonna, dopo di che puoi applicare azioni in base al contenuto di un'altra colonna nella stessa riga. Vedere Attributi di tabella personalizzati .

### Ulteriore vantaggio

- I modelli denominati propri possono essere utilizzati nella parte dell’azione
	- Ad esempio rinominare per un modello trovato

## Utilizzo di condizioni nidificate
E se hai bisogno di combinazioni più elaborate, come "Tutti (Qualsiasi (il tipo è PDF o il tipo è immagine)) e (Qualsiasi (Il nome contiene screenshot o i tag non contengono Ignora))"?

## Esempi

###  Webinar Filippo
-  [Una regola per dominare tutte le email](https://youtu.be/MPUWmqgYwsg)

### Risorse utili

**Articoli Filippo in italiano**

- [Usare Hazel per archiviare i bollettini MAV Cassa Forense](https://www.avvocati-e-mac.it/blog/2017/2/9/usare-hazel-per-archiviare-i-bollettini-mav-di-cassa-forense)
- [Automatizzare la creazione di una nuova pratica con Hazel](https://www.avvocati-e-mac.it/blog/2017/2/9/usare-hazel-per-archiviare-i-bollettini-mav-di-cassa-forense)
	- Poi utilizzato metodo più veloce (Automator come Servizio)
- [Datare, nominare e spostare un documento in automatico](https://www.avvocati-e-mac.it/blog/2016/11/3/hazel-datare-nominare-e-spostare-un-documento-in-automatico)
- [Esempi delle mie automazioni per archiviare](https://www.avvocati-e-mac.it/blog/2016/11/6/hazel-esempi-dei-miei-sistemi-di-archiviazione-automatizzati)

**Altre risorse**

-  [Hazel: organizza automaticamente i file del tuo Mac](https://www.levysoft.it/archivio/2022/11/05/hazel-organizza-automaticamente-i-file-del-tuo-mac/)
-  [Come usare Hazel per la catalogazione di documenti, fatture e bollette](https://www.saggiamente.com/2018/07/recensione-come-usare-hazel-per-la-catalogazione-di-documenti-fatture-e-bollette/)
-  [Hazel un tool per tenere organizzati i files del proprio Mac](https://www.theapplelounge.com/software/applicazioni/hazel-tool-tenere-organizzati-files-del-mac/)
- [Video guida David Sparks in inglese](https://learn.macsparky.com/p/hazel)
