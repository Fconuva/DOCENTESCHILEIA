# Docentes Chile IA

Skills, agentes, procedimientos, plantillas A4 y herramientas locales para
planificar, construir y revisar trabajo docente en Chile. Incluye portafolios
M1/M2/M3, material de aula, inclusión, lectura PAES/SIMCE, preparación ECEP,
registros verificables y calidad de plataformas educativas.

La ampliación incorpora criterios operativos y pedagógicos de Portabot y de las
áreas de Neuromapa. Los procedimientos públicos están despersonalizados:
los casos de clientes, diagnósticos, pagos, chats y credenciales permanecen privados.
No se promete calificación ni infalibilidad de un modelo.

## Usar el paquete

Clonar el repositorio y abrir su carpeta con el agente:

```bash
git clone https://github.com/Fconuva/DOCENTESCHILEIA.git
cd DOCENTESCHILEIA
```

[SKILL.md](SKILL.md) es la entrada completa. [AGENTS.md](AGENTS.md) y
[CLAUDE.md](CLAUDE.md) comparten instrucciones. Las skills especializadas tienen
metadatos de selección y referencias a los procedimientos del paquete.

Para instalar la entrada en un perfil de Claude o Codex, usar el instalador
del paquete. Primero muestra el destino; `--aplicar` instala una copia completa
sin sobrescribir una instalación existente. No modifica conectores ni otras skills.

```bash
python herramientas/instalar_skill.py --cliente codex
python herramientas/instalar_skill.py --cliente claude --aplicar
```

Peticiones que puede resolver:

- «Revisa este M1 contra la rúbrica de mi modalidad; conserva mi tema y señala
  qué evidencia falta antes de afirmar resultados».
- «Prepara la clase grabada con lo que hay en mi sala, un libreto conducible,
  guía, presentación y pauta; comprueba qué imprimir».
- «Convierte la idea del M3 en propuesta completa, sin inventar reuniones,
  participantes ni resultados».
- «Haz una guía impresa y su presentación espejo; deja espacio real para escribir».
- «Audita este ensayo y distingue revisión de contenido, PDF y prueba física OMR».

## Skills y conocimiento

| Área | Entrada y procedimiento |
|---|---|
| Portabot / portafolios | [Skill](.github/skills/portafolio-docente/SKILL.md), [M1](.github/skills/portafolio-docente/references/m1.md), [M2](.github/skills/portafolio-docente/references/m2.md), [M3](.github/skills/portafolio-docente/references/m3.md) |
| Aula e impresión | [Skill de material](.github/skills/creacion-material-docente/SKILL.md), [planificación y paquete](conocimiento/docencia/PLANIFICACION_Y_PAQUETE.md) |
| PAES / SIMCE | [Skill](.github/skills/paes-simce-competencia-lectora/SKILL.md), [diseño y aplicación](conocimiento/docencia/LECTURA_Y_EVALUACION.md) |
| DUA / adecuaciones | [Skill](.github/skills/adecuaciones-curriculares-dua/SKILL.md), [referencia](guias_metodologicas/DISENO_UNIVERSAL_APRENDIZAJE_DUA.md) |
| ECEP | [Skill](.github/skills/ecep-preparacion/SKILL.md), dossiers y temarios conservados en sus carpetas |
| Lirmi | [Skill de contraste y registro](.github/skills/lirmi-registro-verificado/SKILL.md) |
| Plataformas | [Skill](.github/skills/plataforma-educativa-calidad/SKILL.md), [contratos y producción](conocimiento/plataformas/CONTRATOS_Y_VERIFICACION.md) |
| Memoria y tokens | [Skill de contexto](.github/skills/neuromapa-contexto-docente/SKILL.md), [vigencia](conocimiento/operacion/MEMORIA_Y_VIGENCIA.md) |

La [biblioteca](conocimiento/INDICE.md) contiene el detalle. El
[pipeline](.agent/workflows/docencia-completa.md) y los cuatro agentes de
`.github/agents/` distribuyen planeación, ejecución, verificación y evaluación.
La independencia se acredita por actuaciones reales, no por cuatro títulos.
El [ejemplo de clase impresa](ejemplos/clase-interpretacion-2medio/CONTEXTO.md)
incluye guía y pauta terminadas en HTML/PDF, con comprobaciones y límites explícitos.

## Comprobar los archivos

Python 3.12 o superior, sin dependencias externas para las herramientas locales:

```bash
python herramientas/validar_repositorio.py
python -m unittest discover -s tests -v
python herramientas/validar_material_docente.py documentos_modelo/guias_aprendizaje/Guia_Modelo_Regular_A4.html
python herramientas/pipeline_docente.py ejemplos/encargo-sintetico/control.json
```

Los validadores informan cobertura y límites. No califican semánticamente un
objetivo, no acreditan una clase realizada y no certifican una impresora o escáner.
La revisión pedagógica abre los materiales y usa las fuentes propias del encargo.
El ejemplo de pipeline devuelve código 2 porque está pendiente intencionalmente;
el [esquema del registro](conocimiento/operacion/REGISTRO_DEL_PIPELINE.md) explica
cómo registrar un trabajo real. Un resultado técnico completo tampoco certifica pedagogía.
La [verificación de la ampliación](conocimiento/VERIFICACION_2026-10-07.md) documenta
las pruebas realizadas, los hallazgos corregidos y los límites del resultado.

## Fuentes, alcance y derechos

Las exigencias oficiales se consultan en su proceso, modalidad y versión:
[DocenteMás 2026](https://www.docentemas.cl/comienza-la-elaboracion-del-portafolio-2026/),
[Mineduc: Decreto 83](https://bibliotecadigital.mineduc.cl/handle/20.500.12365/14490)
y [DEMRE: publicaciones](https://portaldemre.demre.cl/publicaciones).
No confundir año de aplicación con admisión ni un temario ECEP con un manual de Portafolio.
La matriz de 2026 es una referencia fechada, no una certificación de vigencia futura.

El código y la documentación originales del proyecto se distribuyen bajo MIT.
Los documentos oficiales y recursos de terceros conservan sus derechos y
condiciones de uso; su presencia no les asigna la licencia MIT. Las plantillas
son ejemplos adaptables: membretes, fuentes, márgenes, niveles y escalas se
ajustan al establecimiento y al material acordado.

Autor: Francisco Javier Núñez Valenzuela. [Procedencia y cobertura de la ampliación](conocimiento/PROCEDENCIA_Y_COBERTURA.md).
