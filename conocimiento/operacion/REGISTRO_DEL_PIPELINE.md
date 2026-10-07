# Registro local del pipeline

`python herramientas/pipeline_docente.py ruta/control.json` lee el registro y archivos
relativos a su directorio. No admite rutas que salgan de ese directorio, no escribe
archivos, no se conecta a plataformas y no transforma declaraciones en hechos verificados.

## Esquema versión 1

| Campo | Contenido |
|---|---|
| `version` | Número entero `1` |
| `encargo`, `alcance` | Texto que identifica tarea y universo comprometido |
| `fuentes` | Lista no vacía de objetos `ruta`, `sha256` |
| `artefactos` | Lista no vacía de objetos `ruta`, `sha256`, `destinatario` |
| `criterios` | Lista no vacía con `id`, `resultado`, `fuente`, `ubicacion`, `razon`, `evidencia` |
| `roles` | Identidades reales de `planeador`, `constructor`, `verificador`, `evaluador` |
| `revisiones` | Reportes de verificador y evaluador: `rol`, `identidad`, `estado`, `evidencia` |

`evidencia` es un objeto `ruta`, `sha256`. Generar SHA-256 del archivo exacto revisado;
si después cambia, el registro ya no valida. Un hash identifica bytes, no calidad.
`fuente` y `ubicacion` deben permitir interpretar el criterio y encontrar su evidencia;
el script exige campos, pero la revisión contrasta su significado.

Cada criterio tiene `cumple`, `no_cumple`, `no_verificado` o `no_aplica`. Solo cumple o
no aplica con razón y evidencia permiten completar el registro técnico. No registrar
no aplica para ocultar una falta de comprobación. El constructor no puede figurar
como verificador ni evaluador independiente; tampoco el mismo revisor en ambos roles.
Las identidades declaradas se verifican en el proceso real, no por el script.

## Resultados

Código 2: registro pendiente o inválido, con errores concretos. Código 0:
`REGISTRO_TECNICO_COMPLETO_NO_CERTIFICA_PEDAGOGIA`. Un registro completo no publica,
entrega ni certifica; el dictamen humano/agente con evidencia conserva su propio alcance.

El [ejemplo sintético](../../ejemplos/encargo-sintetico/control.json) está pendiente
intencionalmente. No copiarlo como auditoría realizada. Reemplazar sus campos con hechos
y reportes reales al trabajar. No completar actores ni revisiones ficticias para aprobar.

Los tests construyen registros sintéticos para comprobar rutas, hashes, vacíos,
independencia declarada y fallos. No son evaluación de un portafolio ni certificado.
