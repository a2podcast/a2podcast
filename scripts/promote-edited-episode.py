#!/usr/bin/env python3
"""
Promuove un episodio editato dalla cartella di lavorazione iCloud al sito Hugo A2.

Default: dry-run, nessuna scrittura. Usare --apply per copiare i file.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class PromoteError(Exception):
    pass


@dataclass(frozen=True)
class CopyPlan:
    label: str
    src: Path
    dst: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Promuove un episodio A2 editato nel sito Hugo."
    )
    parser.add_argument("--episode", required=True, type=int, help="Numero episodio, es. 78")
    parser.add_argument(
        "--source",
        required=True,
        type=Path,
        help="Cartella sorgente editata, es. .../A2/078",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Esegue davvero la copia. Senza questa opzione lo script è in dry-run.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Permette di sovrascrivere i due file target previsti.",
    )
    parser.add_argument(
        "--skip-tests",
        action="store_true",
        help="Dopo --apply salta build Hugo e test sito.",
    )
    return parser.parse_args()


def fail(message: str) -> None:
    raise PromoteError(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def extract_front_matter(markdown: str) -> tuple[str, str]:
    if not markdown.startswith("+++\n"):
        fail("index.md deve iniziare con front matter TOML delimitato da +++")
    end = markdown.find("\n+++", 4)
    if end == -1:
        fail("index.md non contiene il delimitatore finale +++ del front matter")
    body_start = end + len("\n+++\n")
    if len(markdown) < body_start:
        body_start = end + len("\n+++")
    return markdown[4:end], markdown[body_start:]


def validate_index(path: Path, episode: int) -> None:
    if not path.is_file():
        fail(f"index.md non trovato: {path}")

    markdown = read_text(path)
    front_matter, body = extract_front_matter(markdown)
    try:
        metadata = tomllib.loads(front_matter)
    except tomllib.TOMLDecodeError as exc:
        fail(f"front matter TOML non valido: {exc}")

    episode_number = metadata.get("episodeNumber")
    if episode_number != episode:
        fail(
            f"episodeNumber non coerente: CLI={episode}, front matter={episode_number!r}"
        )

    slug = metadata.get("slug")
    if slug != str(episode):
        fail(f'slug non coerente: atteso "{episode}", trovato {slug!r}')

    description = metadata.get("description")
    if description is None:
        fail("description mancante nel front matter")
    if not isinstance(description, str):
        fail("description deve essere una stringa TOML")
    if len(description) > 300:
        fail(f"description troppo lunga: {len(description)} caratteri (max 300)")

    in_code = False
    for line_no, line in enumerate(body.splitlines(), start=1):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if not in_code and line.startswith("# "):
            fail(f"H1 non consentito nel corpo di index.md alla riga corpo {line_no}")


def find_srt(source: Path, episode: int) -> Path:
    preferred = source / f"A2 ep. {episode}.srt"
    if preferred.is_file():
        return preferred

    matches = sorted(source.glob("*.srt"))
    if not matches:
        fail(f"SRT non trovato in {source}")
    if len(matches) > 1:
        names = ", ".join(path.name for path in matches)
        fail(f"più file SRT trovati; rinomina quello corretto come 'A2 ep. {episode}.srt': {names}")
    return matches[0]


def build_plan(source: Path, episode: int) -> list[CopyPlan]:
    index_src = source / "index.md"
    srt_src = find_srt(source, episode)
    validate_index(index_src, episode)

    episode_dir = PROJECT_ROOT / "content" / "episodi" / str(episode)
    return [
        CopyPlan("episodio", index_src, episode_dir / "index.md"),
        CopyPlan("trascrizione", srt_src, PROJECT_ROOT / "static" / "trascrizioni" / f"ep-{episode}.srt"),
    ]


def check_overwrites(plan: list[CopyPlan], force: bool) -> None:
    existing = [item.dst for item in plan if item.dst.exists()]
    if existing and not force:
        paths = "\n".join(f"  - {path.relative_to(PROJECT_ROOT)}" for path in existing)
        fail("file target già esistenti; usare --force per sovrascriverli:\n" + paths)


def print_plan(plan: list[CopyPlan], apply: bool, force: bool) -> None:
    mode = "APPLY" if apply else "DRY-RUN"
    print(f"{mode}: promozione episodio")
    if force:
        print("force: sovrascrittura consentita per i due file target previsti")
    for item in plan:
        rel = item.dst.relative_to(PROJECT_ROOT)
        print(f"  {item.label}: {item.src} -> {rel}")


def copy_files(plan: list[CopyPlan]) -> None:
    for item in plan:
        item.dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item.src, item.dst)
        print(f"copiato: {item.dst.relative_to(PROJECT_ROOT)}")


def command_exists(command: str) -> bool:
    return shutil.which(command) is not None


def run_checked(command: list[str]) -> tuple[bool, str]:
    proc = subprocess.run(
        command,
        cwd=PROJECT_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return proc.returncode == 0, proc.stdout


def run_post_apply_checks(skip_tests: bool) -> None:
    if skip_tests:
        print("verifica post-apply saltata (--skip-tests)")
        return
    if not command_exists("hugo"):
        fail("hugo non disponibile nel PATH: copia eseguita, build non verificata")

    print("eseguo: hugo --gc --minify")
    ok, output = run_checked(["hugo", "--gc", "--minify"])
    print(output, end="" if output.endswith("\n") else "\n")
    if not ok:
        fail("build Hugo fallita dopo la copia")

    test_script = PROJECT_ROOT / "scripts" / "test-site.py"
    if test_script.is_file():
        print("eseguo: python3 scripts/test-site.py --no-build")
        ok, output = run_checked(["python3", str(test_script), "--no-build"])
        print(output, end="" if output.endswith("\n") else "\n")
        if not ok:
            fail("test-site.py --no-build fallito dopo la build")
    else:
        print("test-site.py non trovato: eseguita solo la build Hugo")


def main() -> int:
    args = parse_args()
    source = args.source.expanduser().resolve()
    if not source.is_dir():
        fail(f"cartella sorgente non trovata: {source}")

    plan = build_plan(source, args.episode)
    check_overwrites(plan, args.force)
    print_plan(plan, args.apply, args.force)

    if not args.apply:
        print("nessuna scrittura eseguita; aggiungere --apply per copiare")
        return 0

    copy_files(plan)
    run_post_apply_checks(args.skip_tests)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PromoteError as exc:
        print(f"ERRORE: {exc}", file=sys.stderr)
        raise SystemExit(1)
