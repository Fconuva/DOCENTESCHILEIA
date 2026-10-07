# Docentes Chile IA: instrucciones comunes

Escribir en español con ñ y tildes. Leer [SKILL.md](SKILL.md) para elegir el
procedimiento y después las referencias de la tarea. Este repositorio contiene
procedimientos públicos; los expedientes de docentes y estudiantes permanecen
fuera de Git. No convertir una recomendación local en exigencia del Mineduc.

Una solicitud de construir o corregir autoriza esos cambios; no autoriza enviar
mensajes, cobrar, modificar notas, firmar asistencia ni finalizar un portafolio.
Conservar el alcance y las decisiones del docente. Leer las fuentes actuales,
declarar lo que no se pudo comprobar y revisar los archivos finales abiertos.

Cuando exista una instalación privada de Portabot, sus AGENTS y el índice
_gestion/REGLAS.md vigente gobiernan sus casos. Este paquete público no reemplaza
sus acuerdos, controles ni permisos. Lo mismo aplica al repositorio propietario
de una plataforma educativa y al establecimiento que usa Lirmi.

Para producir entregables, aplicar el [pipeline](.agent/workflows/docencia-completa.md).
Planeador, ejecutor, verificador y evaluador registran actuaciones reales; no
inventar independencia cambiando el nombre del mismo agente. Una revisión técnica
no acredita calidad pedagógica ni ejecución en aula. Si falta un revisor
independiente, cerrar como pendiente de revisión, sin simular su firma.

Antes de publicar este paquete: ejecutar los tests y
`python herramientas/validar_repositorio.py`. Agregar rutas explícitas, revisar
el diff, commit acotado y push. No usar `git add -A`, stash ni autostash en un
checkout compartido. Conservar cambios ajenos; usar un checkout aislado si hace falta.

Los ejemplos del paquete son sintéticos. No publicar nóminas, diagnósticos
individuales, chats, credenciales, cartolas, videos de estudiantes ni enlaces
privados. Las fuentes oficiales externas conservan sus derechos y fecha.
