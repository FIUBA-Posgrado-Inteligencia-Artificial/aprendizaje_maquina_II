# GUION DE TELEPROMPTER (QPROMPT)

**Módulo 1: Introducción a MLOps y ciclo de vida de un proyecto de ML — Video 3**
**Duración aproximada:** 18 a 20 minutos
**Recomendaciones para lectura:**
- Mantener un ritmo pausado y conversacional.
- Hacer contacto visual constante con la cámara (la lente).
- Las indicaciones entre corchetes `[...]` y las líneas divisorias son guías visuales y NO deben leerse en voz alta.
- Los números importantes se han escrito en letras para facilitar la lectura fluida.
- Registro: **ustedes**.
- La pregunta de apertura pide una **pausa real** de dos o tres segundos: es la que engancha todo el video.

Nomenclatura:

- CD: Cambio de diapositiva
- C: Click

---

[CD]

[SONREÍR] ¡Hola! En este video le vamos a poner nombre a todo lo que venimos haciendo. Vamos a hablar de MLOps.
[CD] Pero antes, por dónde vamos a ir.
[C] Primero, qué es MLOps: la definición, y qué tiene un sistema de Machine Learning que hizo que no alcanzara con lo que ya existía en el mundo del software.
[C] Después, los tres niveles de madurez: el cero, el uno y el dos, con sus características y sus ventajas.
[C] Y por último, dónde se para cada equipo: cómo se decide qué nivel corresponde... y en cuál nos vamos a parar nosotros.
[CD] Bueno, arranquemos con una pregunta un poco incómoda sobre el modelo que entrenaron.
[PAUSA CORTA] Si mañana les piden reentrenarlo con los datos de este mes, y dejarlo funcionando... [ÉNFASIS] ¿cuánto tardarían?
[PAUSA DE ÉNFASIS]
[CD] Tómense un segundo para contestarla en serio.
[C] Puede ser "una tarde".
[C] Puede ser "dos semanas".
[C] O puede ser "no sabría bien por dónde empezar; tendría que buscar el notebook y acordarme qué celdas correr, y en qué orden".
[PAUSA CORTA] [C] Y acá está el punto: esa respuesta [ÉNFASIS] no dice nada sobre la calidad de su modelo. Dice todo sobre la calidad de su proceso.
Dos equipos con el mismo modelo, con las mismas métricas, pueden estar a una tarde... o a dos meses... de tener una versión actualizada funcionando.
[PAUSA CORTA] Ese proceso tiene nombre. Y, lo que es más útil todavía, tiene niveles bien definidos.
[CD] Así que vamos a la definición.
[CD] MLOps —de Machine Learning Operations— es una cultura y una práctica de ingeniería que busca unificar el desarrollo de los sistemas de aprendizaje automático con su operación.
Dicho de otra manera: que construir el modelo y mantenerlo funcionando dejen de ser dos mundos separados.
Y lo que propone para lograrlo es bien concreto: automatización y monitoreo en todos los pasos de la construcción del sistema. La integración, las pruebas, la publicación, el despliegue, y la gestión de la infraestructura.
[CD] Es una disciplina que vive en la intersección de tres mundos.
[C] El aprendizaje automático, que aporta los modelos.
[C] La ingeniería de software, que aporta las prácticas de construcción.
[C] Y las operaciones, que aportan todo lo necesario para que un sistema se mantenga en pie.
[CD] Y esa mezcla no salió de la nada: viene directamente de DevOps.
DevOps resolvió un problema muy concreto en el desarrollo de software. Había un muro entre los que escribían el código y los que lo ponían a andar.
[C] Y la solución fue automatizar la construcción, las pruebas y el despliegue, y hacer que los dos lados trabajaran sobre el mismo proceso. Con eso se lograron ciclos más cortos, despliegues más frecuentes, y publicaciones confiables.
[PAUSA CORTA] MLOps hereda todo eso.
[CD] Pero cuando uno intenta aplicar DevOps tal cual a un sistema de aprendizaje automático... se rompen algunos supuestos. Cinco, para ser precisos.
[CD] El primero: el equipo.
En un proyecto de Machine Learning trabajan perfiles centrados en la experimentación, que no necesariamente tienen experiencia construyendo software de producción.
[PAUSA CORTA] Y ojo, esto no es una crítica: es una consecuencia de cómo se forma cada rol. Pero explica buena parte de las fricciones que aparecen después.
[CD] El segundo: el desarrollo es experimental por naturaleza.
Uno prueba features distintas, algoritmos distintos, configuraciones distintas.
[PAUSA CORTA] Y el desafío no es probar mucho —eso es lo fácil—. El desafío es [ÉNFASIS] saber después qué fue lo que funcionó, y poder reproducirlo.
[CD] El tercero: las pruebas son mucho más que pruebas de código.
Además de los tests de siempre, hace falta [C] validar los datos, [C] evaluar la calidad del modelo entrenado, [C] y validar el modelo antes de dejarlo pasar a producción.
[CD] El cuarto: el despliegue no es subir un artefacto.
En un sistema maduro no se despliega un modelo: se despliega [ÉNFASIS] un pipeline de varios pasos, que reentrena y publica el modelo automáticamente. Y eso es bastante más complejo que copiar un archivo a un servidor.
[CD] Y el quinto, que es el más importante y el que más cuesta aceptar: en producción, los modelos se degradan de más formas que el software convencional.
[C] Un servicio de software que nadie toca va a hacer exactamente lo mismo el año que viene.
[C] [ÉNFASIS] Un modelo que nadie toca va a funcionar peor. Sin que nadie haya cambiado una línea. Simplemente porque el mundo del que aprendió cambió.
[PAUSA CORTA] Ese fenómeno no existe en el software tradicional. Y es la razón de fondo por la que MLOps tuvo que ser algo más que DevOps. Por eso hay que monitorear las estadísticas de los datos... y no solamente si el servicio responde.
[CD] De esos cinco problemas salen las tres piezas que sostienen todo lo demás. Y conviene tener claras las definiciones, porque se usan todo el tiempo.
[C] Integración continua: probar y validar, cada vez que algo se sube al repositorio, no solo el código y los componentes, sino también [ÉNFASIS] los datos, los esquemas y los modelos.
[C] Entrega continua: desplegar automáticamente el sistema de Machine Learning completo —el pipeline— y no un paquete de software suelto.
[C] Y entrenamiento continuo: volver a entrenar y publicar el modelo de forma automática.
[PAUSA CORTA] Esta última es [ÉNFASIS] una propiedad nueva, exclusiva de los sistemas de Machine Learning. No tiene equivalente en el software tradicional.
[CD] Bueno, con eso en la mano, ya podemos hablar de niveles.
[CD] En la industria se distinguen tres. Y lo que los diferencia es cuánta de esa automatización está efectivamente implementada.
[CD] Empecemos por el nivel cero: el proceso manual.
Es el punto de partida, y es cada paso hecho a mano. Se explora, se prepara el dato, se entrena y se valida de forma interactiva, en notebooks, ejecutando celdas. El proceso termina cuando hay un modelo con métricas aceptables.
[C] El proceso es manual, guiado por scripts e interactivo: todas las transiciones entre etapas las hace una persona.
[C] El código es monolítico: uno o pocos notebooks, con una reusabilidad muy limitada. El objetivo del trabajo es el modelo y sus métricas, no un pipeline.
[C] Hay desconexión entre quien entrena y quien despliega: el modelo se pasa por encima del muro a otro equipo. Y esa desconexión es exactamente el terreno donde crece el training/serving skew, que ya vimos.
[C] Las publicaciones son poco frecuentes: se asume que el modelo se va a cambiar cada muchos meses.
[C] No hay integración continua, porque se asume que el modelo casi no cambia. Directamente no se testea.
[C] Y no hay entrega continua. Y acá hay un detalle importante: lo que se despliega es el servicio de predicción... no el sistema de Machine Learning completo.
[C] Tampoco hay monitoreo activo del desempeño. No se registra qué predice el modelo ni cómo le va.
[CD] Ahora, quiero ser bien claro con esto: [ÉNFASIS] el nivel cero no está mal.
Para un proyecto personal, para una prueba de concepto, o para validar rápido si una idea tiene sentido, es exactamente lo que corresponde. Es lo más rápido y lo más barato, y las ventajas de MLOps no compensan su costo cuando lo único que se busca es saber si el problema se puede resolver.
[PAUSA CORTA] [C] El problema aparece cuando [ÉNFASIS] ese mismo proceso se usa para sostener algo de lo que el negocio depende todos los días.
[CD] Y ahí el síntoma es siempre el mismo: el modelo no se adapta a los cambios del entorno, ni a los cambios en los datos que describen ese entorno.
Se degrada. Y nadie se entera hasta que alguien se queja.
[CD] Vamos al nivel uno: la automatización del pipeline de Machine Learning.
El objetivo de este nivel es lograr el entrenamiento continuo. Y la forma de lograrlo es automatizando el pipeline.
[PAUSA CORTA] Acá hay un cambio de mentalidad que es, probablemente, el más importante de toda la materia: [ÉNFASIS] lo que se entrega deja de ser un modelo, y pasa a ser un pipeline.
[CD] ¿Y qué caracteriza a este nivel?
[C] Experimentación rápida: los pasos están orquestados y las transiciones entre ellos son automáticas, así que probar una idea nueva sale barato.
[C] Entrenamiento continuo en producción, con datos frescos, disparado automáticamente.
[C] Simetría entre experimentación y operación: el mismo pipeline que se usa en desarrollo es el que corre en producción. Esta propiedad es clave, y es la que evita esa clase de sorpresas de la que veníamos hablando.
[C] Código modularizado en componentes reutilizables, componibles, y hasta compartibles entre pipelines.
[C] Entrega continua de modelos: el pipeline produce un modelo y lo publica sin intervención manual.
[C] Se despliega el pipeline de entrenamiento completo, que corre de forma recurrente. No un modelo.
[C] Y la salida es un artefacto de inferencia que ya contiene los pasos de preprocesamiento. Exactamente como vimos al hablar de artifacts: las transformaciones ajustadas viajan con el modelo.
[CD] Para que todo eso funcione, aparecen cuatro componentes que en el nivel cero no existían.
[C] Validación de datos. Antes de entrenar, se chequea que los datos sean los esperados: que el esquema no haya cambiado, y que las propiedades estadísticas no se hayan movido de forma significativa. Si algo no da, el pipeline se detiene, en vez de entrenar sobre basura.
[C] Validación del modelo. Después de entrenar, no alcanza con mirar las métricas: hay que compararlas contra las del modelo que está actualmente en producción, y decidir si el nuevo lo reemplaza. [ÉNFASIS] Un modelo nuevo no es automáticamente mejor.
[C] Repositorio centralizado de features. Un lugar único donde las features están definidas y desde donde se sirven, tanto para entrenar como para predecir. Al haber una sola definición, se elimina de raíz la posibilidad de que entrenamiento y predicción calculen distinto.
[C] Y gestión de metadata. Un registro de cada ejecución: qué versión del pipeline y de cada componente corrió, cuándo, con qué parámetros, dónde quedaron los artifacts y qué métricas dieron. Es el linaje del que ya hablamos, hecho sistema.
[CD] Y aparece algo que en el nivel cero ni tenía sentido preguntarse: ¿qué hace que el pipeline arranque?
[C] Puede ser a demanda: alguien lo ejecuta manualmente.
[C] Por calendario: todos los días, todas las semanas.
[C] Por datos nuevos: cuando llega un lote fresco.
[C] Por degradación del modelo: el monitoreo detecta que las métricas cayeron.
[C] O por cambios en la distribución de los datos, lo que se conoce como concept drift.
[PAUSA CORTA] Y fíjense que los dos últimos cierran el ciclo: [ÉNFASIS] el monitoreo deja de ser un informe que alguien mira, y pasa a ser algo que dispara acciones.
[CD] ¿Y qué gana un equipo al pasar del nivel cero al uno?
[C] Estandarización: el proceso deja de depender de cómo lo hace cada persona.
[C] Prototipado más rápido, porque los componentes se reutilizan en lugar de reescribirse.
[C] Menos tiempo hasta producción para cada nuevo producto de datos.
[C] Y capacidad de responder a la degradación del modelo antes de que se convierta en un problema del negocio.
[CD] Ahora, en el nivel uno todavía queda algo manual: el cambio al pipeline mismo. Si modifican el código del pipeline, alguien lo tiene que actualizar a mano en producción.
[PAUSA CORTA] Y justamente eso es lo que resuelve el nivel siguiente.
[CD] El nivel dos: la automatización del pipeline de integración y entrega continuas.
Está pensado para organizaciones con varios pipelines ya funcionando en producción, y equipos grandes. Acá el foco se corre: ya no se trata de construir el pipeline, sino de mejorar sus componentes de forma continua, y de que quienes experimentan puedan probar ideas nuevas y llevarlas a producción rápido.
[CD] El ciclo completo tiene seis etapas.
[C] Uno. Desarrollo y experimentación: se prueban algoritmos e ideas de forma iterativa, y el resultado es código que se sube al repositorio.
[C] Dos. Integración continua del pipeline: ese código se construye y se somete a pruebas. La salida son componentes listos para desplegar.
[C] Tres. Entrega continua del pipeline: esos componentes se despliegan en el entorno de destino.
[C] Cuatro. Disparo automatizado: el pipeline se ejecuta en producción según su calendario o sus disparadores. Y la salida es un modelo entrenado.
[C] Cinco. Entrega continua del modelo: el modelo se publica como servicio de predicción.
[C] Y seis. Monitoreo: se recolectan estadísticas sobre datos reales, y eso genera los disparadores para volver a empezar.
[CD] Y vale la pena detenerse un momento en qué significa "pruebas" acá, porque va bastante más allá de lo habitual.
[C] Se testea la lógica de construcción de features.
[C] Se testea que los métodos del modelo hagan lo que dicen.
[C] Se verifica que el entrenamiento converja, y que no aparezcan valores inválidos.
[C] Se prueba la integración entre componentes.
[C] Y se verifica que el servicio de predicción sea compatible y responda con la performance esperada.
[CD] Ahora, una advertencia importante: [ÉNFASIS] el nivel más alto no es "el correcto".
El nivel adecuado depende de cuánto cambian los datos, cada cuánto hay que actualizar el modelo, cuántos modelos se mantienen, y cuánta gente los toca.
[PAUSA CORTA] Subir de nivel cuesta tiempo, dinero y complejidad. Y montar un nivel dos para un solo modelo que se actualiza una vez por año... es plata tirada.
[CD] Con todo esto, el diagnóstico honesto: hoy ustedes están en nivel cero.
Y está perfecto que así sea, porque hasta ahora el objetivo era aprender a modelar. Y para eso, el nivel cero es el adecuado.
[C] Lo que vamos a hacer en esta materia es llevarlos a un nivel uno sólido, incorporando además algunas piezas del nivel dos —integración continua desde temprano— porque son prácticas que conviene tener desde el principio, y no agregar al final.
[CD] Y para cerrar, algo que les va a servir mucho más allá de esta materia.
Cuando quieran saber en qué nivel está un equipo —el propio, o uno al que estén por entrar— no busquen la lista de herramientas que usan. Hagan estas cuatro preguntas.
[C] Una. ¿Cuánto tardan en reentrenar el modelo con datos nuevos? [PAUSA CORTA]
[C] Dos. ¿Alguien sabe con certeza qué versión está corriendo en producción, y con qué datos se entrenó? [PAUSA CORTA]
[C] Tres. Si la persona que entrenó ese modelo se va mañana, ¿alguien más puede reproducirlo? [PAUSA CORTA]
[C] Y cuatro. Cuando el modelo empieza a fallar... ¿se enteran ustedes primero, o el cliente? [PAUSA]
Las respuestas ubican el nivel de madurez de un equipo mucho mejor que cualquier inventario de tecnologías.
[CD] Bueno, en este video le pusimos nombre y escala a lo que vamos a construir. Y para cerrar, cinco ideas.
[C] Uno. MLOps es una cultura y una práctica de ingeniería que busca unificar el desarrollo de los sistemas de Machine Learning con su operación, mediante automatización y monitoreo en todos los pasos.
[C] Dos. No alcanzaba con DevOps: en Machine Learning el desarrollo es experimental, las pruebas incluyen datos y modelo, se despliega un pipeline y no un artefacto, y el sistema se degrada solo aunque nadie lo toque. De ahí que al CI y al CD se sume el entrenamiento continuo.
[C] Tres. Nivel cero: proceso manual, código monolítico, el objetivo es el modelo. Correcto para pruebas de concepto, riesgoso para producción.
[C] Cuatro. Nivel uno: el entregable pasa a ser un pipeline automatizado, con validación de datos y de modelo, metadata, disparadores y simetría entre desarrollo y producción. Es el salto que da más valor por unidad de esfuerzo.
[C] Y cinco. Nivel dos: integración y entrega continuas del propio pipeline. Se justifica con varios pipelines en producción. El nivel más alto no siempre es el correcto.
[PAUSA] En la próxima clase empezamos por el primer escalón concreto hacia el nivel uno: convertir ese notebook en código modular y reutilizable.
[CD] [SONREÍR / SALUDO FINAL] ¡Nos vemos en el próximo video!
