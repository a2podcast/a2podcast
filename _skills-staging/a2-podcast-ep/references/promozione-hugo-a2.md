# Fase 6 — Promozione nel sito Hugo

Questa fase serve solo quando la cartella episodio grezza/editata è stata revisionata e l'utente
ha dato un OK esplicito alla promozione nel sito Hugo.

## Regola principale

Non copiare mai manualmente file nel repo Hugo e non rilanciare `scripts/ingest.py` per promuovere
un episodio già arricchito: `ingest.py` rigenera il corpo da RSS/note e può sovrascrivere la sinossi.
Usare invece lo script versionato:

```bash
python3 scripts/promote-edited-episode.py --episode NN --source "/percorso/cartella/NNN"
python3 scripts/promote-edited-episode.py --episode NN --source "/percorso/cartella/NNN" --apply
```

Il primo comando è sempre dry-run e non scrive nulla. Il secondo copia solo dopo conferma esplicita
tramite `--apply`.

## Cosa copia

- `SOURCE/index.md` -> `content/episodi/NN/index.md`
- `SOURCE/A2 ep. NN.srt` oppure l'unico `SOURCE/*.srt` -> `static/trascrizioni/ep-NN.srt`
- Il CSV capitoli resta nella cartella sorgente: serve per inserirlo nell'MP3, non per il sito.

Non copia MP3/WAV/ZIP/JSON/VTT/TXT e non pubblica nulla su Spreaker.

## Protezioni

Lo script valida prima della copia:

- front matter TOML delimitato da `+++`;
- `episodeNumber` coerente con `--episode`;
- `slug = "NN"`;
- `description` entro 300 caratteri;
- nessun H1 (`# `) nel corpo;
- SRT presente;

Se i file target esistono già, lo script si ferma. Usare `--force` solo quando l'utente ha chiesto
esplicitamente di sovrascrivere i due file previsti.

## Dopo `--apply`

Lo script esegue `hugo --gc --minify` e poi, se disponibile, `python3 scripts/test-site.py --no-build`.
Non fa commit, push o deploy: dopo la verifica, l'utente decide quando committare.
