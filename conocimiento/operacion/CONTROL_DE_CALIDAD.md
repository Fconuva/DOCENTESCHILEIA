# Control de calidad y evidencia

## Cuatro funciones, revisión real

| Función | Responsabilidad | Producto |
|---|---|---|
| Planeador | Resolver encargo, fuentes, criterios y dependencias | Plan y contrato de piezas |
| Constructor | Crear o corregir dentro del alcance | Archivos y registro de cambios |
| Verificador | Contrastar archivos con criterios y fuentes | Hallazgos con ubicación y evidencia |
| Evaluador | Decidir sobre hallazgos y cobertura | Dictamen razonado con pendientes |

Las funciones no prueban independencia por sus nombres. Registrar quién actuó,
qué versión abrió y qué comprobó. El verificador y el evaluador deben ser distintos
del constructor y entre sí para registrar una revisión independiente completa.
Si solo está disponible un agente, puede construir y autocontrolar; declarar pendiente
la revisión independiente. No inventar cuatro identidades para completar un registro.

## Coberturas que se informan por separado

1. **Fuente y alcance**: modalidad correcta, última decisión, versión de manual/rúbrica,
   identidad y destinatarios. Una nota o un barrido de nombres no reemplazan esto.
2. **Contenido**: exactitud, coherencia objetivo/tarea/evidencia, apoyos y ausencia de
   vivencias inventadas. Citar el criterio específico, no aprobar por palabras clave.
3. **Integridad**: todos los campos, piezas y recursos requeridos existen y corresponden.
   Una falla de lectura, parseo o acceso deja su cobertura pendiente, nunca aprobada.
4. **Formato y uso**: abrir los archivos reales; comprobar edición, impresión y recursos.
   La detección de CSS no acredita el renderizado. La revisión digital no es prueba física.
5. **Publicación**: proyecto, ruta, versión y lectura posterior. Una copia local no es
   una entrega externa; un HTTP 200 no prueba identidad ni contenido.
6. **Comunicación**: autorización vigente, destinatario, archivo y acción pendiente del
   docente. Envío, recepción y lectura son hechos distintos.

## Registro verificable

Cada criterio tiene resultado `cumple`, `no_cumple`, `no_verificado` o `no_aplica`.
`no_aplica` exige razón. Anotar ubicación, fuente y evidencia; los conteos tienen
denominador. No aprobar el universo porque una muestra salió bien ni la calidad
pedagógica porque una herramienta no mostró errores.

El comando `pipeline_docente.py` valida estructura, archivos, hashes e independencia
declarada de un registro. No verifica la honestidad de esas declaraciones ni emite
un certificado pedagógico. `validar_material_docente.py` informa únicamente controles
técnicos parciales. `validar_repositorio.py` comprueba metadatos y referencias locales.

Corregir hallazgos reales y volver a comprobar lo afectado. Mantener versiones de
base y evitar regenerar un módulo entregado si el encargo solo pide una pieza.
No repetir pruebas aprobadas cuando no cambió nada relevante.

## Archivos compartidos y privacidad

Antes de editar, comprobar estado Git y dueño de la ruta. Usar un checkout aislado
si hay cambios concurrentes. No borrar trabajo ajeno, forzar push ni retirar locks
activos. Preparar commit con rutas explícitas; no usar `git add -A`, stash ni autostash.
Verificar ascendencia remota antes de publicar y lectura de la versión publicada.

Guardar localmente expedientes y evidencia sensible según las reglas del propietario.
Antes de publicar revisar texto, XML, comentarios, alt, propiedades, metadatos y enlaces.
La visualización anónima no basta si el archivo conserva nombres en su interior.
No debilitar los guardas de privacidad para que pase una entrega.

## Estados de cierre

`PROPUESTA` → `CONSTRUIDO` → `REVISADO` → `PUBLICADO/ENTREGADO` → `COMUNICADO`.
Una tarea puede cerrar en construido o revisado si ese era el encargo. Anotar explícitamente
lo que no se ha realizado. «Apto» requiere dictamen con cobertura y pendientes resueltos;
«entregado» requiere evidencia del destino; «recibido/leído» requiere evidencia adicional.
