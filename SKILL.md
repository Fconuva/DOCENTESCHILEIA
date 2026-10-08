---
name: docentes-chile-ia
description: Planificar clases, unidades y el año, crear y revisar materiales y evaluaciones para aula chilena con el currículum oficial citado, y apoyar portafolios, lectura PAES/SIMCE, diversificación y preparación ECEP. Coordina los procedimientos del paquete sin autorizar envíos ni escrituras administrativas.
---

# Docentes Chile IA

Índice de tareas del paquete. Se elige la tarea, se lee su skill completa y
solo las referencias que esa skill indica. Las instrucciones comunes están en
[AGENTS.md](AGENTS.md).

## Elegir la tarea

| Solicitud | Skill que debe leerse completa |
|---|---|
| Primera vez, saludo o «¿qué puedes hacer?» | [Empezar](.agents/skills/empezar/SKILL.md) |
| Una clase, planificación diaria o guion | [Planificar clase](.agents/skills/planificar-clase/SKILL.md) |
| Una unidad, planificación mensual o semestral | [Planificar unidad](.agents/skills/planificar-unidad/SKILL.md) |
| Planificación anual o distribución de los OA del año | [Planificar anual](.agents/skills/planificar-anual/SKILL.md) |
| Prueba, rúbrica, lista de cotejo, pauta o ticket de salida | [Crear evaluación](.agents/skills/crear-evaluacion/SKILL.md) |
| Revisar o mejorar un material ya hecho | [Revisar material](.agents/skills/revisar-material/SKILL.md) |
| Guía impresa, presentación espejo, pauta y recursos | [Creación de material](.agents/skills/creacion-material-docente/SKILL.md) |
| Enseñar lectura, construir o auditar un ensayo PAES/SIMCE | [Competencia lectora](.agents/skills/paes-simce-competencia-lectora/SKILL.md) |
| Identificar barreras, diversificar o aplicar una adecuación acordada | [DUA y adecuaciones](.agents/skills/adecuaciones-curriculares-dua/SKILL.md) |
| Preparación disciplinar y pedagógica ECEP | [Preparación ECEP](.agents/skills/ecep-preparacion/SKILL.md) |
| M1, M2, M3, ficha de grabación, revisión por rúbrica | [Portafolio docente](.agents/skills/portafolio-docente/SKILL.md) |
| Contrastar planificación, asistencia, firma o calificaciones en Lirmi | [Registro verificado](.agents/skills/lirmi-registro-verificado/SKILL.md) |
| Contenido y contratos de entrega de una plataforma educativa | [Plataforma educativa](.agents/skills/plataforma-educativa-calidad/SKILL.md) |
| Entrega formal a otra persona, con revisión independiente | [Docencia completa](.agents/skills/docencia-completa/SKILL.md) |
| Localizar memoria pertinente y comprobar vigencia | [Contexto y Neuromapa](.agents/skills/neuromapa-contexto-docente/SKILL.md) |

Si se trabaja dentro de una instalación privada de Portabot, abrir primero su
AGENTS y su índice de reglas actual y aplicar sus skills canónicas. No usar esta
edición pública como permiso, precio ni estado actual de un cliente. Para las
otras tareas, las instrucciones del repositorio propietario y del establecimiento
también prevalecen sobre una nota histórica.

## Entrada que cambia las decisiones

1. Distinguir consulta, propuesta, construcción, corrección, revisión o entrega.
   No rehacer lo que el docente ya aprobó por una preferencia del agente.
2. Confirmar nivel, asignatura, duración y versión de las fuentes. Buscar
   primero los datos existentes en `mi_trabajo/mi_contexto.md`; no pedir al
   docente un documento público que el paquete ya trae.
3. Identificar destinatarios: estudiante, docente y plataforma. Una pauta con
   respuestas no se publica como guía del estudiante; un libreto no se pega como
   respuesta a un campo de plataforma.
4. Separar hechos comprobados, declaraciones, hipótesis y modelos simulados.
   Un ejemplo puede estar completo y seguir siendo un ejemplo. Cambiar el tiempo
   verbal no transforma una propuesta en experiencia realizada.
5. Listar entregables y dependencias: qué recurso se usa, dónde y por quién.
   Si se nombra una lámina o instrumento, debe existir y servir en la tarea.

## Ejecución y cierre

El material de aula propio del docente se construye, se revisa con la lista de
[errores típicos](conocimiento/docencia/ERRORES_TIPICOS_DE_LA_IA.md) y se
entrega declarando lo no comprobado. Una entrega formal a otra persona usa el
[pipeline completo](.agents/skills/docencia-completa/SKILL.md) y el
[control de calidad](conocimiento/operacion/CONTROL_DE_CALIDAD.md), que
explican cobertura, independencia y las diferencias entre comprobación técnica,
revisión pedagógica, publicación y aviso.

Los comandos del paquete trabajan sobre archivos locales. No escriben en Lirmi,
DocenteMás, Firebase, Drive ni WhatsApp. El registro administrativo o la entrega
externa requieren destino, identidad, alcance y autorización vigentes.

Informar qué se terminó, qué archivo debe abrir el docente, qué se comprobó y
qué falta. No declarar «apto» por un script silencioso ni «entregado» por un archivo
local. El resumen final distingue contenido, formatos, publicación y comunicación.

## Biblioteca y mantenimiento

- [Currículum nacional](marco_curricular/CURRICULUM_NACIONAL.md): qué rige,
  documentos por nivel y cómo encontrar y citar un OA.
- [Índice de conocimiento](conocimiento/INDICE.md): procedimientos y referencias por área.
- [Cobertura y procedencia](conocimiento/PROCEDENCIA_Y_COBERTURA.md): fuentes,
  límites y transferencia desde las áreas privadas.
- [Reglas reutilizables de Portabot](conocimiento/portabot/LECCIONES_OPERATIVAS.md):
  identidad, integridad de campos, edición, simulación, auditoría y entrega.
- [Casos de aceptación](ejemplos/CASOS_DE_ACEPTACION.md): comportamiento esperado
  con materiales sintéticos; no son expedientes ni acreditan resultados reales.

Una modificación de un criterio obliga a revisar sus instrucciones, plantilla,
validador y casos relacionados. Conservar fuente y fecha; no añadir recetas
universales para corregir un caso particular. No releer un archivo sin cambios
si ya está en el contexto vigente; después de una compactación recuperar lo necesario.
