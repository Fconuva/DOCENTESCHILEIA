#!/usr/bin/env python3
"""Instala la biblioteca pública completa. Simulación por defecto; no modifica hooks."""
import argparse
import json
import shutil
import uuid
from pathlib import Path


ROOT_FILES = {"SKILL.md", "README.md", "AGENTS.md", "CLAUDE.md", "LICENSE"}
ROOT_DIRS = {".github", ".agent", "conocimiento", "guias_metodologicas", "herramientas", "ejemplos", "tests", "documentos_modelo", "dossiers_pedagogicos", "marco_curricular", "recursos_paes_simce", "temarios_evaluacion_docente_2026"}


def archivos_paquete(origen):
    origen = Path(origen).resolve()
    result = []
    for path in sorted(origen.rglob("*")):
        rel = path.relative_to(origen)
        if rel.parts[0] not in ROOT_DIRS and rel.as_posix() not in ROOT_FILES:
            continue
        if any(part in {".git", "__pycache__", ".venv"} for part in rel.parts):
            continue
        if ".local." in path.name or path.name.startswith(".env") or path.suffix not in {".md", ".html", ".py", ".pdf", ".txt", ".json", ".yaml", ".yml"} and rel.as_posix() not in ROOT_FILES:
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(origen):
            raise ValueError(f"No se admiten enlaces simbólicos ni rutas externas: {rel}")
        if path.is_file():
            result.append(rel)
    if Path("SKILL.md") not in result:
        raise ValueError("No existe SKILL.md raíz en el paquete.")
    return result


def instalar(origen, destino, aplicar=False):
    origen = Path(origen).resolve()
    destino = Path(destino).expanduser().resolve()
    if destino == origen or destino.is_relative_to(origen):
        raise ValueError("El destino no puede estar dentro del paquete de origen.")
    if destino.exists():
        raise FileExistsError("El destino ya existe; se conserva íntegro. Elegir otro destino o revisar la actualización manualmente.")
    files = archivos_paquete(origen)
    report = {"modo": "aplicado" if aplicar else "simulacion", "destino": str(destino), "archivos": len(files), "bytes": sum((origen / p).stat().st_size for p in files), "limite": "Copia una skill con referencias; no configura MCP, hooks, cuentas ni acciones externas."}
    if not aplicar:
        return report
    destino.parent.mkdir(parents=True, exist_ok=True)
    temporal = destino.parent / (".docentes-chile-ia-install-" + uuid.uuid4().hex)
    temporal.mkdir()
    try:
        for rel in files:
            target = temporal / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(origen / rel, target)
        if destino.exists():
            raise FileExistsError("El destino fue creado durante la instalación; no se sobrescribe.")
        temporal.rename(destino)
    except BaseException:
        # Única eliminación: staging propio comprobado dentro del padre del destino.
        if temporal.exists() and temporal.resolve().parent == destino.parent.resolve() and temporal.name.startswith(".docentes-chile-ia-install-"):
            shutil.rmtree(temporal)
        raise
    return report


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--cliente", choices=("codex", "claude"), required=True)
    cli.add_argument("--destino", type=Path)
    cli.add_argument("--aplicar", action="store_true")
    args = cli.parse_args()
    origen = Path(__file__).resolve().parents[1]
    destino = args.destino or Path.home() / (".codex" if args.cliente == "codex" else ".claude") / "skills" / "docentes-chile-ia"
    try:
        report = instalar(origen, destino, args.aplicar)
    except (OSError, ValueError) as exc:
        print(json.dumps({"estado": "NO_INSTALADO", "error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
