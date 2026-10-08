# Docentes Chile IA

Un asistente para planificar clases, unidades y el año, preparar guías y
evaluaciones y revisar material, con el currículum chileno adentro. Se usa con
Antigravity, un programa gratuito de Google, y no hace falta saber programar.

## Para empezar

1. Instala [Antigravity](https://antigravity.google/download) e inicia sesión con tu cuenta de Google.
2. Descarga esta carpeta: botón verde **Code**, **Download ZIP**, y extráela en Documentos.
3. En Antigravity abre la carpeta con **File, Open Folder**.
4. Abre el asistente con **Ctrl + L** y escribe `/empezar`.

La guía paso a paso, con solución de problemas, está en
[PRIMEROS_PASOS.md](PRIMEROS_PASOS.md).

**Requisitos:** computador con Windows 10 de 64 bits o superior (o Mac o
Linux), 8 GB de RAM o más, cuenta de Google e internet.

## Qué le puedes pedir

| Escribe | Para |
|---|---|
| `/empezar` | Contarle tus cursos y tu sala una sola vez. |
| `/planificar-clase` | Una clase con INICIO, DESARROLLO y CIERRE, su guía y su pauta. |
| `/planificar-unidad` | Una unidad con OA, indicadores, evaluación y secuencia semanal. |
| `/planificar-anual` | Repartir los OA del año en unidades según tu calendario real. |
| `/crear-evaluacion` | Una prueba, rúbrica, lista de cotejo o ticket de salida, con su pauta. |
| `/revisar-material` | Revisar un material tuyo o hecho con IA antes de usarlo. |

También puedes escribir con tus palabras, sin comando. Hay ejemplos listos
para copiar en [QUE_PEDIR.md](QUE_PEDIR.md).

Todo queda guardado en la carpeta `mi_trabajo`. Cada documento se abre en el
navegador y se imprime o guarda como PDF con Ctrl + P.

## Tres cosas que conviene saber

- **El asistente se equivoca.** Lee cada documento antes de usarlo y confirma
  el OA que citó. La lista de [errores típicos de la IA](conocimiento/docencia/ERRORES_TIPICOS_DE_LA_IA.md)
  dice qué mirar.
- **No escribas datos de tus estudiantes.** Ni nombres completos, ni RUT, ni
  notas, ni diagnósticos.
- **La cuota gratuita es limitada.** Se renueva cada semana y Google no
  publica cuánto es. Pide el trabajo completo en un solo mensaje.

### Portafolio de la evaluación docente

DocenteMás limita el uso de IA en el Portafolio: «El uso de IA solo está
permitido para apoyar la organización de sus ideas o para identificar errores
de redacción u ortográficos en sus respuestas», y su uso debe informarse en la
Declaración de autoría
([Preguntas frecuentes 2026](https://www.docentemas.cl/wp-content/uploads/2026/09/Preguntas-frecuentes.pdf),
[orientaciones de veracidad](https://www.docentemas.cl/wp-content/uploads/2026/08/Como-resguardar-las-condiciones-de-veracidad-en-tu-PF_PDF.pdf)).
Las reflexiones y análisis de tu Portafolio los escribes tú.

## Qué trae el paquete

| Carpeta | Contenido |
|---|---|
| [marco_curricular](marco_curricular/CURRICULUM_NACIONAL.md) | Bases Curriculares de todos los niveles y Marco para la Buena Enseñanza, en PDF y en texto buscable, con una guía para encontrar y citar un OA. |
| [conocimiento/docencia](conocimiento/INDICE.md) | Cómo se planifica el año y la unidad, estructura de la clase, evaluación de aula, material para estudiantes y errores típicos de la IA. |
| [guias_metodologicas](guias_metodologicas/REDACCION_OBJETIVOS_DE_CLASE.md) | Redacción de objetivos, corrección de preguntas abiertas, diversificación, lectura PAES. |
| [documentos_modelo](documentos_modelo/planificaciones/Planificacion_Clase_3_Momentos_Modelo.html) | Modelos A4 editables: planificación anual, de unidad y de clase, guías y pauta. |
| [temarios_evaluacion_docente_2026](temarios_evaluacion_docente_2026/) y [dossiers_pedagogicos](dossiers_pedagogicos/) | Temarios de la prueba de conocimientos y apuntes de estudio. |
| `.agents/skills` | Las instrucciones que sigue el asistente en cada tarea. |
| `mi_trabajo` | Tu carpeta: tu contexto y todo lo que produces. |

Otras tareas que el asistente sabe hacer: [adecuaciones y diversificación](.agents/skills/adecuaciones-curriculares-dua/SKILL.md),
[lectura PAES y SIMCE](.agents/skills/paes-simce-competencia-lectora/SKILL.md),
[preparación de la prueba de conocimientos](.agents/skills/ecep-preparacion/SKILL.md),
[revisión de portafolio](.agents/skills/portafolio-docente/SKILL.md),
[registro en Lirmi](.agents/skills/lirmi-registro-verificado/SKILL.md) y
[plataformas educativas](.agents/skills/plataforma-educativa-calidad/SKILL.md).

## Para quien mantiene el paquete

Funciona con cualquier agente que lea `AGENTS.md` y skills en `.agents/skills/`
(Antigravity, Codex). [SKILL.md](SKILL.md) es el índice de tareas y
[CLAUDE.md](CLAUDE.md) apunta a las mismas instrucciones. Para instalarlo como
skill global de Claude o Codex:

```bash
python herramientas/instalar_skill.py --cliente codex
python herramientas/instalar_skill.py --cliente claude --aplicar
```

Comprobaciones, con Python 3.12 o superior y sin dependencias externas:

```bash
python herramientas/validar_repositorio.py
python -m unittest discover -s tests -v
python herramientas/validar_material_docente.py documentos_modelo/guias_aprendizaje/Guia_Modelo_Regular_A4.html
python herramientas/pipeline_docente.py ejemplos/encargo-sintetico/control.json
```

Los validadores informan cobertura y límites: no califican un objetivo, no
acreditan una clase realizada ni certifican una impresora. El ejemplo de
pipeline devuelve código 2 porque está pendiente a propósito; el
[esquema del registro](conocimiento/operacion/REGISTRO_DEL_PIPELINE.md) explica
cómo registrar una entrega real. Las verificaciones hechas están en
[7 de octubre](conocimiento/VERIFICACION_2026-10-07.md) y
[8 de octubre de 2026](conocimiento/VERIFICACION_2026-10-08.md).

## Fuentes, alcance y derechos

Las exigencias oficiales se consultan en su proceso, modalidad y versión:
[Currículum Nacional](https://www.curriculumnacional.cl/),
[DocenteMás 2026](https://www.docentemas.cl/comienza-la-elaboracion-del-portafolio-2026/),
[Mineduc: Decreto 83](https://bibliotecadigital.mineduc.cl/handle/20.500.12365/14490)
y [DEMRE: publicaciones](https://portaldemre.demre.cl/publicaciones).
Las referencias de 2026 están fechadas; no certifican vigencia futura.

El código y la documentación originales del proyecto se distribuyen bajo MIT.
Los documentos oficiales y recursos de terceros conservan sus derechos y
condiciones de uso; su presencia no les asigna la licencia MIT. Las plantillas
son ejemplos adaptables al establecimiento.

Autor: Francisco Javier Núñez Valenzuela. [Procedencia y cobertura](conocimiento/PROCEDENCIA_Y_COBERTURA.md).
