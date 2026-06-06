# Fase 2 — Ricerca e verifica link delle cose citate

Obiettivo: raccogliere gli URL ufficiali di prodotti/app/persone/risorse citati nell'episodio,
per la sezione `## Link` e per i link inline della sinossi.

Questa fase è obbligatoria: la skill deve comportarsi come un ricercatore editoriale, non
limitarsi ai link già presenti. Cerca, verifica e segnala l'affidabilità dei link.

**Priorità delle fonti:**
1. Link **già presenti nelle note** dell'index.md (verificati dai conduttori) — massima priorità,
   NON duplicarli né sostituirli.
2. URL espliciti citati nell'SRT (anche detti a voce).
3. URL ufficiali verificati per prodotti/servizi/persone menzionati.
4. App Store/Mac App Store, GitHub ufficiale, documentazione ufficiale, canale YouTube ufficiale.
5. Articoli o fonti terze solo se sono la risorsa citata in puntata o se non esiste una fonte
   ufficiale.

## Verifica obbligatoria

- Se hai accesso web, apri o cerca l'URL e verifica che sia pertinente al nome citato.
- Se non hai accesso web, usa solo i link già presenti nelle note come "verificati"; tutti gli
  altri vanno marcati `DA_VERIFICARE`.
- Non inventare homepage plausibili. Un link non verificato è peggio di nessun link.
- Mantieni un elenco di lavoro con stato:
  - `ESISTENTE` — già nelle note, non duplicare.
  - `VERIFICATO` — trovato e controllato durante la ricerca.
  - `DA_VERIFICARE` — candidato non controllato o dubbio.

**Delega (se disponibile):** passa questo prompt a un sub-agente con accesso web
(Claude: Haiku + WebSearch; Codex: passo con ricerca). Altrimenti esegui tu la ricerca.

```
Sei un ricercatore. Dall'analisi di questa trascrizione del podcast A2 (tecnologia Apple,
produttività) sono stati citati i seguenti prodotti/app/servizi/persone/risorse:

[LISTA estratta dalla Fase 1]

Per ciascuno trova l'URL ufficiale più pertinente. Formato output, una riga per risorsa:
Nome – Descrizione contestuale breve | URL | STATO

Se non trovi un URL affidabile: Nome – Descrizione | URL candidato o vuoto | DA_VERIFICARE
Priorità: siti ufficiali > App Store/Mac App Store > GitHub > video YouTube > articoli.
Per le app Apple di sistema (Comandi Rapidi, Spotlight, Mail, ecc.) usa la pagina di
supporto Apple ufficiale, oppure ometti il link se è una funzione nativa ovvia.
```

**Regole per la sezione Link finale (Fase 4):**
- Formato riga: `- [Nome – Descrizione breve](https://url-completo)`
- Link ad **altri episodi A2**: sempre `https://a2podcast.it/NN/` (con slash finale).
  MAI `a2podcast.fireside.fm` (vecchio dominio).
- Per URL incerti: includi con commento `<!-- DA VERIFICARE -->` a fine riga, così l'utente
  li controlla prima del commit.
- Nella sinossi usa link inline solo per URL `ESISTENTE` o `VERIFICATO`. Non linkare inline
  risorse `DA_VERIFICARE`; al massimo mettile nella sezione link con il commento.
- Se un link è già presente nelle note, usalo inline nella sinossi ma non aggiungerlo una
  seconda volta alla lista.
- Non inventare URL. Se non sei sicuro, marca DA_VERIFICARE.
