#!/usr/bin/env python3
"""Valida un registro local declarado; no certifica pedagogía ni ejecuta entregas."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def hash_archivo(ruta):
    return hashlib.sha256(Path(ruta).read_bytes()).hexdigest()


def validar_registro(ruta):
    ruta = Path(ruta).resolve()
    base = ruta.parent
    errores = []
    out = {"estado": "PENDIENTE", "errores": errores, "limite": "Valida integridad del registro declarado; no acredita su veracidad, revisión pedagógica ni entrega."}
    try:
        registro = json.loads(ruta.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errores.append(f"Registro no legible: {exc}")
        return out
    if not isinstance(registro, dict):
        errores.append("El registro debe ser un objeto JSON.")
        return out
    if type(registro.get("version")) is not int or registro.get("version") != 1:
        errores.append("Versión de esquema no admitida; se requiere 1.")
    for field in ("encargo", "alcance"):
        if not isinstance(registro.get(field), str) or not registro[field].strip():
            errores.append(f"Falta {field}.")

    def archivo(item, etiqueta):
        if not isinstance(item, dict) or not isinstance(item.get("ruta"), str) or not item["ruta"].strip():
            errores.append(f"{etiqueta}: falta ruta.")
            return
        raw = Path(item["ruta"])
        path = (base / raw).resolve()
        if raw.is_absolute() or not path.is_relative_to(base) or path == base:
            errores.append(f"{etiqueta}: ruta fuera del directorio del registro.")
            return
        try:
            digest = hash_archivo(path)
        except OSError:
            errores.append(f"{etiqueta}: archivo no disponible: {item['ruta']}.")
            return
        if not re.fullmatch(r"[a-f0-9]{64}", str(item.get("sha256", ""))) or digest != item.get("sha256"):
            errores.append(f"{etiqueta}: hash ausente o versión distinta: {item['ruta']}.")

    def lista(field):
        items = registro.get(field)
        if not isinstance(items, list) or not items:
            errores.append(f"{field}: se requiere una lista no vacía.")
            return []
        return items

    for field in ("fuentes", "artefactos"):
        for i, item in enumerate(lista(field)):
            archivo(item, f"{field}[{i}]")
            if field == "artefactos" and (not isinstance(item, dict) or not isinstance(item.get("destinatario"), str) or not item["destinatario"].strip()):
                errores.append(f"{field}[{i}]: falta destinatario.")
    criterios = lista("criterios")
    ids = set()
    for criterio in criterios:
        if not isinstance(criterio, dict):
            errores.append("Criterio no válido.")
            continue
        ident = criterio.get("id")
        if not isinstance(ident, str) or not ident.strip() or ident in ids:
            errores.append("Criterio con id vacío o duplicado.")
        elif ident:
            ids.add(ident)
        if not isinstance(criterio.get("resultado"), str) or criterio["resultado"] not in {"cumple", "no_aplica"}:
            errores.append(f"Criterio {ident}: no cumple o no verificado.")
        for field in ("fuente", "ubicacion", "razon"):
            if not isinstance(criterio.get(field), str) or not criterio[field].strip():
                errores.append(f"Criterio {ident}: falta {field}.")
        archivo(criterio.get("evidencia"), f"Evidencia de criterio {ident}")
    roles = registro.get("roles")
    if not isinstance(roles, dict):
        roles = {}
    for role in ("planeador", "constructor", "verificador", "evaluador"):
        if not isinstance(roles.get(role), str) or not roles[role].strip():
            errores.append(f"Rol {role}: falta identidad declarada.")
    independientes = [roles.get(r) for r in ("constructor", "verificador", "evaluador")]
    if any(not isinstance(x, str) or not x.strip() for x in independientes) or len(set(str(x).strip().casefold() for x in independientes)) != 3:
        errores.append("Falta independencia declarada entre constructor, verificador y evaluador.")
    vistos = set()
    for review in lista("revisiones"):
        if not isinstance(review, dict):
            errores.append("Revisión no válida.")
            continue
        role = review.get("rol")
        if not isinstance(role, str) or role not in {"verificador", "evaluador"} or role in vistos:
            errores.append("Revisión con rol no admitido o duplicado.")
            continue
        else:
            vistos.add(role)
        if not review.get("identidad") or review.get("identidad") != roles.get(role):
            errores.append("Revisión no coincide con identidad del rol.")
        if review.get("estado") != "completa":
            errores.append(f"Revisión {role}: pendiente.")
        archivo(review.get("evidencia"), f"Evidencia de revisión {role}")
    if vistos != {"verificador", "evaluador"}:
        errores.append("Faltan reportes de verificador y evaluador.")
    if not errores:
        out["estado"] = "REGISTRO_TECNICO_COMPLETO_NO_CERTIFICA_PEDAGOGIA"
    return out


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("registro", type=Path)
    args = cli.parse_args()
    out = validar_registro(args.registro)
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 2 if out["errores"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
