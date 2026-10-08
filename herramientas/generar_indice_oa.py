#!/usr/bin/env python3
"""Genera marco_curricular/INDICE_DE_OA.md: dónde empiezan los OA de cada asignatura y curso.

Mantenimiento del paquete. Uso, desde la raíz:
    python herramientas/generar_indice_oa.py .
Lee los .txt de marco_curricular/documentos_oficiales/ y no usa red.
"""
import re
import sys
from pathlib import Path

base = Path(sys.argv[1])
DOCS = base / "marco_curricular" / "documentos_oficiales"
PAG = re.compile(r"^\[página (\d+) del PDF\]$")


def cargar(nombre):
    return (DOCS / nombre).read_text(encoding="utf-8").split("\n")


def pagina_de(lineas, i):
    for j in range(i, -1, -1):
        m = PAG.match(lineas[j])
        if m:
            return int(m.group(1))
    return None


def previas(lineas, i, n):
    """Últimas n líneas con texto antes de i, de la más cercana a la más lejana."""
    out = []
    j = i - 1
    while j >= 0 and len(out) < n:
        if lineas[j].strip():
            out.append((j, lineas[j].strip()))
        j -= 1
    return out


secciones = []  # (titulo_seccion, [(asignatura, curso, pagina, linea)])
avisos = []

# --- 1.° a 6.° básico ---
doc16 = "Bases_Curriculares_1_a_6_Basico.txt"
L = cargar(doc16)
ASIG16 = ["Artes Visuales", "Ciencias Naturales", "Educación Física y Salud",
          "Historia, Geografía y Ciencias Sociales", "Idioma Extranjero Inglés",
          "Lenguaje y Comunicación", "Matemática", "Música", "Orientación", "Tecnología"]
PALABRA = {"Primero": 1, "Segundo": 2, "Tercero": 3, "Cuarto": 4, "Quinto": 5, "Sexto": 6}
vistos = {}
for i, linea in enumerate(L):
    if linea.strip() != "Objetivos de Aprendizaje" or i < 800:
        continue
    prev = previas(L, i, 4)
    curso = asig = None
    for _, texto in prev:
        m = re.fullmatch(r"([1-6])º básico", texto)
        if m and curso is None:
            curso = int(m.group(1))
        m = re.fullmatch(r"(Primero|Segundo|Tercero|Cuarto|Quinto|Sexto) Básico", texto)
        if m and curso is None:
            curso = PALABRA[m.group(1)]
        if texto in ASIG16 and asig is None:
            asig = texto
    if curso is None:
        continue
    if asig is None:  # la asignatura aparece como encabezado de la página siguiente
        for j in range(i, min(i + 120, len(L) - 2)):
            if L[j].strip() in ASIG16:
                asig = L[j].strip()
                break
    if asig is None:
        avisos.append(f"1-6 básico: sin asignatura en línea {i + 1}")
        continue
    vistos.setdefault((asig, curso), (asig, f"{curso}.° básico", pagina_de(L, i), i + 1))
filas16 = sorted(vistos.values(), key=lambda f: (f[0], f[3]))
secciones.append((doc16, "1.° a 6.° básico", filas16))

# --- 7.° básico a 2.° medio ---
doc72 = "Bases_Curriculares_7_Basico_a_2_Medio.txt"
L = cargar(doc72)
cab = re.compile(r"\| 7° básico a 2° medio \| (.+?)\s*$")
titulo = re.compile(r"^(Séptimo básico|Octavo básico|Primero medio|Segundo medio)(?: \d+)?$")
filas72 = []
for i, linea in enumerate(L):
    m = titulo.match(linea)
    if not m:
        continue
    asig = None
    for d in range(1, 15):
        for j in (i - d, i + d):
            if 0 <= j < len(L):
                c = cab.search(L[j])
                if c and c.group(1) != "Introducción":
                    asig = c.group(1)
                    break
        if asig:
            break
    if asig and asig.startswith("Idioma Extranjero"):
        asig = "Idioma Extranjero: Inglés"
    if not asig or "Objetivos de Aprendizaje" not in "\n".join(L[i:i + 30]):
        avisos.append(f"7-2M: revisar línea {i + 1} ({asig})")
        continue
    filas72.append((asig, m.group(1), pagina_de(L, i), i + 1))
filas72.sort(key=lambda f: (f[0], f[3]))
secciones.append((doc72, "7.° básico a 2.° medio", filas72))

# --- 3.° y 4.° medio: inicio de cada página de OA, con su área y primer título ---
doc34 = "Bases_Curriculares_3_y_4_Medio.txt"
L = cargar(doc34)
filas34 = []
for i, linea in enumerate(L):
    if linea.strip() != "Objetivos de Aprendizaje" or i < 1000:
        continue
    prev = previas(L, i, 2)
    if len(prev) < 2 or not PAG.match(prev[1][1]):
        continue  # solo los que abren página: [página N] / Área / Objetivos de Aprendizaje
    area = prev[0][1]
    detalle = ""
    for j in range(i + 1, min(i + 9, len(L))):
        t = L[j].strip()
        if not t or t.isdigit() or t == "Objetivos de Aprendizaje" or PAG.match(t) or "Bases Curriculares" in t:
            continue
        detalle = t if len(t) <= 70 else "Introducción a los objetivos de la asignatura"
        break
    filas34.append((area, detalle or "Introducción a los objetivos de la asignatura", pagina_de(L, i), i + 1))
secciones.append((doc34, "3.° y 4.° medio", filas34))

out = ["# Índice de OA: dónde empieza cada asignatura y curso", "",
       "Tabla generada automáticamente desde los textos de",
       "[documentos_oficiales](documentos_oficiales/). Indica la línea del archivo `.txt`",
       "y la página del PDF donde empieza la lista de Objetivos de Aprendizaje. Sirve",
       "para abrir directamente ese tramo, sin buscar ni usar la terminal.", "",
       "Uso: abrir el `.txt` indicado desde la línea señalada y leer unas 150 líneas, o",
       "hasta que empiece el curso siguiente. La lista de un curso puede seguir en las",
       "páginas siguientes. Confirmar que el encabezado de página nombra la asignatura",
       "buscada. Si algo no calza, manda el PDF.", ""]
for doc, nombre, filas in secciones:
    out += [f"## {nombre}", "", f"Archivo: `marco_curricular/documentos_oficiales/{doc}`", ""]
    if doc == doc34:
        out += ["En 3.° y 4.° medio muchas asignaturas presentan sus objetivos para «3.° o 4.°",
                "medio» y hay electivos. Cada fila es una página donde empiezan o continúan",
                "objetivos; la segunda columna es el primer título que aparece en ella.", "",
                "| Área o asignatura | Primer título de la página | Página del PDF | Línea del .txt |",
                "|---|---|---:|---:|"]
    else:
        out += ["| Asignatura | Curso | Página del PDF | Línea del .txt |", "|---|---|---:|---:|"]
    out += [f"| {a} | {b} | {p} | {l} |" for a, b, p, l in filas]
    out.append("")
out += ["## Lo que este índice no cubre", "",
        "- Educación Parvularia, Formación Diferenciada Técnico-Profesional, Educación",
        "  de Personas Jóvenes y Adultas y Lengua y Cultura de los Pueblos Originarios:",
        "  se busca en su archivo por núcleo, módulo, nivel o eje.",
        "- Los Objetivos de Aprendizaje Transversales y la introducción de cada",
        "  asignatura (enfoque, ejes, habilidades y actitudes) están antes de las",
        "  listas por curso.", ""]
(base / "marco_curricular" / "INDICE_DE_OA.md").write_text("\n".join(out), encoding="utf-8", newline="\n")
for doc, nombre, filas in secciones:
    print(f"{nombre}: {len(filas)} entradas")
for aviso in avisos:
    print("REVISAR:", aviso)
raise SystemExit(2 if avisos else 0)
