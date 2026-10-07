# Contratos de datos y verificación de plataformas

## Estado real del sistema

Confirmar proyecto, entorno, cuenta y fuente de datos. Las variables locales pueden
apuntar a otra base. Antes de decidir sobre producción, leer la fuente acordada;
no mezclar nóminas ni instrumentos solo porque sus nombres coinciden.

| Operación | Simulación local | Comprobación posterior |
|---|---|---|
| Guardar respuesta | Identidad, instrumento, intento, versión y contenido | Relectura desde servidor con las mismas claves |
| Enviar intento | Borrador completo, validación y tratamiento de duplicados | Estado persistido y respuesta íntegra |
| Calificar | Criterios, evidencia y escala aprobada | Resultado y fuente; vacíos preservados según contrato |
| Cambiar nota | Diferencias completas, valores de base y autorización | Columna completa incluyendo filas conservadas |
| Publicar recurso | Ruta, dependencias y destinatario | Apertura pública/autenticada en el entorno real |
| Cerrar inscripción | Límite explícito y zona horaria | Antes/en/después con fixtures; preservar registros existentes |

## Identidad y completitud

Usar UID, claves de curso e instrumento u otra identidad estable. El nombre puede
ayudar a reconciliar, pero no determina una escritura. Si el orden cambia, recalcular
el emparejamiento y resolver ambiguos antes de actuar.

Separar guardado, enviado, evaluado y publicado. Registrar qué se espera de cada
estado. No llamar completo a un intento que tiene campos vacíos requeridos; no
convertir un fallo de red en cero. Conservar borradores y permitir recuperación.

## Concurrencia y fallos

Probar reintentos, doble clic, recarga y timeout con datos sintéticos. El mismo intento
no debe generar duplicados. Antes de un cambio administrativo, releer los valores
de base; si cambiaron, detener y preparar nuevas diferencias. Después de un timeout,
leer antes de repetir, porque la primera escritura pudo persistir.

Simular primero y escribir solo con alcance autorizado. No crear alumnos, reservas,
pagos ni inscripciones reales como prueba. La lectura de salud HTTP solo prueba esa
respuesta; no certifica conexión de un bot ni disponibilidad de todos los servicios.

## Permisos, recursos y cierre

Comprobar acceso por rol y evitar información de estudiantes en rutas públicas.
La pauta, las claves y las nóminas no viajan dentro del archivo del estudiante.
Abrir rutas y dependencias reales, no solo el código. Verificar versión publicada,
PDF descargado, presentación y vista en pantalla pequeña cuando corresponda.

El cierre distingue pruebas locales, lectura en producción, escritura, despliegue
y comunicación. Un reporte describe universo, muestra y límites. No usar «todo OK»
para cubrir permisos, persistencia, aprendizaje y entrega con una única comprobación.
