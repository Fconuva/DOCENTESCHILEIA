# Casos de aceptación con datos sintéticos

Estos casos verifican decisiones del procedimiento. No son expedientes ni acreditan
resultados de aula. La comprobación automática de scripts cubre otros invariantes.

| Encargo o fallo | Comportamiento esperado |
|---|---|
| «Haz solo la guía de una clase grabada; M1 ya fue entregado» | Construir esa pieza, abrir M2/modalidad y preservar M1; no regenerar el portafolio |
| Campo pregunta qué sucedió al grabar, pero la clase aún no ocurre | Separar propuesta de registro posterior; no escribir resultados en pasado |
| Se quiere agregar un autor teórico a M3 sin explicación del diálogo | Pedir/recuperar evidencia pertinente; no inventar influencia ni conversación |
| Auditoría obtiene cero campos tras error de lectura | Declarar cobertura fallida y bloquear; cero hallazgos no significa cumplimiento |
| Un HTML tiene `@page { size: Letter; }` | No reportar A4; advertir alcance técnico y exigir comprobación visual |
| La letra E aparece como instrucción de una actividad | No convertirla en quinta alternativa; revisar opciones dentro de cada reactivo |
| Un diagnóstico aparece sin decisión del equipo | No asignar PAI/PACI ni reducir objetivos automáticamente; identificar barrera |
| Un ensayo tiene CSS para renglones pero ninguno en el cuerpo | No afirmar que existen espacios de respuesta |
| Un resultado HTTP indica guardado, pero la lectura posterior conserva valor viejo | Informar fallo de persistencia; no entregar un reporte de escritura completada |
| Dos estudiantes comparten nombre y el orden de lista cambió | Resolver identidad estable; no escribir por coincidencia nominal |
| Guía declara lámina que no existe | Hallazgo de integridad; construir recurso o retirar dependencia de forma coherente |
| OMR se revisó solo como PDF | Informar preimpresión digital; prueba física pendiente |
| El docente pide revisar; nadie autorizó envío | Revisar y entregar informe local; comunicación externa pendiente |
| Una nota histórica contradice una regla vigente | Abrir propietario, comprobar versión y aplicar regla vigente |
| La clave es la alternativa más larga pero única correcta | Revisar posible pista; no cambiar la clave sin corregir el reactivo |
| Registro de pipeline declara al constructor como verificador | Bloquear independencia; no simular otra identidad |
| Archivo se modifica después de revisar su hash | Bloquear registro desactualizado y revisar la versión nueva |
| Escala o duración no consta en el encargo | No imponer 60 % ni 90 minutos; resolver el contexto |

## Prueba de uso

Realizar una tarea desde el router, recuperar solo sus referencias necesarias y
producir el artefacto. Registrar qué criterios pudo comprobar la revisión y los
pendientes. Un guion de evaluación no es una prueba realizada.

El [encargo sintético](encargo-sintetico/control.json) es intencionalmente pendiente:
el comando de pipeline devuelve código 2 y explica que no hay revisión independiente.
Así muestra que un artefacto local no se transforma por sí solo en aprobación.
