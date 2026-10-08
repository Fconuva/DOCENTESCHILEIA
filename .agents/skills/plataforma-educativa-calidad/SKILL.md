---
name: plataforma-educativa-calidad
description: Construir o revisar contenido y flujos de una plataforma educativa comprobando identidad, intentos, persistencia, permisos y materiales asociados. Usar para plataformas de alumnos; no autoriza despliegues ni ensayos destructivos en producción.
---

# Calidad de plataforma educativa

Leer las instrucciones del repositorio propietario y su estado reciente. Identificar
proyecto, entorno, alias público y versión; no asumir que una copia sincronizada es
la fuente editable. La memoria sirve para localizar el propietario, no para reemplazarlo.

## Contrato de aprendizaje y de datos

Describir qué debe hacer el estudiante, qué se guarda y qué evidencia considera el
docente. Alinear guía, presentación, instrumento y plataforma. Si la actividad es
impresa, la plataforma no debe exigir respuestas digitales que el encargo no contempla.

Especificar identidad estable, curso, instrumento, intento, estado y versión de la
respuesta. Distinguir borrador, envío, recepción, evaluación y publicación de nota.
No inferir aprobación a partir de «enviado» ni cero a partir de dato ausente.

## Comprobaciones que cambian el resultado

- Releer desde el servidor tras guardar; verificar contenido y claves, no solo código HTTP.
- Comprobar pérdida de red, doble clic, recarga y timeout con fixtures o entorno de prueba.
  Reintentar sin duplicar intentos ni perder el trabajo anterior.
- Verificar permisos de estudiante/docente/administrador. Una ruta pública no debe
  exponer nóminas, diagnósticos, respuestas privadas ni claves de corrección.
- Probar límites de fecha con zona horaria explícita y casos antes/en/después del cierre.
  Conservar datos válidos ya registrados si el contrato lo exige.
- Abrir rutas reales, recursos, PDF y vínculos desde una vista de estudiante. Una
  compilación correcta no demuestra que una presentación o una descarga funcione.
- Verificar navegación, teclado, pantalla pequeña, contraste y funcionamiento sin
  recursos remotos cuando el producto sea una guía offline.

No crear matrículas, pagos ni registros reales para probar producción. Obtener
evidencia con lecturas, fixtures y simulaciones. La escritura o el despliegue deben
estar autorizados; después comprobar proyecto, versión y comportamiento público.

## Cierre y referencias

Documentar escenario, evidencia, límite y pendiente. No afirmar «todos los alumnos»
por una muestra. Mantener pruebas adecuadas al cambio; no repetirlas sin motivo.

Leer [contratos y verificación](../../../conocimiento/plataformas/CONTRATOS_Y_VERIFICACION.md)
y [control de calidad](../../../conocimiento/operacion/CONTROL_DE_CALIDAD.md).
Para contenido pedagógico abrir su skill propia. Una comprobación técnica no
reemplaza la revisión del aprendizaje, de la pauta ni de la adecuación.
