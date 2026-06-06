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
 hasTranscript = true
 youtubeId = "Fj1R_KxMlxU"
+++

> In questa puntata Roberto e Filippo esaminano le c.d. sostituzioni del testo. Digitare una serie di lettere e, a queste, si sostituisce un testo differente, abitualmente più lungo. Esaminato come funziona il principio di base ed alcuni trucchi utili da conoscere, il magico duo esaminerà i software per implementare le sostituzioni sul tuo Mac, iPhone e iPad.

## Note dell’episodio
- [Keynote](https://developer.apple.com/wwdc23/): documentazione Apple per sviluppatori richiamata nella parte tecnica della conversazione.
- [Sostituzione testo](https://support.apple.com/it-it/guide/iphone/iph6d01d862/ios): documentazione Apple usata per verificare passaggi operativi o funzioni di sistema citate.
- [TextExpander](https://textexpander.com/): app specializzata per espansioni di testo, snippet condivisi e automazioni di scrittura.
- [Keyboard Maestro](https://www.keyboardmaestro.com/main/): strumento di automazione per Mac usato anche per macro ed espansioni di testo.
- [A2 episodio 52](https://a2podcast.it/52/): puntata A2 n. 52 richiamata come precedente o approfondimento collegato.
- [Dr. Drang](https://leancrew.com/all-this/2021/07/from-textexpander-to-keyboard-maestro-again/): approfondimento collegato a Dr. Drang, utile per seguire il passaggio della puntata su 59: velocizzare la scrittura con le espansioni del testo.
- [Script in Python](https://github.com/rjames86/textexpander_to_keyboardmaestro): repository GitHub collegato a codice, script o progetto tecnico menzionato.
- [Espanso](https://espanso.org): text expander open source e multipiattaforma discusso tra le alternative specialistiche.
- [Allo stato non c’è un sistema rapido di convertire le espansioni di testo da TextExpander ad Espanso](https://github.com/espanso/espanso/discussions/1232): app specializzata per espansioni di testo, snippet condivisi e automazioni di scrittura.
- [Typinator](https://www.ergonis.com/typinator): app per macOS dedicata a espansioni di testo, correzioni e automazioni nella scrittura.
- [Typinator aggionata](https://www.macitynet.it/typinator-aggiornata-lapplicazione-mac-che-scrive-al-posto-vostro-2/): app per macOS dedicata a espansioni di testo, correzioni e automazioni nella scrittura.
- [Espanso problemi con alcune app](https://neilzone.co.uk/2023/04/fixing-espanso-incomplete-text-replacement): text expander open source e multipiattaforma discusso tra le alternative specialistiche.

## Sinossi[^sinossi-ai]

### 1. Messaggi di Apple

> "Benvenuti all'episodio cinquantove di A2, in cui scoprire come ottenere il massimo."
> — Filippo e Roberto, 00:00:00
In questa parte Filippo e Roberto seguono il tema “Messaggi di Apple” dentro il quadro dell’episodio su
Velocizzare la scrittura con le espansioni del testo. I passaggi centrali riguardano evidenza, apple, esempio,
adesso. Si possono mettere allora adesso, per esempio, mi hai mandato Podmaker e te l'ho messo in evidenza.
Text expansion in inglese, espansione del testo sarebbe la traduzione più letterale in lingua italiana, ma per
esempio Apple la denomina. Stiamo sperimentando alcune cose, tra cui, ad esempio, delle cose che mi ha fatto
notare Filippo con messaggi che ci è venuto incontro, soprattutto perché io sono, sapete, sono smemorato. Se
si va nell'angolo a destra nell'interfaccia MAC sul pulsante I, diciamo esatto, e si scende da varie cose ci
sono appunto in evidenza e si trovano i vari file o i link messi in evidenza. Per adesso mi sta dando solo
buone idee, buoni propositi, come per esempio quello che intanto odiato, mettiamola così, da molti, tra cui il
sottoscritto, quando è saldato fuori, che non si poteva utilizzare sulle iPad normale, parlo di stage manager.
Mi ha fatto molto piacere, mi ha fatto vedere, diciamo, le capacità di Apple in queste piccole cose che
secondo me sono fantastiche.

### 2. Prima parte

In questa parte Filippo e Roberto seguono il tema “Prima parte” dentro il quadro dell’episodio su Velocizzare
la scrittura con le espansioni del testo. I passaggi centrali riguardano testo, quello, magari, parte. In
realtà si possono fare tutta una serie di cose che permettono appunto di lavorare col testo. E quindi o avete
la possibilità di ricordarlo a memoria se è abbastanza semplice, se non ce l'avete incastonato nella memoria,
potete utilizzare questi trucchetti di espansione del testo che vi permette appunto di sostituire con poche
lettere magari un testo molto lungo. Perché può capitare spesso e sovente che magari per la fretta o magari
perché siamo distratti, o perché magari non becchiamo il tasto nel modo giusto, quello che dovete scrivere
magari non viene scritto bene. E ovviamente c'è una parte da considerare perché è una parte molto importante,
nella mia fatispecie è proprio un muro very, è quello di ricordarsi le vostre abbreviazioni da tastiera.
D'altra parte, però, c'è da dire che nella mia fatispe sono un po' scusato perché arrivando in un ambiente
come quello del CAD, where le abbreviazioni da tastiera vi permettono davvero di risparmiare un sacco di
tempo. ricollego al terza comunicazione del servizio, a giugno ci sarà la WWDC e quindi ci saranno anche,
presumibilmente, le novità.

### 3. Cosa si intende per text expansion o Sostituzione del testo?

> "Ma appunto la sostituzione del testo, si trova all'interno dell'interfaccia sia delle."
> — Filippo e Roberto, 00:23:51
In questa parte Filippo e Roberto seguono il tema “Cosa si intende per text expansion o Sostituzione del
testo?” dentro il quadro dell’episodio su Velocizzare la scrittura con le espansioni del testo. I passaggi
centrali riguardano testo, tastiera, dispositivi, punte. E quindi gli anglofoni utilizzano punte virgola e il
testo e l'abbreviazione del testo che vogliono utilizzare solitamente poche lettere, e anzi, io consiglio
sempre di utilizzare poche lettere. Secondariamente, l'altra cosa interessante di tutto questo sistema è che
ovviamente c'è la possibilità di sincronizzare i cosiddetti snippet o frammenti di testo tra più dispositivi.
Questo perché abitualmente il punte virgola non è mai, è sempre staccato. Ma appunto la sostituzione del
testo, si trova all'interno dell'interfaccia sia delle impostazioni di macOS che di iOS e iPadOS, legato alla
tastiera, ovviamente. Ma Raiman da cui ho preso e credo tantissimi abbiano preso questa modalità, quindi ha
deciso di evitare di utilizzare il punte e virgola, ma di anporre una X all'abbreviazione. Le sostituzioni del
testo su tutti i dispositivi.

### 4. Quali sono gli utilizzi

In questa parte Filippo e Roberto seguono il tema “Quali sono gli utilizzi” dentro il quadro dell’episodio su
Velocizzare la scrittura con le espansioni del testo. I passaggi centrali riguardano tastiera, esempio,
invece, sistema. È molto comodo questo sistema, perché ovviamente non devo andare a cercare fare: anzi, ALT,
accento e poi la lettera, che spesso e volentieri casomai non viene presa correttamente. Se, per esempio, il
documento è di ieri ma l'ho scansionato oggi, cosa faccio? Scrivo X ieri e mi fa la data di ieri, ovviamente X
altro ieri di due giorni fa, poi dopo invece vado a mano perché non ha molto senso. Quindi tu, per esempio,
potresti aver fatto un aggiornamento a Microsoft Ventura passando alla Big Sure, e sugli altri dispositivi
Apple invece hai gli aggiornamenti, diciamo, iOS 16 presumo. Per cui, per esempio, siccome io spesso e
volentieri utilizzo tastiere americane sia su Mac che su iOS, e ovviamente le lettere accentate a volte non
sono comode da fare. No, però diciamo che rientrano come abbreviazioni da tastiera, visto che per inserire la
sostituzione da tastiera, da quello che ho capito, devo passare da qua, da abbrevazioni up.

### 5. Possibilità di sincronizzare gli “snippet” o frammento di testo

> "Facciamo il cambio, andiamo a favore, sono 35 euro all'anno per un'applicazione."
> — Filippo e Roberto, 00:35:44
In questa parte Filippo e Roberto seguono il tema “Possibilità di sincronizzare gli “snippet” o frammento di
testo” dentro il quadro dell’episodio su Velocizzare la scrittura con le espansioni del testo. I passaggi
centrali riguardano testo, esempio, versione, sempre. Ricordo che mi infilo subito in gamba tesa, il costo è
di 3,33 dollari al mese per la versione individuale, 8,33 dollari per la versione business, sempre per mese,
che permette anche di collaborare e comunicare efficientemente col vostro team. È ovvio che poter condividere
le espansioni del testo con dei collaboratori diventa comodo perché tu generi la risposta standard,
chiamiamolo così, con eventualmente due o tre risposte personalizzabili, ma anche personalizzabili. È ovvio
che più la collezione di espansioni del testo diventa grande, più hai inserito e sei abituato a utilizzare un
determinato programma, più è difficile abbandonarlo. Questo vuol dire che tutte le mie espansioni di testo ce
le hanno anche text expand e ovviamente non sono cifrate e così via. Questo sistema mi permette di lavorare
anche senza Tax Expander, che è attualmente lo strumento che utilizzo abitualmente per le espansioni del
testo, ma farò tutta una serie di piccole parentesi sull'argomento, ma non ora. Ma quando iniziano a essere un
testo di 100-200 parole, il vantaggio più o meno sempre uguale o comunque con delle variazioni sul tema,
chiamiamoli in questi termini.

### 6. Quale scelta utilizzare per le sostituzioni

In questa parte Filippo e Roberto seguono il tema “Quale scelta utilizzare per le sostituzioni” dentro il
quadro dell’episodio su Velocizzare la scrittura con le espansioni del testo. I passaggi centrali riguardano
testo, appunto, espansioni, lanciare. Quindi ovviamente rende molto facile e molto semplice la numerazione
mentre si scrive: stesso discorso sono riuscito a fare con espanso, appunto facendo tutto un giro diverso, ma
utilizzando appunto la possibilità di lanciare questi script da espanso. È che Draft, diciamo, l'idea di fondo
di Tex Expander era un'idea furba, ma di fatto è stata poco applicata, ha creato una sorta di API per
condividere le espansioni del testo. Quindi, ci sono ovviamente trucchi, è ovvio che l'espansione del testo è
molto più rapida, molto più efficace, perché mentre stai scrivendo, non ti devi fermare, lanciare un comando
rapido, guardati di copia e incollare e così via. Drafts può accedere ai dati quindi alle espansioni del testo
di Text Expander e se scrivi le espansioni del testo in Drafts, queste si aprono. Espanso espanso ha appunto
ha il grosso vantaggio di essere multipiattaforma, quindi funziona su Microsoft, su Windows e Linux. Se
interessa, perché si vuole passare da text expander, esistono tutta una serie di azioni che saranno poi
linkate nelle note dell'episodio per la conversione da tex expander a keyborg maestro.

### 7. Seconda parte

In questa parte Filippo e Roberto seguono il tema “Seconda parte” dentro il quadro dell’episodio su
Velocizzare la scrittura con le espansioni del testo. I passaggi centrali riguardano ovviamente, testo,
all'interno, appunto. Espanso è una roba un po' più da smanettoni, chiamiamoli in questo termine, perché devi
andare a creare le espansioni del testo all'interno di un file di configurazione testuale, in particolare
scritto in YAML. Roberto, tu avevi dato un'occhiata espanso, diciamo, per te l'uomo della strada, l'uomo
qualunque l'uomo qualunque dice che è molto interessante. Ovviamente anche l'espansione del testo, se ci metti
dieci minuti a fare un'espansione del testo, diciamo che il risultato, allora, a quel punto lì non è
interessante. Una cosa che non avevo detto e che però può tornare utile, sia Tax Expander che espanso,
abitualmente hanno un'utility da ben un bar. L'altra cosa, piccole chicche espanso è open source. Quindi, se
volete contribuire, comunque troverete tutto quanto all'interno delle note dell'episodio, come sempre.

### 8. Le soluzioni Software: sguardo d'insieme

In questa parte Filippo e Roberto seguono il tema “Le soluzioni Software: sguardo d'insieme” dentro il quadro
dell’episodio su Velocizzare la scrittura con le espansioni del testo. I passaggi centrali riguardano cose,
testo, quello, quelle. Quindi, quindi ovviamente, io, da una parte, con l'espansione del testo, faccio
lanciare lo script, dall'altra, devo creare lo script che faccia quello che voglio io, e le due automazioni
non si devono pestare i piedi l'una con l'altra. Ma come vi ha spiegato Filippo, le cose possono diventare
davvero molto interessanti quando si lavora col testo e soprattutto quando si ha a che fare con azioni
ripetitive, direi in larga parte, perché questo vi può veramente salvare la giornata. Così potete avere anche
più tempo per fare tante di quelle cose come facciamo io e Filippo. Sì, direi che anche in questo caso bisogna
ovviamente farci un giro sopra per renderci conto di quello che si tratta. Quindi, anche qui è molto utile il
sistema, proprio per questo motivo perché ti permette di anche aiutarti a cercare le cose, soprattutto per
quelle cose che non si fanno quotidianamente. Insomma, si possono fare veramente tante cose.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
