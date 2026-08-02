# GUION DE TELEPROMPTER (QPROMPT)

**Módulo 1: Introducción a MLOps y ciclo de vida de un proyecto de ML — Video 2**
**Duración aproximada:** 18 a 20 minutos
**Recomendaciones para lectura:**
- Mantener un ritmo pausado y conversacional.
- Hacer contacto visual constante con la cámara (la lente).
- Las indicaciones entre corchetes `[...]` y las líneas divisorias son guías visuales y NO deben leerse en voz alta.
- Los números importantes se han escrito en letras para facilitar la lectura fluida.
- Registro: **ustedes**, igual que en el video uno.
- **Video largo:** marcar bien las tres transiciones entre bloques y tomarse las pausas. Es lo que sostiene la atención.

Nomenclatura:

- CD: Cambio de diapositiva
- C: Click

---

[CD]

[SONREÍR] ¡Hola de nuevo! Hoy vamos a hablar de pipelines y de artifacts, que son las dos palabras que más van a escuchar de acá en adelante.
[CD] Pero antes, el mapa de por dónde vamos.
[C] Primero: qué es un pipeline de Machine Learning. Vamos a hacer el camino desde el notebook que ya tienen, hasta una secuencia de etapas encadenadas y repetibles.
[C] Después: componentes y artifacts. Qué hace cada etapa... y qué deja como producto.
[C] Y para cerrar, la reproducibilidad: por qué un pipeline que no se puede repetir, en el fondo, no sirve.
[CD] Bueno. En el video anterior vimos el ciclo de vida completo, y quién es responsable de cada etapa. Ahora bajemos un nivel: ¿cómo se ve todo eso en la práctica? ¿En el código?
Piensen un segundo en el notebook con el que vienen trabajando.
[C] Porque ahí adentro están casi todas las etapas del ciclo: cargan los datos, los limpian, arman las features, entrenan, evalúan.
[PAUSA CORTA] O sea que ese notebook [ÉNFASIS] ya es un pipeline.
[C] El problema es que es un pipeline implícito.
[CD] Y eso trae tres preguntas bastante incómodas.
[C] Primera: si les pido que reproduzcan exactamente el modelo que entrenaron hace tres meses... ¿pueden? ¿Con qué datos era? ¿Con qué hiperparámetros?
[C] Segunda: si otra persona clona el repositorio y corre las celdas de arriba hacia abajo, ¿obtiene lo mismo que ustedes?
[C] Y tercera: cuando el modelo tenga que predecir sobre datos nuevos... ¿de dónde sale el escalador que ajustaron en la celda catorce? [PAUSA]
[C] La respuesta a las tres, casi siempre, es "no del todo". Y ojo, no es porque el notebook esté mal hecho. Es porque un notebook está diseñado para explorar... no para producir.
[PAUSA CORTA] Hacer explícito ese pipeline es, básicamente, el trabajo de toda esta materia.
[CD] Así que empecemos por ahí.
[CD] Un pipeline es una secuencia de etapas, donde la salida de una es la entrada de la siguiente, cada una con una responsabilidad única, y que se puede ejecutar de punta a punta de forma automática.
[CD] De esa definición hay tres palabras que importan de verdad.
[C] La primera: secuencia explícita. El orden está declarado en algún lado. No depende de en qué orden ejecutó las celdas la persona que estaba sentada frente a la máquina ese día.
[C] La segunda: responsabilidad única. Cada etapa hace una sola cosa. Y eso es lo que permite testearla, cambiarla, o volver a ejecutarla sin tocar todo lo demás.
[C] Y la tercera: automática. Se dispara con un comando, o con un horario, o con un evento. Sin que nadie tenga que apretar nada.
[CD] Ahora, en la práctica no hay un solo pipeline. Hay por lo menos dos: uno que produce el modelo... y otro que lo usa.
[CD] Vamos con el primero: el pipeline de entrenamiento. Este corre cada tanto, y su producto es un modelo.
[C] Uno. Ingesta de datos: traerlos desde donde estén.
[C] Dos. Validación de datos: chequear que los datos son los que esperábamos. Tipos, rangos, nulos. A esto le vamos a dedicar una clase entera más adelante.
[C] Tres. Preprocesamiento y feature engineering: convertir los datos crudos en la matriz que el modelo va a consumir.
[C] Cuatro. Entrenamiento. Esta parte ya la conocen.
[C] Cinco. Evaluación: medir sobre datos que el modelo no vio, y decidir si es aceptable.
[C] Y seis. Registro del modelo: guardarlo y versionarlo junto con sus métricas.
[CD] Y ahora el segundo: el pipeline de inferencia. Este agarra ese modelo y lo aplica a datos nuevos.
[C] Uno. Ingesta de los datos nuevos.
[C] Dos. [ÉNFASIS] Las mismas transformaciones que en entrenamiento. Y acá "las mismas" es literal. En un ratito vemos por qué.
[C] Tres. Cargar el modelo desde donde quedó registrado.
[C] Cuatro. Predecir.
[C] Y cinco. Entregar esas predicciones a quien las tenga que usar.
[CD] Ahora bien, ese pipeline de inferencia se puede materializar de formas muy distintas, según cuándo y con qué urgencia se necesitan las predicciones.
[C] Puede ser en lote, o batch: corre cada tanto —una vez por día, digamos— sobre un montón de registros, y deja las predicciones escritas en una tabla o en un archivo. El que las necesita, las va a buscar ahí.
[C] Puede ser online, o a demanda: el modelo queda detrás de un servicio que responde de a un caso por vez, en milisegundos, cuando alguien le pregunta.
[C] O puede ser streaming: las predicciones se van generando a medida que llegan los eventos, en un flujo continuo.
[CD] Y acá lo importante: cuál de las tres corresponde [ÉNFASIS] no lo decide la tecnología. Lo decide el problema.
[C] Un scoring de riesgo crediticio que se revisa todas las noches vive perfecto en batch.
[C] Pero una detección de fraude que tiene que frenar una transacción [ÉNFASIS] antes de aprobarla... no.
[C] En esta materia vamos a trabajar el caso batch, porque es el que nos deja recorrer el ciclo completo de MLOps sin meternos con toda la infraestructura de un servicio en vivo. El serving online tiene su propia complejidad, y lo van a ver más adelante en el posgrado. Pero quédense con que la modalidad [ÉNFASIS] es una decisión de diseño. No es la única forma de hacer inferencia.
[CD] Y ahora sí, la idea central de este bloque. Son dos pipelines distintos... que comparten etapas.
[PAUSA CORTA] Y esa etapa compartida —la transformación de features— es el punto donde más fallan los sistemas de Machine Learning en producción.
Y fíjense que el problema existe igual en las tres modalidades: el modelo necesita recibir los datos transformados de la misma manera con la que aprendió. Lo llame un proceso que corre de noche, o lo llame una API.
[CD] Antes de seguir, un dato que vale la pena. Un pipeline bien cortado en etapas les da algo que el notebook no les da nunca: poder reejecutar solamente la parte que cambió.
Si ajustaron un hiperparámetro, no necesitan volver a bajar y limpiar cuarenta gigas de datos. Retoman desde el artifact de la etapa anterior.
[PAUSA] Todo esto lo vamos a implementar de verdad más adelante en el curso, cuando lleguemos a la orquestación. Por ahora quédense con el concepto.
[CD] Bien. Si el pipeline es la secuencia... el componente es cada etapa individual.
[CD] Y un componente se define por su contrato, no por su código.
[C] Tiene entradas: los artifacts que consume.
[C] Tiene parámetros: la configuración que lo gobierna. Hiperparámetros, umbrales, rutas. Fuera del código, no escritos a mano en el medio.
[C] Tiene código: la transformación en sí.
[C] Y tiene salidas: los artifacts que produce.
[PAUSA CORTA] Que el contrato esté explícito es justamente lo que hace que el componente sea reemplazable. Pueden cambiar por completo cómo entrenan adentro de esa etapa, y mientras siga recibiendo el mismo dataset y devolviendo un modelo con la misma interfaz... el resto del pipeline ni se entera.
[CD] Y ahora sí, el concepto central de todo el video.
Un artifact es cualquier objeto [ÉNFASIS] persistido que una etapa del pipeline produce, y que otra etapa —o una persona— va a consumir después.
[PAUSA CORTA] La palabra importante ahí es persistido. Vive en disco, o en un bucket. No en la memoria del proceso.
[CD] ¿Y cuáles son los artifacts típicos de un pipeline de Machine Learning?
[C] El dataset crudo, tal como se ingestó.
[C] El dataset procesado, listo para entrenar.
[C] Los objetos de transformación ajustados: el escalador, el codificador de categóricas, el imputador.
[C] El modelo serializado.
[C] Las métricas de la evaluación.
[C] Los gráficos y los reportes: la matriz de confusión, el reporte de validación.
[C] Y el archivo de predicciones, cuando la inferencia corre en lote.
[CD] Vamos a detenernos en el tercero, porque es el que más cuesta ver.
Cuando ajustan un escalador sobre el conjunto de entrenamiento, ese objeto [ÉNFASIS] aprendió algo de los datos: la media y el desvío de cada columna.
[PAUSA CORTA] O sea que es un objeto entrenado. Igual que el modelo.
[CD] ¿Y qué pasa si guardan el modelo... pero descartan el escalador?
[C] Cuando llegue el momento de predecir, van a tener que ajustar uno nuevo sobre los datos nuevos.
[C] Y la media de los datos nuevos no es la media del entrenamiento.
[C] Así que el modelo va a recibir números que no corresponden a la escala con la que aprendió.
[C] Y va a predecir mal.
[PAUSA] [ÉNFASIS] Y no falla nada. No aparece ningún error en pantalla. El sistema sigue devolviendo predicciones, y nadie se entera.
[C] Eso tiene nombre: se llama training/serving skew, y es una de las causas más comunes de modelos que andan perfecto en el notebook... y pésimo en producción.
[CD] Así que la conclusión, y quiero que esta les quede: el preprocesador ajustado es tan artifact como el modelo. Y viaja con él.
[CD] Ahora, un artifact solo no alcanza. Necesita metadata.
Qué versión del código lo generó, qué datos de entrada usó, con qué parámetros, cuándo, y quién lo corrió.
[PAUSA CORTA] Esa cadena de "de dónde vino cada cosa" se llama linaje. Y es lo que les va a permitir, seis meses después, agarrar el modelo que está en producción y responder con qué datos exactos fue entrenado.
Registrar todo eso a mano no escala, obviamente. Por eso existen dos familias de herramientas que vamos a incorporar más adelante: los sistemas de tracking de experimentos y registro de modelos, que guardan cada corrida con sus parámetros, sus métricas y sus artifacts; y los sistemas de versionado de datos, que le dan a un dataset el mismo tratamiento que el control de versiones le da al código.
[CD] Y de acá sale una regla práctica que vale la pena llevarse: [ÉNFASIS] si no está persistido y versionado, no existe.
Un resultado que vive en la memoria del kernel de un notebook no es un resultado del que se pueda depender.
[CD] Vamos al último bloque.
[CD] Un pipeline vale exactamente lo que vale su capacidad de repetirse. Y para que una corrida sea reproducible hay que fijar tres cosas. No una.
[C] El código. Eso lo resuelve el control de versiones, y es la pata que ya tienen resuelta.
[C] Los datos. Un dataset que se sobrescribe rompe la reproducibilidad, aunque el código esté perfectamente versionado. A esto lo vamos a atacar más adelante, cuando veamos versionado de datos.
[C] Y el entorno: las versiones exactas de Python y de cada librería instalada. Esta es la pata que más se olvida... y de la que vamos a hablar ahora.
[CD] Pensemos cómo lo vienen resolviendo hasta hoy.
Lo más probable es que hayan instalado lo que necesitaban con un pip install, a medida que les iba haciendo falta. Y que si tuvieron que compartir el proyecto con alguien, hayan escrito un requirements punto txt a mano, con la lista de librerías.
[C] Eso alcanza para trabajar solo. Pero deja una pregunta abierta: [ÉNFASIS] ¿qué versión de cada librería?
[CD] Y ahí hay dos agujeros.
[C] Si el archivo dice solamente "scikit-learn", cada persona que lo instale va a recibir la que esté publicada ese día.
[C] Y si dice "scikit-learn igual igual uno punto tres punto dos", bueno, fijaron esa... pero no fijaron nada de lo que scikit-learn instala por debajo. Numpy, scipy, joblib. Nadie las escribió en ninguna lista, y terminan igual en el entorno.
[CD] Acá aparece la distinción que quiero que se lleven, y que es independiente de la herramienta que usen.
[C] Declarar es decir qué necesita el proyecto. Normalmente como un rango: "quiero scikit-learn uno punto equis, de la uno punto cuatro para arriba". Es una intención, y es flexible a propósito: deja entrar correcciones y mejoras sin que haya que tocar el archivo cada semana.
[C] Y resolver es la operación de agarrar esa declaración y decidir, para cada paquete, qué versión exacta se instala. Que es un problema bastante más difícil de lo que parece, porque hay que satisfacer al mismo tiempo todas las restricciones de todas las librerías... y de las librerías de esas librerías.
[CD] El lock file es el resultado escrito de esa resolución.
[C] Fija la versión exacta de cada paquete.
[C] Incluidas las transitivas, esas que nadie declaró.
[C] Y con sus hashes, que permiten verificar que el paquete que se bajó es idéntico bit a bit al que se bajó la primera vez.
[C] Lo genera la herramienta de gestión de dependencias. No se escribe a mano.
[PAUSA CORTA] [C] Y lo más importante de todo: [ÉNFASIS] el lock file se commitea al repositorio. Es lo único que garantiza que la instalación de hoy en su máquina, la de mañana en integración continua, y la del mes que viene en producción... sean idénticas.
[CD] Porque sin lock file, el escenario es siempre el mismo.
Mismo código. Mismo commit. Pero entre una instalación y otra salió una versión nueva de una librería que ni sabían que estaban usando... y el resultado numérico cambió.
[PAUSA CORTA] "En mi máquina andaba" casi siempre es un problema de entorno no fijado.
[CD] Ahora, para poder leer esos rangos hay que entender el versionado semántico. O semver.
Una versión tiene tres números: MAYOR, MENOR y PARCHE. Y cada uno comunica algo distinto.
[C] El parche: de uno punto cuatro punto dos, a uno punto cuatro punto tres. Corrección de errores, sin cambios de interfaz. Actualizar debería ser seguro.
[C] El menor: de uno punto cuatro punto dos, a uno punto cinco punto cero. Funcionalidad nueva, compatible hacia atrás. Lo que ya usaban sigue funcionando.
[C] Y el mayor: de uno punto cuatro punto dos, a dos punto cero punto cero. [ÉNFASIS] Cambios incompatibles. Algo que funcionaba puede dejar de funcionar.
[CD] Por eso una restricción como "mayor o igual a uno punto cuatro, menor a dos punto cero" es una declaración razonable: acepta correcciones y funcionalidad nueva, pero frena justo antes del cambio incompatible.
[C] Pero acá está el punto que quiero que quede: [ÉNFASIS] semver es una convención sobre la que confiamos. No es una garantía. Depende de que quien publica la librería la respete. Y aun respetándola, una corrección de bug perfectamente legítima puede cambiarles el tercer decimal de sus métricas.
[C] Así que: el rango declara la intención. El lock file es el que hace la corrida reproducible.
[CD] Y un último detalle que completa el cuadro. Fijar el entorno no alcanza si el código tiene aleatoriedad sin controlar.
La división de los datos, la inicialización de los pesos, el submuestreo de un random forest... todo eso necesita una semilla fija y explícita.
[C] La semilla es un parámetro más del pipeline. Va con los demás, arriba y con nombre.
[CD] Y para cerrar el círculo con el bloque anterior: el lock file es, él mismo, un artifact del pipeline. Es el artifact que describe el entorno en el que todos los demás fueron producidos.
[CD] Bueno, en este video pasamos del mapa general al objeto concreto que van a construir: el pipeline.
[PAUSA] Y para cerrar, cinco ideas.
[C] Uno. Un pipeline es una secuencia explícita de etapas con responsabilidad única, ejecutable de forma automática. El notebook ya es uno... pero implícito.
[C] Dos. Hay dos pipelines: el de entrenamiento y el de inferencia. Y comparten las transformaciones de features. La inferencia puede ser en lote, online o streaming: la modalidad la decide el problema.
[C] Tres. Un artifact es todo lo que una etapa persiste para que otra lo consuma. Si no está persistido y versionado, no existe.
[C] Cuatro. El preprocesador ajustado viaja con el modelo. No hacerlo es la vía directa al training/serving skew.
[C] Y cinco. La reproducibilidad se apoya en tres patas: código, datos y entorno. El lock file es el que fija el entorno.
[PAUSA] En la clase sincrónica van a crear el repositorio del curso y a configurar su entorno de trabajo. Ahí van a generar su primer lock file, y lo van a commitear. Y en la lectura del aula está el paso a paso con la herramienta concreta que usamos este año.
[CD] [SONREÍR / SALUDO FINAL] ¡Nos vemos en el próximo video!
