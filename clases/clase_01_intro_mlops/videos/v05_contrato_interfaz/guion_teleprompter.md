# GUION DE TELEPROMPTER (QPROMPT)

**Módulo 1: Introducción a MLOps y ciclo de vida de un proyecto de ML — Video 5**
**Duración aproximada:** 21 a 23 minutos
**Recomendaciones para lectura:**
- Mantener un ritmo pausado y conversacional.
- Hacer contacto visual constante con la cámara (la lente).
- Las indicaciones entre corchetes `[...]` y las líneas divisorias son guías visuales y NO deben leerse en voz alta.
- Los números importantes se han escrito en letras para facilitar la lectura fluida.
- Registro: **ustedes**.
- **Es el video más largo del módulo y el que cierra la clase.** Marcar bien las transiciones entre los tres bloques, y bajar el ritmo en la lista de divergencias sutiles: es el momento de mayor impacto.

Nomenclatura:

- CD: Cambio de diapositiva
- C: Click

---

[CD]

[SONREÍR] ¡Hola! Llegamos al último video de esta clase. Y vamos a hablar de algo que parece administrativo pero no lo es: cómo se entrega un modelo para que otro lo pueda usar de verdad.
[CD] Tres cosas vamos a ver.
[C] Primero, qué es un contrato de interfaz, y por qué un modelo se entrega con un contrato y no suelto.
[C] Después, qué viaja con el modelo: todo lo que hay que entregar además del archivo.
[C] Y por último, qué hacer cuando quien consume el modelo no corre la misma tecnología que ustedes.
[CD] Bueno, arranquemos ubicándonos. Ustedes están en el medio de una cadena.
[C] Por un lado reciben algo: un notebook que entrena un modelo sobre un dataset, producido en la etapa anterior de su formación.
[C] Por el otro lado van a entregar algo: un proceso reproducible que produce un modelo versionado y predicciones confiables, que alguien más va a consumir.
[CD] Y acá está el problema.
Cuando el trabajo cruza de un equipo a otro, lo que se pierde no suele ser el modelo. El archivo llega bien.
[PAUSA CORTA] [ÉNFASIS] Lo que se pierde es todo lo que quien lo entrenó sabía... y no escribió.
[C] Que la columna de ingresos venía en miles y no en pesos.
[C] Que las categorías nuevas hay que mapearlas a "otros".
[C] Que el umbral de decisión no es cero coma cinco.
[PAUSA CORTA] Nada de eso está en el archivo del modelo. Y si no está escrito en ningún lado, el que recibe lo va a inventar. Y lo va a inventar distinto.
De eso se trata un contrato de interfaz: de hacer explícito lo que hoy vive en la cabeza de una persona.
[CD] Así que veamos qué es exactamente.
[CD] Un contrato de interfaz es el acuerdo explícito entre quien produce algo y quien lo consume: qué se entrega, en qué formato, con qué garantías, y qué cosas expresamente [ÉNFASIS] no se prometen.
La idea no es nueva ni es de Machine Learning: es la misma que hay detrás de cualquier API. Si dos equipos acuerdan la interfaz, pueden trabajar en paralelo sin reunirse todos los días, y cada uno puede cambiar lo que tiene adentro mientras respete lo acordado.
[CD] Ahora, en un sistema de Machine Learning el contrato tiene tres capas. Y no reciben ni de cerca la misma atención.
[C] La primera: el artefacto. Qué objeto se entrega y en qué formato. Es la capa que todo el mundo recuerda.
[C] La segunda: los datos. Qué espera recibir el modelo para funcionar, y qué devuelve. Es la capa donde se rompen las cosas.
[C] Y la tercera: las garantías operativas. Con qué calidad funciona, sobre qué población fue medido, y hasta cuándo se puede confiar en eso. Es la capa que nadie escribe.
[PAUSA CORTA] Y el problema está justamente en esa progresión: [ÉNFASIS] la atención que le damos a cada capa es inversa a los problemas que causa. La primera se cuida sola, porque sin el archivo no hay nada que hacer. La segunda y la tercera, que son las que después explican los incidentes, quedan libradas a que alguien se acuerde de escribirlas.
[CD] Y de acá sale la clave del bloque: [ÉNFASIS] un contrato implícito no es un contrato.
Es un conjunto de supuestos que funcionan hasta el día que alguien cambia algo. Y como en Machine Learning nada falla ruidosamente —el modelo siempre devuelve un número— el día que se rompe, nadie se entera.
[CD] Entonces, ¿qué hay que entregar?
[CD] El archivo del modelo es apenas el principio. Vamos por partes.
[C] Uno: el modelo entrenado, serializado en un formato que el consumidor pueda abrir.
[C] Dos: las transformaciones ajustadas. Ya lo vimos: el escalador, el encoder y el imputador aprendieron de los datos de entrenamiento, y son tan parte del modelo como los coeficientes. Si no viajan, el modelo recibe números en otra escala.
[C] Tres: el esquema de entrada.
[C] Cuatro: el esquema de salida.
[C] Cinco: las métricas, y la población sobre la que se midieron.
[C] Seis: la identidad de la versión.
[C] Y siete: los requisitos de ejecución.
[CD] Vamos a detenernos en el tercero, el esquema de entrada, porque es donde más rápido se degrada un contrato.
Qué columnas espera, con qué nombres, de qué tipo, [ÉNFASIS] en qué orden, en qué unidades. Qué hacer con los faltantes. Qué categorías son válidas, y qué pasa con una que nunca se vio.
[PAUSA CORTA] ¿Y por qué se degrada tan rápido? Porque los datos de entrada cambian solos. Sin que nadie toque el modelo.
[CD] Y ahora una pregunta chiquita que causa desastres.
El modelo devuelve una probabilidad, y hay que convertirla en un sí o un no. Alguien tiene que decidir dónde se corta.
[C] [ÉNFASIS] ¿Quién aplica el umbral de decisión?
[PAUSA CORTA] [C] Porque si el que entrena asume que lo hace el que sirve, y el que sirve asume lo contrario... el sistema queda con un umbral de cero coma cinco que nadie eligió. Y que probablemente no sea el que optimiza el negocio.
[CD] Otro que vale la pena: las métricas.
No alcanza con decir "tiene cero coma ochenta y siete de AUC". Sobre qué datos. De qué período. Con qué distribución.
[PAUSA CORTA] Eso es lo que le dice al consumidor [ÉNFASIS] dónde vale el modelo... y dónde está extrapolando.
[CD] Y la regla que resume todo el bloque: [ÉNFASIS] todo supuesto que no esté escrito, el otro lado lo va a inventar. Y lo va a inventar distinto.
[CD] Bien. Vamos al último bloque, que es el más largo.
[CD] Hasta acá supusimos algo que en la industria muchas veces no se cumple: que quien consume el modelo corre la misma tecnología con la que se entrenó.
El caso típico es este: ustedes entrenan en Python, porque es donde está todo el ecosistema de ciencia de datos. Pero el sistema que tiene que usar las predicciones es una aplicación de la empresa escrita en Java, que existe hace diez años y no se va a reescribir. O corre en un dispositivo con recursos limitados. O es un motor de base de datos.
[PAUSA CORTA] Hay cuatro estrategias. Y cada una paga un precio distinto.
[CD] La primera: misma tecnología.
Es el caso en el que el problema directamente no existe: los dos lados corren Python. Se guarda el modelo entrenado tal como quedó en memoria, en un archivo, y del otro lado se lo vuelve a cargar. No hay conversión ni traducción de por medio. Cuando se puede, es lo primero que hay que intentar.
[CD] Pero tiene una trampa que conviene conocer, porque es la que sorprende a todo el mundo la primera vez.
[ÉNFASIS] Ese archivo no guarda el modelo. Guarda el estado interno del objeto, y una referencia a la clase que lo creó.
[PAUSA CORTA] Los coeficientes aprendidos están ahí, sí. Pero la receta para reconstruir el objeto, no: esa se busca en la librería instalada. Por eso, para levantarlo, del otro lado tiene que estar la misma librería que lo generó.
[CD] ¿Y qué pasa si está instalada otra versión? Dos cosas, y una es peor que la otra.
[C] Una: no carga, y salta un error. Y este es el caso bueno, aunque no lo parezca: se enteran en el momento.
[C] Y dos: carga igual, y se comporta distinto. Porque entre una versión y otra la librería cambió algo por dentro. Nadie ve ningún error, y las predicciones son otras.
[PAUSA CORTA] Es el mismo problema de entorno que vimos al hablar de reproducibilidad, pero cruzando de un equipo a otro. Y la conclusión es la misma: con esta estrategia, [ÉNFASIS] el entorno es parte de lo que se entrega. El lock file deja de ser una comodidad nuestra y pasa a ser una cláusula del contrato.
[CD] Ahora bien, guardar el objeto entero no es la única opción. Y muchas veces no es la mejor.
Varias librerías de modelos tienen su propio formato de exportación, que no guarda el objeto de Python sino los parámetros aprendidos: la estructura de los árboles, los pesos, los cortes. A veces es un archivo de texto legible, que uno puede abrir y mirar.
[C] Y eso es bastante más robusto, porque lo que se entrega deja de depender de una clase de Python, y pasa a depender del formato de la librería. Que suele mantenerse compatible entre versiones, justamente porque es un formato pensado para durar.
[C] Y hay un paso más: algunas de esas librerías existen en varios lenguajes. La misma implementación tiene interfaces para Java, para C más más, para R. Entonces un modelo entrenado en Python se puede cargar desde otro lenguaje usando la misma librería. Sin exportar a ningún formato de intercambio, y sin levantar ningún servicio.
[CD] Pero —y este es el pero importante— [ÉNFASIS] eso resuelve el modelo. No el pipeline.
El escalador, el encoder, el imputador, todo lo que pasa antes de que el dato llegue al modelo, es código de otras librerías que no tienen esa versión multi-lenguaje. Así que la parte que igual hay que resolver del otro lado es justamente la más silenciosa, y la más propensa a divergir.
[PAUSA CORTA] Volvemos sobre esto en un momento.
[CD] La segunda estrategia: formato de intercambio.
Acá el modelo se exporta a un formato estándar que lo describe como un grafo de operaciones matemáticas, independiente del framework que lo entrenó. Y el consumidor lo ejecuta con un runtime propio, en su lenguaje.
Y se puede exportar bastante más de lo que uno esperaría: no solo el modelo, también buena parte del preprocesamiento.
[CD] Pero la exportación no sale gratis. Y los dolores de cabeza son casi siempre los mismos tres.
[C] Cobertura. Cada operación necesita que alguien haya escrito su traducción al formato. Los modelos y las transformaciones más usadas están cubiertos; para código propio hay que escribir esa traducción a mano, y no siempre vale la pena el esfuerzo.
[C] Versiones. El conversor, el formato y el runtime que lo ejecuta avanzan por separado, cada uno con su propio versionado. Que una conversión funcione con cierta combinación no garantiza que funcione con la siguiente. Y este es de los lugares donde más tiempo se pierde en la práctica.
[C] Y precisión numérica. El modelo exportado no necesariamente calcula con la misma precisión que el original. Las diferencias son minúsculas... pero cerca de un umbral de decisión alcanzan para que una predicción cambie de lado.
[PAUSA CORTA] Por eso una exportación [ÉNFASIS] nunca se da por buena sin verificarla. En un momento vemos con qué se verifica.
[CD] La tercera estrategia: el servicio como frontera.
Acá no se porta el modelo a ningún lado: se lo envuelve en una API.
Concretamente: el modelo se queda corriendo en Python, del lado nuestro, adentro de un contenedor. Y le ponemos adelante un servicio que escucha pedidos por la red. La aplicación que necesita la predicción manda un pedido con los datos de entrada, y recibe la predicción como respuesta.
[CD] Y ahí el problema de la tecnología se disuelve. Porque la pregunta cambia.
[C] Ya no es "¿puede esta aplicación en Java ejecutar un modelo entrenado en Python?", que es difícil...
[C] ...sino "¿puede esta aplicación hacer una llamada de red?". Y eso lo sabe hacer cualquier lenguaje escrito en los últimos treinta años.
[PAUSA CORTA] Cada lado se queda con la tecnología que le conviene, y ninguno necesita saber nada del otro.
Y fíjense que el contrato no desaparece: se mueve. Ahora es el contrato de la API. Qué campos lleva el pedido, qué devuelve la respuesta, qué pasa cuando algo falla.
[CD] El precio es el más alto de las cuatro estrategias, y conviene tenerlo claro.
[ÉNFASIS] Dejamos de entregar un archivo y pasamos a operar un sistema vivo.
[C] Hay que desplegarlo, monitorearlo, escalarlo cuando crece la demanda, y tenerlo disponible.
[C] Suma latencia de red a cada predicción.
[C] Y si el servicio se cae, se cae también quien depende de él.
[PAUSA CORTA] Esto es lo que se llama serving online, y es un tema lo bastante grande como para merecer su propio tratamiento más adelante en el posgrado.
[CD] Y la cuarta estrategia es, en el fondo, esquivar el problema. Predicción en lote.
Todo el cómputo —cargar el modelo, transformar los datos, predecir— pasa entero de nuestro lado, en nuestra tecnología. Lo que se entrega no es un modelo: es una tabla de predicciones ya calculadas, en un archivo o en una base de datos.
Del otro lado, la aplicación en Java no ejecuta ningún modelo. Lee una fila. Igual que lee cualquier otro dato.
[PAUSA CORTA] Y fíjense qué pasó con el problema: [ÉNFASIS] no lo resolvimos. Lo cambiamos por uno mucho más fácil.
[C] Igual que recién, la pregunta se corre... pero esta vez todavía más lejos. Ya no es "¿puede ejecutar un modelo de Python?". Ni siquiera "¿puede hacer una llamada de red?". Ahora es: "¿puede leer una tabla?".
[CD] Y leer una tabla —de un archivo o de una base de datos— es de las cosas más viejas y mejor resueltas de la informática. Todos los lenguajes lo hacen, con herramientas maduras y sin sorpresas.
No hay conversores que mantener, ni versiones de formato que se peleen entre sí, ni diferencias de precisión numérica. Hay una columna con un número, y el otro lado la lee.
[C] El precio: las predicciones son de antes. Se calcularon en la última corrida. Así que esta estrategia sirve cuando la decisión tolera esa demora... y no sirve cuando hay que responder en el momento sobre un caso que acaba de aparecer.
[CD] Y esta es la que vamos a trabajar en esta materia. Y ahora se entiende por qué: es la que nos permite recorrer el ciclo completo de MLOps —entrenar, versionar, testear, orquestar, monitorear— sin arrastrar además la complejidad de operar un servicio en vivo.
[CD] Ahora sí, el punto que quiero que se lleven de todo este bloque.
[PAUSA CORTA] Cualquiera sea la estrategia... [ÉNFASIS] el modelo es la mitad fácil.
Lo que casi nunca viaja bien es el preprocesamiento. Si se exporta el modelo pero las features se recalculan del otro lado, en otro lenguaje, por otra persona, terminamos con dos implementaciones de la misma transformación. Y solo hace falta que difieran un poquito para que el modelo reciba algo distinto de lo que aprendió.
[CD] Y las diferencias son siempre chicas. Y aburridas.
[C] El orden de las columnas, que en un lenguaje se respeta por nombre y en otro por posición.
[C] Los nulos, que cada lenguaje representa y propaga a su manera.
[C] El redondeo y la precisión de los números decimales.
[C] Las categorías nuevas, que de un lado se mapean a "otros" y del otro rompen, o quedan en cero.
[C] Las fechas: zona horaria, formato, qué se considera el primer día de la semana.
[C] Los strings: mayúsculas, acentos, espacios al final.
[PAUSA] [C] [ÉNFASIS] Ninguna de esas cosas levanta un error. Todas cambian la predicción.
[CD] ¿Y cómo se controla? Convirtiendo el contrato en algo ejecutable: un test de paridad.
[C] Se congela un conjunto chico de casos de entrada —un golden dataset—...
[C] ...junto con las salidas que produce la implementación de referencia.
[C] La otra versión procesa ese mismo conjunto...
[C] ...y se comparan los resultados con una tolerancia numérica explícita, acordada de antemano.
[PAUSA CORTA] Ese test corre en la integración continua de los dos lados. Así que si alguien cambia algo que rompe la equivalencia, se entera en minutos. Y no en producción.
[CD] Y sirve para los dos casos que vimos.
[C] Tanto cuando alguien reimplementó la transformación en otro lenguaje...
[C] ...como cuando el modelo se exportó a un formato de intercambio y hay que confirmar que lo exportado predice lo mismo que el original.
[PAUSA CORTA] Y fíjense que la tolerancia acá no es un detalle de implementación: [ÉNFASIS] es una cláusula del contrato. Y hay que acordarla antes. No cuando ya hay una diferencia sobre la mesa.
Cuando el test de paridad existe, la discusión entre los equipos deja de ser una charla de opiniones y pasa a ser un archivo que falla, o no falla.
[CD] Y la mejor estrategia, de todas maneras, sigue siendo evitar el problema: siempre que se pueda, empujar el preprocesamiento [ÉNFASIS] adentro del artefacto que se exporta. Para que no queden dos implementaciones que mantener sincronizadas.
[CD] Bueno, en este video vimos cómo se entrega un modelo para que otro lo pueda usar de verdad. Cinco ideas para cerrar.
[C] Uno. Un contrato de interfaz hace explícito lo que hoy vive en la cabeza de quien entrenó el modelo. Un contrato implícito no es un contrato.
[C] Dos. El contrato tiene tres capas: el artefacto, los datos de entrada y salida, y las garantías operativas. La tercera es la que nadie escribe.
[C] Tres. Con el modelo viaja mucho más que el modelo: transformaciones ajustadas, esquemas, umbral de decisión, métricas con su población, versión y requisitos.
[C] Cuatro. Si el consumidor corre otra tecnología hay cuatro estrategias: misma tecnología, formato de intercambio, el servicio como frontera, o predicción en lote. En esta materia usamos la última.
[C] Y cinco. El modelo es la mitad fácil. El riesgo está en el preprocesamiento duplicado, y se controla con un test de paridad sobre un conjunto congelado de casos.
[CD] Y con esto cerramos la primera clase.
Ya tienen el mapa completo: [C] el ciclo de vida y los roles, [C] el pipeline y sus artifacts, [C] los niveles de madurez, [C] la diferencia entre desarrollo y producción, [C] y qué significa entregar un modelo.
[PAUSA] De acá en adelante, empezamos a construir.
[CD] [SONREÍR / SALUDO FINAL] ¡Muchas gracias, y nos vemos en la próxima clase!
