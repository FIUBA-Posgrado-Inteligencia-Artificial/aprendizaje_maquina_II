# GUION DE TELEPROMPTER (QPROMPT)

**Clase 01: Introducción a MLOps y ciclo de vida de un proyecto de ML**
**Duración aproximada:** 8 a 10 minutos
**Recomendaciones para lectura:**
- Mantener un ritmo pausado y conversacional.
- Hacer contacto visual constante con la cámara (la lente).
- Las indicaciones entre corchetes `[...]` y las líneas divisorias son guías visuales y NO deben leerse en voz alta.
- Los números importantes se han escrito en letras para facilitar la lectura fluida.

Nomenclatura:

- CD: Cambio de diapositiva
- C: Click

---

[CD]

[SONREÍR] ¡Hola! ¿Qué tal? Bueno, hoy vamos a hablar sobre el ciclo de vida de un proyecto de Machine Learning.
[CD] Pero antes, déjenme contarles por dónde vamos a ir.
[C] Primero, vamos a recorrer las diez etapas que tiene un proyecto de Machine Learning. Arrancamos desde que nace la idea de negocio... y llegamos hasta el mantenimiento, ya con todo andando en producción.
[C] Después, les voy a presentar a los protagonistas: los cuatro roles clave que vas a encontrar en la industria de los datos, y de qué se encarga cada uno.
[C] Y para cerrar, vamos a ver por qué el despliegue no es un detalle más, sino que es, en el fondo, de lo que se trata todo MLOps.
[CD] [C] A ver... hasta ahora ustedes venían trabajando sobre un mismo notebook, entrenando un modelo.
Lo exploraron... lo ajustaron... [C] miraron las métricas... y seguramente llegaron a algo bastante razonable.
[PAUSA CORTA] Pero ahora viene la gran pregunta, esa que esta materia les va a responder:
[C] ¿y después qué? [PAUSA CORTA]
[C] ¿Cómo hace ese modelo para llegar a un usuario de verdad?
[C] ¿Quién lo cuida cuando los datos empiezan a cambiar?
[C] ¿Y cómo lo actualiza otra persona, que ni siquiera estuvo cuando lo desarrollaron? [PAUSA DE ÉNFASIS] 
[CD] Para responder todo esto, lo primero que necesitamos es un mapa.
[CD] Así que vamos a ver las etapas por las que pasa un proyecto de Machine Learning, desde que nace hasta que llega a producción.
[CD] Uno. El problema de negocio.
[C] Todo arranca con una necesidad. Alguien quiere predecir algo, clasificar algo, o detectar algo. 
Y antes de tocar una sola línea de datos, tenemos que entender bien qué problema estamos resolviendo... 
y, sobre todo, qué valor tiene resolverlo. [C]
[CD] Dos. La definición de objetivos.
[C] Acá agarramos ese problema de negocio y lo traducimos a un objetivo de Machine Learning concreto. 
¿Qué métrica vamos a optimizar? 
¿Cómo sabemos si el proyecto salió bien? [C]
[CD] Tres. La recolección y preparación de los datos.
[C] Conseguir los datos, limpiarlos, juntarlos. 
[ÉNFASIS] Y miren que esta es la etapa más subestimada de todas... 
y, en el día a día, es la que más tiempo nos termina comiendo. [C]
[CD] Cuatro. El feature engineering.
[C] Acá transformamos los datos crudos en las variables que el modelo realmente va a consumir. 
Y a veces, para hacer esto bien, necesitás conocer muchísimo del dominio. [C]
[CD] Cinco. El entrenamiento del modelo.
[C] Esta parte ya la conocen bien. Ajustamos el algoritmo, 
buscamos los hiperparámetros, y entrenamos sobre el conjunto de entrenamiento. [C]
[CD] Seis. La evaluación del modelo.
[C] Acá lo que queremos es confirmar que el modelo de verdad generaliza, que funciona con datos que nunca vio. 
Y ojo, no nos quedamos solo con las métricas globales... 
también chequeamos que se porte bien en esos segmentos que son críticos para el negocio. [C]
[CD] Siete. El despliegue del modelo.
[C] Es poner el modelo en un lugar donde pueda generar predicciones de verdad. 
Y esto implica infraestructura, empaquetado, y bastante más que simplemente "copiar el archivo punto pe ka ele". [C]
[CD] Ocho. El servicio del modelo.
[C] Acá el modelo ya está desplegado, y está generando predicciones en vivo. 
Y alguien, o algo, lo está usando:
 puede ser un sistema automatizado, puede ser un usuario final a través de una interfaz, 
o puede ser un proceso que corre de noche, en batch. [C]
[CD] Nueve. El monitoreo del modelo.
[C] ¿El modelo sigue funcionando bien?
 Porque los datos cambian... los usuarios cambian... el mundo entero cambia. [PAUSA CORTA] Y un modelo que andaba bárbaro en la evaluación puede empezar a degradarse en producción, sin que nadie se dé cuenta. [C]
[CD] Diez. El mantenimiento del modelo.
[C] Reentrenar, ajustar, corregir. 
El monitoreo nos avisa que hay un problema... 
el mantenimiento lo soluciona... 
y el ciclo vuelve a empezar. [C]
[CD] Y acá está la clave de todo: [ÉNFASIS] este ciclo es cíclico, no es lineal. 
El monitoreo le da de comer de vuelta a la recolección de datos y al reentrenamiento. 
Un modelo no es algo que entregás una vez y listo. Es un proceso que no para nunca.
[C] Y déjenme que les marque algo importante: un modelo con setenta por ciento de exactitud, pero que está en producción... 
genera muchísimo más valor que uno con cien por ciento de exactitud que nunca se llega a usar. 
[PAUSA CORTA] Poner algo en producción no es un detalle técnico al final del camino: es el objetivo. [C]
[CD] A lo largo de todo este ciclo van apareciendo distintos perfiles. 
En la práctica, los límites entre los roles cambian bastante según la organización... 
pero hay cuatro perfiles que se repiten una y otra vez. 
Así que vamos a conocerlos.
[CD] El primero: el Data Engineer. 
Es el responsable de los datos. 
Construye y mantiene los pipelines, que son los que mueven los datos desde las fuentes hasta donde los podemos usar. 
Diseña toda la infraestructura de almacenamiento. 
Y se asegura de que los datos lleguen limpios, completos, y a tiempo. 
[PAUSA CORTA] Porque, sin un Data Engineer, el Data Scientist está trabajando sobre arena.
[CD] El segundo: el Data Scientist. 
Es el responsable del modelo. 
Agarra los datos ya preparados y los convierte en predicciones útiles. 
Elige algoritmos, entrena modelos, optimiza métricas, y explora los datos buscando señales. 
Y este es, justamente, el rol que ustedes vinieron ejerciendo a lo largo de la carrera.
[CD] El tercero: el Data Analyst.
Es el que se asegura de que los datos sean interpretables para los que toman las decisiones de negocio. 
Traduce los números en insights, arma dashboards, detecta tendencias. 
Y trabaja muy de cerca con la gente de negocio.
[CD] El cuarto: el ML Engineer.
Es el responsable de llevar el modelo a producción, y de mantenerlo ahí. 
Agarra el modelo que le entregó el Data Scientist y lo convierte en algo reproducible, versionado, testeado y monitoreable. 
Diseña la infraestructura de despliegue, e integra el modelo con el resto de los sistemas de la empresa.
[CD] Y como se estarán imaginando, no hay una frontera perfecta entre todos estos roles. 
En los equipos chicos, una sola persona termina cubriendo varios. 
Pero entender estas responsabilidades te ayuda un montón a saber qué es lo que espera de vos la persona que recibe tu trabajo. 
[PAUSA]
[C] Al Data Engineer lo vamos a encontrar sobre todo al principio: 
diseñando la recolección de los datos, su procesamiento, y preparando el terreno con el feature engineering. 
[PAUSA]
[C] El Data Scientist entra en juego para traducir el negocio a objetivos concretos, 
entrenar el modelo, y validar bien a fondo su evaluación. 
[PAUSA]
[C] El Data Analyst, por su lado, es clave cuando definimos los objetivos iniciales, 
y después reaparece con fuerza en la evaluación, para aportar esa mirada del negocio. 
[PAUSA]
[C] Y, por último, el ML Engineer toma la posta sobre el final del ciclo: liderando 
el despliegue, el servicio activo, y el mantenimiento a largo plazo. 
[PAUSA]
[CD] Bueno, en este video vieron el mapa completo: las etapas del ciclo de vida de un 
proyecto de Machine Learning, y los roles que aparecen en cada parte. 
[PAUSA] 
Y para cerrar, quiero que se lleven cuatro ideas: 
[PAUSA CORTA] 
[C] Uno. El ciclo de vida de un proyecto tiene diez etapas... y es cíclico.
[C] Dos. Cada etapa tiene sus roles responsables bien definidos: Data Engineer, 
Data Scientist, Data Analyst y ML Engineer.
[C] Tres. Un modelo en producción vale muchísimo más que un modelo 
perfecto que nunca se llega a usar.
[C] Y cuatro. Esta materia los posiciona a ustedes como ML Engineers. O sea: 
van a tomar el trabajo del Data Scientist... y lo van a convertir en algo productivo y real.
[PAUSA]
[CD] [SONREÍR / SALUDO FINAL] ¡Muchas gracias, y nos vemos en el próximo video!