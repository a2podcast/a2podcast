# Skill: a2-podcast-ep — staging per revisione

Skill per arricchire le pagine episodio di A2 con **sinossi + link** a partire dalla
trascrizione SRT. In staging qui (`_skills-staging/`) per revisione e test prima dell'attivazione.

Il prefisso `_` fa sì che Hugo ignori questa cartella in build.

## Struttura

```
a2-podcast-ep/
├── SKILL.md                          # manifest + flusso (name, description, fasi)
├── README.md                         # questo file
└── references/
    ├── correzione-srt-a2.md          # Fase 1: glossario correzione SRT (temi Apple/A2)
    ├── ricerca-link.md               # Fase 2: ricerca URL cose citate
    ├── sinossi-a2.md                 # Fase 3: come scrivere la sinossi (2 conduttori)
    ├── tags-a2.md                    # Fase 4: convenzione tag A2 (kebab-case)
    └── merge-episodio-a2.md          # Fase 4: merge nell'index.md esistente
```

## Compatibilità Claude Code + Codex

Il formato `SKILL.md` (frontmatter YAML `name` + `description`, corpo markdown, `references/`)
è **identico** per i due agenti. Cambia solo la cartella di discovery:

| Agente | Cartella skill di repo | Cartella skill personali |
|--------|------------------------|--------------------------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| OpenAI Codex | `.agents/skills/` | `~/.agents/skills/` |

## Come attivarla dopo la revisione

Scegli una delle due (o entrambe). Esempi dalla root del repo:

**Per Claude Code:**
```bash
mkdir -p .claude/skills
cp -R _skills-staging/a2-podcast-ep .claude/skills/
```

**Per Codex:**
```bash
mkdir -p .agents/skills
cp -R _skills-staging/a2-podcast-ep .agents/skills/
```

In alternativa, per non duplicare, puoi usare un symlink:
```bash
ln -s ../../_skills-staging/a2-podcast-ep .claude/skills/a2-podcast-ep
```

Dopo aver copiato/linkato, riavvia l'agente (o apri una nuova chat) per caricare la skill.

## Come testarla

1. Scegli un episodio con SRT e (idealmente) ospite + youtubeId, es. **74**.
2. Invoca la skill: in Claude `/a2-podcast-ep` o chiedi "elabora l'episodio 74 di A2";
   in Codex `$a2-podcast-ep` o `/skills`.
3. Segui i checkpoint. Alla fine verifica:
   - `hugo --gc --minify` builda senza errori;
   - la pagina `/74/` ha un solo `<h1>`;
   - sinossi e link nuovi sono presenti, le note originali intatte.

## Note di manutenzione

- La sinossi vive **solo** nell'`index.md`. NON rilanciare `ingest.py` su un episodio già
  arricchito: rigenererebbe il corpo dai file note cancellando la sinossi (vedi
  `references/merge-episodio-a2.md`).
- Glossario e tag sono basati sugli episodi reali di A2 al momento della creazione: aggiornali
  quando emergono nuovi prodotti/temi ricorrenti.
