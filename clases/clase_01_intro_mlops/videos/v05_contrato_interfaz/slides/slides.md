# Slides — v05: Contrato de interfaz, qué recibimos y qué entregamos

> Cada sección separada por `---` es una diapositiva.
> Las notas de layout y animación están entre corchetes `[ ]`.
>
> **Recurso transversal del Punto 3 — la escalera de preguntas.** Las estrategias 3 y 4 corren
> la misma pregunta hacia una cada vez más fácil de responder. Conviene una slide que las
> apile y las vaya revelando:
> *"¿puede ejecutar un modelo de Python?"* → *"¿puede hacer una llamada de red?"* → *"¿puede leer una tabla?"*

---

## Diapositiva 1 — Portada

**Operaciones de Aprendizaje Automático I**

Contrato de interfaz: qué recibimos y qué entregamos

`Módulo 1 — Video 5`

[Layout: fondo oscuro, título centrado, subtítulo en gris claro]

---

## Diapositiva 2 — De qué trata este video

**¿De qué trata este video?**

- **El contrato de interfaz:** qué es, y por qué un modelo se entrega con un contrato y no suelto.
- **Qué viaja con el modelo:** todo lo que hay que entregar además del archivo.
- **Cuando la tecnología del otro lado es distinta:** qué hacer si quien lo consume no corre Python.

[Layout: tres bloques que aparecen de a uno]

---

## Diapositiva 3 — La cadena

**Están en el medio de una cadena**

**Reciben** → un notebook que entrena un modelo sobre un dataset

**Transforman** → un proceso reproducible

**Entregan** → un modelo versionado y predicciones confiables, que alguien más va a consumir

[Layout: tres bloques encadenados por flechas. El del medio, resaltado — es donde están ustedes]

---

## Diapositiva 4 — Hook: lo que se pierde

**Cuando el trabajo cruza de un equipo a otro, lo que se pierde no es el modelo.**

El archivo llega bien.

**Lo que se pierde es todo lo que quien lo entrenó sabía y no escribió.**

- Que la columna de ingresos venía en miles, no en pesos
- Que las categorías nuevas hay que mapearlas a "otros"
- Que el umbral de decisión no es cero coma cinco

> Nada de eso está en el archivo del modelo. Y si no está escrito, **el que recibe lo va a inventar.**

[Layout: un archivo de modelo cruzando un muro; del otro lado, los tres supuestos quedan del lado de acá]

---

## Diapositiva 5 — Sección: qué es un contrato

**Qué es un contrato de interfaz**

[Layout: diapositiva de sección]

---

## Diapositiva 6 — Definición

**Contrato de interfaz**

> El acuerdo **explícito** entre quien produce algo y quien lo consume: qué se entrega, en qué
> formato, con qué garantías, y qué cosas expresamente **no** se prometen.

La idea es la misma que hay detrás de cualquier API: si dos equipos acuerdan la interfaz, pueden trabajar en paralelo y cambiar lo de adentro sin romper al otro.

[Layout: definición grande]

---

## Diapositiva 7 — Las tres capas

**Un contrato de ML tiene tres capas — y no reciben la misma atención**

1. **El artefacto** — qué objeto se entrega y en qué formato. *La capa que todo el mundo recuerda.*
2. **Los datos** — qué espera recibir el modelo y qué devuelve. *La capa donde se rompen las cosas.*
3. **Las garantías operativas** — con qué calidad funciona, sobre qué población, hasta cuándo se puede confiar. *La capa que nadie escribe.*

> **La atención que recibe cada capa es inversa a los problemas que causa.**

[Layout: tres capas apiladas, con el grosor de la atención decreciendo y el tamaño del problema creciendo]

---

## Diapositiva 8 — La clave del bloque

**Un contrato implícito no es un contrato.**

Es un conjunto de supuestos que funcionan hasta el día que alguien cambia algo.

Y como en ML nada falla ruidosamente —el modelo siempre devuelve un número— el día que se rompe, **nadie se entera.**

[Layout: frase única]

---

## Diapositiva 9 — Sección: qué viaja

**Qué viaja con el modelo**

[Layout: diapositiva de sección]

---

## Diapositiva 10 — El paquete completo

**El archivo del modelo es apenas el principio**

1. El **modelo entrenado**
2. Las **transformaciones ajustadas**
3. El **esquema de entrada**
4. El **esquema de salida**
5. Las **métricas** y la población sobre la que se midieron
6. La **identidad de la versión**
7. Los **requisitos de ejecución**

[Layout: una caja que se va llenando con cada elemento. Que se vea que el archivo del modelo ocupa una fracción del total]

---

## Diapositiva 11 — El esquema de entrada

**3. El esquema de entrada**

Qué columnas espera, con qué nombres, de qué tipo, **en qué orden**, en qué unidades.

Qué hacer con los faltantes. Qué categorías son válidas, y qué pasa con una que nunca se vio.

> Es el punto donde más rápido se degrada un contrato: **los datos de entrada cambian solos**, sin que nadie toque el modelo.

[Layout: tabla de esquema con tipos y restricciones]

---

## Diapositiva 12 — El umbral de decisión

**Una pregunta chiquita que causa desastres**

El modelo devuelve una probabilidad. Alguien tiene que convertirla en un sí o un no.

# ¿Quién aplica el umbral?

Si el que entrena asume que lo hace el que sirve, y el que sirve asume lo contrario…

**…el sistema queda con un umbral de cero coma cinco que nadie eligió.** Y que probablemente no sea el que optimiza el negocio.

[Layout: dos figuras señalándose mutuamente]

---

## Diapositiva 13 — Las métricas con su población

**5. No alcanza con "tiene 0.87 de AUC"**

Sobre qué datos. De qué período. Con qué distribución.

> Eso es lo que le dice al consumidor **dónde vale** el modelo — y dónde está extrapolando.

[Layout: una métrica grande, y debajo el contexto que la vuelve interpretable]

---

## Diapositiva 14 — La regla del contrato

**Todo supuesto que no esté escrito, el otro lado lo va a inventar.**

**Y lo va a inventar distinto.**

[Layout: frase única, centrada]

---

## Diapositiva 15 — Sección: otra tecnología

**Cuando la tecnología del otro lado es distinta**

[Layout: diapositiva de sección]

---

## Diapositiva 16 — El escenario

**Entrenamos en Python. El que consume, no.**

El sistema que tiene que usar las predicciones es una aplicación escrita en Java, que existe hace diez años y no se va a reescribir.

O corre en un dispositivo con recursos limitados. O es un motor de base de datos.

[Layout: dos mundos separados por una frontera tecnológica]

---

## Diapositiva 17 — Estrategia 1: misma tecnología

**1. Misma tecnología**

Los dos lados corren Python. Se guarda el modelo en un archivo y del otro lado se lo vuelve a cargar. Sin conversión.

**Cuando se puede, es lo primero que hay que intentar.**

[Layout: el camino más corto entre los dos lados]

---

## Diapositiva 18 — La trampa del archivo serializado

**Ese archivo no guarda el modelo**

Guarda **el estado interno del objeto** y **una referencia a la clase que lo creó.**

Los coeficientes están ahí. La receta para reconstruir el objeto, no: esa se busca en **la librería instalada.**

[Layout: abrir el archivo y mostrar que adentro hay datos + un puntero a una clase que vive afuera]

---

## Diapositiva 19 — Qué pasa con otra versión

**Dos escenarios, y uno es peor**

- **No carga y salta un error** → el caso **bueno**, aunque no lo parezca: se enteran en el momento.
- **Carga igual y se comporta distinto** → nadie ve un error, y las predicciones son otras.

> Con esta estrategia, **el entorno es parte de lo que se entrega.** El lock file deja de ser una comodidad y pasa a ser una cláusula del contrato.

[Layout: los dos escenarios, el segundo en rojo]

---

## Diapositiva 20 — Guardar el objeto vs. exportar los parámetros

**Guardar el objeto entero no es la única opción**

Varias librerías tienen **su propio formato de exportación**: no guardan el objeto de Python sino los **parámetros aprendidos** — la estructura de los árboles, los pesos, los cortes. A veces en texto legible.

Más robusto: lo entregado deja de depender de una clase de Python y pasa a depender **del formato de la librería**, pensado para durar.

**Y algunas de esas librerías existen en varios lenguajes**, así que el modelo se carga desde otro lenguaje sin exportar nada ni levantar ningún servicio.

[Layout: contraste entre un objeto serializado opaco y un JSON legible]

---

## Diapositiva 21 — El pero importante

**Eso resuelve el modelo. No el pipeline.**

El escalador, el encoder, el imputador —todo lo que pasa antes de que el dato llegue al modelo— es código de otras librerías, que no tienen esa versión multi-lenguaje.

> La parte que igual hay que resolver del otro lado es **la más silenciosa y la más propensa a divergir.**

[Layout: el modelo en verde, el preprocesamiento en rojo]

---

## Diapositiva 22 — Estrategia 2: formato de intercambio

**2. Formato de intercambio**

El modelo se exporta a un formato estándar que lo describe como un **grafo de operaciones matemáticas**, independiente del framework que lo entrenó.

El consumidor lo ejecuta con su propio runtime, en su lenguaje.

> Y se puede exportar más de lo que uno esperaría: no solo el modelo, también buena parte del preprocesamiento.

[Layout: el modelo convertido en un grafo de nodos matemáticos]

---

## Diapositiva 23 — La exportación no sale gratis

**Tres dolores de cabeza, casi siempre los mismos**

- **Cobertura** — cada operación necesita que alguien haya escrito su traducción. Para código propio, hay que escribirla a mano.
- **Versiones** — el conversor, el formato y el runtime avanzan por separado. Que funcione con una combinación no garantiza la siguiente.
- **Precisión numérica** — el exportado no calcula necesariamente igual. Las diferencias son minúsculas, pero cerca de un umbral **cambian la predicción de lado.**

> Por eso una exportación **nunca se da por buena sin verificarla.**

[Layout: tres bloques. El tercero engancha con el test de paridad]

---

## Diapositiva 24 — Estrategia 3: el servicio como frontera

**3. El servicio como frontera**

No se porta el modelo a ningún lado: **se lo envuelve en una API.**

El modelo se queda corriendo en Python, de nuestro lado, en un contenedor. Adelante, un servicio que escucha pedidos por la red.

[Layout: el modelo encapsulado, con una interfaz de red hacia afuera]

---

## Diapositiva 25 — La pregunta se corre

**El problema se disuelve porque cambia la pregunta**

~~¿Puede esta aplicación en Java ejecutar un modelo entrenado en Python?~~ → difícil

**¿Puede esta aplicación hacer una llamada de red?** → lo sabe hacer cualquier lenguaje escrito en los últimos treinta años

> El contrato no desaparece: **se mueve.** Ahora es el contrato de la API — qué campos lleva el pedido, qué devuelve, qué pasa cuando algo falla.

[Layout: primera aparición de la escalera de preguntas. Dejar espacio abajo: se completa en la diapositiva 27]

---

## Diapositiva 26 — El precio de la estrategia 3

**Es el precio más alto de las cuatro**

**Dejamos de entregar un archivo y pasamos a operar un sistema vivo.**

- Hay que desplegarlo, monitorearlo, escalarlo, tenerlo disponible
- Suma latencia de red a cada predicción
- Si el servicio se cae, se cae también quien depende de él

> Esto se llama **serving online**, y es un tema lo bastante grande como para merecer su propio tratamiento más adelante en el posgrado.

[Layout: lista de costos]

---

## Diapositiva 27 — Estrategia 4: predicción en lote

**4. Predicción en lote — esquivar el problema**

Todo el cómputo pasa **entero de nuestro lado**. Lo que se entrega no es un modelo: es una **tabla de predicciones ya calculadas.**

Del otro lado, la aplicación **no ejecuta ningún modelo: lee una fila**, igual que lee cualquier otro dato.

**La escalera completa:**

1. ~~¿Puede ejecutar un modelo de Python?~~
2. ~~¿Puede hacer una llamada de red?~~
3. **¿Puede leer una tabla?**

[Layout: acá se completa la escalera de preguntas de la diapositiva 25]

---

## Diapositiva 28 — Por qué funciona

**Leer una tabla es de lo más viejo y mejor resuelto de la informática**

Todos los lenguajes lo hacen, con herramientas maduras y sin sorpresas.

**No hay conversores que mantener, ni versiones de formato que se peleen, ni diferencias de precisión.**

Hay una columna con un número, y el otro lado la lee.

> **El precio:** las predicciones son de antes. Sirve cuando la decisión tolera esa demora.

[Layout: contraste con la complejidad de las estrategias anteriores]

---

## Diapositiva 29 — Por eso elegimos batch

**Esta es la que vamos a trabajar en la materia**

Permite recorrer el ciclo completo de MLOps —entrenar, versionar, testear, orquestar, monitorear— **sin arrastrar además la complejidad de operar un servicio en vivo.**

[Layout: el ciclo completo destacado, con el serving fuera del alcance]

---

## Diapositiva 30 — El modelo es la mitad fácil

# El modelo es la mitad fácil

Lo que casi nunca viaja bien es el **preprocesamiento.**

Si se exporta el modelo pero las features se recalculan del otro lado, en otro lenguaje, por otra persona → **dos implementaciones de la misma transformación.**

[Layout: la frase grande. Es la tesis del video]

---

## Diapositiva 31 — Las diferencias son chicas y aburridas

**Y basta que difieran un poquito**

- El **orden de las columnas** — por nombre en un lenguaje, por posición en otro
- Los **nulos** — cada lenguaje los representa y propaga a su manera
- El **redondeo y la precisión** de los decimales
- Las **categorías nuevas** — de un lado van a "otros", del otro rompen o quedan en cero
- Las **fechas** — zona horaria, formato, qué día empieza la semana
- Los **strings** — mayúsculas, acentos, espacios al final

# Ninguna levanta un error. Todas cambian la predicción.

[Layout: **el momento de mayor impacto del video.** Animar dos implementaciones procesando el mismo registro, llegando a features distintas por una diferencia mínima, y la predicción cambiando al final]

---

## Diapositiva 32 — El test de paridad

**Convertir el contrato en algo ejecutable**

1. Se congela un conjunto chico de casos de entrada — un ***golden dataset***
2. Junto con las salidas que produce la implementación de referencia
3. La otra versión procesa ese mismo conjunto
4. Se comparan los resultados **con una tolerancia numérica explícita**

> Corre en la integración continua **de los dos lados**. Si alguien rompe la equivalencia, se entera en minutos y no en producción.

[Layout: el golden dataset entrando a las dos implementaciones, y la comparación con tolerancia]

---

## Diapositiva 33 — Sirve para los dos casos

**El test de paridad cubre las dos situaciones**

- Cuando alguien **reimplementó** la transformación en otro lenguaje
- Cuando el modelo se **exportó** a un formato de intercambio y hay que confirmar que predice lo mismo

> Y la tolerancia no es un detalle de implementación: **es una cláusula del contrato.** Se acuerda antes, no cuando ya hay una diferencia sobre la mesa.

[Layout: dos ramas que llegan al mismo test]

---

## Diapositiva 34 — La mejor estrategia

**Y la mejor estrategia sigue siendo evitar el problema**

Siempre que se pueda, empujar el preprocesamiento **adentro** del artefacto que se exporta.

Así no quedan dos implementaciones que mantener sincronizadas.

[Layout: el preprocesamiento entrando dentro de la caja del modelo]

---

## Diapositiva 35 — Cierre e ideas clave

**Ideas clave de este video**

1. Un **contrato de interfaz** hace explícito lo que vive en la cabeza de quien entrenó el modelo. Un contrato implícito no es un contrato.
2. Tiene **tres capas**: artefacto, datos, garantías operativas. La tercera es la que nadie escribe.
3. **Con el modelo viaja mucho más que el modelo**: transformaciones, esquemas, umbral, métricas con su población, versión y requisitos.
4. Si el consumidor corre otra tecnología hay **cuatro estrategias**. En esta materia usamos la predicción en lote.
5. **El modelo es la mitad fácil.** El riesgo está en el preprocesamiento duplicado, y se controla con un **test de paridad.**

[Layout: lista numerada, cada punto aparece de a uno]

---

## Diapositiva 36 — Cierre del módulo

**Con esto cerramos la primera clase**

Ya tienen el mapa completo:

- El ciclo de vida y los roles
- El pipeline y sus artifacts
- Los niveles de madurez
- Desarrollo y producción
- Qué significa entregar un modelo

**De acá en adelante, empezamos a construir.**

[Layout: los cinco videos del módulo como piezas de un mapa que se completa]

---

## Diapositiva 37 — Despedida

**¡Muchas gracias!**

Nos vemos en la próxima clase.

[Layout: fondo oscuro, logo centrado]
