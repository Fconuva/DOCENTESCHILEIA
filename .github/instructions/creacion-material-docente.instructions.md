---
description: "Regla obligatoria para la creación de guías, evaluaciones y planificaciones escolares en el sistema educativo chileno."
name: "Creación de Material Docente Chile"
applyTo: ["**/*.html", "**/*.md", "herramientas/**", ".github/skills/**"]
---

# Regla de Workspace — Creación de Material Docente (Chile)

Esta instrucción rige toda elaboración de guías de trabajo, evaluaciones, planificaciones y pautas docentes en DOCENTES CHILE IA. Fuente canónica: `.github/skills/creacion-material-docente/SKILL.md`.

## Reglas Obligatorias:

1. **Membrete Escolar**: Toda guía imprimible debe contener cabecera con los datos del establecimiento escolar, asignatura, curso y docente.
2. **Formulación Canónica del Objetivo**:
   `VERBO EN INFINITIVO + CONTENIDO + CONDICIÓN + HABILIDAD TRANSVERSAL`.
3. **Estándar DEMRE de Selección Múltiple**:
   - Exactamente **4 alternativas (A–D)**. Rigurosamente prohibida la opción E.
   - Regla anti-adivinación: la clave **nunca** es la opción más larga en caracteres.
   - Distractores con falla técnica fundamentada (cambio de foco, sobregeneralización, literalización forzada, invención plausible o contradicción).
4. **Espacios de Respuesta para Desarrollo**:
   - Toda pregunta abierta debe incluir renglones de respuesta `.dev-lines` con líneas `.ln` de al menos 22-26px de alto. Prohibido dejar espacios comprimidos.
5. **Inclusión Curricular DUA/PIE (Decreto 83)**:
   - Emitir proactivamente copias de **Adecuación de Acceso** (letra grande, glosario, renglones amplios) y **Adecuación Significativa** (Nunito, párrafos breves con color, opciones binarias A-B, dibujo).
6. **Formato de Impresión A4**:
   - Todo material debe incluir `@page { size: A4 portrait; margin: 7mm 8mm; }`, contenedor `.sheet` y `break-inside: avoid` en reactivos.
7. **Control de Calidad Previo**:
   - Ejecutar `py -3 herramientas/validar_material_docente.py "ruta/a/guia.html"` antes de imprimir o publicar.

