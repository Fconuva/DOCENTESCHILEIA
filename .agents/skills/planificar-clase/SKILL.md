---
name: planificar-clase
description: Planificar una clase para un curso chileno con INICIO, DESARROLLO y CIERRE, objetivo basado en un OA verificado, tiempos que caben, y si se pide, su guía para estudiantes y pauta docente. Usar cuando el docente pide una clase, una planificación diaria, un guion de clase o escribe /planificar-clase.
---

# Planificar una clase

Leer [estructura de la clase](../../../conocimiento/docencia/ESTRUCTURA_DE_LA_CLASE.md)
y [currículum nacional](../../../marco_curricular/CURRICULUM_NACIONAL.md). Para ubicar los OA usar el
[índice de OA](../../../marco_curricular/INDICE_DE_OA.md). Si se
pide guía o presentación, leer también
[material para estudiantes](../../../conocimiento/docencia/MATERIAL_PARA_ESTUDIANTES.md).

## 1. Reunir los datos

Leer `mi_trabajo/mi_contexto.md` si existe. Datos imprescindibles: curso,
asignatura, duración real de la clase y tema u OA. Si falta alguno, preguntar
todo en un solo mensaje, máximo tres preguntas. Lo demás (recursos de la sala,
número de estudiantes, qué vieron antes) se toma del contexto; si no está, se
planifica sin suponer proyector ni internet y se dice.

Si el docente trae su propia idea o material, se conserva su actividad central
y se construye sobre ella.

## 2. Encontrar y citar el OA

Buscar el OA en el `.txt` del nivel, en `marco_curricular/documentos_oficiales/`,
siguiendo el procedimiento de «Cómo encontrar un OA». Copiar el texto literal
con su número y la página del PDF. Si el tema calza con más de un OA, mostrar
los candidatos y elegir con el docente. No inventar códigos ni atribuir un OA
por parecido.

## 3. Acotar el objetivo de la clase

Un contenido y una habilidad para esta clase. Dos líneas en la planificación:

- **OA:** número y texto literal.
- **Objetivo de la clase:** en infinitivo, con el verbo que los estudiantes
  realmente ejecutarán y lo que dejarán como evidencia. Una sola actitud si se
  va a trabajar y observar.

Agregar la frase para decirlo al curso en palabras simples. Ver
[redacción de objetivos](../../../guias_metodologicas/REDACCION_OBJETIVOS_DE_CLASE.md).

## 4. Definir evidencia antes que actividades

Escribir el indicador (qué hará, dirá o producirá el estudiante) y la
evidencia que quedará de todos, no solo de quienes hablan. La tarea central
tiene que pedir el verbo del objetivo.

## 5. Escribir la secuencia

Con los títulos literales **INICIO**, **DESARROLLO** y **CIERRE** y sus
subtítulos, cada uno con su rango de minutos encadenado. Los tres momentos
suman la duración exacta. Incluir:

- en el INICIO, una activación conectada al contenido y el objetivo dicho al curso;
- en el DESARROLLO, modelado breve con un caso distinto, la consigna literal
  de la tarea central, dos preguntas de monitoreo y qué hace el docente ante
  acierto, error y silencio;
- en el CIERRE, síntesis con respuestas de estudiantes y una pregunta de cómo
  aprendieron;
- qué se recorta si falta tiempo y qué hace quien termina antes;
- la tabla «qué imprimir, cuántas copias, para quién».

Antes de cerrar, responder las cuatro preguntas de factibilidad del documento
de estructura. Si la clase no cabe, quitar actividades, no minutos.

## 6. Guardar los archivos

Usar como base el [modelo de clase](../../../documentos_modelo/planificaciones/Planificacion_Clase_3_Momentos_Modelo.html)
y reemplazar todos los campos entre corchetes. Al guardar el documento final, quitar del `<body>` la marca
`data-plantilla` y la nota de «modelo editable» del pie. Guardar en
`mi_trabajo/<año>/<curso>-<asignatura>/` con nombres que digan qué es y para
quién, por ejemplo `clase-conflicto-en-el-cuento_planificacion-docente.html`,
`…_guia-estudiantes.html`, `…_pauta-docente.html`. La guía y la pauta van en
archivos separados; la guía nunca trae respuestas.

## 7. Revisarse y cerrar

Aplicar la tabla «Antes de usar un material en clases» de
[errores típicos](../../../conocimiento/docencia/ERRORES_TIPICOS_DE_LA_IA.md).
Si hay Python instalado se puede correr
`python herramientas/validar_material_docente.py <archivo>`; si no, no es
necesario y no se le pide al docente instalar nada.

Responder al docente, en pocas líneas:

1. qué archivos se crearon y cuál abrir primero;
2. cómo imprimir: doble clic, Ctrl + P, A4, guardar como PDF;
3. el OA usado, con su página, para que lo confirme;
4. qué se supuso de su curso y qué debe revisar antes de usarlo.
