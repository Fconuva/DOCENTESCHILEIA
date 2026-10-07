# Verificación de la ampliación · 7 de octubre de 2026

## Comprobaciones realizadas

- 32 pruebas de regresión de scripts: lectura fallida/vacía, reactivos por pregunta,
  opciones duplicadas, tamaño Letter frente a A4, CSS sin elementos, imágenes ausentes,
  claves expuestas, hashes cambiados, rutas fuera del encargo, revisiones pendientes,
  independencia declarada, JSON incorrecto e instalación no destructiva.
- Nueve entradas SKILL con metadatos válidos: router y ocho especializadas. Se usó
  también el validador de skill-creator, no solo el comprobador del repositorio.
- Referencias locales resueltas por `validar_repositorio.py`; cero enlaces rotos.
  No se verificaron todas las anclas ni la disponibilidad futura de cada enlace externo.
- Doce HTML comprobados técnicamente: cinco modelos, sus cinco plantillas y dos
  archivos del ejemplo de uso. Cero errores técnicos y sin hojas de estilo remotas.
  Los modelos se identifican como editables pendientes de completar, no productos finales.
- Revisión de publicación de los archivos modificados y nuevos: procedimientos
  despersonalizados, sin expedientes ni importación de chats/caja. Escaneo complementario
  de claves privadas, tokens, JID, RUT formateados y rutas privadas: cero alertas.
- Simulación de instalación en ambos clientes y pruebas de preservación de destinos
  existentes. La instalación copia referencias completas y no configura hooks/MCP.

## Prueba de uso independiente

Un agente distinto del autor del paquete recibió un encargo sintético de guía de
una página para 2.º medio, sin proyector, M1 fuera de alcance y sin resultados de
aplicación. Usó el router y referencias; produjo guía y pauta separadas. Renderizó
y abrió visualmente tres páginas A4 en grises. El ejemplo conserva ficción rotulada,
instrucciones segmentadas y criterios, sin adecuación individual automática.

Durante la prueba se encontraron reglas antiguas de PAI/PACI y contradicciones de
plantilla. Se corrigieron objetivo, diagnóstico, claves visibles, escala y duración.
Un contraste posterior verificó la correspondencia de las cinco parejas por hash.
La edición detectó corrupción de tildes en una conversión PowerShell; se regeneró
en UTF-8 y comprobó antes de publicar. Después se retiraron las fuentes remotas
y rótulos normativos que podían inducir una asignación automática.

El responsable del paquete abrió guía y pauta, revisó su contenido y vista de la
guía y comprobó páginas/metadatos de ambos PDF antes de incorporar el ejemplo.
No se presentan estas comprobaciones como dictamen oficial de M2.

## Límites del resultado

La prueba no acredita clase realizada, efectos de aprendizaje, impresión física,
lectura OMR ni cumplimiento completo de una rúbrica de modalidad. En el ejemplo
quedan pendientes fuente curricular/modalidad, tiempos reales y aplicación.
Los scripts no ejecutaron registros en Lirmi, plataformas, envíos ni cobros.
El ejemplo de pipeline mantiene estado pendiente y código 2; no se fabricaron
actores ni revisiones para que aprobara. La integridad técnica de un registro
completo tampoco certifica la veracidad o calidad de sus declaraciones.
