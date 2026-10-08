---
name: lirmi-registro-verificado
description: Revisar y preparar registros de notas, planificación, asistencia y firmas en Lirmi con identidad, simulación y verificación posterior. No autoriza modificaciones ni obtiene códigos de autenticación.
---

# Registro verificado en Lirmi

Abrir las reglas del repositorio propietario y el encargo vigente. Una instrucción
de revisar no autoriza escribir notas, asistencia ni firmas. Los comandos públicos
de este paquete no se conectan a Lirmi.

## Lectura y propuesta

1. Confirmar cuenta autenticada, establecimiento, año, curso, asignatura, instrumento
   y columna objetivo. Registrar identificadores disponibles; emparejar por nombre
   no decide identidad cuando hay homónimos, cambios de nómina o distinto orden.
2. Leer el estado actual completo de la columna o registro objetivo. Guardar evidencia
   local protegida; no subir nóminas, calificaciones individuales ni sesiones al repositorio.
3. Confirmar la fuente de las notas y su proyecto real. Una variable local puede apuntar
   a desarrollo; una pantalla con un valor no prueba que sea la fuente acordada.
4. Preparar diferencias fila por fila: identidad, valor actual, valor propuesto, fuente,
   justificación y acción. Separar conservar, corregir, añadir y no resuelto.
5. Simular y comparar cantidades, vacíos, escala, redondeo, fecha e instrumento.
   Un vacío no equivale a cero; una entrega incompleta no equivale a falta de aprendizaje.

No reemplazar notas existentes salvo alcance autorizado. Una excepción de un
curso privado no se convierte en regla general de este paquete.

## Ejecución autorizada

Confirmar que destino y diferencias siguen vigentes justo antes de escribir.
Si cambió la nómina, la columna o un valor de base, detener ese conjunto y recalcular.
Usar el mecanismo permitido por el propietario; conservar un respaldo de los valores
previos y el registro de acciones. Nunca eludir autenticación ni guardar códigos TOTP.
Si falta acceso, informar el bloqueo y entregar la propuesta verificable.

## Verificación y cierre

Volver a leer la columna completa desde la plataforma después de guardar, mediante
una lectura distinta de la respuesta de escritura. Comparar todas las filas objetivo
y las que debían conservarse. Un toast de éxito no prueba persistencia ni cobertura.

En planificación y firma, verificar la clase, fecha, estado y cuenta efectiva.
No firmar clases inexistentes ni completar fechas de portafolio por deducción.
Si el resultado es parcial, detallar lo persistido, lo intacto y lo pendiente;
no repetir ciegamente una operación tras un timeout.

El informe final separa propuesta, autorización, escritura y lectura posterior.
Aplicar [contratos y verificación](../../../conocimiento/plataformas/CONTRATOS_Y_VERIFICACION.md)
y el [pipeline](../../../.agents/skills/docencia-completa/SKILL.md) a los artefactos locales.
