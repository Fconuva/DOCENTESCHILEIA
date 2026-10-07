#!/usr/bin/env python3
"""Comprobación técnica parcial de HTML. No emite aprobación pedagógica."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class AnalizadorHTMLGuia(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.textos = []
        self.estilos = []
        self.clases = set()
        self.reactivos = []
        self.imagenes = []
        self.css_externo = False
        self.objetivo = False
        self.plantilla = False
        self.estructura_invalida = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "data-plantilla" in attrs:
            self.plantilla = True
        hidden = any(n[1] for n in self.stack) or tag in {"script", "style", "template"} or "hidden" in attrs
        question = next((n[2] for n in reversed(self.stack) if n[2] is not None), None)
        if "data-reactivo" in attrs:
            if question is not None:
                self.estructura_invalida = True
            question = {"id": attrs["data-reactivo"], "cantidad": attrs.get("data-opciones"), "opciones": [], "clave": attrs.get("data-clave")}
            self.reactivos.append(question)
        if not hidden:
            self.clases.update(attrs.get("class", "").split())
            if "data-objetivo" in attrs:
                self.objetivo = True
            if tag == "img" and attrs.get("src"):
                self.imagenes.append(attrs["src"])
            if "data-opcion" in attrs and question is not None:
                question["opciones"].append(attrs["data-opcion"])
        if tag == "link" and "stylesheet" in attrs.get("rel", "").split():
            self.css_externo = True
        if tag not in VOID:
            self.stack.append((tag, hidden, question))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                if index != len(self.stack) - 1:
                    self.estructura_invalida = True
                del self.stack[index:]
                return

    def handle_data(self, data):
        if any(n[0] == "style" for n in self.stack):
            self.estilos.append(data)
        elif not any(n[1] for n in self.stack):
            self.textos.append(data)


def auditar_guia_html(ruta_archivo):
    ruta = Path(ruta_archivo)
    out = {"archivo": str(ruta), "estado": "COMPROBACION_TECNICA_PARCIAL", "errores": [], "advertencias": [], "comprobaciones": [], "no_verificado": ["Coherencia pedagógica, exactitud, pauta y fuente", "Renderizado, impresión física y lectura OMR"], "estadisticas": {}}
    try:
        contenido = ruta.read_text(encoding="utf-8-sig")
    except (OSError, UnicodeError) as exc:
        out["errores"].append(f"No se pudo leer el HTML: {exc}")
        return out
    parser = AnalizadorHTMLGuia()
    parser.feed(contenido)
    parser.close()
    texto = " ".join(parser.textos)
    if parser.plantilla:
        out["advertencias"].append("Modelo editable: completar y revisar campos, textos, pauta y recursos antes de usar como material final.")
    css = re.sub(r"/\*.*?\*/", "", " ".join(parser.estilos), flags=re.S)
    if not texto.strip():
        out["errores"].append("El cuerpo no contiene texto visible comprobable.")
    if parser.estructura_invalida or parser.stack:
        out["errores"].append("Estructura incompleta o anidamiento incompatible con la comprobación; revisar HTML.")
    if parser.objetivo:
        out["comprobaciones"].append("Existe un elemento marcado data-objetivo; su contenido exige revisión.")
    else:
        out["no_verificado"].append("Objetivo sin marca data-objetivo; no se infiere de verbos sueltos.")
    if re.search(r"@page(?:\s+[^\{]+)?\s*\{[^}]*\bsize\s*:\s*A4\b", css, flags=re.I):
        out["comprobaciones"].append("Se declara tamaño A4 en CSS interno; falta verificar el PDF.")
    else:
        out["advertencias"].append("No se comprobó declaración size: A4 en CSS interno.")
    if parser.css_externo:
        out["no_verificado"].append("Hojas de estilo externas: contenido y disponibilidad no inspeccionados.")
    espacios = parser.clases.intersection({"dev-lines", "ln", "write-line", "writing-box", "renglones", "lineas-respuesta"})
    if espacios:
        out["comprobaciones"].append("Hay elementos de espacio de respuesta en el cuerpo; dimensiones y suficiencia requieren revisión.")
    else:
        out["no_verificado"].append("No se detectaron elementos de espacio de respuesta; CSS aislado no demuestra su presencia.")
    ids = set()
    for item in parser.reactivos:
        identidad = item["id"]
        if not identidad or identidad in ids:
            out["errores"].append(f"Identificador de reactivo vacío o duplicado: {identidad!r}.")
        ids.add(identidad)
        try:
            cantidad = int(item["cantidad"])
            if not 2 <= cantidad <= 5:
                raise ValueError
        except (TypeError, ValueError):
            out["errores"].append(f"Reactivo {identidad}: declarar data-opciones entre 2 y 5 según perfil verificado.")
            continue
        esperadas = list("ABCDE"[:cantidad])
        opciones = item["opciones"]
        if len(opciones) != cantidad or sorted(opciones) != esperadas:
            out["errores"].append(f"Reactivo {identidad}: opciones {opciones!r}; se declararon {cantidad} ({esperadas!r}).")
        if item["clave"] is not None and item["clave"] not in opciones:
            out["errores"].append(f"Reactivo {identidad}: clave fuera de las opciones declaradas.")
        if item["clave"] is not None:
            out["advertencias"].append(f"Reactivo {identidad}: contiene clave en el HTML; retirar de la versión de estudiante en un ensayo cerrado.")
    out["estadisticas"]["reactivos_marcados"] = len(parser.reactivos)
    if not parser.reactivos:
        out["no_verificado"].append("Sin reactivos marcados: no se comprobó cantidad, alternativas ni claves.")
    for src in parser.imagenes:
        if src.startswith(("https://", "http://", "data:", "//")):
            out["no_verificado"].append("Imagen remota o embebida: legibilidad y disponibilidad requieren revisión.")
        elif not (ruta.parent / src.split("#")[0].split("?")[0]).is_file():
            out["errores"].append(f"Imagen local ausente: {src}")
    return out


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("archivo", type=Path)
    cli.add_argument("--json", action="store_true")
    args = cli.parse_args()
    out = auditar_guia_html(args.archivo)
    if args.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        print(out["estado"])
        for group in ("errores", "advertencias", "comprobaciones", "no_verificado"):
            for item in out[group]:
                print(f"{group}: {item}")
    return 2 if out["errores"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
