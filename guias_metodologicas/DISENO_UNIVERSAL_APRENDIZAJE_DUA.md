# Guía Metodológica: Diseño Universal para el Aprendizaje (DUA) e Inclusión

## Aplicación Práctica del Decreto 83 / 2015 Mineduc en Materiales de Aula

El **Decreto N° 83/2015** del Ministerio de Educación de Chile establece los criterios y orientaciones para la diversificación de la enseñanza y las adecuaciones curriculares en Educación Parvularia, Básica y Media.

El objetivo central es eliminar las barreras para el aprendizaje y garantizar que **todos los estudiantes participen y progresen en el currículum nacional**, sin rebajar las expectativas formativas.

---

## 1. Los Tres Principios del DUA en Material Didáctico

| Principio DUA | Foco Pedagógico | Aplicación en Guías y Evaluaciones Imprimibles |
|---|---|---|
| **Principio I: Múltiples formas de Representación** | El *«QUÉ»* del aprendizaje (cómo perciben y comprenden la información). | • Textos con conceptos clave en **negrita** o destacados con color (`mark`, `.hl-g`).<br>• Inclusión de **glosarios contextuales** de vocabulario técnico.<br>• Apoyo visual mediante esquemas, infografías y párrafos numerados.<br>• Aumento de tipografía base (14px a 16px) e interlineado amplio (1.65+). |
| **Principio II: Múltiples formas de Acción y Expresión** | El *«CÓMO»* del aprendizaje (cómo demuestran lo que saben). | • Renglones pautados profundos (26–28px) para disgrafía.<br>• Alternativas en tarjetas visuales amplias (`.opt-card`).<br>• Preguntas binarias (A y B) o V/F para estudiantes con discapacidad intelectual.<br>• Recuadros para expresión gráfica, mapas conceptuales o dibujo guiado. |
| **Principio III: Múltiples formas de Implicación / Motivación** | El *«POR QUÉ»* del aprendizaje (interés, esfuerzo y persistencia). | • Cajas de modelado didáctico (*"ATENCIÓN"* / *worked examples*).<br>• Instrucciones cortas, numeradas y directas.<br>• Vínculo explícito del contenido con situaciones cotidianas o laborales reales. |

---

## 2. Tipos de Adecuación Curricular (Decreto 83)

### 2.1. Adecuaciones de Acceso (PAI / Necesidades Educativas Transitorias - NEET)
*No modifican los objetivos de aprendizaje de las Bases Curriculares; ajustan el formato y las vías de acceso a la información.*

- **Población destinataria**: Estudiantes con Dificultades Específicas del Aprendizaje (DEA), Trastornos del Lenguaje (TEL), Trastorno por Déficit Atencional (TDAH), disgrafía, baja visión o hipoacusia leve.
- **Modificaciones en el material**:
  - Mismo objetivo cognitivo y mismas preguntas que el curso general.
  - Tipografía base aumentada (`13.5px` a `14.5px`) con interlineado `1.65` o superior.
  - Palabras complejas definidas en una caja lateral o al pie (`.gloss-box`).
  - Opciones de selección múltiple organizadas en bloques/tarjetas independientes con bordes claros.
  - Renglones de respuesta con separación generosa (26 a 28px) para evitar amontonamiento.

### 2.2. Adecuaciones Significativas (PACI / Necesidades Educativas Permanentes - NEEP)
*Ajustan la profundidad o complejidad de los objetivos para hacerlos pertinentes a las capacidades del estudiante (priorización de contenidos, graduación de exigencia o eliminación de objetivos no esenciales).*

- **Población destinataria**: Estudiantes con Discapacidad Intelectual (DI / DIL Fuerte), Trastorno del Espectro Autista severo (TEA) o retos múltiples.
- **Modificaciones en el material**:
  - Tipografía altamente legible y amigable: Google Font `'Nunito'` (tamaño 15 a 16px).
  - Textos condensados a 1 o 2 párrafos breves con oraciones directas (Sujeto + Verbo + Predicado).
  - Uso de marcadores de color para identificar hechos fundamentales.
  - Eliminación de preguntas de desarrollo abstracto y reemplazo por opciones binarias (A y B) con círculos de marcación grandes.
  - Inclusión de actividades de emparejamiento visual, completar frases con pistas o dibujo guiado (`.draw-container`).
  - Emisión foliada con el nombre del estudiante pre-impreso.

---

## 3. Lista de Chequeo de Accesibilidad para Material Impreso

Antes de enviar a fotocopiar o imprimir una guía, verificar:
- [ ] ¿El tamaño de la fuente es de al menos 13px en la versión regular y 14–16px en la adaptada?
- [ ] ¿Los contrastes de color son legibles incluso si se imprime en escala de grises / blanco y negro?
- [ ] ¿El interlineado permite leer sin saltarse líneas accidentalmente (`line-height: 1.6+`)?
- [ ] ¿Los renglones de respuesta manual tienen al menos 22mm de alto?
- [ ] ¿Las instrucciones fueron simplificadas y redactadas en oraciones simples?

