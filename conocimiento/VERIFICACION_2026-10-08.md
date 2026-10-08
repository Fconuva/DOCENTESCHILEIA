# Verificación de la ampliación · 8 de octubre de 2026

## Qué cambió

- Las skills se movieron de `.github/skills/` a `.agents/skills/`, que es la
  ruta que leen Antigravity y otros agentes. El flujo `.agent/workflows/` se
  convirtió en la skill `docencia-completa`.
- Seis skills nuevas para docentes: `empezar`, `planificar-clase`,
  `planificar-unidad`, `planificar-anual`, `crear-evaluacion`, `revisar-material`.
- Guías nuevas de currículum, planificación anual y de unidad, estructura de
  la clase, evaluación de aula, material para estudiantes y errores típicos de
  la IA; modelos imprimibles de planificación anual y de unidad; modelo de
  clase rehecho.
- Texto buscable de todos los PDF oficiales con marca de página, e índice de
  OA por asignatura y curso.
- Guías de uso para docentes: `PRIMEROS_PASOS.md` y `QUE_PEDIR.md`.

## Comprobaciones realizadas

- **Detección de skills en Antigravity.** Con el CLI de Antigravity 1.2.4 se
  pidió la lista de skills del proyecto. En la versión publicada el 7 de
  octubre respondió que no veía ninguna skill de proyecto; con la estructura
  nueva listó las del paquete y confirmó que `AGENTS.md` venía cargado.
- **Pedido real de clase.** Con el modelo Gemini 3.8 Flash (Medium) se envió
  `/planificar-clase` para 8.° básico, Lengua y Literatura, 90 minutos. El
  asistente usó la skill, citó el OA 3 con su texto literal y la página 58 del
  PDF, guardó el archivo en `mi_trabajo/2026/…` con el nombre acordado y cerró
  con archivo, impresión, OA y supuestos. El HTML se imprimió a PDF y se leyó:
  títulos INICIO, DESARROLLO y CIERRE, rangos de minutos encadenados que suman
  90, modelado con un caso distinto y devoluciones ante acierto, error y silencio.
- **Búsqueda de OA con el modelo más liviano.** Gemini 3.8 Flash (Low)
  intentaba ejecutar un comando de terminal para buscar. Tras agregar el
  índice de OA respondió sin terminal los OA 7 a 10 de Matemática de 5.°
  básico, con texto coincidente con el oficial y página 250 del PDF.
- **Bienvenida.** `/empezar` hizo las ocho preguntas en un solo mensaje y
  recordó no entregar datos de estudiantes.
- **Índice de OA.** 148 entradas (56 de 1.° a 6.° básico, 40 de 7.° básico a
  2.° medio, 52 de 3.° y 4.° medio), sin avisos del generador. Un test recorre
  cada fila y exige que el tramo indicado contenga la lista de objetivos y que
  la página coincida. Se abrieron a mano entradas de Matemática 5.° básico,
  Historia 3.° básico, Lenguaje 6.° básico y Matemática 8.° básico.
- **Impresión.** Los siete modelos se imprimieron a PDF con Chrome sin
  encabezados. Los tres de planificación tienen texto en todas sus páginas.
  La guía de acceso y el solucionario generaban una segunda hoja en blanco: se
  corrigió la regla de impresión y ahora ocupan una página.
- **Marco para la Buena Enseñanza.** Los doce enunciados se copiaron de la
  visión sinóptica del PDF de 2021 incluido (página 17).
- **Estructura.** 40 pruebas automáticas y `validar_repositorio.py` sin
  errores: 16 skills con metadatos válidos y enlaces locales resueltos.
- **Publicación.** Se revisaron los archivos nuevos y modificados buscando
  RUT, teléfonos, correos, rutas privadas y nombres propios: sin hallazgos
  fuera de la autoría declarada.

## Hallazgos corregidos en lo ya publicado

- El resumen del Marco para la Buena Enseñanza describía la estructura
  anterior de criterios, no la de 2021.
- `Temario_Media_historia_geografia_y_ciencias_sociales.pdf` era una página de
  error guardada con extensión PDF; se retiró. El temario de Historia de media
  sigue en `Temario_Media_historia.pdf`.
- Dos modelos imprimían una hoja en blanco.
- La guía de lectura decía que las tareas con letras no eran nomenclatura de
  DEMRE; el temario de la Admisión 2027 sí las usa.

## Límites del resultado

- Las pruebas se hicieron con el CLI de Antigravity en Windows, no con la
  interfaz gráfica, y sin comprobar qué plan tiene la cuenta usada. Los pasos de
  instalación de `PRIMEROS_PASOS.md` siguen la documentación oficial y un
  tutorial de Google; no se recorrieron en un computador recién instalado. Los
  nombres de menús y botones pueden variar entre versiones.
- No se midió cuántos pedidos permite la cuota gratuita semanal.
- La planificación de prueba no fue revisada por un docente distinto ni
  aplicada en aula. No se incorporó al paquete.
- Las guías y la regla de impresión se comprobaron en Chrome; no en papel.
  La guía regular y la de adecuación significativa pasan a una segunda página
  con sus últimas líneas.
- El texto extraído de los PDF puede desplazar títulos de eje y tablas. El
  índice de 3.° y 4.° medio lista páginas de objetivos por área, no por curso.
- No se abrieron los Programas de Estudio, los Planes de Estudio ni el texto
  del Decreto 67 en la Biblioteca del Congreso. El sitio Currículum Nacional
  no respondió durante la sesión.
- El estado de la actualización de las Bases Curriculares de 1.° básico a
  2.° medio se dejó como «en trámite» con fuentes de 2025 y las orientaciones
  de inicio de 2026; no se encontró una resolución posterior.
