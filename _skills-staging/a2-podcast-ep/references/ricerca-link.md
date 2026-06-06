# Fase 2 — Ricerca link delle cose citate

Obiettivo: raccogliere gli URL ufficiali di prodotti/app/persone/risorse citati nell'episodio,
per la sezione `## Link` e per i link inline della sinossi.

**Priorità delle fonti:**
1. Link **già presenti nelle note** dell'index.md (verificati dai conduttori) — massima priorità,
   NON duplicarli né sostituirli.
2. URL espliciti citati nell'SRT (anche detti a voce).
3. URL ufficiali noti per prodotti/servizi menzionati.

**Delega (se disponibile):** passa questo prompt a un sub-agente con accesso web
(Claude: Haiku + WebSearch; Codex: passo con ricerca). Altrimenti esegui tu la ricerca.

```
Sei un ricercatore. Dall'analisi di questa trascrizione del podcast A2 (tecnologia Apple,
produttività) sono stati citati i seguenti prodotti/app/servizi/persone/risorse:

[LISTA estratta dalla Fase 1]

Per ciascuno trova l'URL ufficiale più pertinente. Formato output, una riga per risorsa:
Nome – Descrizione contestuale breve | URL

Se non trovi un URL affidabile: Nome – Descrizione | DA_VERIFICARE
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
- Non inventare URL. Se non sei sicuro, marca DA_VERIFICARE.
