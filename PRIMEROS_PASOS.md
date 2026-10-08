# Primeros pasos: instalar y empezar a trabajar

Esta guía es para docentes. No necesitas saber programar. En unos 20 minutos
tendrás un asistente que planifica y prepara material contigo, usando el
currículum chileno que viene dentro de esta carpeta.

## Qué necesitas

- Un computador con Windows 10 de 64 bits o superior (también funciona en Mac y Linux).
- 8 GB de memoria RAM o más. Es la recomendación del curso: con menos, el programa se pone lento.
- Una cuenta de Google personal (la de tu Gmail).
- Internet mientras trabajas.
- El programa Antigravity, que es gratuito. Se instala en el paso 1.

No necesitas instalar Python, Git ni ningún otro programa.

## Paso 1. Instalar Antigravity

1. Entra a <https://antigravity.google/download>. Descárgalo solo desde ese sitio oficial.
2. Abre el instalador y acepta las opciones que vienen marcadas.
3. Al abrir el programa, inicia sesión con tu cuenta de Google.
4. Elige el tema de colores que prefieras.
5. Cuando pregunte cómo quieres trabajar con el agente, elige **Review-driven development**.
   Así el asistente te muestra lo que va a hacer y tú lo apruebas.

## Paso 2. Descargar esta carpeta

1. Entra a <https://github.com/Fconuva/DOCENTESCHILEIA>.
2. Presiona el botón verde **Code** y luego **Download ZIP**.
3. Busca el archivo en tu carpeta Descargas, haz clic derecho y elige **Extraer todo**.
4. Mueve la carpeta extraída a **Documentos**. Se llama `DOCENTESCHILEIA-main`.

Ojo: a veces Windows deja una carpeta dentro de otra con el mismo nombre. La
correcta es la que al abrirla muestra el archivo `PRIMEROS_PASOS.md` y la
carpeta `mi_trabajo`.

## Paso 3. Abrir la carpeta en Antigravity

1. En Antigravity, ve al menú **File** y elige **Open Folder** (en español: Archivo, Abrir carpeta).
2. Selecciona `DOCENTESCHILEIA-main` y confirma.
3. Si pregunta si confías en los autores de la carpeta, responde que sí.
4. Abre el panel del asistente con **Ctrl + L** (en Mac, Cmd + L).

## Paso 4. Presentarte

En el cuadro de texto del asistente escribe:

```text
/empezar
```

El asistente te hará unas pocas preguntas (asignatura, cursos, duración de tus
clases, recursos de tu sala) y las guardará en `mi_trabajo/mi_contexto.md`.
Desde ahí ya no tendrás que repetirlas.

## Paso 5. Pedir tu primer trabajo

Escribe lo que necesitas con tus palabras. Por ejemplo:

```text
/planificar-clase 8° básico, Lengua y Literatura, 90 minutos.
Quiero trabajar el conflicto en un cuento. No tengo proyector.
```

Mientras trabaja, el asistente puede pedirte permiso para crear o cambiar
archivos. Revisa y presiona **Accept all** para aceptar. Si te muestra un plan
antes de empezar, presiona **Proceed** para que continúe.

En [QUE_PEDIR.md](QUE_PEDIR.md) hay más ejemplos listos para copiar.

## Dónde queda lo que haces

Todo se guarda en la carpeta `mi_trabajo`, ordenado por curso. Para usar un documento:

1. Ábrelo con doble clic desde el Explorador de archivos. Se abre en tu navegador.
2. Presiona **Ctrl + P**.
3. Elige tamaño **A4** y luego **Guardar como PDF** o tu impresora.

Lee siempre el documento completo antes de imprimirlo o llevarlo a la sala.
El asistente se equivoca: tú eres quien conoce a tu curso y quien decide.

## Cuida tu cuota gratuita

El plan gratuito de Antigravity tiene una cuota que se renueva cada semana.
Google no publica cuánto es y puede cambiarla. Para que te alcance:

- Pide el trabajo completo en un solo mensaje, con curso, asignatura, duración y tema.
- No repitas un pedido que ya salió bien; pide solo el cambio («en la actividad 2, cambia el texto por uno más corto»).
- Si el asistente avisa que se acabó la cuota de un modelo, prueba con otro en el selector de modelos del panel.
- Si se acabó del todo, vuelve cuando se renueve. Tus archivos siguen en `mi_trabajo`.

## Cuida los datos de tus estudiantes

No escribas nombres completos, RUT, notas ni diagnósticos de estudiantes en el
asistente. Para un ejemplo usa «Estudiante 1» o iniciales. Lo que escribes se
envía a los servidores del proveedor del modelo.

## Si algo no funciona

| Qué pasa | Qué hacer |
|---|---|
| Escribo `/empezar` y no lo reconoce | Abriste una carpeta equivocada. Vuelve al paso 3 y elige la que contiene `PRIMEROS_PASOS.md`. |
| No veo el panel del asistente | Presiona Ctrl + L. Si no aparece, cierra y abre Antigravity. |
| Pide iniciar sesión otra vez | Entra con la misma cuenta de Google del paso 1. |
| El documento se ve cortado al imprimir | En la ventana de impresión elige A4, márgenes «Predeterminados» y activa «Gráficos de fondo». |
| Quiero el documento en Word | Abre el archivo desde Word (Archivo, Abrir). Revisa que las tablas no se hayan movido. |
| Pide permiso para «ejecutar un comando» | Suele ser una búsqueda dentro de los documentos del currículum. Puedes aceptarla. Si no entiendes qué va a hacer, recházala y escríbele: «hazlo sin usar la terminal». |
| Me dio un OA que no calza | Pídele: «muéstrame el texto del OA y la página del PDF de donde lo sacaste». Los PDF oficiales están en `marco_curricular/documentos_oficiales`. |

## Actualizar el paquete

Cuando salga una versión nueva, descarga el ZIP otra vez (paso 2) y copia tu
carpeta `mi_trabajo` antigua dentro de la carpeta nueva. Así conservas tu
contexto y tus documentos.
