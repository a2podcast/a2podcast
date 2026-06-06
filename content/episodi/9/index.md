+++
title = "9: La sicurezza delle password ed il gestore di password"
date = "2021-03-29T06:00:00+01:00"
episodeNumber = 9
slug = "9"
audioUrl = "https://dts.podtrac.com/redirect.mp3/api.spreaker.com/download/episode/64336050/e8c303e9_1cb9_4c43_bf91_8168807c2c83.mp3"
spreakerEpisodeId = "64336050"
duration = "1:01:02"
description = "In questo episodio Andrea, Roberto e Filippo vi parlano di sicurezza delle password e di come utilizzare i programmi di gestione delle password per renderci la vita più semplice!"
tags = ["sicurezza", "password-manager", "privacy", "cybersecurity"]
draft = false

[params]
  hasTranscript = true
  youtubeId = "Mhq2YnKDih8"
+++

> In questo episodio Andrea, Roberto e Filippo vi parlano di sicurezza delle password e di come utilizzare i programmi di gestione delle password per renderci la vita più semplice!

## Note dell’episodio

- [Bloccare o sbloccare le note su iPhone o iPad](https://support.apple.com/it-it/HT205794): guida Apple citata per spiegare perché le note protette possono essere un ripiego, ma non un vero password manager.
- [Rendere disponibili le password e le passkey su tutti i dispositivi con il portachiavi iCloud](https://support.apple.com/it-it/guide/ipad/ipada39a7fa0/ipados): documentazione Apple su Portachiavi iCloud, sincronizzazione tra dispositivi e protezione delle password.
- [Utilizzare Password iCloud in Chrome su computer Windows](https://support.apple.com/it-it/guide/icloud/mmfeee20145e/1.0/icloud): pagina Apple citata per il caso d’uso di Password iCloud fuori dall’ecosistema solo Apple.
- [1Password](https://1password.com): password manager usato da Filippo, discusso per vault cifrati, sincronizzazione, estensioni browser e piani personali/famiglia.
- [1Password per iPhone e iPad](https://apps.apple.com/it/app/1password-password-manager/id568903335): app iOS/iPadOS citata tra le opzioni multipiattaforma per usare 1Password su dispositivi mobili.
- [Scarica 1Password per Mac](https://1password.com/downloads/mac/): pagina download richiamata per l’installazione diretta e le opzioni fuori dal solo App Store.
- [LastPass](https://www.lastpass.com/it/): password manager citato come alternativa multipiattaforma non testata direttamente dai conduttori.
- [Bitwarden](https://bitwarden.com): password manager open source citato come alternativa a 1Password, anche per chi vuole valutare self-hosting.
- [Prezzi Bitwarden](https://bitwarden.com/pricing/): pagina prezzi richiamata per distinguere piano gratuito, premium personale e piano famiglia.
- [KeePassXC](https://keepassxc.org): password manager open source desktop, citato per la gestione locale di database cifrati.
- [KeePass Password Safe](https://keepass.info): progetto KeePass da cui deriva l’ecosistema compatibile con KeePassXC e app mobili.
- [Syncthing](https://syncthing.net/): strumento di sincronizzazione citato da Filippo come possibile modo per spostare un database KeePass tra dispositivi senza cloud proprietario.
- [KeePassium](https://keepassium.com): app iOS per usare database KeePass su iPhone e iPad con funzioni avanzate.
- [Strongbox](https://strongboxsafe.com/): app iOS e macOS compatibile con KeePass, citata come alternativa per database locali.
- [Prezzi e funzioni Strongbox](https://strongboxsafe.com/pricing/): pagina richiamata perché nella puntata si distingue tra funzioni gratuite e sblocco biometrico avanzato.

## Sinossi[^sinossi-ai]

### 1. Il problema quotidiano: troppe password, spesso troppo deboli

Roberto, Filippo e Andrea Strozzi aprono la puntata dal problema più comune: ogni servizio digitale richiede credenziali, ma la memoria umana non è fatta per gestire decine o centinaia di password diverse, lunghe e robuste. Roberto ricorda il web degli anni Novanta, quando un indirizzo email poteva avere una password semplice e il rischio percepito era molto più basso. Oggi la situazione è diversa: email, Apple ID, social, account di lavoro, servizi cloud, dispositivi e app producono un numero di accessi che non si può più gestire “a mano” senza errori.

> "Le password sono un gran bel casino: bisogna crearne di nuove ogni tanto, ricordarsele e soprattutto farle difficili."
> — Roberto, 00:03:08

Il primo errore discusso è usare password banali. La classifica delle password più usate nel 2020, con esempi come `123456` e `password`, serve a mostrare che molte persone proteggono dati importanti con combinazioni presenti in qualsiasi dizionario di attacco. Roberto allarga il discorso anche ai router domestici: lasciare credenziali predefinite come `admin` e `password` può esporre la rete, soprattutto in condomini, uffici o contesti in cui il Wi-Fi è raggiungibile da più persone.

Filippo aggiunge il profilo giuridico e pratico: se qualcuno usa la rete di casa per attività illecite, il primo collegamento tecnico porta al titolare della linea. Dimostrare che l’accesso è stato abusivo può essere possibile, ma è comunque un problema serio. La sicurezza della password del router, quindi, non è un dettaglio da smanettoni: riguarda responsabilità, privacy e controllo della propria rete.

### 2. Pensare come un attaccante: dizionari, dati personali e riuso

Filippo racconta di aver seguito corsi pensati per capire gli strumenti usati dagli hacker. Non entra nel dettaglio operativo, ma usa quell’esperienza per spiegare un metodo: bisogna ragionare dal punto di vista di chi vuole entrare. Una password breve, solo numerica o composta da parole comuni, può essere testata rapidamente con attacchi a forza bruta o con dizionari di password già note.

> "Bisogna cercare di pensare come un hacker e quindi sapere le cose che un hacker può fare."
> — Filippo, 00:13:32

I dizionari non sono solo liste generiche in inglese. Possono contenere varianti locali e combinazioni prevedibili: stagioni, anni, nomi, date di nascita, parole italiane comuni, informazioni recuperabili dai social. Per questo Filippo sconsiglia password basate su compleanni, nomi di familiari, figli, coniugi o riferimenti visibili online. In molti casi non serve un attaccante sofisticato: basta qualcuno con poche informazioni personali e strumenti automatici.

La puntata richiama anche i suggerimenti di sicurezza di iOS, dove Apple segnala password riutilizzate o compromesse. Il riuso è uno dei problemi centrali: se la stessa password viene usata per email, social, servizi professionali e acquisti online, la compromissione di un sito può aprire la porta a tutti gli altri. La sicurezza non dipende solo dalla forza della singola password, ma anche dalla sua unicità.

### 3. Come costruire password più robuste senza renderle ingestibili

La regola base proposta è combinare lunghezza e varietà: lettere maiuscole e minuscole, numeri, simboli speciali e almeno otto caratteri, con l’avvertenza che otto caratteri sono ormai un minimo molto basso. Filippo spiega il problema con un criterio matematico semplice: più caratteri e più tipi di caratteri aumentano le combinazioni possibili, quindi rendono più costoso trovare la password provando tutte le varianti.

La puntata però non si ferma al modello “stringa impossibile da ricordare”. Roberto e Filippo parlano anche di passphrase: frasi o combinazioni di parole che possono risultare più lunghe, più facili da ricordare e più robuste di una password breve piena di simboli. Esempi come “1000 mari blu” o sequenze di parole casuali mostrano una via intermedia: aumentare l’entropia senza costringere l’utente a memorizzare codici impronunciabili.

Il punto pratico è che una password robusta non serve se l’utente la scrive su un foglietto visibile, la riusa ovunque o la comunica male. Roberto cita anche il rischio, visto durante videoconferenze, di post-it con credenziali lasciati alle spalle della persona in video. La sicurezza non è solo tecnica: è fatta anche di abitudini, ambiente di lavoro e attenzione ai dettagli.

### 4. Autenticazione a due fattori e login social

Filippo introduce l’autenticazione a due fattori come livello aggiuntivo rispetto a utente e password. L’OTP, cioè one-time password, è un codice temporaneo generato da un’app o inviato tramite SMS. Se un malintenzionato ottiene la password, deve comunque superare un secondo controllo legato a un dispositivo o a un canale separato.

> "L'autenticazione a due fattori non è legata strettamente alla password, ma è un sistema di sicurezza aggiuntivo."
> — Filippo, 00:27:24

La puntata distingue anche tra soluzioni più e meno solide. L’SMS è comodo, ma passa su un canale meno robusto; un’app di autenticazione sullo smartphone o su un altro dispositivo è preferibile in molti scenari. Filippo cita il caso dei conti correnti e dello SPID per far capire che il secondo fattore è già entrato nella vita quotidiana, anche quando non lo si chiama con il suo nome tecnico.

L’ultima avvertenza riguarda i login con Facebook, Google o servizi simili. Sono comodi, ma concentrano molto potere in un singolo account: se quell’account viene compromesso, l’attaccante può entrare nei servizi collegati. Apple viene citata come caso un po’ diverso, perché “Accedi con Apple” può generare indirizzi email fittizi e limitare la diffusione dell’indirizzo reale, ma il consiglio resta prudente: la comodità dei login federati va valutata insieme al rischio di dipendenza da un unico account.

### 5. A cosa serve davvero un password manager

La seconda metà della puntata entra nel tema centrale: il gestore di password. Roberto lo definisce come un software pensato per custodire in modo sicuro le credenziali e rendere più semplice usare password robuste. Il vantaggio non è solo “ricordare al posto nostro”, ma cambiare il modo in cui si lavora con le credenziali.

Un password manager genera password casuali, le salva in una cassaforte cifrata, le inserisce nei siti tramite estensioni browser o autofill e può sbloccarsi con sistemi biometrici come Face ID e Touch ID. Questo riduce due cattive abitudini: scegliere password facili da ricordare e copiare/incollare password complesse negli appunti di sistema.

> "Un gestore di password è un programma software pensato per custodire in modo sicuro le vostre password."
> — Roberto, 00:33:53

Roberto spiega anche la distinzione tra gestione locale e gestione online. Nel modello locale, le password stanno in una cassaforte, cioè un file cifrato protetto da una master password. Quella password principale diventa fondamentale: se si perde, si perde l’accesso a tutto il resto. Nel modello web, il fornitore offre sincronizzazione tra dispositivi e funzioni di condivisione, spesso tramite abbonamento. È più comodo, soprattutto per famiglie e uffici, ma richiede fiducia nel servizio.

### 6. Note protette e Portachiavi iCloud: le soluzioni Apple

Filippo parte da un chiarimento: le note protette di Apple possono essere meglio di un foglio di carta lasciato in vista, ma non sono un password manager. Le note cifrate servono a bloccare contenuti privati, non a generare password, compilarle nei siti, controllare riusi, gestire vault o sincronizzare credenziali in modo strutturato. Per questo nella sezione note resta la guida Apple sulle note protette, ma viene presentata come ripiego, non come soluzione consigliata.

Subito dopo si passa a Portachiavi iCloud, che Roberto usa perché è integrato e richiede pochissima manutenzione. Il sistema salva credenziali, le sincronizza tra dispositivi Apple e permette di inserirle con Touch ID o Face ID. Roberto sottolinea il miglioramento delle versioni recenti di macOS e iOS: quando si crea un account, il sistema propone una password robusta, la salva e poi la ripresenta automaticamente al login.

La comodità di Portachiavi iCloud è anche il suo limite: funziona molto bene dentro l’ecosistema Apple, meno quando la vita digitale comprende Windows, Android, browser diversi o condivisione avanzata con persone esterne. Filippo ricorda inoltre che l’Apple ID è il cardine dell’intero ecosistema: può bloccare o localizzare dispositivi, accedere a funzioni iCloud e, se configurato, intervenire anche su dischi cifrati. Per questo l’Apple ID deve avere una password forte e l’autenticazione a due fattori attiva.

### 7. 1Password: multipiattaforma, vault e costo dell’ecosistema

Il software principale discusso è [1Password](https://1password.com), usato da Filippo e presentato come uno dei password manager più noti in ambiente Apple, ma ormai disponibile anche su Windows, Linux, iOS, iPadOS e Android. Filippo ne apprezza la storia, la maturità e la disponibilità multipiattaforma, soprattutto rispetto a chi non vive solo nell’ecosistema Apple.

La puntata distingue tra il modello più vecchio, con vault cifrato sincronizzato tramite cloud esterni o soluzioni locali, e il modello più recente basato sul cloud di 1Password. Filippo preferisce un approccio più conservativo, con controllo maggiore sulla cassaforte, ma riconosce che la sincronizzazione proprietaria rende più semplice condividere password con familiari, collaboratori o altri utenti.

> "Ho quasi 600 password salvate in 1Password."
> — Filippo, 00:50:25

Questo numero mostra il costo di uscita da un password manager: una volta inserite centinaia di credenziali, migrare richiede tempo, affidabilità dell’importazione e verifica. Filippo cita la possibilità di passare a soluzioni open source, ma riconosce che 1Password funziona bene e che il vero problema non è solo il prezzo dell’abbonamento, ma l’intero flusso di lavoro costruito nel tempo.

### 8. LastPass, Bitwarden, KeePassXC e app compatibili

Nella parte finale Filippo elenca alternative non testate direttamente in modo approfondito. [LastPass](https://www.lastpass.com/it/) viene citato come password manager multipiattaforma con piano gratuito e premium, estensioni browser e funzioni simili a 1Password. La puntata non entra in una recensione completa, ma lo colloca tra le opzioni note del mercato.

[Bitwarden](https://bitwarden.com) interessa perché è open source e offre sia un servizio online simile a 1Password sia possibilità più avanzate per chi vuole gestire in proprio l’infrastruttura. Filippo avverte però che il self-hosting richiede competenze e manutenzione: non pagare un servizio può significare assumersi direttamente responsabilità tecniche.

[KeePassXC](https://keepassxc.org) e [KeePass](https://keepass.info) rappresentano l’approccio opposto al cloud proprietario: un database locale cifrato, sincronizzabile con strumenti scelti dall’utente, per esempio [Syncthing](https://syncthing.net/). La flessibilità è alta, ma su iOS servono app compatibili come [KeePassium](https://keepassium.com) o [Strongbox](https://strongboxsafe.com/), spesso con funzioni avanzate a pagamento. Filippo nota che lo sblocco biometrico con Face ID o Touch ID diventa rapidamente una funzione difficile da abbandonare, perché rende pratico usare password robuste senza tornare ogni volta alla master password.

[^sinossi-ai]: Questa sinossi è generata con l’intelligenza artificiale a partire dalla trascrizione della puntata.
