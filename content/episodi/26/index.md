+++
title = "26: Comandi Rapidi per Calendario ed applicazioni utili per fissare appuntamenti"
date = "2022-01-17T06:00:00+01:00"
episodeNumber = 26
slug = "26"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336011/bae0eb8f_10f7_484d_bcd1_57e1fab1ffec.mp3"
spreakerEpisodeId = "64336011"
duration = "59:07"
description = "Come promesso nella scorsa puntata oggi concludiamo l’approfondimento sui calendari: vedremo alcune azioni di comandi rapidi interessanti e tutta una serie di applicazioni che non sono proprio dei calendari ma che permettono di aiutare a gestire i calendari e gli appuntamenti."
tags = ["shortcuts", "calendario", "automazione", "produttivita"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "FvskHBRqOg0"
+++

> Come promesso nella scorsa puntata oggi concludiamo l’approfondimento sui calendari: vedremo alcune azioni di comandi rapidi interessanti e tutta una serie di applicazioni che non sono proprio dei calendari ma che permettono di aiutare a gestire i calendari e gli appuntamenti.

## Note dell’episodio
- [Agenda](https://www.agenda.com): app per note in Markdown organizzate per data, utile per collegare appunti, riunioni e calendario nello stesso flusso.
- [Agenda su App Store](https://apps.apple.com/it/app/agenda/id1370289240?ign-itsct=apps_box&ign-itscg=30200): versione iOS/iPadOS dell’app citata in puntata, con funzioni gratuite e acquisti premium.
- [Sorted³](https://www.sortedapp.com): applicazione che unisce calendario e attività in una timeline giornaliera, con strumenti per riorganizzare rapidamente gli impegni.
- [Strategr](https://khrykin.github.io/StrategrDesktop/): progetto open source per Mac orientato al time blocking e alla pianificazione strategica della giornata.
- [CornerCal](https://github.com/ekreutz/CornerCal): calendario open source da barra dei menu per macOS.
- [Up Next](https://github.com/ellenli/up-next): app open source da barra dei menu che mostra i prossimi appuntamenti, in particolare le videochiamate da calendario.
- [MeetingBar](https://github.com/leits/MeetingBar): applicazione open source da barra dei menu per visualizzare e raggiungere rapidamente meeting e call.
- [Calcurse](https://calcurse.org): calendario e gestore attività da terminale, pensato per chi preferisce lavorare da riga di comando.
- [Itsycal](https://www.mowglii.com/itsycal/): piccolo calendario gratuito per la barra dei menu di macOS.
- [InstaCal](http://instacalapp.com): calendario da barra dei menu con supporto a calendari Apple, Google, Outlook e Office 365.
- [Doodle](https://doodle.com/it/): servizio per scegliere date comuni tra più partecipanti, utile quando bisogna incrociare molte disponibilità.
- [Calendly](https://calendly.com/): servizio per pubblicare fasce disponibili e permettere ad altri di prenotare appuntamenti.
- [Cal.com su GitHub](https://github.com/calendso/calendso): progetto open source, nato come Calendso, per creare un sistema di prenotazione appuntamenti anche in self-hosting.
- [Nextcloud Hub II](https://nextcloud.com/blog/nextcloud-hub-2-brings-major-overhaul-introducing-nextcloud-office-p2p-backup-and-more/): versione di Nextcloud che introduce, tra le altre novità, funzionalità per fissare appuntamenti.
- [The 6 best calendar apps for Mac in 2021](https://zapier.com/blog/best-calendar-apps-for-mac/): articolo di riferimento citato nelle note originali per confrontare app calendario su Mac.

## Sinossi[^sinossi-ai]

### 1. Ripresa del tema calendario e ruolo di Comandi Rapidi
Filippo e Roberto aprono l’episodio come seconda parte dell’approfondimento sui calendari iniziato nella puntata precedente. L’obiettivo non è tornare sulle funzioni di base del calendario, ma mostrare strumenti collaterali: prima alcune automazioni con Comandi Rapidi, poi una lunga panoramica di applicazioni che non sono calendari puri ma aiutano a gestire appuntamenti, giornate e riunioni.

Roberto introduce il tema con il suo consueto tono autoironico, raccontando la difficoltà di incastrare lavoro, cena e registrazione del podcast. Filippo raccoglie il punto e propone un approccio pratico: usare il calendario non solo come archivio di appuntamenti, ma come oggetto modificabile e automatizzabile. La parte iniziale è quindi costruita come un laboratorio: Roberto segue su iPad, Filippo guida passo passo la creazione di un comando rapido.

Il primo comando rapido ha una funzione semplice ma concreta: prendere i prossimi eventi di calendario, mostrarli in un elenco, farne scegliere uno e spostarlo in avanti. Filippo chiarisce subito che non si tratta di un’automazione spettacolare, ma di uno spunto per capire il modo in cui Comandi Rapidi può interagire con date, eventi e variabili.

> "Comandi rapidi è molto ben strutturato e ha molte funzioni."
> — Filippo, 00:02:57

L’idea pratica è quella delle attività rimandate: se un evento o un blocco di lavoro previsto per oggi non può essere svolto, lo si seleziona da un elenco e lo si sposta al giorno successivo, o a un’altra distanza temporale scelta dall’utente. La spiegazione insiste su un punto importante: l’automazione non sostituisce il ragionamento, ma evita passaggi ripetitivi come aprire il calendario, cercare l’evento e modificarlo manualmente.

### 2. Costruire un comando rapido per spostare un evento
Filippo guida Roberto nella costruzione dell’automazione. Il primo passaggio è creare un nuovo comando rapido e cercare le azioni legate al calendario. Dopo un piccolo inciampo tra “ottieni dettagli degli eventi di calendario” e “ottieni i prossimi eventi”, i due individuano l’azione corretta: “Ottieni i prossimi eventi”. Filippo suggerisce di impostare il numero a cinque, così da avere una lista gestibile dei prossimi appuntamenti.

La seconda azione è “Scegli dall’elenco”. Qui entra in gioco il concetto di variabile magica: l’output della prima azione, cioè l’elenco dei prossimi eventi, viene passato alla seconda, che permette all’utente di scegliere quale evento modificare. Roberto prova il comando e verifica che l’elenco dei cinque appuntamenti venga effettivamente mostrato.

Il passaggio successivo è “Modifica data”. Filippo spiega che questa azione permette di aggiungere o sottrarre giorni, ore, minuti o secondi a una data. Nel caso più semplice, si aggiunge un giorno alla data dell’evento scelto; ma l’automazione può essere resa più flessibile chiedendo ogni volta di quanti giorni o ore spostare l’appuntamento. L’esempio è molto concreto: un’attività del venerdì può essere rimandata direttamente al lunedì, oppure un appuntamento delle 17 può essere spostato alle 18 o alle 19.

L’ultima azione è quella decisiva: “Modifica evento del calendario”. Filippo sottolinea che fino a quel momento il comando ha solo calcolato una nuova data; per cambiare davvero il calendario bisogna prendere l’evento selezionato e impostare la sua nuova data di inizio. Roberto riassume correttamente il meccanismo: la prima variabile è l’elemento scelto dall’elenco, la seconda è la data modificata prodotta dall’azione precedente.

> "Il computer è stupido, tra virgolette, cioè è molto bravo a seguire gli ordini, ma stupido."
> — Filippo, 00:18:35

Da questa spiegazione emerge una regola generale di Comandi Rapidi: bisogna ragionare per passaggi minimi, quasi come in una ricetta. Ogni azione deve ricevere un input chiaro e produrre un output da passare all’azione successiva. Roberto nota proprio questo aspetto: per chi non programma, non è immediato capire che bisogna dire al comando non solo cosa calcolare, ma anche dove applicare il risultato.

### 3. Selezione multipla, conflitti e automazioni ricorrenti
Filippo accenna poi a una possibile evoluzione del comando: abilitare la selezione multipla nell’azione “Scegli dall’elenco”. In questo modo sarebbe possibile selezionare più eventi e spostarli insieme. L’automazione diventerebbe però più complessa, perché servirebbe un ciclo “ripeti per ogni elemento”: per ciascun evento selezionato bisognerebbe calcolare la nuova data e poi applicare la modifica. Filippo decide di non addentrarsi troppo, ma usa l’esempio per mostrare come un comando semplice possa diventare una base per soluzioni più articolate.

Un altro punto pratico riguarda i conflitti. Se un evento viene spostato su una fascia oraria già occupata, il calendario non impedisce necessariamente la sovrapposizione: mostra gli eventi affiancati. Su iOS, durante l’esecuzione, si può anche vedere un’anteprima del risultato nel calendario, utile per capire dove finirà l’appuntamento.

Da qui Filippo passa a un secondo esempio, legato alla vita domestica: la programmazione dei pasti. Racconta di essere il cuoco di famiglia e di usare il calendario anche per pianificare menu e cene. L’esempio è la pizza del sabato: si potrebbe creare un evento ricorrente, ma Filippo preferisce maggiore flessibilità. Gli eventi ricorrenti sono comodi quando la routine è stabile, ma diventano rigidi quando serve spostare, adattare o ripensare la settimana.

Il secondo comando rapido usa quindi l’azione “Aggiungi nuovo evento”. L’utente può precompilare titolo, data, ora di inizio, ora di fine, calendario, eventuale posizione e avvisi. Filippo immagina una shortcut che, con un solo lancio, crea tutti gli eventi dei pasti della settimana: lunedì, martedì, mercoledì, giovedì, venerdì e sabato. In futuro, si potrebbe rendere il sistema ancora più dinamico, scegliendo da menu già pronti e decidendo dove collocarli nel calendario.

> "Potete cucinare le vostre automazioni un po’ come volete."
> — Filippo, 00:26:27

Roberto resta colpito dalla quantità di opzioni disponibili in Comandi Rapidi. Filippo precisa che il vantaggio è massimo quando si hanno operazioni tipiche e ripetute, soprattutto se richiedono impostazioni dettagliate: più avvisi, calendari specifici, orari ricorrenti, note o posizioni. In questi casi l’automazione riduce il tempo speso in micro-operazioni manuali.

### 4. Agenda: note, date e riunioni nello stesso ambiente
Conclusa la parte su Comandi Rapidi, Filippo e Roberto passano alle applicazioni che non sono calendari in senso stretto ma ruotano attorno all’organizzazione del tempo. Filippo chiarisce il proprio assetto quotidiano: usa Fantastical come calendario e Todoist per le attività. Le app citate in questa puntata non sono necessariamente parte del suo flusso stabile, ma strumenti interessanti per esigenze specifiche.

La prima è Agenda. Filippo la descrive come un’app ibrida: non è un calendario, ma un sistema per prendere note in Markdown collegate alle date. L’idea è avere una vera agenda digitale in cui gli appuntamenti non sono solo blocchi orari, ma punti di ingresso per materiali, scalette, appunti e resoconti.

L’esempio è una riunione tra Filippo e Roberto per programmare A2. Nel calendario c’è l’appuntamento; dentro Agenda si possono preparare gli argomenti da trattare e, durante la riunione, prendere appunti sulle decisioni. Questi appunti possono poi essere riutilizzati per scrivere una relazione, una scaletta o un documento più formale. Filippo precisa che per il suo lavoro non è un’esigenza centrale, perché spesso gestisce appunti e documenti separatamente, ma riconosce che per altri professionisti può essere una soluzione molto efficace.

Agenda viene presentata anche dal punto di vista dell’interfaccia: ha vinto un Apple Design Award nel 2018, è disponibile in italiano, ha una base gratuita e funzioni premium. Roberto, guardandola su iPad, nota un dettaglio per lui importante: consente anche di prendere appunti disegnando. Il confronto implicito è con strumenti come Notion, molto potenti ma non sempre adatti a chi vuole integrare scrittura e input grafico nello stesso spazio.

### 5. Sorted³ e la pianificazione visuale della giornata
La seconda applicazione approfondita è Sorted³, che Filippo definisce molto attraente ma non perfetta per il suo flusso personale. Sorted³ unisce calendario e attività in una timeline giornaliera, con un’interfaccia pensata per spostare, ordinare e riorganizzare gli impegni velocemente, soprattutto su iPhone e iPad.

Filippo collega Sorted³ all’automazione costruita nella prima parte della puntata: ciò che in Comandi Rapidi hanno creato manualmente, Sorted³ lo rende disponibile con tap e interazioni native. L’app si integra con il calendario, quindi le modifiche fatte in Sorted³ vengono rispecchiate nell’app Calendario di Apple.

Il limite, per Filippo, è la gestione delle attività. Sorted³ non si aggancia a Todoist e non usa nemmeno Promemoria come motore principale per i task: le attività vengono gestite internamente. Questo è un problema per chi, come lui, ha già una struttura complessa fatta di pratiche, progetti e attività collegate. Per un uso più lineare, invece, Sorted³ può avere molto senso.

La forza dell’app è la timeline unificata: appuntamenti e cose da fare convivono nello stesso spazio temporale. Sorted³ offre anche funzioni di pianificazione rapida e una forma di “intelligenza” per suggerire dove collocare o ricollocare gli impegni in base agli spazi liberi. Filippo la considera quindi una soluzione interessante per chi vuole pianificare la giornata in modo visivo, ma meno adatta a chi ha bisogno di un sistema task management più articolato e già consolidato.

### 6. Strumenti open source e time blocking
Filippo apre poi una parentesi sugli strumenti open source, spiegando che non tutti hanno motivo di pagare applicazioni come Fantastical o Todoist, soprattutto se non le usano per lavoro. Per chi vuole organizzarsi senza investire in software commerciali, le alternative open source possono essere una risorsa concreta.

Il primo progetto citato è Strategr, un’app per Mac orientata al time blocking. Filippo non l’ha provata sul campo, ma ne è rimasto colpito. L’app prende i dati dal calendario e aiuta a costruire una scaletta della giornata, organizzando le attività in blocchi successivi. È pensata per chi vuole decidere cosa fare, quando farlo e in quale ordine, lavorando su una singola giornata alla volta.

Roberto, che sta cercando un metodo per fare time blocking in Notion, trova Strategr interessante proprio perché evita una duplicazione problematica. Filippo spiega infatti che uno dei rischi del time blocking è mantenere due sistemi separati: un calendario per gli appuntamenti e un altro spazio per i blocchi di lavoro. Se i due non comunicano, la pianificazione diventa costosa in termini di tempo. Strategr, prendendo i dati dal calendario, riduce questa frizione.

> "Avere tutto in un posto solo [...] mi fa molto comodo."
> — Filippo, 00:40:11

Filippo collega questo punto anche al suo uso di Fantastical e Todoist: l’integrazione gli permette di vedere nello stesso spazio appuntamenti e attività, e di spostare i blocchi di lavoro in base al tempo disponibile. Roberto prova Strategr durante la registrazione e lo definisce “molto carino”, lasciando intendere che potrebbe tornarci sopra in futuro.

### 7. Calendari da barra dei menu e utility verticali
La puntata prosegue con una serie di strumenti più piccoli e verticali, molti dei quali vivono nella barra dei menu di macOS. Filippo parte da CornerCal, che offre un calendario e un orologio accessibili rapidamente dal menu. Il punto non è sostituire l’app Calendario, ma avere una vista immediata del mese, dei giorni e degli impegni senza interrompere il lavoro.

Filippo racconta di usare una funzione simile tramite iStat Menus: cliccando sulla data nella barra dei menu, vede il mese, gli impegni e i calendari coinvolti. Roberto nota che macOS, di default, non sfrutta abbastanza bene il clic su data e ora: invece di mostrare un calendario utile, apre impostazioni poco rilevanti.

Tra le utility verticali vengono citate anche Up Next e MeetingBar. Entrambe servono a mostrare i prossimi appuntamenti, in particolare le videochiamate, direttamente dalla barra dei menu. Filippo osserva che sono soluzioni molto adatte a contesti in cui si passa la giornata tra Zoom, Google Meet e riunioni online. Prendono i dati dal calendario e rendono più rapido capire qual è la prossima call o raggiungerla.

C’è poi Calcurse, presentato come una “chicca” per chi vive nel terminale. È un calendario da riga di comando, con gestione testuale degli appuntamenti. Filippo lo cita più come curiosità tecnica che come consiglio generalista: per alcuni utenti può essere perfettamente naturale, per altri del tutto estraneo.

La carrellata continua con Itsycal, Calendar 366 II, InstaCal e iStat Menus. Itsycal viene indicato come una soluzione gratuita e leggera; Calendar 366 II come alternativa più ricca ma a pagamento; InstaCal come strumento più completo, capace di interagire anche con calendari Google, Outlook e Office 365. iStat Menus, invece, non nasce come app calendario: è un pacchetto di utility da menu bar per monitorare CPU, rete, disco e sensori, ma include anche una vista utile della data e del calendario.

### 8. Doodle, Calendly, Cal.com e Nextcloud per fissare appuntamenti
L’ultima parte reale dell’episodio riguarda i servizi collaterali al calendario, cioè strumenti che non servono tanto a gestire la propria agenda interna, quanto a fissare appuntamenti con altre persone. Filippo li colloca soprattutto in ambito business, professionale o associativo, dove le riunioni sono frequenti e bisogna coordinare molte disponibilità.

Il primo è Doodle. Filippo lo descrive come uno dei servizi storici per proporre più date e far scegliere ai partecipanti quella più adatta. Lo ha usato in contesti associativi, dove bisognava incastrare gli impegni di diversi avvocati. Il metodo è semplice: si indicano alcune date possibili, i partecipanti votano le proprie disponibilità e si individua il giorno che va bene a tutti, o almeno alla maggioranza. La versione gratuita può essere sufficiente, ma comporta pubblicità e limiti; la versione Pro costa quasi sette euro al mese e ha senso soprattutto per chi organizza molte riunioni.

Calendly viene presentato come un servizio diverso: non serve a votare tra più date, ma a pubblicare fasce disponibili in cui altre persone possono prenotarsi. L’esempio di Filippo è quello del professionista che riceve il martedì pomeriggio: può inviare un link, mostrare solo gli slot liberi e lasciare che il cliente prenoti. Il sistema si collega al calendario e impedisce, in linea di principio, prenotazioni sovrapposte. Il limite indicato è la lingua inglese, che può renderlo meno adatto a tutti i destinatari.

Filippo passa poi a Cal.com, nato come Calendso: un progetto open source che permette di costruire un sistema simile anche in self-hosting. Qui la cautela è forte. La soluzione gratuita richiede competenze tecniche, capacità di installazione e configurazione, e una certa attenzione alla sicurezza. Collegare un servizio di prenotazione al proprio calendario significa dare accesso a dati e possibilità operative sensibili.

> "Da avvocato, come si suol dire, io consiglio cautela."
> — Filippo, 00:52:50

L’ultimo strumento citato è Nextcloud Hub II. Filippo spiega che A2 usa Nextcloud come back-end e che la versione 23 introduce anche funzioni per fissare appuntamenti. La considera una possibile alternativa interessante, soprattutto per chi vuole mantenere maggiore controllo sul proprio cloud e sui propri dati. Nextcloud è sviluppato da una società tedesca e viene presentato come una piattaforma pensata anche con attenzione al contesto europeo e al GDPR. Filippo però non l’ha ancora testata a fondo: per ora preferisce appoggiarsi a servizi terzi, anche perché gestire direttamente un server richiede competenze e responsabilità non banali.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
