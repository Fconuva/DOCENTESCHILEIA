#!/usr/bin/env python3
"""Extrae a .txt el texto de los PDF oficiales, en orden de lectura y con marca de página.

Mantenimiento del paquete: requiere `pdftotext` (Poppler). Uso:
    python herramientas/extraer_texto_pdf.py marco_curricular/documentos_oficiales/*.pdf
Después de regenerar textos, rehacer el índice con generar_indice_oa.py.
"""
import subprocess, sys
from pathlib import Path

def extraer(pdf: Path) -> tuple[int, int]:
    crudo = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True, check=True).stdout.decode("utf-8", "replace")
    paginas = crudo.split("\f")
    if paginas and not paginas[-1].strip():
        paginas.pop()
    partes = [f"# Texto extraído de {pdf.name}\n",
              "# Extracción automática en orden de lectura (pdftotext); cada bloque indica la página del PDF.\n",
              "# Sirve para buscar y citar. Tablas, columnas y títulos de eje pueden quedar desplazados:\n",
              "# ante cualquier duda manda el PDF oficial del mismo nombre.\n\n"]
    con_texto = 0
    for n, texto in enumerate(paginas, 1):
        lineas = [l.rstrip() for l in texto.replace("\r", "").split("\n")]
        while lineas and not lineas[-1]:
            lineas.pop()
        cuerpo = "\n".join(lineas).strip("\n")
        if cuerpo.strip():
            con_texto += 1
        partes.append(f"[página {n} del PDF]\n{cuerpo}\n\n")
    pdf.with_suffix(".txt").write_text("".join(partes), encoding="utf-8", newline="\n")
    return len(paginas), con_texto

for ruta in sys.argv[1:]:
    p = Path(ruta)
    total, con = extraer(p)
    print(f"{p.name}: {total} páginas, {con} con texto, {p.with_suffix('.txt').stat().st_size} bytes")
