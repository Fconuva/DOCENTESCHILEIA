# Evaluación de aula: norma, instrumentos y notas

## Lo que dice la norma nacional

El Decreto 67 de 2018 fija las normas mínimas de evaluación, calificación y
promoción. Según la [ficha del Mineduc](https://ayudamineduc.cl/print/9392845):

- La evaluación puede usarse de forma formativa o sumativa. Tiene uso
  formativo «en la medida en que se integra a la enseñanza» para acompañar el
  aprendizaje; la sumativa certifica aprendizajes, generalmente con una
  calificación.
- Los estudiantes «no podrán ser eximidos de ninguna asignatura o módulo del
  plan de estudio».
- La calificación final anual de cada asignatura se expresa «en una escala de
  1.0 a 7.0, hasta con un decimal», y la calificación mínima de aprobación es 4.0.
- Cada establecimiento tiene un reglamento de evaluación con procedimientos
  «de carácter objetivo y transparente», que se comunica a la comunidad.
- La promoción considera el logro de los objetivos y la asistencia (85 % de
  las clases del calendario escolar, con facultad del director para casos
  fundados).

Lo que la norma nacional no fija y define cada reglamento:

- el porcentaje de exigencia para la nota 4.0;
- la cantidad de calificaciones por asignatura o semestre;
- las ponderaciones;
- los formatos de prueba o de rúbrica.

Por eso, antes de construir un instrumento calificado se pregunta al docente
qué dice el reglamento de su colegio. No se supone 60 %.

## Qué se evalúa

- Solo lo que hubo oportunidad de aprender en clases.
- El verbo del objetivo. Si el objetivo dice «explicar», una pregunta de
  completar una palabra o marcar una alternativa no lo mide. Se leen objetivo
  y consigna uno al lado del otro.
- Con evidencia de todos: se cuenta en cuántos estudiantes queda demostrado el
  indicador principal y por qué vía. Si solo responden oralmente los que
  levantan la mano, no hay evidencia del curso.

## Indicadores

Un indicador describe una conducta observable, con su contenido y la condición
necesaria: qué hará, dirá, escribirá o producirá el estudiante. Se evitan
«comprende», «valora» o «participa adecuadamente» si no se dice cómo se observa.

## Elegir el instrumento por su estructura

| Instrumento | Estructura | Sirve para |
|---|---|---|
| Lista de cotejo | Criterios con Sí / No | Comprobar presencia de pasos o elementos. |
| Escala de apreciación | Criterios con niveles (por ejemplo, logrado, medianamente logrado, por lograr) | Graduar frecuencia o calidad sin describir cada nivel. |
| Rúbrica | Criterios con niveles y un descriptor por cada nivel | Desempeños complejos: escritura, exposición, proyecto. |
| Pauta de corrección | Respuesta esperada, variantes válidas y puntaje por pregunta | Preguntas abiertas de una prueba o guía. |
| Prueba con tabla de especificaciones | Ítems distribuidos por OA, habilidad y puntaje | Evaluación sumativa de una unidad. |
| Ticket de salida | Una o dos preguntas al final de la clase | Evidencia rápida, de uso formativo. |

El nombre debe calzar con la estructura: un instrumento con niveles no es una
lista de cotejo.

## Reglas de una buena rúbrica o escala

- Descriptores observables: lo que se ve, se oye o se produce. En un
  descriptor de nivel se evitan «comprende», «valora», «sabe», «entiende»,
  «aprecia». Sirven: ejecuta, identifica, nombra, escribe, clasifica, calcula,
  construye, explica con….
- Niveles paralelos: cada nivel difiere en una sola dimensión (cuántos
  elementos, qué calidad o cuánta autonomía), sin vacíos ni solapes.
- En vez de «comete pocos errores», nombrar los elementos del criterio y
  graduar por cuántos cumple: «incluye 4 / 3 / 2 / 0 a 1 de los 4 elementos: …».
- Un criterio por fila. Técnica, actitud y puntualidad no se agrupan.
- Una leyenda define qué significa cada nivel.
- Tamaño de referencia: 5 a 7 criterios y 3 a 4 niveles.
- Lo que la planificación declara que se evalúa existe físicamente en el
  instrumento.
- Sin RUT ni diagnósticos en el instrumento.

## Tabla de especificaciones

Se arma antes de escribir las preguntas.

| OA o indicador | Habilidad | Contenido | N.° de ítems | Tipo de ítem | Puntaje |
|---|---|---|---|---|---|
| OA 3, analiza la evolución de un personaje | Interpretar | Cuento leído en clases | 4 | Selección múltiple | 4 |
| OA 3, justifica con evidencia | Evaluar | Mismo cuento | 1 | Respuesta abierta | 6 |

Revisión de la tabla:

- cada OA evaluado se trabajó en clases;
- el peso de cada habilidad corresponde a lo enseñado;
- el puntaje total y la exigencia vienen del reglamento del colegio;
- la versión con apoyos, si existe, sale de la misma tabla.

## Preguntas de selección múltiple

- Una sola respuesta correcta que se pueda defender con el texto o el dato.
- Cada distractor responde a un error real: una confusión frecuente, un
  cálculo típico equivocado, una lectura parcial. La pauta dice por qué engaña.
- Alternativas de largo parejo. Que la correcta sea siempre la más larga es
  una pista.
- En la prueba completa, la posición de la correcta se reparte entre las
  letras, sin patrones como ABCDABCD y sin evitar que una letra se repita.
- Tipos de distractor útiles en lectura: cambio de foco, generalización
  excesiva, lectura demasiado literal, información inventada pero creíble,
  contradicción con el texto, respuesta parcialmente correcta.
- Tipos útiles en matemática: error de signo o de jerarquía, mala traducción
  al álgebra, lectura parcial de un gráfico, sumar donde corresponde
  proporción, error de unidades, conteo incompleto.

## Preguntas abiertas

Ver [corrección de preguntas abiertas](../../guias_metodologicas/PROTOCOLO_CORRECCION_DESARROLLO.md).
En resumen: criterios declarados, se aceptan respuestas equivalentes, no hay
descuentos ocultos por ortografía o extensión, y un mismo error no descuenta
dos veces.

## De puntaje a nota

La escala 1.0 a 7.0 y el 4.0 de aprobación son norma. El porcentaje de
exigencia lo fija el reglamento del colegio. Con una exigencia `e` (en
porcentaje) y un logro `p` (porcentaje de puntaje obtenido), la conversión
lineal de uso habitual es:

```text
si p ≥ e:  nota = 4,0 + 3,0 × (p − e) / (100 − e)
si p < e:  nota = 1,0 + 3,0 × p / e
```

Ejemplo: prueba de 40 puntos con exigencia de 60 %. La nota 4,0 se obtiene con
24 puntos. Un estudiante con 32 puntos tiene 80 % de logro:
4,0 + 3,0 × 20 / 40 = 5,5.

Es una convención de cálculo, no un artículo del decreto. Si el reglamento
del colegio define otra tabla, manda el reglamento.

## Registro y retroalimentación

- El registro distingue lo observado, lo logrado con apoyo y lo que no se
  alcanzó a observar. No haber podido observar no es «no logrado».
- Un registro imposible de llenar mientras se circula no produce evidencia:
  se reparte qué se observa en vivo y qué se revisa después.
- Retroalimentar es devolver una pista o una pregunta para que el estudiante
  revise su trabajo. Repetir la respuesta correcta no es retroalimentar.
- Después de una prueba se miran los resultados por pregunta: aciertos,
  omisiones y qué alternativa eligieron. Una pregunta que fallan justo los que
  más saben obliga a revisar la clave y el enunciado antes de culpar a la
  enseñanza.
- Si una habilidad salió baja, se vuelve a trabajar con un texto o problema
  distinto, no repitiendo el mismo.

## Inclusión en la evaluación

- La versión con apoyos conserva el objetivo y la habilidad, salvo decisión
  individual del equipo competente. Ver la [skill de adecuaciones](../../.agents/skills/adecuaciones-curriculares-dua/SKILL.md).
- El apoyo no puede resolver la tarea: si se evalúa encontrar la evidencia, no
  se entrega subrayada.
- El apoyo se registra aparte y no equivale a menor logro.
