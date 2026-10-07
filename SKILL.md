---
name: docentes-chile-ia
description: Planificar, construir, revisar y preparar materiales docentes chilenos, portafolios M1/M2/M3, pruebas de lectura y apoyos curriculares con fuentes verificadas. Coordina los procedimientos del paquete sin autorizar envíos ni escrituras administrativas.
---

# Docentes Chile IA

Este paquete reúne el procedimiento completo de producción y revisión docente,
las lecciones reutilizables de Portabot y referencias públicas del sistema chileno.
La profundidad está distribuida por tarea: los procedimientos se conservan, y
se abre el necesario en vez de cargar toda la biblioteca en cada consulta.

## Elegir la tarea

| Solicitud | Skill que debe leerse completa |
|---|---|
| M1, M2, M3, ficha de grabación, revisión por rúbrica, materiales del portafolio | [Portafolio docente](.github/skills/portafolio-docente/SKILL.md) |
| Planificación, guía impresa, presentación espejo, pauta y recursos | [Creación de material](.github/skills/creacion-material-docente/SKILL.md) |
| Enseñar lectura, construir o auditar un ensayo PAES/SIMCE | [Competencia lectora](.github/skills/paes-simce-competencia-lectora/SKILL.md) |
| Identificar barreras, diversificar o aplicar una adecuación acordada | [DUA y adecuaciones](.github/skills/adecuaciones-curriculares-dua/SKILL.md) |
| Preparación disciplinar/pedagógica ECEP | [Preparación ECEP](.github/skills/ecep-preparacion/SKILL.md) |
| Contrastar planificación, asistencia, firma o calificaciones en Lirmi | [Registro verificado](.github/skills/lirmi-registro-verificado/SKILL.md) |
| Contenido y contratos de entrega de una plataforma educativa | [Plataforma educativa](.github/skills/plataforma-educativa-calidad/SKILL.md) |
| Localizar memoria pertinente y comprobar vigencia | [Contexto y Neuromapa](.github/skills/neuromapa-contexto-docente/SKILL.md) |

Si se trabaja dentro de una instalación privada de Portabot, abrir primero su
AGENTS y su índice de reglas actual y aplicar sus skills canónicas. No usar esta
edición pública como permiso, precio ni estado actual de un cliente. Para las
otras tareas, las instrucciones del repositorio propietario y del establecimiento
también prevalecen sobre una nota histórica.

## Entrada que cambia las decisiones

1. Distinguir consulta, propuesta, construcción, corrección, revisión o entrega.
   No rehacer lo que el docente ya aprobó por una preferencia del agente.
2. Confirmar nivel, asignatura, modalidad, encargo y versión de las fuentes. Buscar
   primero los datos existentes; no pedir al docente un manual público disponible.
3. Identificar destinatarios: estudiante, docente y plataforma. Una pauta con
   respuestas no se publica como guía del estudiante; un libreto no se pega como
   respuesta a un campo de plataforma.
4. Separar hechos comprobados, declaraciones, hipótesis y modelos simulados.
   Un ejemplo puede estar completo y seguir siendo un ejemplo. Cambiar el tiempo
   verbal no transforma una propuesta en experiencia realizada.
5. Listar entregables y dependencias: qué recurso se usa, dónde y por quién.
   Si se nombra una lámina o instrumento, debe existir y servir en la tarea.

## Ejecución y cierre

Usar el [pipeline completo](.agent/workflows/docencia-completa.md) cuando haya
producción de entregables. Una consulta de lectura no necesita abrir un ciclo
de construcción. El [control de calidad](conocimiento/operacion/CONTROL_DE_CALIDAD.md)
explica cobertura, independencia y las diferencias entre comprobación técnica,
revisión pedagógica, publicación y aviso.

Los comandos del paquete trabajan sobre archivos locales. No escriben en Lirmi,
DocenteMás, Firebase, Drive ni WhatsApp. El registro administrativo o la entrega
externa requieren destino, identidad, alcance y autorización vigentes.

Informar qué se terminó, qué archivo debe abrir el docente, qué se comprobó y
qué falta. No declarar «apto» por un script silencioso ni «entregado» por un archivo
local. El resumen final distingue contenido, formatos, publicación y comunicación.

## Biblioteca y mantenimiento

- [Índice de conocimiento](conocimiento/INDICE.md): procedimientos y referencias por área.
- [Cobertura y procedencia](conocimiento/PROCEDENCIA_Y_COBERTURA.md): transferencia desde
  las once áreas de Neuromapa, límites y fuentes canónicas.
- [Reglas reutilizables de Portabot](conocimiento/portabot/LECCIONES_OPERATIVAS.md):
  identidad, integridad de campos, edición, simulación, auditoría y entrega.
- [Casos de aceptación](ejemplos/CASOS_DE_ACEPTACION.md): comportamiento esperado
  con materiales sintéticos; no son expedientes ni acreditan resultados reales.

Una modificación de un criterio obliga a revisar sus instrucciones, plantilla,
validador y casos relacionados. Conservar fuente y fecha; no añadir recetas
universales para corregir un caso particular. No releer un archivo sin cambios
si ya está en el contexto vigente; después de una compactación recuperar lo necesario.
