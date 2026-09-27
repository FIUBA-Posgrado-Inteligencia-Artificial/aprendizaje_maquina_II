# Slides — v02: Pipelines de ML, componentes y artefactos

> Cada sección separada por `---` es una diapositiva.
> Las notas de layout y animación están entre corchetes `[ ]`.

---

## Diapositiva 1 — Portada

**Operaciones de Aprendizaje Automático I**

Pipelines de ML: componentes y artefactos

`Módulo 1 — Video 2`

[Layout: fondo oscuro, título centrado, subtítulo en gris claro. Mismo estilo que v01]

---

## Diapositiva 2 — De qué trata este video

**¿De qué trata este video?**

- **Qué es un pipeline de ML:** del notebook a una secuencia de etapas encadenadas y repetibles.
- **Componentes y artefactos:** qué hace cada etapa y qué deja como producto persistido.
- **Reproducibilidad:** código, datos y entorno.

[Layout: tres bloques que aparecen de a uno, mismo estilo que v01]

---

## Diapositiva 3 — Hook: el notebook ya es un pipeline

**El notebook que ya tienen es un pipeline**

Adentro están casi todas las etapas: cargar, limpiar, transformar, entrenar, evaluar.

**El problema es que es un pipeline implícito.**

[Layout: a la derecha, un notebook dibujado como una columna de rectángulos tipo `In [1]`, `In [2]`… **sin código legible** — interesa la forma, no el contenido. La forma más rápida de armarlo es una captura de un notebook real con el código desenfocado.

Animación, en dos tiempos:
1. Primero el notebook pelado: todas las celdas iguales, sin etiquetas ni colores.
2. Después aparecen bandas de color agrupando celdas contiguas, cada una con su etapa al costado: celdas 1–3 *Ingesta y limpieza*, 4–6 *Feature engineering*, 7–8 *Entrenamiento*, 9 *Evaluación*.

Ese segundo tiempo es el momento "ah, ya estaban ahí": el alumno reconoce su propio notebook. La frase final —"es un pipeline implícito"— entra al último, en color de acento, una vez que las etiquetas ya están puestas]

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

[Layout: la definición grande y centrada, sin bullets. Debajo, el **diagrama base** del video.

**Diagrama base — armarlo una sola vez, se reutiliza cinco veces:**
- Cuatro rectángulos iguales, en fila horizontal, misma altura y separación.
- Etiquetas **genéricas** (`Etapa A`, `B`, `C`, `D`): las etapas reales llegan recién en la diapositiva 9, y ponerlas acá le compite a la definición.
- Flechas entre cajas consecutivas. Son lo único que tiene que leerse con claridad, porque son la definición hecha dibujo: *la salida de una es la entrada de la siguiente*.
- Sin colores de énfasis: es el estado neutro, del que parten todas las variaciones.

**Dónde reaparece:** duplicado en dos carriles (diapositivas 8 a 10), con la etapa compartida resaltada (11), con las primeras etapas en gris (17, usando el carril de entrenamiento real de la 10), y con los artefactos cayendo de cada etapa hacia una capa de almacenamiento (18). Conviene que sea un objeto reutilizable y no cinco dibujos distintos: la repetición visual es lo que hace que el alumno siga la misma idea a lo largo del video]

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

## Diapositiva 11 — La idea central

**Dos pipelines distintos que comparten una etapa**

⚠ Acá es donde hay más fallas en producción

[Layout: la diapositiva 10 duplicada, con tres cambios y nada más, para que se lea como el mismo diagrama:

1. Todas las cajas no compartidas pasan a gris, y los títulos de carril también.
2. Las dos cajas compartidas pasan a rojo de alerta y se unen con una línea gruesa del mismo rojo. Las dos llevan la **misma etiqueta, "Feature engineering"**: entra en dos líneas sin cortar palabras, y que diga lo mismo arriba y abajo refuerza que es la misma etapa.
3. El título pasa a "Dos pipelines distintos que comparten una etapa", y la etiqueta "⚠ Acá es donde hay más fallas en producción" va en rojo, en el hueco entre carriles a la derecha de la línea.

La frase larga —"la transformación de features es el punto donde más fallan los sistemas de ML en producción"— queda solo en la narración: en pantalla no entra y no hace falta. Si la herramienta tiene transición tipo *Magic Move* / *Morph*, usarla: el pase a gris se anima solo]

---

## Diapositiva 12 — Modalidades de inferencia

**La inferencia se materializa de tres formas**

- **En lote (*batch*)** — corre cada tanto sobre muchos registros; deja las predicciones escritas.
- **Online (*on demand*)** — un servicio responde de a un caso, en milisegundos.
- **Streaming** — las predicciones se generan a medida que llegan los eventos.

> Cambia la entrega, no el modelo ni las transformaciones: **el problema de la etapa compartida existe igual en las tres.**

[Layout: las tres ramas salen del MISMO pipeline de inferencia — mismo modelo, mismas transformaciones, distinta entrega. La etapa compartida conserva el color de alerta de la diapositiva anterior, para que se vea que atraviesa las tres ramas]

---

## Diapositiva 13 — Batch vs. online: el criterio

**Cuál corresponde no lo decide la tecnología, lo decide el problema**

| | |
|---|---|
| Scoring de riesgo que se revisa cada noche | **Batch** |
| Frenar una transacción antes de aprobarla | **Online** |

**En esta materia trabajamos batch.**

[Layout: tabla de dos filas. Al aparecer la línea final, atenuar —no borrar— online y streaming en el diagrama anterior: son caminos válidos que se recorren en otro momento. Cierra el bloque de qué es un pipeline]

---

## Diapositiva 14 — Sección: Componentes y artefactos

**Componentes y artefactos**

[Layout: diapositiva de sección]

---

## Diapositiva 15 — Anatomía de un componente

**Un componente se define por su contrato, no por su código**

- **Entradas** — los artefactos que consume
- **Parámetros** — la configuración que lo gobierna, fuera del código
- **Código** — la transformación en sí
- **Salidas** — los artefactos que produce

> Si respeta el contrato, se puede reemplazar por completo sin que el resto del pipeline se entere.

[Layout: una caja central "Código" con flechas de entrada y salida, y los parámetros entrando desde arriba]

---

## Diapositiva 16 — Qué es un artefacto

**Artefacto** *(artifact)*

> Cualquier objeto **persistido** que una etapa produce y que otra etapa —o una persona— consume después.

Vive en disco o en un bucket. **No en la memoria del proceso.**

[Layout: definición grande. La palabra "persistido" en color de acento]

---

## Diapositiva 17 — Por qué persistido: reejecutar solo lo que cambió

**Reejecutar solo lo que cambió**

Si ajustan un hiperparámetro, no hace falta volver a descargar y limpiar cuarenta gigas de datos.

Se retoma desde el artefacto de la etapa anterior.

[Layout: **vuelve el carril de entrenamiento de la diapositiva 10**, solo, sin el de inferencia: duplicar esa diapositiva y borrar el carril de abajo, así el alumno reconoce el mismo diagrama.

- *Ingesta*, *Validación* y *Feature engineering* en gris: ya corrieron, no se reejecutan.
- *Entrenamiento*, *Evaluación* y *Registro del modelo* en color: es lo único que se vuelve a correr cuando cambia un hiperparámetro.
- Entre *Feature engineering* y *Entrenamiento*, un ícono de archivo con la etiqueta "dataset procesado": es el artefacto desde donde se retoma. Si no hay espacio en la flecha, ponerlo debajo de ella con una línea que lo conecte.

Anticipa la diapositiva siguiente: acá se muestra un solo artefacto; en la 18 aparecen todos, cayendo a la capa de almacenamiento]

---

## Diapositiva 18 — Los artefactos de un pipeline de ML

**Qué se persiste**

- El dataset crudo, tal como se ingestó
- El dataset procesado
- **Los objetos de transformación ajustados**
- El modelo serializado
- Las métricas de la evaluación
- Los gráficos y reportes
- El archivo de predicciones

[Layout: sobre el diagrama del pipeline, mostrar cada artefacto "cayendo" de su etapa a una capa de almacenamiento dibujada abajo. El tercer ítem, resaltado]

---

## Diapositiva 19 — El caso del escalador

**El escalador también aprendió**

Al ajustarlo sobre el conjunto de entrenamiento, guardó **la media y el desvío de cada columna.**

Es un objeto entrenado, igual que el modelo.

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

joblib.dump(model, "model.joblib")
```

[Layout: el fragmento de código de arriba, en dos tiempos:

1. El código entero, con la línea `scaler.fit_transform(X_train)` con fondo de color y una anotación al costado: "← acá aprende la media y el desvío".
2. Debajo del `joblib.dump(model, …)`, una línea vacía con recuadro punteado rojo y la anotación "🤔 ¿Y el escalador?". Va como anotación de la diapositiva, no como comentario dentro del código: tiene que leerse como algo que *falta*, no como parte del programa. El segundo tiempo le da al alumno un segundo para notar la falta antes de señalarla.

En pantalla dice "escalador", igual que la narración — no "scaler". Los nombres de scikit-learn en el código son inevitables y estables; en la narración se sigue diciendo "el escalador"]

---

## Diapositiva 20 — Training/serving skew

**Qué pasa si no lo guardan**

1. Al predecir, se ajusta un escalador nuevo sobre los datos nuevos
2. La media de los datos nuevos **no es** la del entrenamiento
3. El modelo recibe números en otra escala
4. Predice mal

**🤫 Y no falla nada. No hay ningún error en pantalla.**

> Esto tiene nombre: ***training/serving skew***, el desfasaje entre cómo se entrenó y cómo se predice.

[Layout: los cuatro pasos aparecen de a uno; después la frase en negrita, en rojo. El nombre entra en un último click, separado: es el momento en que la narración dice "eso tiene nombre", y el término tiene que aparecer justo ahí, no antes]

---

## Diapositiva 21 — La conclusión

**El preprocesador ajustado es tan artefacto como el modelo, y viaja con él.**

[Layout: diapositiva de una sola frase, centrada, grande]

---

## Diapositiva 22 — Artefactos + metadata = linaje

**Un artefacto solo no alcanza**

Necesita **metadata**: qué versión del código lo generó, con qué datos, con qué parámetros, cuándo y quién.

> Esa cadena se llama **linaje**, y es lo que permite —seis meses después— responder con qué datos exactos se entrenó el modelo que está en producción.

[Layout: en dos tiempos, que siguen la narración. Se arma con el mismo ícono de archivo de la diapositiva 17 y tarjetas de texto chicas.

**Tiempo 1 — "un artefacto solo no alcanza, necesita metadata":** un solo artefacto, `modelo.joblib`, con una tarjeta debajo. El campo *datos* todavía dice "¿?".

**Tiempo 2 — "esa cadena se llama linaje":** el campo *datos* del modelo se completa con "procesado v3" y aparece a su izquierda el artefacto al que apunta, y después el siguiente, de derecha a izquierda, como quien sigue el rastro. Las flechas van hacia atrás a propósito: el linaje se recorre desde el modelo en producción hacia el origen.

```
📄 dataset crudo            📄 dataset procesado         📄 modelo.joblib
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│ código:  commit 7c21 │    │ código:  commit 7c21 │    │ código:  commit a3f9 │
│ datos:   tabla ventas│◀── │ datos:   crudo v4    │◀── │ datos:   procesado v3│
│ params:  —           │    │ params:  imputar=    │    │ params:  C=0.5       │
│                      │    │          mediana     │    │                      │
│ fecha:   01/03/2026  │    │ fecha:   05/03/2026  │    │ fecha:   12/03/2026  │
│ autor:   ana         │    │ autor:   ana         │    │ autor:   ana         │
└──────────────────────┘    └──────────────────────┘    └──────────────────────┘
```

- Las tres tarjetas tienen **los mismos campos**; el campo *datos* es el eslabón que apunta al artefacto de la izquierda.
- El dataset crudo es el final de la cadena: su *datos* dice de dónde se extrajo, no otro artefacto, y no tiene *params* porque no se transformó nada.
- Fechas crecientes de izquierda a derecha; commits distintos entre el procesado y el modelo, para que se vea que el código cambió y aun así se puede rastrear.
- Las versiones en *datos* ("crudo v4", "procesado v3") son la respuesta a "¿con qué datos exactos?", y anticipan el versionado de datos sin nombrar herramientas]

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

## Diapositiva 26 — ¿Cómo lo vienen resolviendo?

**¿Cómo lo vienen resolviendo?**

```bash
$ pip install pandas
$ pip install scikit-learn
$ pip install matplotlib
```

```text
# requirements.txt
pandas
scikit-learn
matplotlib
```

**¿Qué versión de cada librería?**

[Layout: es el espejo del alumno: tiene que reconocer cómo trabaja hoy antes de ver el problema. En dos tiempos:

**Tiempo 1 — [CD] "Pensemos cómo lo vienen resolviendo":** lado a lado. A la izquierda, una terminal oscura con los `pip install` apareciendo de a uno ("a medida que les iba haciendo falta"). A la derecha, el `requirements.txt` como ventana de editor clara, escrito a mano. Entre los dos, una flecha opcional: "lo pasé a mano".

**Tiempo 2 — [C] "¿qué versión de cada librería?":** al lado de cada línea del `requirements.txt` aparece un "?" en color de acento (`pandas ?`, `scikit-learn ?`, `matplotlib ?`), y abajo, grande, la pregunta.

El `requirements.txt` va **sin versiones**: el `==1.3.2` aparece recién en la 27, y adelantarlo acá le saca el efecto]

---

## Diapositiva 27 — Los dos agujeros

**Dos cosas quedan sin fijar**

- Si dice `scikit-learn`, cada persona recibe **la que esté publicada ese día**.
- Si dice `scikit-learn==1.3.2`, fijaste esa — pero no lo que instala por debajo: `numpy`, `scipy`, `joblib`.

> Nadie las escribió en ninguna lista, y terminan igual en el entorno.

[Layout: continúa la 26, reusando la misma ventana del `requirements.txt`. La pantalla se divide en dos mitades que se llenan una por click.

**[C] Mitad izquierda — sin versión, depende del día:** el archivo con `scikit-learn` a secas, y debajo dos máquinas que lo instalan en fechas distintas y reciben versiones distintas.

```
┌─ requirements.txt ─┐
│ scikit-learn       │
└────────────────────┘
      │         │
      ▼         ▼
  💻 marzo    💻 septiembre
   1.3.2       1.5.0
```

**[C] Mitad derecha — fijaste una, no las de abajo:** el archivo con `scikit-learn==1.3.2` y candado en verde; debajo, el árbol de dependencias con `numpy`, `scipy` y `joblib` en gris, borde punteado y "?". La cita al pie.

```
┌─ requirements.txt ────┐
│ scikit-learn==1.3.2 🔒│
└───────────────────────┘
          │
   ┌──────┼──────┐
   ▼      ▼      ▼
 numpy  scipy  joblib
   ?      ?      ?
```

La secuencia 26 → 27 se lee "no pusiste versión → la pusiste → igual no alcanza", y deja servidas la 28 (declarar vs. resolver) y la 29 (el lock file fija justamente esas transitivas)]

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

```toml
# pyproject.toml
[project]
name = "mi-modelo"
requires-python = ">=3.11"
dependencies = [
    "pandas>=2.2,<3",
    "scikit-learn>=1.4,<2",
]
```

```text
# Generado automáticamente. No editar a mano.
joblib==1.4.2 \
    --hash=sha256:06d478d5674cbc26…
    # via scikit-learn
numpy==1.26.4 \
    --hash=sha256:2a02aba9ed12e4ac…
    # via pandas, scikit-learn
pandas==2.2.2 \
    --hash=sha256:90c6fca2acf13916…
scikit-learn==1.4.2 \
    --hash=sha256:4ffb2ef4a1b76d71…
scipy==1.13.0 \
    --hash=sha256:1bb5f4d2de3a1b8e…
    # via scikit-learn
…
```

[Layout: los dos archivos lado a lado —la declaración a la izquierda, el extracto del lock a la derecha— con una flecha "resolver" entre ellos. El título es el único texto fijo: los bullets de antes pasan a ser **anotaciones sobre el lock**, que se resaltan de a una siguiendo la narración:

| Click | Narración | Qué se resalta en el lock |
|---|---|---|
| [CD] | "El lock file es el resultado escrito de esa resolución" | Aparecen los dos archivos y la flecha "resolver" |
| [C] | "Fija la versión exacta…" | Los `==1.4.2`, `==1.26.4`, etc. |
| [C] | "Incluidas las transitivas…" | Las líneas de `joblib`, `numpy` y `scipy`, con los `# via` resaltados: son justo las del "?" de la 27 |
| [C] | "Y con sus hashes…" | Las líneas `--hash=sha256:…` |
| [C] | "Lo genera la herramienta…" | El encabezado "Generado automáticamente. No editar a mano." |
| [C] | "…se commitea al repositorio" | Un sello o ícono de git sobre el lock: "✔ se commitea" |

Arriba de cada archivo, un contador chico: **"2 declaradas"** y **"10 instaladas"** (pandas y scikit-learn arrastran, entre otras, `python-dateutil`, `pytz`, `tzdata`, `six` y `threadpoolctl`). El contraste de tamaño tiene que verse sin leer nada.

El lock se muestra en formato `requirements.txt` con hashes y no como `uv.lock`: es el formato estándar de pip, así que no ata el video a una herramienta, y el `# via` muestra las transitivas sin explicación. Los hashes van truncados y son ilustrativos]

---

## Diapositiva 30 — Sin lock file

**🤷 "En mi máquina andaba"**

```
  💻 Tu máquina — marzo          💻 CI — septiembre
  ┌─────────────────────────┐    ┌─────────────────────────┐
  │ commit a3f9             │    │ commit a3f9             │
  │ $ pip install -r req... │    │ $ pip install -r req... │
  │                         │    │                         │
  │ numpy 1.26.4            │    │ numpy 2.0.1             │
  │ accuracy: 0.874         │    │ accuracy: 0.861         │
  └─────────────────────────┘    └─────────────────────────┘
```

[Layout: las dos máquinas de la 27, ahora con el desenlace. En tres tiempos, alineados con el teleprompter:

1. **[CD] "Mismo código. Mismo commit":** las dos máquinas, solo con las líneas idénticas (commit e instalación), en gris neutro.
2. **[C] "…salió una versión nueva… y el resultado numérico cambió":** aparecen en rojo la versión de `numpy` y la métrica. Es lo único que tiene que saltar a la vista.
3. **[C] remate:** arriba, en un recuadro, "🤷 En mi máquina andaba".

Detalles que conectan con el resto:
- El commit `a3f9` es el mismo del modelo en la tarjeta de linaje de la 22.
- La librería que cambia es `numpy`, que no está declarada: es una de las transitivas con "?" de la 27 — "la librería que ni sabían que estaban usando". En el lock de la 29 figura fijada en `1.26.4`.
- `1.26` → `2.0` es un salto *mayor*: deja servida la 31 (semver) sin decirlo]

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

**El lock file también es un artefacto**

Es el artefacto que describe **el entorno en el que todos los demás fueron producidos.**

[Layout: volver al diagrama de artefactos de la diapositiva 18, agregando el lock file como una pieza más]

---

## Diapositiva 35 — Cierre e ideas clave

**Ideas clave de este video**

1. Un **pipeline** es una secuencia explícita de etapas con responsabilidad única. Tu notebook ya es uno — pero implícito.
2. Hay **dos pipelines**: entrenamiento e inferencia, y comparten las transformaciones. La inferencia puede ser batch, online o streaming.
3. Un **artefacto** es todo lo que una etapa persiste. Si no está persistido y versionado, no existe.
4. El **preprocesador ajustado viaja con el modelo.** No hacerlo lleva directo al *training/serving skew*.
5. La reproducibilidad se apoya en **código, datos y entorno**. El **lock file** fija el entorno.

[Layout: lista numerada, cada punto aparece de a uno]

---

## Diapositiva 36 — Despedida

**¡Muchas gracias!**

Nos vemos en el próximo video.

[Layout: fondo oscuro, logo centrado. Mismo cierre que v01]
