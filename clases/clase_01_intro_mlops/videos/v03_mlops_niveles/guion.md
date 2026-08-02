# MLOps: definición y niveles de madurez

**Clase 01 — Introducción a MLOps y ciclo de vida de un proyecto de ML**
**Duración estimada:** 18–20 min _(video largo — excepción deliberada al formato habitual de 8–15 min)_

## De qué trata este video / Agenda (1 min)

En este video le ponemos nombre a lo que vamos a hacer durante toda la materia:
- **Qué es MLOps:** la definición, y qué tiene un sistema de ML que no alcanzaba con lo que ya existía en el mundo del software.
- **Los tres niveles de madurez:** el 0, el 1 y el 2, con sus características y sus ventajas.
- **Dónde se para cada equipo:** cómo se decide qué nivel corresponde, y en cuál nos vamos a parar nosotros.

**[Slide: De qué trata este video]**

---

## Introducción (1–2 min)

Arranquemos con una pregunta incómoda sobre el modelo que entrenaron.

**Si mañana les piden reentrenarlo con los datos de este mes y dejarlo funcionando, ¿cuánto tardarían?**

**[Slide: la pregunta — ¿cuánto tardás en reentrenar y dejarlo andando?]**

Tómense un segundo para contestarla en serio. Puede ser "una tarde". Puede ser "dos semanas". Puede ser "no sabría bien por dónde empezar, tendría que buscar el notebook y acordarme qué celdas correr y en qué orden".

Y acá está el punto: **esa respuesta no dice nada sobre la calidad de su modelo.** Dice todo sobre la calidad de su **proceso**. Dos equipos con el mismo modelo y las mismas métricas pueden estar a una tarde o a dos meses de tener una versión actualizada funcionando.

Ese proceso tiene nombre —MLOps— y, lo que es más útil, tiene niveles bien definidos. Vamos a ver cuáles son y cómo se reconoce cada uno.

---

## Desarrollo

### Punto 1: Qué es MLOps y por qué hizo falta (4–5 min)

**[Slide: definición]**

**MLOps** —de *Machine Learning Operations*— es una **cultura y una práctica de ingeniería que busca unificar el desarrollo de los sistemas de aprendizaje automático con su operación.** Dicho de otro modo: que construir el modelo y mantenerlo funcionando dejen de ser dos mundos separados.

Y lo que propone para lograrlo es concreto: **automatización y monitoreo en todos los pasos** de la construcción del sistema — la integración, las pruebas, la publicación, el despliegue y la gestión de la infraestructura.

Si esa idea les suena conocida, es porque viene directamente de **DevOps**.

**[Slide: de DevOps a MLOps]**

DevOps resolvió un problema concreto en el desarrollo de software: había un muro entre quienes escribían el código y quienes lo ponían a funcionar. Automatizando la construcción, las pruebas y el despliegue se logró acortar los ciclos de desarrollo, desplegar más seguido y tener publicaciones confiables. MLOps hereda todo eso.

Pero un sistema de aprendizaje automático **no es un sistema de software cualquiera**, y las diferencias no son detalles. Son cinco.

**[Slide: cinco cosas que hacen distinto a un sistema de ML]**

**1. El equipo.** En un proyecto de ML trabajan perfiles centrados en la experimentación, que no necesariamente tienen experiencia construyendo software de producción. No es una crítica: es una consecuencia de cómo se forma cada rol, y explica buena parte de las fricciones que aparecen después.

**2. El desarrollo es experimental por naturaleza.** Uno prueba features distintas, algoritmos distintos, configuraciones distintas. El desafío no es probar mucho —eso es lo fácil— sino **saber después qué fue lo que funcionó y poder reproducirlo**, manteniendo la mayor reutilización posible de código.

**3. Las pruebas son más que pruebas de código.** Además de los tests unitarios y de integración de siempre, hace falta **validar los datos**, **evaluar la calidad del modelo entrenado** y **validar el modelo** antes de dejarlo pasar a producción.

**4. El despliegue no es subir un artefacto.** En un sistema maduro no se despliega un modelo: se despliega **un pipeline de varios pasos que reentrena y publica el modelo automáticamente**. Eso es bastante más complejo que copiar un archivo a un servidor.

**5. En producción, los modelos se degradan de más formas que el software convencional.** Un servicio que nadie toca hace exactamente lo mismo el año que viene. **Un modelo que nadie toca empeora**, sin que nadie haya cambiado una línea, simplemente porque el mundo del que aprendió cambió. Por eso hay que monitorear las estadísticas de los datos, y no solamente si el servicio responde.

**[Slide: CI, CD y CT]**

De esas diferencias salen las tres piezas que sostienen todo lo demás, y conviene tener claras las definiciones porque se usan todo el tiempo:

- **Integración continua (CI):** probar y validar, cada vez que algo se sube al repositorio, no solo el código y los componentes, sino también **los datos, los esquemas y los modelos**.
- **Entrega continua (CD):** desplegar automáticamente **el sistema de ML completo** —el pipeline— y no un paquete de software suelto.
- **Entrenamiento continuo (CT):** volver a entrenar y publicar el modelo de forma automática. Esta es **una propiedad nueva, exclusiva de los sistemas de ML**: no tiene equivalente en el software tradicional.

---

### Punto 2: Los tres niveles de madurez (7–8 min)

Con eso en la mano, ya podemos hablar de niveles. En la industria se distinguen **tres**, y lo que los diferencia es cuánta de esa automatización está efectivamente implementada.

**[Slide: los tres niveles, vista general]**

#### Nivel 0 — Proceso manual

**[Slide: Nivel 0]**

Es el punto de partida: **cada paso se hace a mano.** Se explora, se prepara el dato, se entrena y se valida de forma interactiva, en notebooks, ejecutando celdas. El proceso termina cuando hay un modelo con métricas aceptables.

Sus características:

- **Proceso manual, guiado por scripts e interactivo.** Todas las transiciones entre etapas las hace una persona.
- **El código es monolítico:** uno o pocos notebooks o scripts, con reusabilidad muy limitada. El objetivo del trabajo es el modelo y sus métricas, no un pipeline.
- **Desconexión entre quien entrena y quien despliega.** El modelo se pasa por encima del muro a otro equipo. Y esa desconexión es exactamente el terreno donde crece el *training/serving skew*, que ya vimos.
- **Publicaciones poco frecuentes.** Se asume que el modelo se va a cambiar cada muchos meses.
- **No hay integración continua**, porque se asume que el modelo casi no cambia: no se testea.
- **No hay entrega continua.** Y hay un detalle importante acá: lo que se despliega es **el servicio de predicción**, no el sistema de ML completo.
- **No hay monitoreo activo del desempeño.** No se registra qué predice el modelo ni cómo le va.

**[Slide: cuándo el Nivel 0 está bien]**

**Y quiero ser claro: el nivel 0 no está mal por definición.** Para un proyecto personal, una prueba de concepto, o para validar rápido si una idea tiene sentido, es exactamente lo que corresponde: es lo más rápido y lo más barato, y el costo de MLOps no se justifica cuando lo único que se busca es saber si el problema se puede resolver.

El problema aparece cuando **ese mismo proceso** se usa para sostener algo de lo que el negocio depende todos los días. Ahí el síntoma es siempre el mismo: **el modelo no se adapta a los cambios del entorno ni a los cambios en los datos que describen ese entorno.** Se degrada, y nadie se entera hasta que alguien se queja.

#### Nivel 1 — Automatización del pipeline de ML

**[Slide: Nivel 1]**

El objetivo de este nivel es lograr el **entrenamiento continuo**, y la forma de lograrlo es automatizando el pipeline.

Acá hay un cambio de mentalidad que es, probablemente, el más importante de toda la materia: **lo que se entrega deja de ser un modelo y pasa a ser un pipeline.**

Sus características:

- **Experimentación rápida:** los pasos están orquestados y las transiciones entre ellos son automáticas, así que probar una idea nueva es barato.
- **Entrenamiento continuo en producción**, con datos frescos, disparado automáticamente.
- **Simetría entre experimentación y operación:** el mismo pipeline que se usa en desarrollo es el que corre en producción. Esta propiedad es clave, y es la que evita la clase de sorpresas de la que veníamos hablando.
- **Código modularizado en componentes** reutilizables, componibles y potencialmente compartibles entre pipelines.
- **Entrega continua de modelos:** el pipeline produce un modelo y lo publica sin intervención manual.
- **Se despliega el pipeline de entrenamiento completo**, que corre de forma recurrente — no un modelo.
- **La salida es un artefacto de inferencia que ya contiene los pasos de preprocesamiento**, exactamente como vimos al hablar de artifacts: las transformaciones ajustadas viajan con el modelo.

**[Slide: los componentes nuevos que aparecen en el Nivel 1]**

Para que todo eso funcione aparecen cuatro componentes que en el nivel 0 no existían:

**Validación de datos.** Antes de entrenar, se chequea que los datos sean los esperados: que el esquema no haya cambiado y que las propiedades estadísticas no se hayan movido de forma significativa. Si algo no da, el pipeline se detiene en vez de entrenar sobre basura.

**Validación del modelo.** Después de entrenar, no alcanza con mirar las métricas: hay que **compararlas contra las del modelo que está actualmente en producción** y decidir si el nuevo lo reemplaza. Un modelo nuevo no es automáticamente mejor.

**Repositorio centralizado de features.** Un lugar único donde las features están definidas y desde donde se sirven, tanto para entrenar como para predecir. Al haber una sola definición, se elimina de raíz la posibilidad de que entrenamiento y predicción calculen distinto.

**Gestión de metadata.** Un registro de cada ejecución: qué versión del pipeline y de cada componente corrió, cuándo, con qué parámetros, dónde quedaron los artifacts y qué métricas dieron. Es el linaje del que ya hablamos, hecho sistema.

**[Slide: los disparadores del pipeline]**

Y aparece algo que en el nivel 0 no tenía sentido preguntarse: **¿qué hace que el pipeline arranque?** Hay cinco disparadores típicos:

1. **A demanda:** alguien lo ejecuta manualmente.
2. **Por calendario:** todos los días, todas las semanas.
3. **Por datos nuevos:** cuando llega un lote de datos frescos.
4. **Por degradación del modelo:** el monitoreo detecta que las métricas cayeron.
5. **Por cambios en la distribución de los datos**, lo que se conoce como *concept drift*.

Fíjense que los dos últimos cierran el ciclo: **el monitoreo deja de ser un informe que alguien mira y pasa a ser algo que dispara acciones.**

**[Slide: ventajas del Nivel 1 sobre el Nivel 0]**

¿Qué gana un equipo al pasar del nivel 0 al 1?

- **Estandarización:** el proceso deja de depender de cómo lo hace cada persona.
- **Prototipado más rápido**, porque los componentes se reutilizan en lugar de reescribirse.
- **Menos tiempo hasta producción** para cada nuevo producto de datos.
- **Capacidad de responder a la degradación del modelo** antes de que se convierta en un problema del negocio.

Y lo que **sigue siendo manual** en este nivel es el cambio al pipeline mismo: si modifican el código del pipeline, alguien lo tiene que actualizar a mano en producción. Justamente eso es lo que resuelve el nivel siguiente.

#### Nivel 2 — Automatización del pipeline de CI/CD

**[Slide: Nivel 2]**

El nivel 2 está pensado para organizaciones con **varios pipelines ya funcionando en producción** y equipos grandes. El foco se corre: ya no se trata de construir el pipeline, sino de **mejorar sus componentes** de forma continua, y de que quienes experimentan puedan probar ideas nuevas y llevarlas a producción rápido.

El ciclo completo tiene **seis etapas**:

1. **Desarrollo y experimentación.** Se prueban algoritmos e ideas de forma iterativa; el resultado es código que se sube al repositorio.
2. **Integración continua del pipeline.** Ese código se construye y se somete a pruebas; la salida son **componentes listos para desplegar**.
3. **Entrega continua del pipeline.** Esos componentes se despliegan en el entorno de destino.
4. **Disparo automatizado.** El pipeline se ejecuta en producción según su calendario o sus disparadores; la salida es **un modelo entrenado**.
5. **Entrega continua del modelo.** El modelo se publica como servicio de predicción.
6. **Monitoreo.** Se recolectan estadísticas sobre datos reales, y eso genera los disparadores para volver a empezar.

**[Slide: qué se testea en el CI de un sistema de ML]**

Y vale la pena detenerse en qué significa "pruebas" acá, porque va bastante más allá de lo habitual: se testea **la lógica de construcción de features**, se testea **que los métodos del modelo hagan lo que dicen**, se verifica **que el entrenamiento converja** y que no aparezcan valores inválidos, se prueba **la integración entre componentes**, y se verifica **que el servicio de predicción sea compatible y responda con la performance esperada**.

**[Slide: los niveles no son una medalla]**

**La clave: el nivel más alto no es "el correcto".** El nivel adecuado depende de cuánto cambian los datos, cada cuánto hay que actualizar el modelo, cuántos modelos se mantienen y cuánta gente los toca. Subir de nivel cuesta tiempo, dinero y complejidad — y montar un nivel 2 para un solo modelo que se actualiza una vez por año es plata tirada.

---

### Punto 3: Dónde estamos y cómo se diagnostica (2 min)

Con todo esto, el diagnóstico honesto: **hoy están en nivel 0.** Y está perfecto que así sea, porque hasta ahora el objetivo era aprender a modelar, y para eso el nivel 0 es el adecuado.

**[Slide: hacia dónde vamos]**

Lo que vamos a hacer en esta materia es llevarlos a un **nivel 1 sólido**, incorporando además algunas piezas del nivel 2 —integración continua desde temprano— porque son prácticas que conviene tener desde el principio y no agregar al final.

**[Slide: cuatro preguntas de diagnóstico]**

Y para cerrar, algo que les va a servir mucho más allá de esta materia. Cuando quieran saber en qué nivel está un equipo —el propio, o uno al que estén por entrar— no busquen la lista de herramientas que usan. Hagan estas cuatro preguntas:

1. **¿Cuánto tardan en reentrenar el modelo con datos nuevos?**
2. **¿Alguien sabe con certeza qué versión está corriendo en producción, y con qué datos se entrenó?**
3. **Si la persona que entrenó ese modelo se va mañana, ¿alguien más puede reproducirlo?**
4. **Cuando el modelo empieza a fallar, ¿se enteran ustedes primero, o el cliente?**

Las respuestas ubican el nivel de madurez de un equipo mucho mejor que cualquier inventario de tecnologías.

---

## Cierre (1 min)

En este video le pusimos nombre y escala a lo que vamos a construir.

Las ideas clave para llevarse:
1. **MLOps** es una cultura y una práctica de ingeniería que busca **unificar el desarrollo de los sistemas de ML con su operación**, mediante automatización y monitoreo en todos los pasos.
2. **No alcanzaba con DevOps:** en ML el desarrollo es experimental, las pruebas incluyen datos y modelo, se despliega un pipeline y no un artefacto, y el sistema se degrada solo aunque nadie lo toque. De ahí que al CI y al CD se sume el **CT**, el entrenamiento continuo.
3. **Nivel 0:** proceso manual, código monolítico, el objetivo es el modelo. Correcto para pruebas de concepto, riesgoso para producción.
4. **Nivel 1:** el entregable pasa a ser un **pipeline automatizado**, con validación de datos y de modelo, metadata, disparadores y simetría entre desarrollo y producción. Es el salto que da más valor por unidad de esfuerzo.
5. **Nivel 2:** integración y entrega continuas **del propio pipeline**. Se justifica con varios pipelines en producción — el nivel más alto no siempre es el correcto.

En la próxima clase empezamos por el primer escalón concreto hacia el nivel 1: convertir ese notebook en código modular y reutilizable.

---

## Notas de producción

- **Fuente principal:** este guion sigue de cerca el documento de referencia de Google Cloud sobre MLOps (ver Referencias). La clasificación en niveles 0/1/2, la lista de cinco diferencias entre un sistema de ML y otro software, los componentes del nivel 1, los cinco disparadores y las seis etapas del nivel 2 están tomados de ahí, con la terminología traducida. Conviene mantener esa fidelidad: es la referencia que los alumnos van a encontrar citada en todos lados.
- **Pantalla:** slides. Para el Punto 2, usar **un mismo diagrama base de etapas que se va llenando de automatización** al pasar de nivel a nivel, en lugar de tres diagramas independientes: así se ve una progresión y no tres cosas distintas. El diagrama del nivel 2 es el único que necesita mostrar dos ciclos anidados (el del pipeline y el del modelo).
- **Animaciones:** en el nivel 0, marcar con un ícono de intervención manual cada transición entre etapas; al pasar al nivel 1, que esos íconos desaparezcan del ciclo de entrenamiento y quede uno solo sobre el despliegue del pipeline; en el nivel 2, que también desaparezca ese. La progresión visual explica la diferencia entre niveles sin una palabra. Las cuatro preguntas de diagnóstico aparecen de a una, con aire para que el alumno las piense.
- **Referencias:** Google Cloud, *MLOps: Continuous delivery and automation pipelines in machine learning* — <https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning> (fuente principal); D. Sculley et al., *Hidden Technical Debt in Machine Learning Systems* (NeurIPS 2015) para la deuda técnica y el código del modelo como fracción pequeña del sistema; Chip Huyen, _Designing Machine Learning Systems_ (O'Reilly) para la degradación del modelo en producción.
- **Continuidad:** retoma el artifact y el artefacto de inferencia del video de pipelines, y el *training/serving skew* del video de contrato de interfaz — el nivel 0 lo produce estructuralmente, por la desconexión entre quien entrena y quien despliega. Prepara el refactor del notebook, el registro de experimentos, la validación de datos, el versionado y la orquestación, sin nombrar herramientas ni ubicarlos por número de clase. El material previo de la cátedra usaba esta misma clasificación; se mantuvo la caracterización para no romper continuidad.
- **Criterio de agnosticismo:** el video no nombra ninguna herramienta. CI, CD y CT se usan como conceptos, que es lo que son; "repositorio centralizado de features" se prefiere a la marca del componente. Si al armar las slides se agregan logos por nivel, se pierde el criterio: mejor dejar que cada tecnología aparezca en su clase.
