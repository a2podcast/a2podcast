+++
title = "59: Velocizzare la scrittura con le espansioni del testo"
date = "2023-05-15T05:00:00+01:00"
episodeNumber = 59
slug = "59"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64335977/68214cb9_7f43_4b47_9bc2_530adf7baf53.mp3"
spreakerEpisodeId = "64335977"
duration = "1:04:41"
description = "In questa puntata Roberto e Filippo esaminano le c.d. sostituzioni del testo. Digitare una serie di lettere e, a queste, si sostituisce un testo differente, abitualmente più lungo. Esaminato come funziona il principio di base ed alcuni trucchi utili da conoscere, il magico duo esaminerà i software p"
tags = ["espansioni testo", "produttivita", "mac", "iphone", "automazione"]
draft = false

[params]
  hasTranscript = false
  youtubeId = "Fj1R_KxMlxU"
+++

> In questa puntata Roberto e Filippo esaminano le c.d. sostituzioni del testo. Digitare una serie di lettere e, a queste, si sostituisce un testo differente, abitualmente più lungo. Esaminato come funziona il principio di base ed alcuni trucchi utili da conoscere, il magico duo esaminerà i software per implementare le sostituzioni sul tuo Mac, iPhone e iPad.

## Comunicazioni di servizio
Iniziamo registrazioni molto prima della loro pubblicazione
- Alcune informazioni potrebbero non essere super aggiornate

### [Keynote](https://developer.apple.com/wwdc23/) con Alex Raccuglia, Davide Gatti e Daniele Borghi

- 5/6 verso le 18:30

### Messaggi di Apple

- Messaggi in evidenza in una conversazione
	- Come ritrovarli

## Prima parte

### Cosa si intende per text expansion o Sostituzione del testo?

- Digitare una serie di lettere e, a queste, si sostituisce un testo differente, abitualmente più lungo
- Immaginate di digitare il vostro nome e cognome, o peggio ancora il vostro codice fiscale o la vostra partita IVA
	- È un lavoro tedioso
	- Prono ad errori
	- Richiede memoria
- Filippo
	- XFS diventa “Filippo Strozzi”
	- XCF diventa “STRFPP…”
	- XCS diventa “Un caro saluto Filippo”
Avete capito l'idea …

### Quali sono gli utilizzi

- Scrivere testo lungo velocemente
- Evitare errori
	- Anche come auto-correzione
- Date
	- Oggi
	- Domani
	- ieri
	- Data con anche giorno
	- Etc …
- Modelli
	- Testo base con campi da compilare e personalizzare
- Lanciare script o automazioni

### Possibilità di sincronizzare gli “snippet” o frammento di testo

### Quale scelta utilizzare per le sostituzioni

- Originariamente per il mondo anglofono
	- ;testo ovvero puntoevirgola e la combinazione di caratteri della sostituzione
	- Utile per gli anglofoni perché nelle loro tastiere il puntoevirgola è una tasto apposto …per noi invece è shift-virgola … non comodo
		- Inoltro non comodo nelle tastiere mobile
- Merlin Mann
	- Usa anteporre la lettera X all’abreviazione
	- Comoda anche per gli italiani

## Seconda parte

### Le soluzioni Software: sguardo d'insieme

- Apple base
	- [Sostituzione testo](https://support.apple.com/it-it/guide/iphone/iph6d01d862/ios)
	- Sincronizzazione tra differenti dispositivi Mac / iPhone / iPad
		- MA non sempre funziona
	- Limitazioni
		- Non è possibile andare a capo
		- Creare modelli complessi
- [TextExpander](https://textexpander.com/)
	- In abbonamento / sottoscrizione
	- Multipiattaforma
		- Windows Mac ed iOS
	- Sincronizzazione online
		- Un grosso limite per Filippo
		- MA utile se si lavora in gruppo
	- Filippo usa ancora la versione 5
		- Finché regge!
		- Passaggio ad Espanso per il prossimo futuro
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/)
	- Non la sua prima funzione
	- [Puntata N. 52](http://a2podcast.it/52)
		- Fatto approfondimento
	- Conversione snippet da TextExpander a Keyboard Maestro
		- [Dr. Drang](https://leancrew.com/all-this/2021/07/from-textexpander-to-keyboard-maestro-again/)
		- [Script in Python](https://github.com/rjames86/textexpander_to_keyboardmaestro)
		- Non testati nessuno dei 2
- [Espanso](https://espanso.org)
	- Multipiattaforma
		- macOS, Windows e Linux
		- No iOS / iPadOS
	- Sviluppatore italiano
		- Federico Terzi
	- Open-source
	- Particolarità
		- Non ha un’interfaccia grafica di configurazione
		- Utilizza un file di configurazione YAML
		- Dedicato ad utenti un pelo più esperti
	- Se ci sarà interesse
		- Possibile puntata dedicata
	- [Allo stato non c’è un sistema rapido di convertire le espansioni di testo da TextExpander ad Espanso](https://github.com/espanso/espanso/discussions/1232)
- [Typinator](https://www.ergonis.com/typinator)
	- € 36,59
	- Mai usato Filippo

## Link

- [Typinator aggionata](https://www.macitynet.it/typinator-aggiornata-lapplicazione-mac-che-scrive-al-posto-vostro-2/)
- [Espanso problemi con alcune app](https://neilzone.co.uk/2023/04/fixing-espanso-incomplete-text-replacement)
