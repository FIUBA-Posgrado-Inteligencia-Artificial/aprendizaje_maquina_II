# Slides — v02: Pipelines de ML, componentes y artifacts

> Cada sección separada por `---` es una diapositiva.
> Las notas de layout y animación están entre corchetes `[ ]`.

---

## Diapositiva 1 — Portada

**Operaciones de Aprendizaje Automático I**

Pipelines de ML: componentes y artifacts

`Módulo 1 — Video 2`

[Layout: fondo oscuro, título centrado, subtítulo en gris claro. Mismo estilo que v01]

---

## Diapositiva 2 — De qué trata este video

**¿De qué trata este video?**

- **Qué es un pipeline de ML:** del notebook a una secuencia de etapas encadenadas y repetibles.
- **Componentes y artifacts:** qué hace cada etapa y qué deja como producto persistido.
- **Reproducibilidad:** código, datos y entorno.

[Layout: tres bloques que aparecen de a uno, mismo estilo que v01]

---

## Diapositiva 3 — Hook: el notebook ya es un pipeline

**El notebook que ya tienen es un pipeline**

Adentro están casi todas las etapas: cargar, limpiar, transformar, entrenar, evaluar.

**El problema es que es un pipeline implícito.**

[Layout: captura estilizada de un notebook con las celdas agrupadas por etapa y etiquetadas. La frase final aparece al último, en color de acento]

---

## Diapositiva 4 — Tres preguntas incómodas

**Tres preguntas incómodas**

- ¿Pueden reproducir exactamente el modelo que entrenaron hace tres meses?
- Si otra persona clona el repositorio y corre las celdas, ¿obtiene lo mismo?
- Cuando haya que predecir sobre datos nuevos, ¿de dónde sale el escalador de la celda catorce?

> Un notebook está diseñado para **explorar**, no para **producir**.

[Layout: las tres preguntas aparecen de a una; la cita al final, separada]

---

## Diapositiva 5 — Sección: Qué es un pipeline

**Qué es un pipeline de ML**

[Layout: diapositiva de sección, fondo de color, texto centrado]

---

## Diapositiva 6 — Definición

**Pipeline**

> Una secuencia de etapas donde la salida de una es la entrada de la siguiente,
> cada una con una responsabilidad única, ejecutable de punta a punta de forma automática.

[Layout: definición grande y centrada, sin bullets. Debajo, un diagrama simple de cuatro cajas encadenadas por flechas]

---

## Diapositiva 7 — Las tres palabras que importan

**Tres palabras de esa definición**

- **Secuencia explícita** — el orden está declarado, no depende de en qué orden se ejecutaron las celdas.
- **Responsabilidad única** — cada etapa hace una cosa: se puede testear, cambiar y reejecutar sola.
- **Automática** — se dispara con un comando, un horario o un evento. Sin intervención manual.

[Layout: tres bloques, aparecen de a uno]

---

## Diapositiva 8 — No hay un pipeline, hay dos

**Uno produce el modelo, otro lo usa**

[Layout: dos carriles horizontales paralelos, vacíos por ahora, con los títulos "Entrenamiento" y "Inferencia". Se completan en las dos diapositivas siguientes]

---

## Diapositiva 9 — Pipeline de entrenamiento

**Pipeline de entrenamiento**

1. Ingesta de datos
2. Validación de datos
3. Preprocesamiento y feature engineering
4. Entrenamiento
5. Evaluación
6. Registro del modelo

[Layout: carril superior completo, etapas apareciendo de a una. El carril de inferencia queda visible pero atenuado]

---

## Diapositiva 10 — Pipeline de inferencia

**Pipeline de inferencia**

1. Ingesta de los datos nuevos
2. **Las mismas transformaciones** que en entrenamiento
3. Carga del modelo
4. Predicción
5. Entrega de las predicciones

[Layout: ahora se completa el carril inferior. Al llegar al punto 2, resaltar simultáneamente la etapa de features en LOS DOS carriles y unirlas con una línea vertical: es la idea central del video]

---

## Diapositiva 11 — Modalidades de inferencia

**La inferencia se materializa de tres formas**

- **En lote (*batch*)** — corre cada tanto sobre muchos registros; deja las predicciones escritas.
- **Online (*on demand*)** — un servicio responde de a un caso, en milisegundos.
- **Streaming** — las predicciones se generan a medida que llegan los eventos.

> Cuál corresponde **no lo decide la tecnología, lo decide el problema.**

[Layout: las tres ramas salen del MISMO pipeline de inferencia — mismo modelo, mismas transformaciones, distinta entrega]

---

## Diapositiva 12 — Batch vs. online: el criterio

**El criterio es la decisión que hay que tomar**

| | |
|---|---|
| Scoring de riesgo que se revisa cada noche | **Batch** |
| Frenar una transacción antes de aprobarla | **Online** |

**En esta materia trabajamos batch.**

[Layout: tabla de dos filas. Al aparecer la línea final, atenuar —no borrar— online y streaming en el diagrama anterior: son caminos válidos que se recorren en otro momento]

---

## Diapositiva 13 — La idea central

**Dos pipelines distintos que comparten una etapa**

La transformación de features es **el punto donde más fallan los sistemas de ML en producción.**

Y el problema existe igual en las tres modalidades: el modelo necesita recibir los datos transformados como aprendió, lo llame un proceso nocturno o una API.

[Layout: el diagrama de los dos carriles con la etapa compartida resaltada en color de alerta]

---

## Diapositiva 14 — Ventaja concreta

**Reejecutar solo lo que cambió**

Si ajustan un hiperparámetro, no hace falta volver a descargar y limpiar cuarenta gigas de datos.

Se retoma desde el artifact de la etapa anterior.

[Layout: el diagrama del pipeline con las tres primeras etapas en gris y las últimas resaltadas]

---

## Diapositiva 15 — Sección: Componentes y artifacts

**Componentes y artifacts**

[Layout: diapositiva de sección]

---

## Diapositiva 16 — Anatomía de un componente

**Un componente se define por su contrato, no por su código**

- **Entradas** — los artifacts que consume
- **Parámetros** — la configuración que lo gobierna, fuera del código
- **Código** — la transformación en sí
- **Salidas** — los artifacts que produce

> Si respeta el contrato, se puede reemplazar por completo sin que el resto del pipeline se entere.

[Layout: una caja central "Código" con flechas de entrada y salida, y los parámetros entrando desde arriba]

---

## Diapositiva 17 — Qué es un artifact

**Artifact**

> Cualquier objeto **persistido** que una etapa produce y que otra etapa —o una persona— consume después.

Vive en disco o en un bucket. **No en la memoria del proceso.**

[Layout: definición grande. La palabra "persistido" en color de acento]

---

## Diapositiva 18 — Los artifacts de un pipeline de ML

**Qué se persiste**

- El dataset crudo, tal como se ingestó
- El dataset procesado
- **Los objetos de transformación ajustados**
- El modelo serializado
- Las métricas de la evaluación
- Los gráficos y reportes
- El archivo de predicciones

[Layout: sobre el diagrama del pipeline, mostrar cada artifact "cayendo" de su etapa a una capa de almacenamiento dibujada abajo. El tercer ítem, resaltado]

---

## Diapositiva 19 — El caso del escalador

**El escalador también aprendió**

Al ajustarlo sobre el conjunto de entrenamiento, guardó **la media y el desvío de cada columna.**

Es un objeto entrenado, igual que el modelo.

[Layout: fragmento de código real con el `fit` del escalador resaltado, y debajo el `dump` del modelo... sin el del escalador. Que se vea la ausencia]

---

## Diapositiva 20 — Training/serving skew

**Qué pasa si no lo guardan**

1. Al predecir, se ajusta un escalador nuevo sobre los datos nuevos
2. La media de los datos nuevos **no es** la del entrenamiento
3. El modelo recibe números en otra escala
4. Predice mal

**Y no falla nada. No hay ningún error en pantalla.**

> *Training/serving skew*

[Layout: los cuatro pasos aparecen de a uno; la frase en negrita, en rojo, al final]

---

## Diapositiva 21 — La conclusión

**El preprocesador ajustado es tan artifact como el modelo, y viaja con él.**

[Layout: diapositiva de una sola frase, centrada, grande]

---

## Diapositiva 22 — Artifacts + metadata = linaje

**Un artifact solo no alcanza**

Necesita **metadata**: qué versión del código lo generó, con qué datos, con qué parámetros, cuándo y quién.

> Esa cadena se llama **linaje**, y es lo que permite —seis meses después— responder con qué datos exactos se entrenó el modelo que está en producción.

[Layout: un artifact en el centro con etiquetas de metadata alrededor, encadenadas hacia atrás hasta el dato crudo]

---

## Diapositiva 23 — Regla práctica

**Si no está persistido y versionado, no existe.**

Un resultado que vive en la memoria del kernel de un notebook no es un resultado del que se pueda depender.

[Layout: frase única, centrada]

---

## Diapositiva 24 — Sección: Reproducibilidad

**Reproducibilidad**

[Layout: diapositiva de sección]

---

## Diapositiva 25 — Las tres patas

**Para repetir una corrida hay que fijar tres cosas**

- **El código** — lo resuelve el control de versiones. Esta ya la tienen.
- **Los datos** — un dataset que se sobrescribe rompe la reproducibilidad aunque el código esté perfecto.
- **El entorno** — las versiones exactas de cada librería. **La que más se olvida.**

[Layout: banco de tres patas; si falta una, se cae. Las patas aparecen de a una]

---

## Diapositiva 26 — ¿Cómo instalamos hoy?

**El punto de partida**

```bash
pip install pandas
pip install scikit-learn
```

```text
# requirements.txt
pandas
scikit-learn
```

**¿Qué versión de cada librería?**

[Layout: mostrar el requirements.txt escrito a mano. La pregunta final, en grande]

---

## Diapositiva 27 — Los dos agujeros

**Dos cosas quedan sin fijar**

- Si dice `scikit-learn`, cada persona recibe **la que esté publicada ese día**.
- Si dice `scikit-learn==1.3.2`, fijaste esa — pero no lo que instala por debajo: `numpy`, `scipy`, `joblib`.

> Nadie las escribió en ninguna lista, y terminan igual en el entorno.

[Layout: árbol de dependencias donde solo el nodo raíz está fijado y el resto queda en interrogación]

---

## Diapositiva 28 — Declarar vs. resolver

**Dos operaciones distintas**

| | |
|---|---|
| **Declarar** | Qué necesita el proyecto, normalmente como un rango. Una intención, flexible a propósito. |
| **Resolver** | Decidir qué versión exacta se instala de cada paquete, satisfaciendo todas las restricciones a la vez. |

[Layout: dos columnas. Es la diapositiva conceptual del bloque: dejarla en pantalla mientras se explica]

---

## Diapositiva 29 — El lock file

**El lock file es el resultado escrito de resolver**

- Versión **exacta** de cada paquete
- Incluidas las **transitivas**, las que nadie declaró
- Con sus **hashes**: verifican que el paquete es idéntico bit a bit
- **Lo genera la herramienta.** No se escribe a mano.

**Y se commitea al repositorio.**

[Layout: lado a lado, el archivo de declaración con rangos y un extracto del lock con versiones exactas y hashes. El contraste tiene que verse]

---

## Diapositiva 30 — Sin lock file

**"En mi máquina andaba"**

Mismo código. Mismo commit.

Pero entre una instalación y otra salió una versión nueva de una librería que ni sabías que estabas usando, y el resultado numérico cambió.

[Layout: dos máquinas con el mismo commit y distinto resultado]

---

## Diapositiva 31 — Versionado semántico

**MAJOR . MINOR . PATCH**

- **PATCH** `1.4.2` → `1.4.3` — corrección de errores. Actualizar debería ser seguro.
- **MINOR** `1.4.2` → `1.5.0` — funcionalidad nueva, compatible hacia atrás.
- **MAJOR** `1.4.2` → `2.0.0` — **cambios incompatibles.**

[Layout: los tres números grandes, y cada uno se incrementa por separado al explicarlo]

---

## Diapositiva 32 — El rango declara la intención

```text
>=1.4,<2.0
```

Acepta correcciones y funcionalidad nueva. Frena antes del cambio incompatible.

> **Pero semver es una convención, no una garantía.** Depende de que quien publica la librería la respete — y una corrección legítima puede cambiar el tercer decimal de tus métricas.

**El rango declara la intención. El lock file hace la corrida reproducible.**

[Layout: la restricción en grande arriba; la advertencia y el remate, debajo]

---

## Diapositiva 33 — El detalle que falta

**Fijar el entorno no alcanza si el código tiene azar sin controlar**

La división de los datos, la inicialización, el submuestreo de un ensamble.

> La semilla es **un parámetro más del pipeline**: va fija y explícita, con los demás.

[Layout: lista corta]

---

## Diapositiva 34 — El círculo se cierra

**El lock file también es un artifact**

Es el artifact que describe **el entorno en el que todos los demás fueron producidos.**

[Layout: volver al diagrama de artifacts de la diapositiva 18, agregando el lock file como una pieza más]

---

## Diapositiva 35 — Cierre e ideas clave

**Ideas clave de este video**

1. Un **pipeline** es una secuencia explícita de etapas con responsabilidad única. Tu notebook ya es uno — pero implícito.
2. Hay **dos pipelines**: entrenamiento e inferencia, y comparten las transformaciones. La inferencia puede ser batch, online o streaming.
3. Un **artifact** es todo lo que una etapa persiste. Si no está persistido y versionado, no existe.
4. El **preprocesador ajustado viaja con el modelo.** No hacerlo lleva directo al *training/serving skew*.
5. La reproducibilidad se apoya en **código, datos y entorno**. El **lock file** fija el entorno.

[Layout: lista numerada, cada punto aparece de a uno]

---

## Diapositiva 36 — Despedida

**¡Muchas gracias!**

Nos vemos en el próximo video.

[Layout: fondo oscuro, logo centrado. Mismo cierre que v01]
