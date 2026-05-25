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

[SONREÍR] Buenas, ¿cómo están? En este video, vamos a hablar del ciclo de vida de un proyecto de ML

[CD] Veamos primero el mapa de ruta de la materia:

[C] Primero, recorreremos las diez etapas del ciclo de vida de un proyecto de Machine Learning, desde el nacimiento de la idea de negocio hasta el mantenimiento continuo en producción.

[C] Segundo, presentaremos a los protagonistas: los cuatro roles clave en la industria de datos y cuáles son sus áreas de responsabilidad.

[C] Y por último, entenderemos por qué el despliegue no es un simple detalle, sino el verdadero objetivo de MLOps.

[CD] [C] Hasta ahora, venían trabajando sobre un mismo notebook en el que entrenaban un modelo.

Lo exploraron...
lo ajustaron... [C] 
midieron sus métricas...
y, probablemente, lograron algo razonable.

[PAUSA CORTA] Pero ahora viene la gran pregunta que esta materia va a responder:

[C] ¿Y después qué?

[PAUSA CORTA]

[C] ¿Cómo llega ese modelo a un usuario real?

[C] ¿Quién lo mantiene cuando los datos cambian?

[C] ¿Cómo lo actualiza otra persona que no estuvo en el desarrollo original?

[PAUSA DE ÉNFASIS] 

[CD] Para responder eso, primero necesitamos un mapa:

Qué etapas tiene un proyecto de Machine Learning...
desde que nace, hasta que está en producción...
y quién es el responsable de cada parte.

Ese... es el objetivo de este video.

[CD] Un proyecto de Machine Learning no termina cuando el modelo da buenas métricas en el notebook.
Tiene un ciclo de vida mucho más amplio que podemos dividir en etapas.

Vamos a verlas una por una.

[CD] Uno. Problema de negocio.

[C] Todo empieza con una necesidad.

Alguien quiere predecir algo, clasificar algo, o detectar algo.

Antes de tocar una sola línea de datos, hay que entender bien qué problema se está resolviendo...
y qué valor genera resolverlo.

[CD] Dos. Definición de objetivos.

[C] Traducir ese problema de negocio a un objetivo de Machine Learning concreto.

¿Qué métrica vamos a optimizar?

¿Cuál es el criterio de éxito para el proyecto?

[CD] Tres. Recolección de datos y preparación.

[C] Conseguir los datos, limpiarlos y unificarlos.

[ÉNFASIS] Esta etapa suele ser la más subestimada...
y la que más tiempo consume en la práctica diaria. 

[CD] Cuatro. Feature engineering.

[C] Transformar los datos crudos en las variables que el modelo va a consumir.

A veces, esto requiere un conocimiento de dominio muy profundo.

[CD] Cinco. Entrenamiento del modelo.

[C] Esta es la parte que ya conocen bien.

Ajustar el algoritmo, buscar hiperparámetros y entrenar sobre el conjunto de entrenamiento.

[CD] Seis. Evaluación del modelo.

[C] Validar que el modelo realmente generaliza sobre datos que nunca vio.

No nos quedamos solo con métricas globales...
también validamos que el modelo se comporte bien en los segmentos que son críticos para el negocio.

[CD] Siete. Despliegue del modelo.

[C] Poner el modelo en un entorno donde pueda generar predicciones reales.

Esto implica infraestructura, empaquetado y mucho más que simplemente "copiar el archivo punto pe ka ele". 

[CD] Ocho. Servicio del modelo.

[C] El modelo ya está desplegado y está generando predicciones en vivo.

Alguien o algo lo usa:
puede ser un sistema automatizado,
puede ser un usuario final mediante una interfaz,
o puede ser un proceso en batch que corre por las noches. 

[CD] Nueve. Monitoreo del modelo.

[C] El modelo sigue funcionando bien?

Los datos cambian...
los usuarios cambian...
y el mundo cambia.

[PAUSA CORTA]

Un modelo que funcionó muy bien en la evaluación puede degradarse silenciosamente en producción.

[CD] Diez. Mantenimiento del modelo.

[C] Reentrenar, ajustar y corregir.

El monitoreo detecta el problema...
el mantenimiento lo resuelve...
y el ciclo vuelve a empezar. 

[CD] La clave de todo esto es que:

[ÉNFASIS] Este ciclo es cíclico, no lineal.

El monitoreo alimenta de vuelta la recolección de datos y el reentrenamiento.

Un modelo no es algo que se entrega una sola vez y listo.

Es un proceso continuo.

[C] Y aquí va un dato muy importante:

Un modelo con setenta por ciento de exactitud que está en producción...
genera mucho más valor que uno con cien por ciento de exactitud que nunca llega a ser usado.

[PAUSA CORTA] La puesta en producción no es un simple detalle técnico:

Es el objetivo final. 

[CD] A lo largo de este ciclo intervienen distintos perfiles.

En la práctica, los límites entre roles varían según la organización...
pero hay cuatro perfiles que aparecen de forma recurrente.

Vamos a conocerlos.

[CD] Primero: el Data Engineer.

Es el responsable de los datos.

Construye y mantiene los pipelines que mueven los datos desde las fuentes hasta donde pueden ser usados.

Diseña la infraestructura de almacenamiento.

Se encarga de que los datos lleguen limpios, completos y a tiempo.

[PAUSA CORTA] Sin un Data Engineer, el Data Scientist trabaja sobre arena.

[CD] Segundo: el Data Scientist.

Es el responsable del modelo.

Toma los datos preparados y los convierte en predicciones útiles.

Selecciona algoritmos, entrena modelos, optimiza métricas y explora los datos en busca de señales.

Este es el rol que ejercieron previamente durante la carrera.

[CD] Tercero: el Data Analyst.

Es el responsable de que los datos sean interpretables para quienes toman decisiones de negocio.

Traduce los números en insights, construye dashboards y detecta tendencias.

Trabaja muy de cerca con el equipo de negocio.

[CD] Cuarto: el ML Engineer.

Es el responsable de llevar el modelo a producción y mantenerlo ahí.

Toma el modelo que entregó el Data Scientist y lo convierte en un proceso reproducible, versionado, testeado y monitoreable.

Diseña la infraestructura de despliegue e integra el modelo con el resto de los sistemas de la empresa.

[CD] Como se imaginarán, no existe una frontera perfecta.

En equipos pequeños, una sola persona cubre varios de estos roles.

Pero entender estas responsabilidades ayuda a saber qué está esperando de vos quien recibe tu trabajo.

[PAUSA]

[C] Al Data Engineer lo encontramos sobre todo al principio: diseñando la recolección de datos, su procesamiento y preparando el terreno con la feature engineering.

[C] El Data Scientist entra en juego para traducir el negocio a objetivos concretos, entrenar el modelo y validar meticulosamente su evaluación.

[C] Por su parte, el Data Analyst es clave definiendo los objetivos iniciales y reaparece con fuerza en la evaluación para aportar la mirada del negocio.

[C] Y finalmente, el ML Engineer toma la posta al final del ciclo: liderando el despliegue, el servicio activo y el mantenimiento a largo plazo.

[CD] En este video vieron el mapa completo:

Las etapas del ciclo de vida de un proyecto de Machine Learning,
y los roles que intervienen en cada parte.

Para cerrar, las cuatro ideas clave que se tienen que llevar hoy:

[PAUSA CORTA] [C] Uno. El ciclo de vida de un proyecto tiene diez etapas... y es cíclico.

[C] Dos. Cada etapa tiene roles responsables bien definidos:
Data Engineer, Data Scientist, Data Analyst y ML Engineer.

[C] Tres. Un modelo en producción vale muchísimo más que un modelo perfecto que no llega a usarse.

[C] Y cuatro. Esta materia los posiciona a ustedes como ML Engineers:

Es decir, toman el trabajo del Data Scientist...
y lo convierten en algo productivo y real.

[PAUSA] [CD] [SONREÍR / SALUDO FINAL] ¡Muchas gracias y nos vemos en el próximo video!
