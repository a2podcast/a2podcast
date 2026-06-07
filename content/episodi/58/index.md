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
- [A2 episodio 57 con Lucio Bragagnolo](https://a2podcast.it/57/): puntata precedente sull'intelligenza artificiale, richiamata come contesto.
- [Create ML](https://developer.apple.com/machine-learning/create-ml/): strumento Apple per creare e addestrare modelli.
- [I modelli di Apple](https://developer.apple.com/machine-learning/models/#text): raccolta di modelli e risorse Apple per sviluppatori.
- [Natural Language](https://developer.apple.com/documentation/naturallanguage): framework Apple per analisi del linguaggio naturale.
- [Come lemmatizzare il testo usando NLTagger](https://www.hackingwithswift.com/example-code/naturallanguage/how-to-lemmatize-text-using-nltagger): esempio Swift collegato all'analisi linguistica.
- [Riconoscere nomi di entità in un testo](https://monkeylearn.com/blog/named-entity-recognition/): approfondimento sul named entity recognition.
- [Introduzione al Linguaggio Naturale in Swift](https://www.appcoda.com/natural-language-processing-swift/): guida introduttiva a Natural Language.
- [Le ricerche Apple sul machine learning](https://machinelearning.apple.com): pagina Apple sulle ricerche sponsorizzate o pubblicate.
- [Il chip M1 di Apple e il machine learning](https://towardsdatascience.com/apples-new-m1-chip-is-a-machine-learning-beast-70ca8bfa6203): articolo citato per il ruolo di Apple Silicon.
- [Come Apple usa il machine learning](https://arstechnica.com/gadgets/2020/08/apple-explains-how-it-uses-machine-learning-across-ios-and-soon-macos/): approfondimento sul machine learning integrato nei sistemi Apple.
- [ChatGPT](https://chat.openai.com/): richiamato nel confronto tra IA generativa e machine learning applicativo.
- [OpenAI](https://openai.com/): azienda citata per modelli generativi e Whisper.

## Sinossi[^sinossi-ai]

### 1. Da intelligenza artificiale a machine learning

Dopo la puntata con Lucio, Filippo e Roberto invitano [Alex Raccuglia](https://a2podcast.it/ospiti/alex-raccuglia/) per scendere dal dibattito generale sull'IA al machine learning usato dagli sviluppatori. Alex chiarisce subito il perimetro: non parla da teorico dell'intelligenza artificiale, ma da sviluppatore che usa strumenti concreti.

> "Il machine learning è un insieme di metodi"

La distinzione è utile: il machine learning non è magia, ma una famiglia di tecniche che permette a un sistema di riconoscere pattern dopo aver visto esempi. L'immagine ricorrente è semplice: se si mostrano moltissime foto di una scimmia, il sistema impara a riconoscere caratteristiche ricorrenti e a classificarne una nuova.

### 2. L'approccio Apple: on-device e invisibile

Alex e i conduttori spiegano che Apple usa machine learning da anni, spesso senza chiamarlo così nel marketing. Live Text, riconoscimento delle foto, sfocatura, suggerimenti e funzioni di sistema lavorano con modelli ottimizzati per girare sui dispositivi.

> "Apple fa questa cosa interessante"

Il punto chiave è l'esecuzione locale. Apple Silicon e Neural Engine permettono di usare modelli con consumi più bassi e maggiore privacy rispetto a servizi che mandano tutto a server remoti. Questo approccio è coerente con l'ecosistema Apple, ma crea anche limiti: non tutti i modelli disponibili sul mercato sono pronti, documentati o abbastanza buoni per gli sviluppatori.

### 3. Core ML, Create ML e transfer learning

La parte tecnica entra in Core ML e Create ML. Apple mette a disposizione modelli già istruiti e strumenti per rifinirli con dati propri. Alex spiega il concetto di transfer learning: partire da un modello generale e addestrarlo ulteriormente per un compito specifico, senza dover costruire tutto da zero.

> "viene chiamato da Apple Transfer Learning"

Questo è importante per sviluppatori indipendenti: creare un dataset enorme è costoso, ma rifinire un modello esistente può rendere possibile un'app utile. La difficoltà resta nella qualità dei dati: pochi esempi buoni possono essere più utili di molti esempi confusi, ma costruire e validare il dataset è spesso la parte più faticosa.

### 4. Linguaggio naturale, testo e API

Alex racconta esperienze con Natural Language, trascrizione, tag, entità e analisi del testo. Il linguaggio naturale è un campo in cui le API Apple possono aiutare, ma non sempre reggono il confronto con modelli più recenti o servizi esterni. La puntata cita anche Whisper, DeepL, Microsoft Azure e ChatGPT come strumenti che, messi insieme, possono creare flussi di lavoro molto potenti.

La filosofia di Alex non è "premi un bottone e lascia fare tutto". Le sue applicazioni cercano di dare controllo all'utente: suggerire, trasformare, assistere, ma mantenere una revisione critica umana. Questo torna più volte come criterio di progettazione.

### 5. Foto, classificazione e futuro su Apple Silicon

Roberto porta un esempio quotidiano: Foto su iPhone riconosce piante, animali e oggetti. Alex lo collega ai modelli di classificazione e alla soglia di confidenza: un sistema può dire che una foto contiene un albero con una certa probabilità, ma Apple sceglie quando mostrare l'informazione all'utente per non creare risultati troppo incerti.

> "dataset fatti bene per il machine learning"

La chiusura guarda al futuro: Apple ha investito nei propri SoC e in acceleratori dedicati proprio perché modelli locali, foto, testo, trascrizione e perfino ricostruzioni 3D richiedono molta energia. Il vantaggio competitivo sta nel far girare questi strumenti vicino all'utente, con hardware e software progettati insieme.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
