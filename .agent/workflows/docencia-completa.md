---
description: Producir y revisar un paquete docente con fuentes, alcance, artefactos y evidencia de cierre.
---

# Pipeline docente completo

## 1. Resolver encargo y fuente

Abrir [SKILL](../../SKILL.md) y la skill de la tarea. Identificar propietario,
alcance, última decisión, modalidad y destinatarios. Registrar fuentes actuales.
Si falta un dato imprescindible, preguntar y avanzar en lo independiente;
no rellenar con vivencias, fechas ni notas inventadas.

## 2. Planear piezas y criterios

Crear contrato de entregables: archivo/formato/destinatario, criterio, dependencia
y comprobación. Alinear objetivo, actividad, recurso e instrumento. Una corrección
acotada conserva lo entregado que está fuera del alcance. No regenerar todo por comodidad.

## 3. Construir

Crear contenido y recursos completos. Separar versión del estudiante, pauta y
campos de plataforma. Guardar editables y derivados, registrar cambios y comprobar
que los recursos nombrados existen. Los ejemplos sintéticos se identifican como tales.

## 4. Verificar

Abrir archivos reales y contrastar criterios y fuente. Registrar hallazgos con
ubicación, evidencia y versión. Aplicar los controles técnicos pertinentes, renderizado
y revisión semántica; la falta de una de estas comprobaciones queda explícita.
Un parseo vacío o fallido no aprueba. Verificar el universo comprometido, no una muestra oculta.

## 5. Evaluar y corregir

Obtener dictamen independiente del constructor según [control de calidad](../../conocimiento/operacion/CONTROL_DE_CALIDAD.md).
Corregir lo observado y volver a comprobar lo afectado. Registrar la independencia
real; si no está disponible, entregar el paquete con esa revisión pendiente.

## 6. Publicar o entregar dentro del permiso

Solo si el encargo autoriza ese destino. Simular/comparar antes de escrituras
administrativas; comprobar identidad y valores de base. Después releer destino,
versión y contenido. Conservar evidencia privada cuando contenga datos personales.
Los scripts del paquete no ejecutan esta etapa ni envían mensajes.

## 7. Cerrar con evidencia

Informar archivo/enlace, versión, qué fue comprobado y próximos pasos. Si se
autorizó comunicación, verificar destinatario y envío. No llamar comunicado a una
bitácora local. Mantener estados separados: construido, revisado, publicado y comunicado.

Para registrar el control local usar `herramientas/pipeline_docente.py` y el
[esquema del registro](../../conocimiento/operacion/REGISTRO_DEL_PIPELINE.md). El ejemplo
[sintético](../../ejemplos/encargo-sintetico/control.json) ilustra una revisión pendiente;
no acredita ejecución de cuatro agentes ni un dictamen real. El script bloquea
registros incompletos y solo confirma integridad técnica del registro declarado.
