#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
validar_material_docente.py
===========================
Auditor y validador de calidad para instrumentos y guías pedagógicas en HTML
diseñadas para el sistema escolar chileno y preparación PAES / SIMCE.

Parte de DOCENTES CHILE IA (github.com/Fconuva/DOCENTESCHILEIA).
Sin dependencias externas (utiliza la biblioteca estándar de Python).

Reglas que verifica:
1. Membrete Institucional (datos de institución y docente).
2. Metadatos de Estudiante y Evaluación (Nombre, Curso, Fecha, Puntaje/Escala 60%).
3. Redacción del Objetivo de Clase (Fórmula canónica de 4 componentes).
4. Formato de Selección Múltiple (4 alternativas A-D, nunca 5; control anti-adivinación).
5. Espacios de Respuesta en Preguntas de Desarrollo (.dev-lines / .ln).
6. Configuración de Impresión A4 (@page, .sheet, break-inside: avoid).
"""

import sys
import re
import argparse
from pathlib import Path
from html.parser import HTMLParser

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


class AnalizadorHTMLGuia(HTMLParser):
    def __init__(self):
        super().__init__()
        self.imagenes = []
        self.clases = set()
        self.textos = []
        self.en_style = False
        self.estilos = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == "img":
            src = attrs_dict.get("src", "")
            if src:
                self.imagenes.append(src)
        if "class" in attrs_dict:
            for c in attrs_dict["class"].split():
                self.clases.add(c)
        if tag == "style":
            self.en_style = True

    def handle_endtag(self, tag):
        if tag == "style":
            self.en_style = False

    def handle_data(self, data):
        if self.en_style:
            self.estilos.append(data)
        else:
            self.textos.append(data)


def auditar_guia_html(ruta_archivo: Path) -> dict:
    hallazgos = {
        "archivo": str(ruta_archivo),
        "errores": [],
        "advertencias": [],
        "exitos": [],
        "estadisticas": {}
    }

    if not ruta_archivo.exists():
        hallazgos["errores"].append(f"El archivo no existe: {ruta_archivo}")
        return hallazgos

    contenido = ruta_archivo.read_text(encoding="utf-8", errors="replace")
    parser = AnalizadorHTMLGuia()
    parser.feed(contenido)

    texto_total = " ".join(parser.textos)
    estilos_totales = " ".join(parser.estilos)

    # 1. Membrete Institucional
    tiene_membrete = any(c in parser.clases for c in ["header-tbl", "inst-header-table", "membrete-banner", "inst-info", "header-banner"]) or bool(re.search(r"colegio|liceo|escuela|instituto|educativo", texto_total, re.IGNORECASE))
    if tiene_membrete:
        hallazgos["exitos"].append("Membrete: Estructura de cabecera institucional identificada.")
    else:
        hallazgos["advertencias"].append("Membrete: Verifique que la cabecera contenga los datos del establecimiento educativo.")

    # 2. Metadatos de Estudiante y Evaluación
    tiene_nombre = bool(re.search(r"Nombre|Estudiante|Alumno", texto_total, re.IGNORECASE))
    tiene_curso = bool(re.search(r"Curso|Nivel|Básico|Medio|1°|2°|3°|4°|5°|6°|7°|8°", texto_total, re.IGNORECASE))
    tiene_fecha = bool(re.search(r"Fecha", texto_total, re.IGNORECASE))
    tiene_puntaje = bool(re.search(r"Puntaje|Pts|Nota|Calificación|Nivel de Logro", texto_total, re.IGNORECASE))

    if tiene_nombre and tiene_curso:
        hallazgos["exitos"].append("Metadatos: Campos de identificación del estudiante presentes (Nombre, Curso).")
    else:
        hallazgos["advertencias"].append("Metadatos: Faltan campos explícitos de Nombre y Curso del estudiante.")

    if tiene_puntaje:
        hallazgos["exitos"].append("Evaluación: Campos de puntaje y calificación presentes (Escala 60%).")
    else:
        hallazgos["advertencias"].append("Evaluación: No se detectó casilla de puntaje o calificación.")

    # 3. Objetivo de Clase / Guía (Fórmula canónica de 4 partes)
    # VERBO EN INFINITIVO + CONTENIDO + CONDICIÓN + HABILIDAD
    verbos_infinitivo = [
        "analizar", "comprender", "identificar", "evaluar", "reflexionar",
        "interpretar", "comparar", "sintetizar", "explicar", "producir",
        "redactar", "reconocer", "caracterizar", "diferenciar", "relacionar",
        "modelar", "resolver", "diseñar", "aplicar", "describir"
    ]
    conectores_condicion = ["mediante", "a través de", "con el uso", "a partir de", "mediante la", "a traves de", "con apoyo de"]

    tiene_verbo = any(re.search(rf"\b{v}\b", texto_total, re.IGNORECASE) for v in verbos_infinitivo)
    tiene_condicion = any(re.search(rf"\b{c}\b", texto_total, re.IGNORECASE) for c in conectores_condicion)

    if tiene_verbo and tiene_condicion:
        hallazgos["exitos"].append("Objetivo Pedagógico: Cumple estructura canónica (Verbo en infinitivo + Condición metodológica).")
    else:
        detalles_obj = []
        if not tiene_verbo:
            detalles_obj.append("verbo en infinitivo observable")
        if not tiene_condicion:
            detalles_obj.append("condición (ej: 'mediante...', 'a través de...')")
        hallazgos["advertencias"].append(f"Objetivo Pedagógico: Podría faltar {' o '.join(detalles_obj)} en la formulación de 4 partes.")

    # 4. Alternativas de Selección Múltiple
    # Buscar opciones E)
    opciones_e = re.findall(r"\b[eE][\)\.\-–]\s+[A-Za-z0-9]", texto_total)
    if opciones_e:
        hallazgos["errores"].append(f"Formato Reactivos: Se encontraron {len(opciones_e)} opciones 'E)'. Las pruebas DEMRE (PAES/SIMCE) vigentes son estrictamente A-D (4 opciones).")
    else:
        hallazgos["exitos"].append("Formato Reactivos: Sin opciones E (cumple estándar DEMRE de 4 alternativas A-D).")

    preguntas_bloque = re.findall(r"[A-Da-d][\)\.\-–]\s*([^\n\r]+)", contenido)
    if len(preguntas_bloque) >= 4:
        hallazgos["estadisticas"]["alternativas_detectadas"] = len(preguntas_bloque)
        hallazgos["exitos"].append(f"Reactivos: Detectadas al menos {len(preguntas_bloque)} alternativas de selección múltiple.")

    # 5. Preguntas de Desarrollo y Espacio de Respuesta
    tiene_dev_lines = any(c in parser.clases for c in ["dev-lines", "ln", "write-line", "writing-box", "renglones", "lineas-respuesta"])
    if tiene_dev_lines or ".ln" in estilos_totales or "dev-lines" in estilos_totales:
        hallazgos["exitos"].append("Desarrollo: Renglones pautados presentes (.dev-lines / .ln).")
    else:
        pide_desarrollo = bool(re.search(r"\b(explica|fundamenta|justifica|redacta|argumenta|evalúa)\b", texto_total, re.IGNORECASE))
        if pide_desarrollo:
            hallazgos["advertencias"].append("Desarrollo: Hay preguntas de desarrollo pero no se detectaron clases de renglones (.dev-lines / .ln).")

    # 6. Configuración de Impresión A4
    tiene_page_a4 = bool(re.search(r"@page\s*\{[^}]*A4", estilos_totales, re.IGNORECASE)) or "@page" in estilos_totales
    tiene_sheet = "sheet" in parser.clases or ".sheet" in estilos_totales
    tiene_break_avoid = "break-inside: avoid" in estilos_totales or "page-break-inside: avoid" in estilos_totales

    if tiene_page_a4 and tiene_sheet:
        hallazgos["exitos"].append("Impresión: Configuración A4 definida (@page y contenedor .sheet).")
    else:
        hallazgos["advertencias"].append("Impresión: Se recomienda incluir '@page { size: A4 portrait; margin: 7mm 8mm; }' y contenedor .sheet.")

    if tiene_break_avoid:
        hallazgos["exitos"].append("Impresión: Reglas de protección de corte activas (break-inside: avoid).")
    else:
        hallazgos["advertencias"].append("Impresión: Falta 'break-inside: avoid' para evitar corte de preguntas entre páginas.")

    return hallazgos


def imprimir_reporte(hallazgos: dict) -> int:
    print("\n" + "=" * 78)
    print(f"  AUDITORÍA DOCENTES CHILE IA: {Path(hallazgos['archivo']).name}")
    print("=" * 78)

    if hallazgos["exitos"]:
        print("\n  [OK] CRITERIOS CUMPLIDOS:")
        for ex in hallazgos["exitos"]:
            print(f"       + {ex}")

    if hallazgos["advertencias"]:
        print("\n  [!] ADVERTENCIAS / RECOMENDACIONES:")
        for adv in hallazgos["advertencias"]:
            print(f"       * {adv}")

    if hallazgos["errores"]:
        print("\n  [X] ERRORES CRÍTICOS:")
        for err in hallazgos["errores"]:
            print(f"       ! {err}")
        print("\n" + "-" * 78)
        print("  RESULTADO: REPROBADO (Corrija los errores antes de imprimir/publicar)")
        print("-" * 78 + "\n")
        return 1

    print("\n" + "-" * 78)
    print("  RESULTADO: APROBADO CON ÉXITO")
    print("-" * 78 + "\n")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Auditar calidad de material didáctico escolar en HTML.")
    parser.add_argument("archivo", help="Ruta al archivo HTML de la guía, evaluación o planificación.")
    args = parser.parse_args()

    ruta = Path(args.archivo)
    hallazgos = auditar_guia_html(ruta)
    codigo_salida = imprimir_reporte(hallazgos)
    sys.exit(codigo_salida)


if __name__ == "__main__":
    main()

