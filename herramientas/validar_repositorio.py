#!/usr/bin/env python3
"""Comprueba metadatos de skills y enlaces locales; no certifica contenido."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


EXCLUDED = {".git", "__pycache__", ".venv", "node_modules"}


def archivos_markdown(base):
    return sorted(p for p in base.rglob("*.md") if not EXCLUDED.intersection(p.relative_to(base).parts))


def validar(base):
    base = Path(base).resolve()
    errors = []
    docs = archivos_markdown(base)
    skills = []
    links = 0
    for path in docs:
        rel = path.relative_to(base).as_posix()
        try:
            body = path.read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{rel}: lectura fallida: {exc}")
            continue
        if not body.strip():
            errors.append(f"{rel}: documento vacío.")
        if path.name == "SKILL.md":
            skills.append(rel)
            front = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", body, re.S)
            if not front:
                errors.append(f"{rel}: falta frontmatter.")
            else:
                campos = dict(re.findall(r"^(name|description):\s*(.+)$", front.group(1), re.M))
                name = campos.get("name", "").strip().strip("\"'")
                description = campos.get("description", "").strip().strip("\"'")
                if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                    errors.append(f"{rel}: name inválido.")
                if not description or len(description) > 1024:
                    errors.append(f"{rel}: description ausente o demasiado larga.")
                if "[TODO" in body or "TODO: replace" in body:
                    errors.append(f"{rel}: plantilla de skill sin completar.")
        # Los bloques de código muestran comandos, no constituyen enlaces navegables.
        sin_codigo = re.sub(r"```.*?```", "", body, flags=re.S)
        for match in re.finditer(r"!?\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)(?:\s+[\"'][^)]*)?\)", sin_codigo):
            target = match.group(1).strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith("#"):
                continue
            local = unquote(parsed.path)
            if not local:
                continue
            links += 1
            resolved = (base / local.lstrip("/")) if local.startswith("/") else path.parent / local
            resolved = resolved.resolve()
            if not resolved.is_relative_to(base):
                errors.append(f"{rel}: enlace local sale del paquete: {target}")
            elif not resolved.exists():
                errors.append(f"{rel}: enlace local roto: {target}")
    if not skills:
        errors.append("No hay skills comprobables.")
    return {"estado": "ESTRUCTURA_TECNICA_COMPROBADA" if not errors else "ERRORES", "markdown": len(docs), "skills": len(skills), "enlaces_locales": links, "errores": errors, "limite": "No comprueba anclas, enlaces remotos, decisiones pedagógicas ni privacidad semántica."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("raiz", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    out = validar(args.raiz)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 2 if out["errores"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
