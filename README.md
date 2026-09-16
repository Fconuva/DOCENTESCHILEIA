# DOCENTES CHILE IA 🇨🇱
### Ecosistema Abierto de Skills, Agentes y Pipeline de Creación de Material Docente para Chile
### Ecosistema Abierto de Skills, Agentes, Marco Curricular y Pipeline de Creación de Material Docente para Chile

> **Repositorio Oficial:** [github.com/Fconuva/DOCENTESCHILEIA](https://github.com/Fconuva/DOCENTESCHILEIA)  
> **Orientado a:** Profesores, Equipos PIE, Directores de Departamento y Diseñadores Instruccionales del sistema escolar chileno (Educación Básica, Educación Media HC y Técnico-Profesional).
> **Orientado a:** Profesores, Educadores Diferenciales / PIE, Equipos UTP, Directores y Diseñadores Instruccionales del sistema escolar chileno (Educación Parvularia, Básica, Media HC, Media Técnico-Profesional y EPJA).

---

## 📖 ¿Qué es Docentes Chile IA?

**Docentes Chile IA** es una suite profesional de **Skills de IA, Workflows Pedagógicos, Plantillas Imprimibles A4 y Herramientas de Validación de Calidad** diseñada específicamente para los estándares del sistema educativo chileno:
**Docentes Chile IA** es una suite integral y abierta de **Skills de IA, Marco Curricular Oficial, Documentos del Marco para la Buena Enseñanza (MBE), Temarios de Evaluación Docente CPEIP 2026, Dossiers Pedagógicos, Plantillas Imprimibles A4 y Herramientas de Auditoría**, creada para elevar el estándar de la docencia nacional mediante el uso riguroso y ético de la Inteligencia Artificial:

1. **Bases Curriculares Mineduc**: Cobertura estricta de Objetivos de Aprendizaje (OA), indicadores de logro y priorización curricular.
2. **Marco DEMRE y Metodología PAES / SIMCE**: Diseño de instrumentos y reactivos de alta exigencia basados en evidencia, con exactamente 4 alternativas (A–D), control anti-adivinación y 14 tareas lectoras oficiales.
3. **Inclusión Curricular y DUA (Decreto 83 / Decreto 170)**: Generación proactiva y foliada de guías con **Adecuación de Acceso** (PAI / NEET / Disgrafía / Baja visión) y **Adecuación Significativa** (PACI / NEEP / DIL Fuerte).
4. **Planificación Didáctica en 3 Momentos**: Redacción de clases con fórmula canónica obligatoria (`VERBO EN INFINITIVO + CONTENIDO + CONDICIÓN + HABILIDAD TRANSVERSAL`).
5. **Protocolos de Evaluación Formativa y Sumativa**: Pautas docentes con matriz DEMRE, justificación técnica de distractores y calificación de desarrollo por tercios (`3/3`, `2/3`, `1/3`, `0/3`).
1. **Marco para la Buena Enseñanza (MBE / CPEIP)**: Dominios A, B, C y D, criterios y descriptores del estándar de la profesión docente en Chile.
2. **Bases Curriculares y Objetivos de Aprendizaje (OA)**: Cobertura completa de la trayectoria escolar desde Educación Parvularia hasta 4° Medio (formación general y diferenciada TP).
3. **Temarios Oficiales de Evaluación Docente 2026 (CPEIP / DocenteMás)**: Los 19 temarios oficiales para la Prueba de Conocimientos Específicos y Pedagógicos (ECEP) y Portafolios.
4. **Dossiers de Conocimiento Pedagógico del Contenido (PCK)**: Síntesis de didáctica y disciplina para Generalista, Lenguaje, Matemática y Educación Diferencial.
5. **Marco DEMRE y Metodología PAES / SIMCE**: Diseño de reactivos analíticos de 4 alternativas (A–D), control anti-adivinación y 14 tareas lectoras oficiales (*a–n*).
6. **Inclusión Curricular y DUA (Decreto 83 / Decreto 170 / Decreto 67)**: Generación proactiva y foliada de guías con **Adecuación de Acceso (PAI)** y **Adecuación Significativa (PACI)**.
7. **Planificación Didáctica en 3 Momentos**: Redacción con fórmula canónica obligatoria (`VERBO EN INFINITIVO + CONTENIDO + CONDICIÓN + HABILIDAD TRANSVERSAL`).
8. **Protocolos de Evaluación por Tercios**: Criterios de calificación de desarrollo (`3/3`, `2/3`, `1/3`, `0/3`) con match semántico flexible.

---

## 📁 Estructura del Repositorio

```text
DOCENTESCHILEIA/
├── .github/
│   ├── instructions/                      # Instrucciones de workspace para Copilot y Agentes
│   │   ├── creacion-material-docente.instructions.md
│   │   ├── paes-competencia-lectora.instructions.md
│   │   └── adecuaciones-pie-dua.instructions.md
│   └── skills/                            # Skills de IA listas para Antigravity / Claude / Codex
│       ├── creacion-material-docente/     # Skill central de planificación y guías A4
│       │   ├── SKILL.md
│       │   └── templates/                 # Plantillas HTML maestras reutilizables
│       ├── paes-simce-competencia-lectora/# Skill especializada en pruebas y reactivos DEMRE
│       │   └── SKILL.md
│       └── adecuaciones-curriculares-dua/ # Skill de inclusión y diversificación (Decreto 83)
│           └── SKILL.md
├── marco_curricular/                      # Marco oficial del Mineduc y CPEIP
│   ├── MARCO_PARA_LA_BUENA_ENSENANZA.md   # Síntesis estructurada de Dominios A, B, C, D
│   ├── BASES_CURRICULARES_Y_OAS.md        # Ejes y progresión de OAs por asignatura
│   └── documentos_oficiales/              # Documentos PDF y TXT oficiales Mineduc
│       ├── Marco_para_la_Buena_Ensenanza_General.pdf
│       ├── Marco_para_la_Buena_Ensenanza_Parvularia.pdf
│       ├── Bases_Curriculares_1_a_6_Basico.pdf
│       ├── Bases_Curriculares_7_Basico_a_2_Medio.pdf
│       ├── Bases_Curriculares_3_y_4_Medio.pdf
│       ├── Bases_Curriculares_Educacion_Parvularia.pdf
│       ├── Bases_Curriculares_Formacion_Diferenciada_TP.pdf
│       └── Bases_Curriculares_EPJA_2024.pdf
├── temarios_evaluacion_docente_2026/      # Temarios oficiales CPEIP 2026 para ECEP y Portafolio
│   ├── Temario_Basica_Generalista_2026.pdf
│   ├── Temario_Basica_Lenguaje_2026.pdf
│   ├── Temario_Basica_Matematica_2026.pdf
│   ├── Temario_Basica_Ciencias_2026.pdf
│   ├── Temario_Basica_Historia_2026.pdf
│   ├── Temario_Especial_DEA_2026.pdf
│   ├── Temario_Especial_DI_2026.pdf
│   ├── Temario_Especial_TEA_2026.pdf
│   ├── Temario_Especial_TEL_2026.pdf
│   ├── Temario_Media_lengua_y_literatura.pdf
│   ├── Temario_Media_matematica.pdf
│   ├── Temario_Media_biologia.pdf
│   ├── Temario_Media_fisica.pdf
│   ├── Temario_Media_quimica.pdf
│   ├── Temario_Media_historia.pdf
│   └── Temario_Parvularia_2026.pdf
├── dossiers_pedagogicos/                  # Conocimiento Pedagógico del Contenido (PCK) por área
│   ├── DOSSIER_CONOCIMIENTO_DOCENTE_GENERALISTA.md
│   ├── DOSSIER_CONOCIMIENTO_DOCENTE_LENGUAJE.md
│   ├── DOSSIER_CONOCIMIENTO_DOCENTE_MATEMATICA.md
│   └── DOSSIER_CONOCIMIENTO_DOCENTE_DIFERENCIAL_PIE.md
├── recursos_paes_simce/                   # Herramientas metodológicas y banco de textos
│   ├── METODOLOGIA_PAES_extraida.md       # Método DEMRE extraído de Moraleja y Puntaje Nacional
│   └── CATALOGO_TEXTOS_PAES.md            # Catálogo de textos por género y habilidad
├── documentos_modelo/                     # Documentos imprimibles A4 listos para el aula
│   ├── guias_aprendizaje/
│   │   ├── Guia_Modelo_Regular_A4.html
│   │   ├── Guia_Modelo_PIE_Acceso_A4.html
│   │   └── Guia_Modelo_PIE_Significativa_A4.html
│   ├── planificaciones/
│   │   └── Planificacion_Clase_3_Momentos_Modelo.html
│   └── solucionarios/
│       └── Solucionario_y_Pauta_Docente_Modelo.html
├── guias_metodologicas/                   # Manuales de ingeniería pedagógica
│   ├── REDACCION_OBJETIVOS_DE_CLASE.md    # Fórmula de 4 partes y taxonomía cognitiva
│   ├── METODOLOGIA_PAES_DEMRE.md          # 14 tareas lectoras, distractores y anti-adivinación
│   ├── PROTOCOLO_CORRECCION_DESARROLLO.md # Rúbrica de tercios y match semántico
│   └── DISENO_UNIVERSAL_APRENDIZAJE_DUA.md# Pautas prácticas del Decreto 83
├── herramientas/                          # Scripts de automatización y auditoría
│   └── validar_material_docente.py        # Validador de calidad en Python estándar
└── README.md                              # Este documento
```

---

## 🚀 Cómo Usar las Skills en tu Entorno de IA

Estas skills son compatibles de forma nativa con los principales agentes y entornos de pair programming pedagógico:
- **Google Antigravity (AGY)**
- **Claude Code (Anthropic)**
- **OpenAI Codex**
- **GitHub Copilot Workspace**

### 1. Activar la Skill de Creación de Material
Al solicitar a tu agente pedagógico:
> *«Crea una guía de trabajo de 2 planas en A4 para 3° Medio sobre argumentación falaz, con su versión PIE de Acceso y su Pauta Docente.»*

El agente activará `.github/skills/creacion-material-docente/SKILL.md` y ejecutará el pipeline completo en 4 fases:
1. Formulación del objetivo con la fórmula de 4 partes.
1. Formulación del objetivo con la fórmula de 4 partes (`VERBO + CONTENIDO + CONDICIÓN + HABILIDAD`).
2. Maquetación A4 con fuentes *Inter* y *Merriweather*, párrafos numerados y reactivos A–D con badges DEMRE.
3. Derivación de la guía adaptada (letra 14px+, glosario y renglones de 28px).
4. Generación de la pauta con justificación de distractores y escala de tercios.

### 2. Validar la Calidad de tu Material antes de Imprimir
Ejecuta el script validador en tu terminal (utiliza la biblioteca estándar de Python, sin dependencias externas):

```powershell
py -3 herramientas/validar_material_docente.py "documentos_modelo/guias_aprendizaje/Guia_Modelo_Regular_A4.html"
```

El script auditará automáticamente:
- [x] Integridad del membrete institucional y metadatos.
- [x] Formulación canónica de 4 partes en el objetivo de la clase.
- [x] Formato A–D en selección múltiple (sin opciones E de formato PSU obsoleto).
- [x] Regla anti-adivinación (la clave no es la alternativa más larga).
- [x] Presencia de renglones pautados (`.dev-lines`) en preguntas de desarrollo.
- [x] Reglas de corte de impresión A4 (`@page`, `.sheet`, `break-inside: avoid`).

---

## 🎯 Estándares Pedagógicos Centrales

### 1. Fórmula de Objetivos de Clase
### 1. Marco para la Buena Enseñanza (MBE)
- **Dominio A**: Preparación rigurosa de la enseñanza, dominio disciplinar (PCK) y evaluación coherente.
- **Dominio B**: Clima de respeto, equidad, normas claras y altas expectativas de logro.
- **Dominio C**: Interacciones desafiantes, preguntas de orden superior, andamiaje, uso formativo del error y monitoreo activo.
- **Dominio D**: Reflexión pedagógica continua, trabajo colaborativo con pares y compromiso comunitario.

### 2. Fórmula de Objetivos de Clase
Todo objetivo pedagógico se redacta bajo la fórmula:
```text
VERBO EN INFINITIVO + CONTENIDO + CONDICIÓN + HABILIDAD TRANSVERSAL
```
*Ejemplo:*
> *«**Analizar** las estrategias argumentativas y falacias en columnas de opinión, **mediante** la lectura crítica guiada y el trabajo en parejas, **desarrollando** el pensamiento crítico y la fundamentación rigurosa.»*

### 2. Reactivos DEMRE de 4 Alternativas (Anti-Adivinación)
### 3. Reactivos DEMRE de 4 Alternativas (Anti-Adivinación)
- **4 Alternativas (A, B, C, D)** con registro y longitud balanceada.
- **La clave nunca es la opción más larga**.
- **Distractores con falla técnica documentada**: *cambio de foco*, *sobregeneralización*, *literalización forzada*, *invención plausible* o *contradicción*.
- **Principio rector de claridad**: *«La complejidad debe estar en el CONTENIDO, no en la INSTRUCCIÓN»*.

### 3. Inclusión Curricular (Decreto 83 / DUA)
### 4. Inclusión Curricular (Decreto 83 / DUA)
- **Regular**: Formato estándar para el curso general.
- **PIE Acceso (PAI / NEET)**: Tamaño de letra aumentado, glosarios laterales, opciones en tarjetas y renglones profundos para disgrafía.
- **PIE Significativa (PACI / NEEP)**: Tipografía *Nunito* (15–16px), textos condensados en 1–2 párrafos con marcas de color (`mark`, `hl-g`), opciones binarias A–B y actividades de expresión gráfica.

---

## 👨‍🏫 Autor y Créditos

- **Profesor Francisco Javier Núñez Valenzuela** — Profesor de Lengua y Literatura, Centro Educativo Salesianos Talca (CEST).
- Iniciativa de código abierto para la modernización de la docencia con Inteligencia Artificial en Chile.

---

## 📄 Licencia
Este proyecto se distribuye bajo licencia **MIT**, permitiendo su uso, adaptación y redistribución libre para fines educativos y pedagógicos en todo Chile.

