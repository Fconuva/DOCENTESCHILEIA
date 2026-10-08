---
name: empezar
description: Primera conversación con un docente que acaba de abrir el paquete. Usar cuando escribe /empezar, saluda sin pedir nada concreto, pregunta qué puede hacer el asistente o cuando no existe mi_trabajo/mi_contexto.md. Reúne sus datos de trabajo en pocas preguntas y los guarda para no volver a pedirlos.
---

# Empezar: conocer al docente y guardar su contexto

Quien escribe es un docente de aula. Probablemente no programa y es su primera
vez con un asistente como este. Hablar claro, breve y sin jerga técnica.

## 1. Revisar si ya hay contexto

Leer `mi_trabajo/mi_contexto.md`. Si existe, saludar por su nombre, resumir en
tres líneas lo guardado y preguntar qué quiere hacer o corregir. No repetir
las preguntas.

## 2. Preguntar lo necesario, en un solo mensaje

Si no existe, presentarse en dos líneas y pedir estos datos juntos, numerados,
aclarando que puede dejar en blanco lo que no sepa:

1. ¿Cómo te llamas y en qué colegio o liceo trabajas? (comuna)
2. ¿Qué asignaturas haces y en qué cursos?
3. ¿Cuántas horas a la semana tienes con cada curso y cómo se reparten?
   (por ejemplo: un bloque de 90 minutos y uno de 45)
4. ¿Cuántos estudiantes tiene cada curso, más o menos?
5. ¿Qué hay en tu sala? (proyector, parlantes, pizarra, computadores, internet)
6. ¿Puedes imprimir? ¿En qué tamaño de hoja y en color o blanco y negro?
7. ¿Tu colegio tiene un formato propio de planificación o una plataforma
   donde se registra? ¿Cuál?
8. ¿Qué exigencia usa tu colegio para la nota 4,0? (si no lo sabes, lo dejamos pendiente)

No pedir nombres, RUT, notas ni diagnósticos de estudiantes. Si el docente los
escribe, no guardarlos.

## 3. Guardar

Crear `mi_trabajo/mi_contexto.md` con este formato, usando solo lo que el
docente dijo. Lo que no respondió queda como «Pendiente».

```markdown
# Mi contexto de trabajo

Actualizado: AAAA-MM-DD

## Docente y establecimiento
- Nombre:
- Establecimiento y comuna:

## Cursos y asignaturas
| Curso | Asignatura | Horas semanales y bloques | Estudiantes |
|---|---|---|---|

## Sala y recursos
- Proyección y sonido:
- Computadores e internet:
- Impresión (tamaño de hoja, color):

## Colegio
- Formato o plataforma de planificación:
- Exigencia para la nota 4,0:

## Preferencias y acuerdos
- (lo que el docente pida mantener siempre)
```

## 4. Mostrar qué puede pedir

Cerrar con cuatro ejemplos adaptados a sus cursos, uno por línea:

- `/planificar-clase` para una clase con guía y pauta.
- `/planificar-unidad` para ordenar una unidad completa.
- `/planificar-anual` para repartir el año.
- `/crear-evaluacion` para una prueba, rúbrica o ticket de salida.

Y una frase: todo queda en la carpeta `mi_trabajo`, y siempre conviene leer el
documento antes de imprimirlo. Más ejemplos en [QUE_PEDIR.md](../../../QUE_PEDIR.md).

## Durante el uso

Cuando el docente entregue un dato estable que no estaba (otro curso, cambio
de sala, formato del colegio), ofrecer agregarlo a `mi_contexto.md`.
