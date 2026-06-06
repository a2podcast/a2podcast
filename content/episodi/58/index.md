+++
title = "58: Machine Learning con Alex Raccuglia"
date = "2023-05-01T05:00:00+01:00"
episodeNumber = 58
slug = "58"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336012/97415564_c34f_41ca_9b49_6ae37dc46b7d.mp3"
spreakerEpisodeId = "64336012"
duration = "1:20:34"
description = "In questa puntata Roberto e Filippo con l'ospite d'eccezione, Alex Raccuglia, – dopo aver parlato di IA con Lucio Bragagnolo – chiacchierano di Machine Learning in salsa Apple: delle sue possibilità attuali e delle speranze future dal punto di uno sviluppatore e dell'utente finale."
tags = ["intelligenza-artificiale", "apple"]
draft = false

[params]
 hasTranscript = true
 youtubeId = "KaLU8utCNns"
 guest = "alex-raccuglia"
+++

> In questa puntata Roberto e Filippo con l'ospite d'eccezione, Alex Raccuglia, – dopo aver parlato di IA con Lucio Bragagnolo – chiacchierano di Machine Learning in salsa Apple: delle sue possibilità attuali e delle speranze future dal punto di uno sviluppatore e dell'utente finale.

## Note dell’episodio
- [A2 episodio 57 con Lucio Bragagnolo](https://a2podcast.it/57/): puntata A2 n. 57 richiamata come precedente o approfondimento collegato.
- [Create ML](https://developer.apple.com/machine-learning/create-ml/): strumento Apple per addestrare modelli di machine learning dentro il flusso degli sviluppatori.
- [I modelli di Apple](https://developer.apple.com/machine-learning/models/#text): documentazione Apple per sviluppatori richiamata nella parte tecnica della conversazione.
- [Linguaggio naturale](https://developer.apple.com/documentation/naturallanguage): framework Apple per analisi linguistica, tokenizzazione e riconoscimento di entità.
- [Come lemmatizzare il testo usando NLTagger](https://www.hackingwithswift.com/example-code/naturallanguage/how-to-lemmatize-text-using-nltagger): approfondimento collegato a Come lemmatizzare il testo usando NLTagger, utile per seguire il passaggio della puntata su 58: machine learning con alex raccuglia.
- [Riconoscere nomi di entità in un testo](https://monkeylearn.com/blog/named-entity-recognition/): approfondimento collegato a Riconoscere nomi di entità in un testo, utile per seguire il passaggio della puntata su 58: machine learning con alex raccuglia.
- [Introduzione al Linguaggio Naturale in Swift](https://www.appcoda.com/natural-language-processing-swift/): approfondimento collegato a Introduzione al Linguaggio Naturale in Swift, utile per seguire il passaggio della puntata su 58: machine learning con alex raccuglia.
- [Le ricerche di Apple o che sponsorizza Apple](https://machinelearning.apple.com): approfondimento collegato a Le ricerche di Apple o che sponsorizza Apple, utile per seguire il passaggio della puntata su 58: machine learning con alex raccuglia.
- [Il nuovo chip M1 di Apple è una bestia di apprendimento automatico](https://towardsdatascience.com/apples-new-m1-chip-is-a-machine-learning-beast-70ca8bfa6203): approfondimento collegato a Il nuovo chip M1 di Apple è una bestia di apprendimento automatico, utile per seguire il passaggio della puntata su 58: machine learning con alex raccuglia.
- [Ecco perché Apple crede di essere un leader dell'IA e perché dice che i critici hanno tutto sbagliato](https://arstechnica.com/gadgets/2020/08/apple-explains-how-it-uses-machine-learning-across-ios-and-soon-macos/): approfondimento collegato a Ecco perché Apple crede di essere un leader dell'IA e perché dice che i critici hanno tutto sbagliato, utile per seguire il passaggio della puntata su 58: machine learning con alex raccuglia.
- [ChatGPT](https://chat.openai.com/): assistente conversazionale usato come riferimento pratico per discutere IA generativa e interfacce in linguaggio naturale.
- [OpenAI](https://openai.com/): azienda citata nel contesto di ChatGPT, GPT-4 e modelli generativi.

## Sinossi[^sinossi-ai]

### 1. A2 episodio 57 con Lucio Bragagnolo

> "machine learning all'interno del mondo dell'informatica, ma non solo questo, lo stiamo."
> — Filippo, Roberto e Alex Raccuglia, 00:01:54
In questa parte Filippo e Roberto seguono il tema “A2 episodio 57 con Lucio Bragagnolo” dentro il quadro
dell’episodio su Machine Learning con [Alex Raccuglia](https://a2podcast.it/ospiti/alex-raccuglia/). I passaggi centrali riguardano tutti, alex, artificiale,
cose. Che ribadisco, e ribadiamo tutti quanti assieme perché siamo molto allineati anche su questo punto di
vista, non si tratta di un'intelligenza artificiale. Io personalmente, dal mio punto di vista di tecnico
architetto, ho pensato a rinominare questa intelligenza artificiale perché non se ne può più chiamarla
intelligenza artificiale. Introduciamo il nostro mitico Alex Raccuglia. E soprattutto, come dicevo, volevo
ringraziare in particolar modo Nicola e il nostro mitico Magnetar Tech che ha cambiato il nome a NASO, in ogni
caso lo conosciamo bene o male tutti quanti. E arrivo, diciamo, in ufficio, riesco a ritagliarmi a questo
punto qualche decina di minuti di qua e là per poter sviluppare cose. Cosa ci vuoi raccontare, caro il nostro
Alex del Machine Learning?

### 2. Cos’è ML?

In questa parte Filippo e Roberto seguono il tema “Cos’è ML?” dentro il quadro dell’episodio su Machine
Learning con Alex Raccuglia. I passaggi centrali riguardano cose, machine, learning, apple. Ma dietro dietro,
effettivamente ci sono degli strumenti sviluppati, ormai anche da tempo, perché Apple non è stata qui a
guardare , Apple ha approcciato l'idea del machine learning e della gestione, diciamo, delle varie branche sia
da una parte creando hardware apposta. Apple dice: il 25% dei transistor che sono in questo processore sono
dedicati esclusivamente al machine learning. Quindi ormai tutti i dispositivi Apple moderni, chiamiamoli così,
hanno comunque una parte di processori che è dedicata esclusivamente a quello. Questo significa due cose: che
traducono tutti i vari modelli in modo tale che possono essere macinati attraverso le loro tecnologie, per cui
attraverso i loro processori. Quando c'è il machine learning, la cacca è sempre lì, vuol dire che prima o poi,
in qualche modo salta fuori, va a passatemi il termine, sputtanare, la confidenza che puoi dare nel risultato
di una risposta. Perché ovviamente tu tratti della materia perché la conosci, poi non l'abbiamo detto, ma
adesso ti stai occupando, e dopo lo approfondiremo meglio, anche di sviluppare varie applicazioni che si
basano su machine learning e su tecnologie simili.

### 3. Cosa offre Apple con coreML ?

> "E di conseguenza, quando c'erano gli effetti sonori finali, tipo la musica."
> — Filippo, Roberto e Alex Raccuglia, 00:25:45
In questa parte Filippo e Roberto seguono il tema “Cosa offre Apple con coreML ?” dentro il quadro
dell’episodio su Machine Learning con Alex Raccuglia. I passaggi centrali riguardano modello, apple, cose,
device. Con CoreML e Create ML, che sono, diciamo, le due librerie che ha sviluppato Apple per gli
sviluppatori, diciamo che c'è la possibilità di creare micro modelli che a questo punto sono molto meno
pesanti. Altro esempio: Whisper, che è il modello open source di OpenAI per la trascrizione del testo, su cui
si sta lavorando tantissimo, che è, secondo me, una delle cose più avanzate che ci sia in giro. Però, per il
resto, sì, il fatto di avere tutto un device è comodo e bisogna essere sinceri, Apple, quando fa le cose per i
propri device, per i propri sistemi, le ottimizza molto molto molto bene. Vuol dire che se c'è questa roba,
c'è in un modello da 3 GB open source, non so pensare cosa ci sia dentro le cose che noi non possiamo vedere.
Un modello, diciamo, che io posso andare a raffinare con le mie cose specifiche della mia attività, per
esempio. Questo dal punto di vista di quello che mettono a disposizione dell'utente.

### 4. Create ML

In questa parte Filippo e Roberto seguono il tema “Create ML” dentro il quadro dell’episodio su Machine
Learning con Alex Raccuglia. I passaggi centrali riguardano testo, cose, senso, allora. Io ho lavorato
tantissimo con le API di Apple per la trascrizione del testo, che sono state le prime a nascere. Ti ho anche
chiesto qualcosa proprio perché ho qualche test basilare, l'ho fatto, ma ovviamente allo stato attuale non ho
le capacità per fare cose clamorose, committamole in questi termini. Solo che da allora, nel senso che Siri è
rimasto molto seduto su se stesso. Però, tra le varie cose, Toolbox Pro è un'applicazione sostanzialmente che
dà azioni a comandi rapidi, è per questo che ovviamente ci ho giocato e ho approfondito la vicenda. Per cui,
alla fine, queste due classi di applicazione utilizzano tre servizi: Whisper per la trascrizione del testo,
Deep per la traduzione, Microsoft Azure per lo speaker. Per cui la trascrizione non era utilizzabile, però
diciamo che poteva andare a servire per generare delle keyword, vedere quali erano i nomi più ripetuti, le
cose più ripetute.

### 5. I modelli su cui è possibile creare / personalizzare

> "allo spickeraggio, comunque consentono sempre e in maniera molto forte all'utente di."
> — Filippo, Roberto e Alex Raccuglia, 00:39:43
In questa parte Filippo e Roberto seguono il tema “I modelli su cui è possibile creare / personalizzare”
dentro il quadro dell’episodio su Machine Learning con Alex Raccuglia. I passaggi centrali riguardano modo,
cose, immagini, chat. Nel senso, chiedi a chat GPT di iscriverti una routine di Swift che non sia una cosa
molto semplice, ti tira fuori delle cose assolutamente astruse, che sono delle cose quasi inutilizzabili per
dirti. Mi hanno dato i dati e allora, visto che i copy non tardava a mandarmelo, l'ho scritto io in questo
modo qui. Guarda che belle immagini che sono state create, però, non ti fanno vedere le mille volte tante
immagini che sono delle cose inutilizzabili, completamente scrause. E io mi auguro sono abbastanza sicuro, ma
mi auguro che lei questi testi che vengano generati in qualche modo, poi comunque li supervisioni in qualche
modo. Stiamo parlando di cose che sì, nella testa di chi fa marketing, sono adesso non c'è più bisogno di
programmatori. Se i modelli non sono sicuri o comunque se non sono stati controllati perfettamente, è ovvio
che c'è un problema.

### 6. Linguaggio naturale

In questa parte Filippo e Roberto seguono il tema “Linguaggio naturale” dentro il quadro dell’episodio su
Machine Learning con Alex Raccuglia. I passaggi centrali riguardano parte, apple, foto, tutti. D'altra parte,
ritornando invece, per quanto riguarda Apple, volevo chiedere appunto ad Alex una cosa che proprio oggi mi è
capitato mentre stavo sfogliando le fotografie tramite l'applicazione foto di iPhone. Ma d'altra parte è
altrettanto vero che il punto di vista critico non tutti ce l'hanno ed è anche difficile riuscire ad avere un
punto di vista critico su qualcosa che stai chiedendo e molto probabilmente non ne hai la conoscenza perfetta.
Al di là della questione è che anche il garante da parte sua, non dico che si è messo contro, ma ha sollevato
un problema non di poco conto, che è quello appunto di riuscire a rettificare in modo puntuale le informazioni
che vengono fornite. Tant'è che avevo letto da qualche parte che c'era forse una persona che aveva diciamo
interrogato Chat GPT riguardo proprio a se stesso e aveva ottenuto delle nozioni fuorvianti che non
c'entravano niente con la sua vita e ha intentato causa appunto a Chat GPT. È difficile riuscire a capire
perché viene fornito un tipo di risposta, ma soprattutto dalla parte, diciamo del back-end, chiamiamolo in
questo modo, non si riesce poi a correggere in modo puntuale. Perché ci stiamo tutti che un'informazione da
parte di questi programmi, di questi acceleratori ti diano delle informazioni magari sbagliate, non corrette,
non perfette.

### 7. Cos’è?

In questa parte Filippo e Roberto seguono il tema “Cos’è?” dentro il quadro dell’episodio su Machine Learning
con Alex Raccuglia. I passaggi centrali riguardano punto, artificiale, vista, tipo. Ma la cosa interessante
che stavo ragionando appunto in questo periodo è che sotto un certo punto di vista Apple in questo senso si
sta portando avanti con un vantaggio competitivo perché all'interno dei suoi SOC c'è appunto una parte
dedicata a questo tipo di elaborazioni. Che in effetti l'idea di Apple di mettere all'interno dei SOC un
coprocessore dedicato a questo tipo di lavorazioni che permette appunto di mantenere le temperature basse.
Quindi passare dalla bidimensione alla tridimensione in modo abbastanza semplice, ovviamente ci vorrà, come
sempre, il controllo umano perché c'è poco da fare dal punto di vista delle capacità e delle qualità. Siamo
arrivati al punto che un'intelligenza artificiale, un acceleratore, riesce a riconoscere, dandogli in pasto
una fotografia, riesce a ricreare la mesh tridimensionale. Quindi penso che dobbiamo già iniziare a pensare un
po' in modo esteso e in modo molto più civile questo nuovo evento che è l'intelligenza artificiale, la nascita
della base dell'intelligenza artificiale. Però, giustamente, se un'azienda ha investito dei soldi per fare
questo tipo di classificazione, il suo modello, il suo dataset, è anche giusto che voglia ritornare in qualche
modo.

### 8. Che attività può svolgere?

In questa parte Filippo e Roberto seguono il tema “Che attività può svolgere?” dentro il quadro dell’episodio
su Machine Learning con Alex Raccuglia. I passaggi centrali riguardano cose, alex, tutti, dice. Lo dico tutti
gli anni, ma questo giro, visto che sono interessato a varie cose, potrei anche cercare di fare con te la
notte, anche se la mia età anziana, non so quanto reggo. Come si dice, oltre alle cose interessanti, che con
Alex, le cose potrebbero andare avanti altre un paio d'ore, tre, e ci sarebbe ancora da divertirci. Se invece
il dirigente dell'ospedale ti dice tu hai questa malattia e nessuno ha controllato, ma magari le cose
diventano un pochettino più complicate. Quindi vado a chiudere dicendo a Alex se vuoi salutare i nostri
ascoltatori, hai carta di più. Ma diciamo che dopo aver ringraziato Alex per averci intrattenuto con le sue
cose interessantissime. Ho appena chiesto, mi ha detto: non è una persona abbastanza famosa da sapere qualcosa
per cui non dico niente.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
