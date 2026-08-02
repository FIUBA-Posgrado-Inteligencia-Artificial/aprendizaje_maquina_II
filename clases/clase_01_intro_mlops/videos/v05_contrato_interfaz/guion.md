# Contrato de interfaz: qué recibimos y qué entregamos

**Clase 01 — Introducción a MLOps y ciclo de vida de un proyecto de ML**
**Duración estimada:** 21–23 min _(video largo — excepción deliberada al formato habitual de 8–15 min)_

## De qué trata este video / Agenda (1 min)

En este video vamos a ver cómo se entrega un modelo para que otro lo pueda usar:
- **El contrato de interfaz:** qué es, y por qué un modelo se entrega con un contrato y no suelto.
- **Qué viaja con el modelo:** todo lo que hay que entregar además del archivo del modelo.
- **Cuando la tecnología del otro lado es distinta:** qué hacer si quien consume el modelo no corre Python.

**[Slide: De qué trata este video]**

---

## Introducción (1–2 min)

Ustedes están en el medio de una cadena.

Por un lado **reciben** algo: un notebook que entrena un modelo sobre un dataset, producido en la etapa anterior de su formación. Por el otro lado van a **entregar** algo: un proceso reproducible que produce un modelo versionado y predicciones confiables, que alguien más va a consumir.

**[Slide: la cadena — recibimos / transformamos / entregamos]**

Y acá está el problema. Cuando el trabajo cruza de un equipo a otro, lo que se pierde no suele ser el modelo: el archivo llega bien. Lo que se pierde es **todo lo que quien lo entrenó sabía y no escribió.** Que la columna de ingresos venía en miles y no en pesos. Que las categorías nuevas hay que mapearlas a "otros". Que el umbral de decisión no es 0.5.

Nada de eso está en el archivo del modelo. Y si no está escrito en ningún lado, el que recibe va a inventarlo — y lo va a inventar distinto.

De eso se trata un contrato de interfaz: de hacer explícito lo que hoy vive en la cabeza de una persona.

---

## Desarrollo

### Punto 1: Qué es un contrato de interfaz (3 min)

Un **contrato de interfaz** es el acuerdo explícito entre quien produce algo y quien lo consume: qué se entrega, en qué formato, con qué garantías, y qué cosas expresamente **no** se prometen.

**[Slide: definición + analogía con una API]**

La idea no es nueva ni es de ML: es la misma que hay detrás de cualquier API. Si dos equipos acuerdan la interfaz, pueden trabajar en paralelo sin reunirse todos los días, y cada uno puede cambiar lo que tiene adentro mientras respete lo acordado. El contrato es lo que permite que los cambios de un lado no rompan el otro.

En un sistema de ML el contrato tiene **tres capas**, y no reciben ni de cerca la misma atención:

1. **El artefacto:** qué objeto se entrega y en qué formato. Es la capa que todo el mundo recuerda.
2. **Los datos:** qué espera recibir el modelo para funcionar, y qué devuelve. Es la capa donde se rompen las cosas.
3. **Las garantías operativas:** con qué calidad funciona, sobre qué población fue medido, y hasta cuándo se puede confiar en eso. Es la capa que nadie escribe.

Y el problema está justamente en esa progresión: **la atención que le damos a cada capa es inversa a los problemas que causa.** La primera se cuida sola, porque sin el archivo no hay nada que hacer. La segunda y la tercera, que son las que después explican los incidentes, quedan libradas a que alguien se acuerde de escribirlas.

**La clave: un contrato implícito no es un contrato.** Es un conjunto de supuestos que funcionan hasta el día que alguien cambia algo. Y como en ML nada falla ruidosamente —el modelo siempre devuelve un número— el día que se rompe, nadie se entera.

---

### Punto 2: Qué viaja con el modelo (4 min)

Entonces, ¿qué hay que entregar? El archivo del modelo es apenas el principio.

**[Slide: el paquete completo — el modelo es una pieza entre varias]**

**1. El modelo entrenado.** Serializado en un formato que el consumidor pueda abrir.

**2. Las transformaciones ajustadas.** Ya lo vimos: el escalador, el encoder y el imputador aprendieron de los datos de entrenamiento, y son tan parte del modelo como los coeficientes. Si no viajan, el modelo recibe números en otra escala.

**3. El esquema de entrada.** Qué columnas espera, con qué nombres, de qué tipo, **en qué orden**, en qué unidades. Qué hacer con los faltantes. Qué categorías son válidas y qué pasa con una que nunca se vio. Este es el punto donde más rápido se degrada un contrato, porque los datos de entrada cambian solos, sin que nadie toque el modelo.

**4. El esquema de salida.** Qué devuelve exactamente: ¿una clase, una probabilidad, un score sin calibrar? ¿En qué rango? ¿Cómo se interpreta?

Y una pregunta chiquita que causa desastres: **¿quién aplica el umbral de decisión?** Si el modelo devuelve una probabilidad y hay que convertirla en un sí o un no, alguien tiene que decidir dónde se corta. Si el que entrena asume que lo hace el que sirve, y el que sirve asume lo contrario, el sistema queda con un umbral de 0.5 que nadie eligió — y que probablemente no sea el que optimiza el negocio.

**5. Las métricas y la población sobre la que se midieron.** No alcanza con "tiene 0.87 de AUC". Sobre qué datos, de qué período, con qué distribución. Eso es lo que le dice al consumidor **dónde vale** el modelo y dónde está extrapolando.

**6. La identidad de la versión.** Qué versión es, qué datos y qué código la produjeron. Es el linaje que ya vimos: sin eso, dentro de seis meses nadie puede responder qué se está ejecutando.

**7. Los requisitos de ejecución.** Qué necesita para correr: versiones, recursos, dependencias.

**[Slide: regla del contrato]**

**Regla para llevarse: todo supuesto que no esté escrito, el otro lado lo va a inventar.** Y lo va a inventar distinto.

---

### Punto 3: Cuando la tecnología del otro lado es distinta (9–10 min)

Hasta acá supusimos algo que en la industria muchas veces no se cumple: que quien consume el modelo corre la misma tecnología con la que se entrenó.

**[Slide: el escenario — entrenamos en Python, el sistema que consume está en Java]**

El caso típico: ustedes entrenan en Python, porque es donde está todo el ecosistema de ciencia de datos. Pero el sistema que tiene que usar las predicciones es una aplicación de la empresa escrita en Java, que existe hace diez años y no se va a reescribir. O corre en un dispositivo con recursos limitados. O es un motor de base de datos.

Hay cuatro estrategias, y cada una paga un precio distinto.

**[Slide: las cuatro estrategias]**

**1. Misma tecnología.** Es el caso en el que el problema directamente no existe: los dos lados corren Python. Se guarda el modelo entrenado tal como quedó en memoria, en un archivo, y del otro lado se lo vuelve a cargar. No hay conversión ni traducción de por medio. Cuando se puede, es lo primero que hay que intentar.

Pero tiene una trampa que conviene conocer, porque es la que sorprende a todo el mundo la primera vez. **Ese archivo no guarda el modelo: guarda el estado interno del objeto y una referencia a la clase que lo creó.** Los coeficientes aprendidos están ahí, sí, pero la receta para reconstruir el objeto no — esa se busca en la librería instalada. Por eso, para levantarlo, del otro lado tiene que estar la misma librería que lo generó.

¿Y qué pasa si está instalada otra versión? Dos cosas, y una es peor que la otra:

- **No carga y salta un error.** Es el caso bueno, aunque no lo parezca: se enteran en el momento.
- **Carga igual y se comporta distinto**, porque entre una versión y otra la librería cambió algo por dentro. Nadie ve un error, y las predicciones son otras.

Es el mismo problema de entorno que vimos al hablar de reproducibilidad, pero cruzando de un equipo a otro. Y la conclusión es la misma: con esta estrategia, **el entorno es parte de lo que se entrega.** El lock file deja de ser una comodidad nuestra y pasa a ser una cláusula del contrato.

**[Slide: guardar el objeto vs. exportar los parámetros]**

Ahora bien, guardar el objeto entero no es la única opción, y muchas veces no es la mejor. **Varias librerías de modelos tienen su propio formato de exportación**, que no guarda el objeto de Python sino los **parámetros aprendidos**: la estructura de los árboles, los pesos, los cortes. A veces es un archivo de texto legible, tipo JSON, que uno puede abrir y mirar.

Eso es bastante más robusto, porque lo que se entrega deja de depender de una clase de Python y pasa a depender del formato de la librería, que suele mantenerse compatible entre versiones justamente porque es un formato pensado para durar.

Y hay un paso más: **algunas de esas librerías existen en varios lenguajes.** La misma implementación tiene interfaces para Java, para C++, para R. Entonces un modelo entrenado en Python se puede cargar desde otro lenguaje usando la misma librería, sin exportar a ningún formato de intercambio y sin levantar ningún servicio. Cuando el modelo que están usando es de ese tipo, el problema de portabilidad se les simplifica muchísimo.

**Pero — y este es el pero importante — eso resuelve el modelo, no el pipeline.** El escalador, el encoder, el imputador, todo lo que pasa antes de que el dato llegue al modelo, es código de otras librerías que no tienen esa versión multi-lenguaje. Así que la parte que igual hay que resolver del otro lado es justamente la más silenciosa y la más propensa a divergir. Volvemos sobre esto en un momento.

**2. Formato de intercambio.** El modelo se exporta a un formato estándar que lo describe como un **grafo de operaciones matemáticas**, independiente del framework que lo entrenó. El consumidor lo ejecuta con un runtime propio, en su lenguaje. El más extendido hoy es ONNX.

Y se puede exportar bastante más de lo que uno esperaría: no solo el modelo, también buena parte del preprocesamiento. Pero la exportación no sale gratis, y los dolores de cabeza son casi siempre los mismos tres:

- **Cobertura.** Cada operación necesita que alguien haya escrito su traducción al formato. Los modelos y las transformaciones más usadas están cubiertos; para código propio hay que escribir esa traducción a mano, y no siempre vale la pena el esfuerzo.
- **Versiones.** El conversor, el formato y el runtime que lo ejecuta avanzan por separado, cada uno con su propio versionado. Que una conversión funcione con cierta combinación no garantiza que funcione con la siguiente, y este es de los lugares donde más tiempo se pierde en la práctica.
- **Precisión numérica.** El modelo exportado no necesariamente calcula con la misma precisión que el original. Las diferencias son minúsculas, pero cerca de un umbral de decisión alcanzan para que una predicción cambie de lado.

Por eso una exportación **nunca se da por buena sin verificarla**. En un momento vemos con qué se verifica.

**3. El servicio como frontera.** Acá no se porta el modelo a ningún lado: se lo envuelve en una **API**.

Concretamente: el modelo se queda corriendo en Python, del lado nuestro, adentro de un contenedor, y le ponemos adelante un servicio que escucha pedidos por la red. La aplicación que necesita la predicción manda un pedido con los datos de entrada y recibe la predicción como respuesta.

**Y ahí el problema de la tecnología se disuelve**, porque la pregunta cambia. Ya no es "¿puede esta aplicación en Java ejecutar un modelo entrenado en Python?" —que es difícil— sino "¿puede esta aplicación hacer una llamada de red?" — y eso lo sabe hacer cualquier lenguaje escrito en los últimos treinta años. Cada lado se queda con la tecnología que le conviene y ninguno necesita saber nada del otro.

Fíjense que el contrato no desaparece: se mueve. Ahora es el contrato de la API — qué campos lleva el pedido, qué devuelve la respuesta, qué pasa cuando algo falla.

El precio es el más alto de las cuatro estrategias, y conviene tenerlo claro: **dejamos de entregar un archivo y pasamos a operar un sistema vivo.** Hay que desplegarlo, monitorearlo, escalarlo cuando crece la demanda y tenerlo disponible. Suma latencia de red a cada predicción. Y si el servicio se cae, se cae también quien depende de él.

Esto es lo que se llama **serving online**, y es un tema lo bastante grande como para merecer su propio tratamiento más adelante en el posgrado.

**4. Predicción en lote.** La cuarta estrategia es, en el fondo, esquivar el problema.

Todo el cómputo —cargar el modelo, transformar los datos, predecir— pasa entero de nuestro lado, en nuestra tecnología. Lo que se entrega no es un modelo: es una **tabla de predicciones ya calculadas**, en un archivo o en una base de datos. Del otro lado, la aplicación en Java no ejecuta ningún modelo; lee una fila, igual que lee cualquier otro dato.

**Y fíjense qué pasó con el problema: no lo resolvimos, lo cambiamos por uno mucho más fácil.** Igual que recién, la pregunta se corre — pero esta vez todavía más lejos. Ya no es "¿puede ejecutar un modelo de Python?", ni siquiera "¿puede hacer una llamada de red?": ahora es **"¿puede leer una tabla?"**.

Y leer una tabla —de un archivo o de una base de datos— es de las cosas más viejas y mejor resueltas de la informática. Todos los lenguajes lo hacen, con herramientas maduras y sin sorpresas. No hay conversores que mantener, ni versiones de formato que se peleen entre sí, ni diferencias de precisión numérica: hay una columna con un número, y el otro lado la lee.

El precio: las predicciones son de antes. Se calcularon en la última corrida, así que esta estrategia sirve cuando la decisión tolera esa demora, y no sirve cuando hay que responder en el momento sobre un caso que acaba de aparecer.

**Esta es la que vamos a trabajar en esta materia**, y ahora se entiende por qué: es la que permite recorrer el ciclo completo de MLOps —entrenar, versionar, testear, orquestar, monitorear— sin arrastrar además la complejidad de operar un servicio en vivo.

**[Slide: el modelo es la mitad fácil]**

Ahora, el punto que quiero que se lleven de este bloque.

**Cualquiera sea la estrategia, el modelo es la mitad fácil.** Lo que casi nunca viaja bien es el **preprocesamiento**. Si se exporta el modelo pero las features se recalculan del otro lado, en otro lenguaje, por otra persona, terminamos con **dos implementaciones de la misma transformación** — y solo hace falta que difieran un poquito para que el modelo reciba algo distinto de lo que aprendió.

Y las diferencias son siempre chicas y aburridas:

- El **orden de las columnas**, que en un lenguaje se respeta por nombre y en otro por posición.
- Los **nulos**, que cada lenguaje representa y propaga a su manera.
- El **redondeo y la precisión** de los números decimales.
- Las **categorías nuevas**, que de un lado se mapean a "otros" y del otro rompen o quedan en cero.
- Las **fechas**: zona horaria, formato, qué se considera el primer día de la semana.
- Los **strings**: mayúsculas, acentos, espacios al final.

Ninguna de esas cosas levanta un error. Todas cambian la predicción.

**[Slide: cómo se controla — el test de paridad]**

La forma de controlarlo es convertir el contrato en algo **ejecutable**: un **test de paridad**.

Se congela un conjunto chico de casos de entrada —un *golden dataset*— junto con las salidas que produce la implementación de referencia. La otra versión procesa ese mismo conjunto, y se comparan los resultados **con una tolerancia numérica explícita**, acordada de antemano. Ese test corre en la integración continua de los dos lados. Si alguien cambia algo que rompe la equivalencia, se entera en minutos y no en producción.

Y sirve para los dos casos que vimos: tanto cuando alguien **reimplementó** la transformación en otro lenguaje, como cuando el modelo se **exportó** a un formato de intercambio y hay que confirmar que lo exportado predice lo mismo que el original. Fíjense que la tolerancia acá no es un detalle de implementación: es una cláusula del contrato, y hay que acordarla antes, no cuando ya hay una diferencia sobre la mesa.

Cuando el test de paridad existe, la discusión entre los equipos deja de ser una charla de opiniones y pasa a ser un archivo que falla o no falla.

**Y la mejor estrategia sigue siendo evitar el problema:** siempre que se pueda, empujar el preprocesamiento **adentro** del artefacto que se exporta, para que no queden dos implementaciones que mantener sincronizadas.

---

## Cierre (1 min)

En este video vimos cómo se entrega un modelo para que otro lo pueda usar de verdad.

Las ideas clave para llevarse:
1. Un **contrato de interfaz** hace explícito lo que hoy vive en la cabeza de quien entrenó el modelo. Un contrato implícito no es un contrato.
2. El contrato tiene **tres capas**: el artefacto, los datos de entrada y salida, y las garantías operativas. La tercera es la que nadie escribe.
3. **Con el modelo viaja mucho más que el modelo:** transformaciones ajustadas, esquemas, umbral de decisión, métricas con su población, versión y requisitos.
4. Si el consumidor corre otra tecnología hay **cuatro estrategias**: misma tecnología, formato de intercambio, el servicio como frontera, o predicción en lote. En esta materia usamos la última.
5. **El modelo es la mitad fácil.** El riesgo está en el preprocesamiento duplicado, y se controla con un **test de paridad** sobre un conjunto congelado de casos.

Con esto cerramos la primera clase. Ya tienen el mapa: el ciclo de vida, el pipeline y sus artifacts, los niveles de madurez, la diferencia entre desarrollo y producción, y qué significa entregar un modelo. De acá en adelante empezamos a construir.

---

## Notas de producción

- **Pantalla:** slides. En el Punto 2 conviene mostrar el "paquete" como una caja que se va llenando con cada elemento, para que se vea que el archivo del modelo ocupa una fracción. En el Punto 3, mostrar las cuatro estrategias como cuatro diagramas chicos con la frontera tecnológica marcada en distinto lugar en cada uno.
- **La escalera de preguntas:** las estrategias 3 y 4 usan el mismo recurso a propósito — la pregunta que hay que responder se va corriendo hacia una más fácil: *"¿puede ejecutar un modelo de Python?"* → *"¿puede hacer una llamada de red?"* → *"¿puede leer una tabla?"*. Vale la pena una slide que muestre las tres preguntas apiladas, cada una apareciendo cuando se llega a su estrategia. Es lo que hace visible que la predicción en lote no resuelve el problema sino que lo cambia por uno resuelto.
- **Animaciones:** para el bloque de divergencias sutiles, una animación de dos implementaciones procesando el mismo registro y llegando a features distintas por una diferencia mínima, con la predicción cambiando al final. Es el momento de mayor impacto del video. Para el test de paridad, mostrar el golden dataset entrando a las dos implementaciones y la comparación con tolerancia.
- **Referencias:** Chip Huyen, _Designing Machine Learning Systems_ (O'Reilly) — cap. 7 y 8 para deployment y training/serving skew; Google, *Rules of Machine Learning* (regla 29 y siguientes) para la equivalencia entre training y serving; especificación de ONNX para el formato de intercambio, y la documentación de su conversor para scikit-learn (sección de *discrepancies*), que documenta las diferencias numéricas por precisión y la matriz de compatibilidad entre conversor, opset y runtime — es la fuente concreta detrás del bloque de "la exportación no sale gratis"; D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems* para el costo de los contratos implícitos.
- **Continuidad:** este video cierra la clase 1 y retoma explícitamente el concepto de artifact del video de pipelines. La contracara práctica —cómo se escribe un test de paridad y un schema de features— se trabaja en la clase de testing y validación. La discusión sobre qué representación del modelo se publica se retoma en la clase de tracking y registry. **En cámara nada de eso se ubica por número de clase ni por materia.**
- **Ejemplo concreto para la estrategia 1:** si al grabar se quiere aterrizar el bloque de "exportar los parámetros en vez del objeto", el caso canónico es XGBoost — exporta el modelo a JSON y tiene interfaces oficiales en Java/Scala, C++ y R, así que un modelo entrenado en Python se carga desde la JVM sin conversión de por medio. LightGBM está en la misma situación. Se dejó fuera de cámara por el criterio de agnosticismo; mostrarlo como texto en la slide es una alternativa intermedia.
- **Criterio de agnosticismo:** ONNX se nombra **una sola vez**, como el formato más extendido "hoy", porque es el único caso del video donde el ejemplo concreto ayuda a entender el concepto. Las demás tecnologías se mencionan por lo que hacen. Python y Java se nombran solo como ilustración del escenario de heterogeneidad, no como stack del curso.
