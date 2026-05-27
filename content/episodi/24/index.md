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
  hasTranscript = false
  youtubeId = "ObNc3_33C4U"
+++

> Per la tua gioia di Filippo facciamo un ulteriore approfondimento su Comandi Rapidi. Ne abbiamo già parlato nella precedente puntata 22 che, se non avete ascoltato, vi consigliamo di recuperare prima di ascoltare questa. Infatti daremo per scontato l’introduzione già fatta in quella puntata. In questa puntata creeremo il nostro primo Comando Rapido

## Come potete sostenerci

Se volete **supportare il podcast** vi chiediamo con il cuore di fare una **recensione su Apple Podcast.** In questo fase iniziale tante recensioni ci permetteranno di essere visti da più persone possibili.

Se volete sapere come fare una recensione trovate il [link nelle note dell’episodio](https://www.avvocati-e-mac.it/podcast/itunes).

Potete anche scriverci a scrivi.a🐌a2podcast.it

## 0. Comunicazioni di servizio

1. Non ne parleremo, allo stato, in queste puntate. Il perché è presto detto, lo stesso [David Sparks che sta creando sul tema una video guida ritiene che Comandi Rapidi per Mac sia ancora una beta](https://www.macsparky.com/blog/2021/12/shortcuts-in-limbo), ovvero un software ancora sperimentale. Se avete quindi macOS Monterey e volete sperimentare Comandi Rapidi armatevi di sana pazienza e, soprattutto, non scoraggiatevi su un vostro comando rapido non funzionasse correttamente.

[Craft](https://www.craft.do) ha vinto [il premio come una delle migliori app del 2021 da Apple](https://www.apple.com/it/newsroom/2021/12/app-store-awards-honor-the-best-apps-and-games-of-2021/). Abbiamo discusso di questa app nella [puntata 22](http://www.a2podcast.it/22) in cui ne parliamo con Daniele Borghi.

1. [Craft X](https://www.craft.do/s/OhmDYXrBwI2wZS):

   > “Non abbiamo mai creduto in "uno strumento per governarli tutti". Pensiamo che dovresti attenerti agli strumenti che funzionano per te, ma essere in grado di integrare tutti i tuoi pensieri - sia che prendano la forma di testo, immagini, codice, equazioni matematiche, eventi del calendario e così via - nel tuo flusso di lavoro. Craft X permette di collegare Craft con gli strumenti di cui hai bisogno nel tuo flusso di lavoro. Craft X significa estendere le capacità di Craft alle tue esigenze. Niente di più, niente di meno.”

   Stiamo ragionando di fare puntata su [KMS (knowledge management Sofware)](https://en.wikipedia.org/wiki/Knowledge_management_software) tipo Obsidian, DEVONthink, Notion e Roam. Diteci se vi può interessare e se li usate scriveteci una email o contattateci su Twitter o Telegram.

## 1. Dove eravamo rimasti

* Visto come provare Comandi Rapidi attraverso la galleria
* Esaminato l’interfaccia base di Comandi Rapidi
* Oggi ci addentreremo su come creare un Comando Rapido personalizzato
* Parleremo dell’interfaccia per iOS ed iPadOS 15

## 2. Interfaccia di base di Comandi Rapidi

* Immagini nelle note dell’episodio
* Il funzionamento di base
  * Scegli una foto
  * Con uno testo pre-impostato
  * Invia un messaggio al contatto pre-selezionato
  * Questa automazione, che credevo semplice, non lo è così tanto …
    * Comunque la vedremo e vi spiegherò come aggirare alcune limitazioni di Comandi Rapidi
* iPhone: unica finestra, nella parte alta potete inserire le azioni, nella parte centrale vedete i suggerimenti e nella parte bassa potete cercare le azioni e trascinarle nella parte centrale per inserirle nel vostro Comando Rapido. Abitualmente se avete un iPad è più comodo creare i comandi rapidi su iPad e farli sincronizzare con l’iPhone. MA comunque sempre possibile lavorare con iPhone anche se in modo meno comodo.

![](https://images.squarespace-cdn.com/content/v1/55b2626fe4b0bfab95304b93/a7afd96d-4d95-40f3-bd6f-fcc85d7ddfc0/iPhone+interfaccia+editor+Comandi+rapidi.jpeg?format=500w)

* iPad
  * Colonna sinistra: in alto le impostazioni per nominare il comando, tasti annulla e rifai, tasto Condivisione e tasto Play per eseguire il comando rapido; sotto l’editor vero e proprio dei comandi rapidi
  * Colonna destra
    * Azioni da inserire nell’editor e nel flusso di lavoro
    * Opzioni di Comandi Rapidi (vedi immagine)

![](https://images.squarespace-cdn.com/content/v1/55b2626fe4b0bfab95304b93/6abc75c9-bd6c-4064-9451-01c10da88ad4/iPad+interfaccia+editor+Comandi+Rapidi.jpeg?format=750w)

![](https://images.squarespace-cdn.com/content/v1/55b2626fe4b0bfab95304b93/b33ddd1d-947f-4570-9103-5581407cbd95/Pannello+opzioni.jpeg?format=750w)

## 3. Uno sguardo complessivo alle azioni presenti

* Aggiungi azione
  * aggiunta un’azione possibile vedere cosa fa premendo sull’icona I che sta per informazioni
    * Descrizione azione
    * Input : Cosa accetta l’azione
    * Output : Cosa restituisce l’azione
* Cerca app e azioni
  * Categorie
    * Tutte le azioni
    * Preferite
    * Scripting
    * Condivisione
    * Posizione
    * Documenti
    * Media
    * Web
  * App
    * Oltre a quelle di sistema di Apple
    * Terze parti
      * MA devono essere implementate dallo sviluppatore
      * NECESSARIO che applicazione sia installata sul dispositivo

## 4. Il nostro primo Comando rapido

* Seleziona foto
* Testo
* Invia Messaggio
  * Seleziona il contatto
* Duplica l'azione
  * Pressione prolungata sull’icona dell’azione e da menù a tendina scegliete Duplica (icona con 2 quadrati uno sopra l’altro e con un segno + sul quadrato più vicino a voi)
* Cliccate sulla variabile testo
  * Compare menù, premete su *Create Variabile* (pulisci variabile ancora non tradotto)
* Cliccate / fate tap su In Invia “ Messaggio grigio “, nella parte bassa dello schermo comparirà la voce “seleziona variabile”
  * Scegliete foto
  * Se selezionate la voce “Seleziona variabile”
    * L’editor cambierà e potrete usare le variabili magiche
      * NE parliamo dopo

## 5. Le variabili magiche

* Sono un’invenzione di Workflow e permette di lavorare con le variabili in Comandi rapidi in modo semplificato
* Invece di dover dichiarare le variabili e richiamarle è possibile usare le variabile magiche

Premendo sul tasto variabile magica si entra in una modalità a se stante dell’editor in cui vengono mostrate tutte le variabili che vengono usate dalle varie azioni. A questo punto è possibile selezionare la variabile (ed il suo contenuto) che si preferisce.

La particolarità (relativamente avanzata) di questo sistema è che le variabili di Comandi Rapidi non hanno un solo dato (come capita abitualmente in un linguaggio di programmazione ad esempio: solo testo, solo un numero, solo vero o falso, solo dei dati) ma cattura un insieme di informazioni a cui l’utente ha completo accesso. Da esempio se passo una foto come *variabile magica* posso oltre all’immagine vera e propria ad esempio scegliere il suo nome, o la risoluzione o il suo peso in Kb o i dati exif ovvero con che dispositivo è stata scattata il giorno e l’ora dello scatto. Spesso tutte queste informazioni non vi potrebbero interessare ma è utile sapere che esistono e che sono a vostra disposizione.

Sempre facendo l’esempio della foto, con questo sistema è possibile prendere il nome della foto, anteporre casomai una data o un dato identificativo (vacanza in montaglia ad esempio) e salvarla in una specifica cartella.

## 6. Comandi Rapidi intelligenti

Oltre che creare dei flussi di azioni lineari è possibile creare dei comandi “intelligenti” ovvero che permetto di modificare la sequenza di azioni in base a determinate condizioni o parametri ed in generale permettono all’utente di scegliere un certo tipo di risultato.

* L’azione SE: permette di inserire una logica di scelta “automatica” ad esempio se è vero fai una cosa se è falso un’altra, oppure se è maggiore di 5 scegli un percorso se è minore un altro e così via.
  * Esempio [Numerazione documenti per PCT](https://www.icloud.com/shortcuts/b91888e61d62480db15b5ec781e7dda9)
* L’azione Elenco: permette di scegliere (uno o più risultati) da un elenco che può essere creato da una precedente azione.
* L’azione scegli dal menu: permette di scegliere tra differenti opzioni
  * Esempio [Comando Rapido di Normattiva](https://www.icloud.com/shortcuts/4f80efc6ec4242049b9b7afd1e16d2f8)
  * I launcher, ovvero dei Comandi rapidi che permettono di lanciare una specifica applicazione o un altro comando
    * Ricordarsi che un Comando Rapido può far partire un altro comando rapido
* Le azioni ripeti i c.d. loop: permettono di svolgere un particolare compito o azione N volte, Filippo ha usato un loop per rinominare e numerare i documenti nel suo Comando Rapido per il PCT.

## Articoli di Filippo

Alcuni articoli parlano di *Workflow*, quest’applicazione è stata comprata da Apple ed è diventata *Comandi Rapidi*. Alcuni articoli sono risalente e non tutto potrebbe funzionare come mostrato a causa del passaggio del tempo ma i concetti espressi sono ancora validi.

* [Creare un’email pre-compilata con selezione di documenti a scelta dell’utente](https://www.avvocati-e-mac.it/blog/2018/10/25/creare-unemail-pre-compilata-con-selezione-di-documenti-a-scelta-dellutente)
* [Salvare i file .EML in iOS 11 con Mail ed Drag & Drop e come automatizzare con Workflow](https://www.avvocati-e-mac.it/blog/2017/11/12/salvare-file-eml-in-ios-11)
* Magic Variabile / Variabili Magiche
  * [Automatizzare progetti in OmniFocus - parte prima](https://www.avvocati-e-mac.it/blog/2018/3/4/automatizzare-progetti-in-omnifocus-parte-prima)
  * [Automatizzare i progetti in OmniFocus - parte seconda](https://www.avvocati-e-mac.it/blog/2018/3/12/automatizzare-i-progetti-in-omnifocus-2-parte-seconda)
* [Usare Workflow e Copied per velocizzare la creazione di una notifiche in proprio](https://www.avvocati-e-mac.it/blog/2016/11/17/usare-workflow-e-copied-per-velocizzare-la-creazione-di-una-notifiche-in-proprio)
* [Usare Workflow per salvare, come PDF, estratti di una pagina web](https://www.avvocati-e-mac.it/blog/2017/2/2/usare-workflow-per-salvare-estratti-di-una-pagina-web-in-pdf)
* [Scrivere atti telematici avanzati su iOS (con un piccolo trucco)](https://www.avvocati-e-mac.it/blog/2018/11/15/scrivere-atti-telematici-avanzati-su-ios-con-un-piccolo-trucco)
* [Esempio di semplice automazione su iPad per modelli di atti telematici in testo semplice](https://www.avvocati-e-mac.it/blog/2021/6/20/esempio-di-semplice-automazione-su-ipad-per-modelli-di-atti-telematici-in-testo-semplice)
