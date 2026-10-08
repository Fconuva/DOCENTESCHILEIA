---
name: creacion-material-docente
description: Crear y revisar planificaciones, guías impresas o digitales, presentaciones espejo, instrumentos y pautas para aula chilena, conservando el objetivo y comprobando claridad, recursos, accesibilidad, coherencia y formatos finales.
---

# Creación completa de material docente

Leer [planificación y paquete](../../../conocimiento/docencia/PLANIFICACION_Y_PAQUETE.md)
y [objetivos](../../../guias_metodologicas/REDACCION_OBJETIVOS_DE_CLASE.md). La
guía, la planificación y la presentación explican el mismo aprendizaje, con
contenidos completos para cada destinatario. No basta una plantilla vacía.

## Encargo y currículo

Confirmar curso, asignatura, unidad, OA o referente, propósito de la clase,
duración real, material existente y producto solicitado. Buscar antes de pedir
lo ya declarado. Verificar el código y enunciado curricular en su fuente vigente;
no adjudicar un OA por parecido de tema. Una preferencia de diseño es local,
no una exigencia ministerial.

Conservar contenidos y decisiones del docente. Distinguir guía de enseñanza,
evaluación, libreto y campo de Portafolio. Para el portafolio se lee también la
[skill propia](../portafolio-docente/SKILL.md); no convertir este molde de aula
en una casilla obligatoria de DocenteMás.

## Objetivo, actividad y evidencia

Formular aprendizaje abordable con habilidad y conocimiento. Seleccionar
actividad y evidencia que permitan observarlo; incluir la dimensión actitudinal
cuando corresponde y diseñar cómo se trabaja y monitorea. Una fórmula con verbo,
contenido, condición y transversal puede ayudar, pero no se impone universalmente.
«Mediante» dentro de cualquier párrafo no acredita coherencia del objetivo.

Definir: qué harán los estudiantes, consigna literal, primera acción, recurso,
producto, criterio de logro y próxima acción si hay error. Las preguntas y la
pauta valoran la habilidad, no solo la presencia de palabras o la realización de
una ficha. No bajar la habilidad aprobada para resolver una dificultad de diseño.

## Secuencia conducible

Mostrar Inicio, Desarrollo y Cierre, con tiempos ajustados al bloque, no una
distribución fija 15/60/15. Incluir activación y sentido, objetivo explicado al
curso, modelado pertinente, práctica guiada, trabajo progresivamente autónomo,
monitoreo, devolución, sistematización y metacognición cuando aporten al encargo.
No sumar actividades para cumplir una lista; relacionar cada etapa con el aprendizaje.

El docente necesita frases para conducir y cambiar de etapa. Los estudiantes
necesitan consignas cortas, recursos y espacio para trabajar. Prever respuesta
parcial, error y silencio. El modelado muestra procedimiento y razonamiento,
sin revelar las respuestas de un instrumento de evaluación.

## Paquete por destinatario

| Pieza | Revisión que debe hacerse |
|---|---|
| Planificación | Objetivo, secuencia, evidencias, tiempos, apoyos y recursos reales. |
| Guía del estudiante | Identificación, objetivo e instrucciones separados, lectura o recurso completo, tareas y espacios útiles. |
| Presentación espejo | Mismo orden y conceptos; preguntas visibles; sin apuntes docentes mezclados. |
| Pauta/solucionario docente | Criterios, respuestas aceptables, evidencia y justificación; separada de la guía. |
| Instrumento | Recoge la evidencia prevista, con unidades, leyenda y criterio de valoración. |
| Recursos adicionales | Existen, corresponden a la actividad y están identificados por su nombre de uso. |

Una clase impresa incluye todo lo que se lee y completa. Un QR o enlace no
sustituye el texto cuando se acordó papel. Los ejemplos simulados se identifican;
imágenes de acompañamiento no acreditan hechos. Comprobar fuentes y condiciones de uso.

## Inclusión y evaluación

Leer [DUA](../adecuaciones-curriculares-dua/SKILL.md) si hay barreras o adecuación
acordada. Diversificar acceso y expresión sin modificar el objetivo por diagnóstico
automático. Una modificación curricular individual requiere contexto y decisión
del equipo competente; no emitir proactivamente una versión «significativa» para todos.

La pauta se construye desde el aprendizaje. El esquema de 0–3 puntos es una
opción de instrumento, no norma nacional. Definir qué significa cada nivel en
esa tarea. La exigencia y conversión a nota se toman del reglamento o encargo;
no suponer 60% por encontrar la palabra «Puntaje».

## Impresión, edición y verificación

Las [plantillas](templates/plantilla_guia_regular.html) son ejemplos reutilizables,
no sustituyen el formato institucional confirmado. Ajustar A4 y márgenes al
contenido, conservar membrete aprobado y usar tipografías legibles. Si se usa
tinta negra, revisar sin fondos y en escala de grises. Una fuente de internet
puede fallar al imprimir sin conexión: confirmar disponibilidad o usar alternativas locales.

Reservar renglones medidos para la respuesta esperada; 7 mm es una referencia
operativa ajustable, no una disposición legal. No reducir espacio o letra para
forzar un número fijo de páginas. Revisar tablas, gráficos, encabezados, pies,
numeración, cortes y páginas finales en el PDF renderizado.

Ejecutar el control técnico y abrir el archivo final:

```bash
python herramientas/validar_material_docente.py ruta/guia.html
```

El script declara qué puede comprobar; no aprueba calidad pedagógica ni impresora.
Aplicar el [pipeline](../../../.agents/skills/docencia-completa/SKILL.md) para una
entrega: recursos, versiones, revisión independiente, dictamen y estado real de
publicación/aviso. Las lecturas ya vigentes no se repiten por ritual.
