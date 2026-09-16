# Creación de Material Docente — Docentes Chile IA

Skill canónica para la planificación de clases, diseño de guías de aprendizaje (imprimibles e interactivas), adaptación curricular DUA/PIE (Decreto 83) y elaboración de solucionarios y pautas docentes en el **sistema escolar chileno** y preparación para **PAES / SIMCE**.

---

## 1. Cuándo usar esta Skill

- Cuando se deba **planificar o redactar una clase** de cualquier nivel o modalidad escolar (Educación Básica, Media Humanístico-Científica o Técnico-Profesional).
- Cuando se deba **crear, revisar o auditar guías de aprendizaje, talleres o evaluaciones formativas/sumativas**.
- Cuando se requiera emitir **adecuaciones curriculares PIE**:
  - Copias con **Adecuación de Acceso** (PAI / NEET / Disgrafía / Baja visión / Hipoacusia).
  - Copias con **Adecuación Significativa** (PACI / NEEP / Discapacidad Intelectual / DIL Fuerte).
- Cuando se deba construir la **pauta de corrección docente** con matriz DEMRE, justificación de distractores y protocolo de tercios.
- Base obligatoria de diseño: respeta el estándar visual, tipográfico e institucional del colegio y los lineamientos de evaluación ministerial.

---

## 2. Fase 1: Planificación de Clase y Redacción Pedagógica

Toda clase de 90 minutos (bloque doble) o 45 minutos (bloque simple) debe estructurarse rigurosamente en tres momentos pedagógicos:

### 2.1. Fórmula Obligatoria de Objetivos de Clase
Los objetivos de clase se redactan siempre bajo la siguiente fórmula canónica:

```text
VERBO EN INFINITIVO + CONTENIDO + CONDICIÓN + HABILIDAD TRANSVERSAL
```

| Componente | Descripción | Ejemplos Recomendados |
|---|---|---|
| **Verbo en Infinitivo** | Acción cognitiva observable | *Analizar, Interpretar, Comparar, Evaluar, Comprender, Sintetizar, Producir, Modelar* |
| **Contenido** | Objeto de estudio o concepto central | *las estrategias argumentativas en una columna de opinión*, *la función cuadrática* |
| **Condición** | Contexto o medio de realización | *mediante la lectura crítica guiada*, *a través del análisis de reactivos modelados*, *con apoyo de organizadores gráficos* |
| **Habilidad Transversal** | Competencia genérica desarrollada | *fomentando el pensamiento crítico*, *desarrollando la comunicación efectiva y la fundamentación rigurosa* |

### 2.2. Estructura de la Clase en Tres Momentos
1. **Inicio (15 min)**:
   - Saludo formativo y presentación visual del objetivo de la clase en pizarra.
   - Activación de conocimientos previos mediante una pregunta detonante de la vida cotidiana.
   - Explicitación del sentido formativo (para qué sirve en la vida ciudadana y en la PAES/SIMCE).
2. **Desarrollo (60 min)**:
   - **Modelado Docente ("ATENCIÓN", 15 min)**: Demostración explícita (*worked example*) de cómo pensar, localizar evidencias y descartar distractores.
   - **Trabajo en Guía de Aprendizaje (35 min)**: Distribución de las guías según perfil (Regular, PIE Acceso, PIE Significativa).
   - **Monitoreo activo de aula (10 min)**: Recorrido docente con andamiaje focalizado y verificación del test de claridad de instrucciones.
3. **Cierre (15 min)**:
   - Socialización plenaria de la pregunta de mayor complejidad cognitiva.
   - Síntesis metacognitiva o **Ticket de Salida** (*«¿Qué pista del texto te permitió justificar la clave?»*).
   - Registro formativo y cierre de bloque.

---

## 3. Fase 2: Elaboración de Guías de Aprendizaje Imprimibles (Formato Regular)

Las guías deben generarse en HTML maquetado con precisión para **impresión directa en papel A4**.

### 3.1. Membrete Institucional
Toda guía debe incluir la tabla de 3 celdas `.header-tbl`:
- **Izquierda**: Logo / Escudo institucional del establecimiento escolar.
- **Centro**: Nombre del establecimiento, ciudad/comuna, departamento de asignatura y profesor(a).
- **Derecha**: Logo institucional complementario o escudo de congregación/red educativa.
- **Línea divisoria**: `<hr class="header-line">` con borde destacado.

### 3.2. Metadatos de Estudiante y Evaluación
Tabla de control con campos:
- Nombre completo del estudiante, Curso, N° de Lista, Fecha, RUT.
- Puntaje Obtenido / Puntaje Total (Pts).
- Nota / Nivel de Logro calculada con **escala de exigencia al 60%**.

### 3.3. Metadatos Curriculares y Didácticos
- **Unidad Curricular** y **Plan Lector / Foco temático**.
- **Tiempo Estimado de Trabajo** (70 a 90 minutos de resolución efectiva).
- **Objetivo de la Guía** redactado con la fórmula de 4 partes.
- **Código Curricular Oficial** (ej: `OA ministerial`) y habilidades evaluadas.
- **Instrucciones claras y numeradas**: Principio rector: *«La complejidad debe estar en el CONTENIDO, no en la INSTRUCCIÓN»*.

### 3.4. Textos Fuente y Formato Tipográfico
- Contenedor `.sheet` con ancho `210mm` y alto mínimo `297mm`.
- `@page { size: A4 portrait; margin: 7mm 8mm; }`.
- Tipografía general: Google Font `'Inter'` (13px, color `#1e293b`).
- Tipografía de lectura de textos: Google Font `'Merriweather'` (serif, 9pt, `line-height: 1.68`, texto justificado).
- **Párrafos numerados**: Cada párrafo debe iniciar con `<span class="parr">N</span>` para facilitar la citación en reactivos.
- Extensión del texto: 500 a 1.200 palabras para medir resistencia lectora.
- Cita bibliográfica formal al pie de la lectura.

### 3.5. Modelado Didáctico: Caja "ATENCIÓN"
Antes de la práctica independiente, incluir una caja `.modeled-box` (fondo `#fffbeb`, borde ámbar `#d97706`) que demuestre el paso a paso del razonamiento.

### 3.6. Reactivos de Selección Múltiple (Marco DEMRE)
- **Exactamente 4 alternativas A–D**: Rigurosamente prohibido incluir alternativa E (formato PSU antiguo en desuso).
- **Badges de Habilidad DEMRE**: Localizar, Interpretar, Evaluar.
- **Regla Anti-adivinación**: La clave **nunca debe ser la alternativa más larga** por conteo de caracteres.
- **Distractores Técnicos Fundados**: *Cambio de foco*, *sobregeneralización*, *literalización forzada*, *invención plausible*, *contradicción* o *confusión causa-efecto*.

### 3.7. Preguntas de Desarrollo y Espacios de Escritura
- Toda pregunta abierta debe contener: Contexto, Tarea cognitiva con un solo verbo principal y Criterio de extensión.
- **Renglones Físicos Pautados**: Es obligatorio insertar bloques `.dev-lines` con renglones limpios `.ln` (altura 22-26px).

---

## 4. Fase 3: Diversificación e Inclusión DUA / PIE (Decreto 83)

### 4.1. Especificaciones de la Guía "PIE Acceso" (PAI / NEET)
- Mismo objetivo cognitivo y mismas preguntas que la guía regular.
- Tamaño de letra aumentado (`13.5px` a `14.5px`, interlineado `1.65`).
- Conceptos y palabras clave destacados en negrita o sombreado suave.
- Glosario contextual de apoyo al pie de la lectura (`.gloss-box`).
- Alternativas en tarjetas visualmente separadas (`.opt-card`).
- Renglones de desarrollo profundos (26 a 28px de altura) para disgrafía.

### 4.2. Especificaciones de la Guía "PIE Significativa" (PACI / NEEP)
- Tipografía Google Font `'Nunito'` (15-16px, interlineado `1.7`).
- Textos adaptados y condensados a un máximo de 1 a 2 párrafos concisos.
- Marcas visuales de color (`mark`, `.hl-g`, `.hl-p`) para resaltar los datos clave.
- Eliminación de preguntas de desarrollo extenso.
- Preguntas con **opciones binarias simplificadas (A y B)** con círculos de marcación grandes.
- Actividad de expresión gráfica o recuadro de dibujo guiado (`.draw-container`).

---

## 5. Fase 4: Solucionarios y Pautas de Corrección Docente

### 5.1. Matriz de Especificaciones DEMRE
Tabla con: Ítem, OA Curricular, Habilidad DEMRE, Tarea Lectora (a–n), Clave Correcta, Puntaje y Clasificación técnica de distractores.

### 5.2. Reformulación Simple Obligatoria
Cada reactivo en la pauta debe incluir una **«📌 Reformulación simple»** que traduzca la instrucción a lenguaje cotidiano del estudiante.

### 5.3. Protocolo de Calificación por Tercios (Preguntas de Desarrollo)
- **3 / 3 pts (Logrado Completo)**: Identifica con exactitud, fundamenta con cita textual o paráfrasis precisa y elabora un juicio valorativo coherente.
- **2 / 3 pts (Logrado Parcial)**: Reconoce el elemento central pero la fundamentación es incompleta.
- **1 / 3 pts (Insuficiente)**: Menciona un concepto aislado sin elaboración.
- **0 / 3 pts (No Observado)**: En blanco, ilegible o incongruencia total.
- **Principio de corrección**: Match semántico flexible; no penalizar caligrafía ni ortografía cuando la idea central sea comprensible.

---

## 6. Auditoría Automática de Calidad

Antes de entregar o imprimir cualquier material didáctico, ejecutar:

```bash
py -3 herramientas/validar_material_docente.py "ruta/a/la/guia.html"
```

