# Pipelines de ML: componentes y artifacts

**Clase 01 — Introducción a MLOps y ciclo de vida de un proyecto de ML**
**Duración estimada:** 18–20 min _(video largo — excepción deliberada al formato habitual de 8–15 min)_

## De qué trata este video / Agenda (1 min)

En este video vamos a ver la unidad de trabajo que van a construir durante toda la materia:
- **Qué es un pipeline de ML:** el paso del notebook a una secuencia de etapas encadenadas y repetibles.
- **Componentes y artifacts:** qué hace cada etapa y qué deja como producto persistido.
- **Reproducibilidad:** por qué un pipeline que no se puede repetir no sirve — código, datos y entorno.

**[Slide: De qué trata este video]**

---

## Introducción (1–2 min)

En el video anterior vimos el ciclo de vida completo de un proyecto de ML y quién es responsable de cada etapa. Ahora bajemos un nivel: ¿cómo se ve eso en la práctica, en el código?

Piensen en el notebook con el que vienen trabajando. Ahí adentro están casi todas las etapas del ciclo: cargan los datos, los limpian, arman features, entrenan, evalúan. El notebook **ya es un pipeline** — el problema es que es un pipeline implícito.

Y eso trae tres preguntas incómodas:

- Si les pido que reproduzcan exactamente el modelo que entrenaron hace tres meses, ¿pueden? ¿Con qué datos fue? ¿Con qué hiperparámetros?
- Si otra persona clona el repositorio y corre las celdas de arriba hacia abajo, ¿obtiene el mismo resultado?
- Cuando el modelo tenga que predecir sobre datos nuevos, ¿de dónde sale el `scaler` que ajustaron en la celda 14?

**[Slide: el notebook como pipeline implícito]**

La respuesta a las tres suele ser "no del todo". Y no es porque el notebook esté mal hecho: es porque un notebook está diseñado para explorar, no para producir. Hacer explícito ese pipeline es el trabajo de esta materia, y este video es el vocabulario que vamos a usar de acá en adelante.

---

## Desarrollo

### Punto 1: Qué es un pipeline de ML (4–5 min)

Un **pipeline** es una secuencia de etapas donde la salida de una es la entrada de la siguiente, cada una con una responsabilidad única, y que se puede ejecutar de punta a punta de forma automática.

**[Slide: definición de pipeline + diagrama de etapas encadenadas]**

Tres palabras de esa definición importan:

- **Secuencia explícita:** el orden está declarado en algún lado, no depende de en qué orden ejecutó las celdas la persona que estaba sentada frente a la máquina.
- **Responsabilidad única:** cada etapa hace una cosa. Eso permite testearla, cambiarla o reejecutarla sin tocar el resto.
- **Automática:** se dispara con un comando, o con un schedule, o con un evento — sin intervención manual.

En la práctica no hay un solo pipeline, hay al menos dos: uno que **produce** el modelo y otro que lo **usa**.

**[Slide: pipeline de entrenamiento vs pipeline de inferencia]**

**El pipeline de entrenamiento**, que corre cada tanto y produce un modelo:

1. **Ingesta de datos:** traer los datos desde su fuente.
2. **Validación de datos:** chequear que los datos son los que esperábamos — tipos, rangos, nulos. (Le vamos a dedicar una clase entera más adelante.)
3. **Preprocesamiento y feature engineering:** transformar los datos crudos en la matriz que consume el modelo.
4. **Entrenamiento:** ajustar el modelo sobre el conjunto de entrenamiento.
5. **Evaluación:** medir sobre datos que el modelo no vio y decidir si el modelo es aceptable.
6. **Registro del modelo:** guardar y versionar el modelo resultante junto con sus métricas.

**El pipeline de inferencia**, que toma ese modelo y lo aplica a datos nuevos:

1. **Ingesta de los datos nuevos.**
2. **Las mismas transformaciones** que en entrenamiento — y acá "las mismas" es literal, ya vamos a ver por qué.
3. **Carga del modelo** desde donde quedó registrado.
4. **Predicción.**
5. **Entrega de las predicciones** a quien las tenga que consumir.

**[Slide: modalidades de inferencia — batch, online, streaming]**

Ahora, ese pipeline de inferencia se puede materializar de formas muy distintas según cuándo y con qué urgencia se necesitan las predicciones:

- **En lote (*batch*):** corre cada tanto —una vez por día, por ejemplo— sobre un conjunto grande de registros, y deja las predicciones escritas en una tabla o un archivo. El consumidor las busca ahí cuando las necesita.
- **Online (*on demand*):** el modelo queda expuesto detrás de un servicio que responde de a un caso por vez, en milisegundos, cuando alguien lo consulta.
- **Streaming:** las predicciones se generan a medida que llegan eventos en un flujo continuo.

**Cuál corresponde no lo decide la tecnología, lo decide el problema.** Un scoring de riesgo crediticio que se revisa todas las noches vive perfecto en batch; una detección de fraude que tiene que frenar una transacción antes de aprobarla, no.

**En esta materia vamos a trabajar el caso batch** — es el que nos permite recorrer el ciclo completo de MLOps sin meternos con infraestructura de servicios. El serving online tiene su propia complejidad y lo van a ver más adelante en el posgrado; lo que produzcamos acá, un modelo versionado y listo para usar, es justamente el punto de partida de ese trabajo. Pero quédense con que **la modalidad es una decisión de diseño**, no la única forma de hacer inferencia.

**La clave: son dos pipelines distintos que comparten etapas.** Esa etapa compartida — la transformación de features — es el punto donde más fallan los sistemas de ML en producción, y es exactamente el problema que resuelven los artifacts. Y notemos que el problema existe igual en las tres modalidades: el modelo necesita recibir los datos transformados de la misma manera con la que aprendió, lo llame un job nocturno o una API.

**Un dato importante:** un pipeline bien cortado en etapas les da algo que el notebook no les da nunca — poder reejecutar solo la parte que cambió. Si ajustan un hiperparámetro, no necesitan volver a descargar y limpiar cuarenta gigas de datos. Retoman desde el artifact de la etapa anterior.

Todo esto lo vamos a implementar de verdad más adelante en el curso, cuando lleguemos a la orquestación. Por ahora quédense con el concepto.

---

### Punto 2: Componentes y artifacts (3–4 min)

Si el pipeline es la secuencia, el **componente** es cada etapa individual. Y un componente se define por su contrato, no por su código.

**[Slide: anatomía de un componente — entradas, parámetros, código, salidas]**

Un componente tiene:
- **Entradas:** los artifacts que consume.
- **Parámetros:** la configuración que lo gobierna (hiperparámetros, umbrales, rutas). Fuera del código, no hardcodeados.
- **Código:** la transformación en sí.
- **Salidas:** los artifacts que produce.

Que el contrato esté explícito es lo que hace que el componente sea reemplazable. Pueden cambiar por completo cómo entrenan adentro de la etapa de entrenamiento, y mientras siga recibiendo el mismo dataset y devolviendo un modelo con la misma interfaz, el resto del pipeline no se entera.

Ahora, el concepto central de este video.

**[Slide: qué es un artifact]**

Un **artifact** es cualquier objeto persistido que una etapa del pipeline produce y que otra etapa —o una persona— va a consumir después. La palabra importante es **persistido**: vive en disco o en un bucket, no en la memoria del proceso.

Los artifacts típicos de un pipeline de ML:

- El **dataset crudo** tal como se ingestó.
- El **dataset procesado**, listo para entrenar.
- Los **objetos de transformación ajustados**: el escalador, el encoder de categóricas, el imputador.
- El **modelo serializado**.
- Las **métricas** de la evaluación.
- Los **gráficos y reportes**: matriz de confusión, reporte de validación de datos.
- El **archivo de predicciones**, cuando la inferencia corre en lote.

**[Slide: el caso del scaler — training/serving skew]**

Detengámonos en el tercero, porque es el que más cuesta ver. Cuando ajustan un escalador sobre el set de entrenamiento, ese objeto **aprendió** algo de los datos: la media y el desvío de cada columna. Es un objeto entrenado, igual que el modelo.

Si guardan solo el modelo y descartan el scaler, cuando llegue el momento de predecir van a tener que volver a ajustar uno sobre los datos nuevos. Y la media de los datos nuevos no es la media del entrenamiento. El modelo va a recibir números que no corresponden a la escala con la que aprendió, y va a predecir mal — sin que nada falle, sin ningún error en pantalla. Eso se llama **training/serving skew**, y es una de las causas más comunes de modelos que funcionan perfecto en el notebook y pésimo en producción.

La conclusión: **el preprocesador ajustado es tan artifact como el modelo, y viaja con él.**

**[Slide: artifacts + metadata = linaje]**

Un artifact solo no alcanza. Necesita **metadata**: qué versión del código lo generó, qué datos de entrada usó, con qué parámetros, cuándo, y quién lo corrió. Esa cadena de "de dónde vino cada cosa" se llama **linaje** o *lineage*, y es lo que permite, seis meses después, agarrar el modelo que está en producción y responder con qué datos exactos fue entrenado.

Registrar todo eso a mano no escala, y por eso existen dos familias de herramientas que vamos a incorporar más adelante: los **sistemas de tracking de experimentos y registro de modelos**, que guardan cada corrida con sus parámetros, sus métricas y sus artifacts, y los **sistemas de versionado de datos**, que le dan a un dataset el mismo tratamiento que el control de versiones le da al código.

**Regla práctica para llevarse: si no está persistido y versionado, no existe.** Un resultado que vive en la memoria del kernel de un notebook no es un resultado del que se pueda depender.

---

### Punto 3: Reproducibilidad — versionado, lock files y semver (3–4 min)

Un pipeline vale exactamente lo que vale su capacidad de repetirse. Y para que una corrida sea reproducible hay que fijar tres cosas, no una.

**[Slide: las tres patas de la reproducibilidad — código, datos, entorno]**

- **El código:** lo resuelve el control de versiones. Es la pata que ya tienen resuelta.
- **Los datos:** un dataset que se sobreescribe rompe la reproducibilidad aunque el código esté perfectamente versionado. Lo vamos a atacar más adelante, cuando veamos versionado de datos.
- **El entorno:** las versiones exactas de Python y de cada librería instalada. Esta es la pata que más se olvida, y de la que vamos a hablar ahora.

**[Slide: ¿cómo instalamos hoy? — pip install y requirements.txt]**

Pensemos cómo vienen resolviendo esto hasta ahora. Lo más probable es que hayan instalado lo que necesitaban con un `pip install` a medida que les hacía falta, y que si tuvieron que compartir el proyecto con alguien, hayan escrito un `requirements.txt` a mano con la lista de librerías.

Eso alcanza para trabajar solo, pero deja una pregunta abierta: **¿qué versión de cada librería?** Si el archivo dice `scikit-learn`, sin más, cada persona que lo instale va a recibir la que esté publicada ese día. Y si dice `scikit-learn==1.3.2`, fijaron esa, pero no fijaron nada de lo que scikit-learn instala por debajo — numpy, scipy, joblib — que nadie escribió en ninguna lista y que igual termina en el entorno.

**[Slide: declarar vs resolver]**

Acá aparece la distinción que quiero que se lleven, y que es independiente de la herramienta que usen.

**Declarar** es decir qué necesita el proyecto, normalmente como un rango: "quiero scikit-learn 1.x, de la 1.4 para arriba". Es una intención, y es flexible a propósito: deja entrar correcciones y mejoras sin tener que tocar el archivo cada semana. Esa declaración vive en un archivo de configuración del proyecto — hoy el estándar de Python es el `pyproject.toml`, que van a conocer en detalle más adelante, cuando convirtamos el notebook en un paquete.

**Resolver** es la operación de agarrar esa declaración y decidir, para cada paquete, qué versión exacta se instala. Es un problema más difícil de lo que parece, porque hay que satisfacer al mismo tiempo todas las restricciones de todas las librerías y de las librerías de esas librerías.

El **lock file** es el resultado escrito de esa resolución. Fija la versión exacta de cada paquete —incluidas las **transitivas**, esas que nadie declaró— junto con sus hashes, que permiten verificar que el paquete que se bajó es idéntico bit a bit al que se bajó la primera vez. Lo genera la herramienta de gestión de dependencias: **no se escribe a mano.**

Y lo más importante: **el lock file se commitea al repositorio.** Es lo único que garantiza que la instalación de hoy en su máquina, la de mañana en CI y la del mes que viene en producción sean idénticas.

Sin lock file, el escenario clásico: el código es el mismo, el commit es el mismo, pero entre una instalación y otra salió una versión nueva de una librería que ustedes ni sabían que estaban usando, y el resultado numérico cambió. "En mi máquina andaba" casi siempre es un problema de entorno no fijado.

**[Slide: versionado semántico]**

Para leer esos rangos hay que entender el **versionado semántico** o *semver*. Una versión tiene tres números — `MAJOR.MINOR.PATCH`, por ejemplo `1.4.2` — y cada uno comunica algo distinto:

- **PATCH** (`1.4.2` → `1.4.3`): corrección de bugs, sin cambios de interfaz. Actualizar debería ser seguro.
- **MINOR** (`1.4.2` → `1.5.0`): funcionalidad nueva, compatible hacia atrás. Lo que ya usaban sigue funcionando.
- **MAJOR** (`1.4.2` → `2.0.0`): cambios incompatibles. Algo que funcionaba puede dejar de funcionar.

Por eso una restricción como `>=1.4,<2.0` es una declaración razonable: acepta correcciones y funcionalidad nueva, pero frena antes del cambio incompatible.

**Y acá está el punto que quiero que quede:** semver es una convención sobre la que confiamos, no una garantía. Depende de que quien publica la librería la respete, y una corrección de bug perfectamente legítima puede cambiar el tercer decimal de sus métricas. El rango declara la intención; el **lock file** es el que hace la corrida reproducible.

**Un último detalle que completa el cuadro:** fijar el entorno no alcanza si el código tiene aleatoriedad sin controlar. Los splits de datos, la inicialización de pesos, el subsampling de un random forest — todo eso necesita una semilla fija y explícita, tratada como un parámetro más del pipeline.

Y para cerrar el círculo con el punto anterior: el lock file es, él mismo, un artifact del pipeline. Es el artifact que describe el entorno en el que todos los demás fueron producidos.

---

## Cierre (1 min)

En este video pasamos del mapa general al objeto concreto que van a construir: el pipeline.

Las ideas clave para llevarse:
1. Un **pipeline** es una secuencia explícita de etapas con responsabilidad única, ejecutable de forma automática. El notebook ya es un pipeline — pero implícito.
2. Hay al menos **dos pipelines**: el de entrenamiento y el de inferencia, y comparten las transformaciones de features. La inferencia puede ser **batch, online o streaming** — la modalidad la decide el problema; en esta materia trabajamos batch.
3. Un **artifact** es todo lo que una etapa persiste para que otra lo consuma: datos procesados, transformadores ajustados, modelo, métricas, predicciones. Si no está persistido y versionado, no existe.
4. El **preprocesador ajustado viaja con el modelo**. No hacerlo es la vía directa al *training/serving skew*.
5. La reproducibilidad se apoya en tres patas: **código, datos y entorno**. El **lock file** es lo que fija el entorno; **semver** es la convención que permite leer los rangos declarados.

En la clase sincrónica van a crear el repositorio del curso y a configurar su entorno de trabajo — ahí van a generar su primer lock file y a commitearlo. La lectura de Moodle sobre gestión de dependencias tiene el paso a paso con la herramienta concreta que usamos este año.

---

## Notas de producción

- **Duración:** ~2500 palabras, unos 19 minutos hablados. **Se decidió dejarlo largo:** el tema no se parte bien y los tres puntos se sostienen entre sí. Si en alguna edición hiciera falta acortarlo, el corte natural es en dos videos —pipelines y artifacts (Puntos 1 y 2) por un lado, reproducibilidad (Punto 3) por otro— porque el Punto 3 abre con planteo propio y solo retoma que el lock file también es un artifact. Al grabar, cuidar el ritmo y marcar bien las transiciones entre puntos, que es lo que sostiene la atención en un video de esta duración.
- **Pantalla:** slides. En el Punto 2 conviene mostrar un fragmento de código real (el `fit` del scaler y el `pickle.dump` faltante) para que el training/serving skew se vea, no solo se explique. En el Punto 3, arrancar mostrando un `requirements.txt` escrito a mano (el punto de partida del alumno) y recién después el par `pyproject.toml` con rangos / extracto de `uv.lock` con versiones exactas y hashes, para que el contraste declarar-resolver se vea en pantalla.
- **Animaciones:** el diagrama de etapas se construye de a una; al llegar a features, resaltar en ambos pipelines simultáneamente la etapa compartida. En la diapositiva de modalidades, mostrar las tres ramas saliendo del mismo pipeline de inferencia (mismo modelo, mismas transformaciones, distinta forma de entrega) y atenuar online y streaming al indicar que en esta materia trabajamos batch — sin borrarlas, para que se lean como caminos válidos que se recorren en otro momento y no como opciones descartadas. Para los artifacts, mostrarlos apareciendo como "salidas" que caen de cada etapa a una capa de almacenamiento debajo del diagrama. La diapositiva de semver puede animar los tres números incrementándose por separado.
- **Referencias:** Chip Huyen, _Designing Machine Learning Systems_ (O'Reilly) — cap. 4 y 6 para feature engineering y training/serving skew; Google Cloud, *MLOps: Continuous delivery and automation pipelines in machine learning* para la anatomía del pipeline y los artifacts; [semver.org](https://semver.org) para la especificación de versionado semántico; documentación de `uv` sobre `uv.lock`.
- **Continuidad:** este video prepara el vocabulario del tracking de experimentos (MLflow), el versionado de datos (DVC) y la orquestación (Dagster). **El guion es deliberadamente agnóstico a las herramientas:** los adelantos van como "más adelante en el curso" —sin número de clase— y las herramientas se nombran por lo que hacen, no por su marca. Los nombres concretos del stack viven en las lecturas de Moodle y en la clase sincrónica, que se actualizan sin regrabar. Sostener este criterio si se editan las slides.
