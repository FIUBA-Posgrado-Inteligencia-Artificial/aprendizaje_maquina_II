# Slides — v03: MLOps, definición y niveles de madurez

> Cada sección separada por `---` es una diapositiva.
> Las notas de layout y animación están entre corchetes `[ ]`.
>
> **Nota de diseño transversal:** para el bloque de niveles, usar **un mismo diagrama base
> de etapas que se va llenando de automatización** al pasar de nivel a nivel, en lugar de
> tres diagramas independientes. Así se ve una progresión y no tres cosas separadas.

---

## Diapositiva 1 — Portada

**Operaciones de Aprendizaje Automático I**

MLOps: definición y niveles de madurez

`Módulo 1 — Video 3`

[Layout: fondo oscuro, título centrado, subtítulo en gris claro]

---

## Diapositiva 2 — De qué trata este video

**¿De qué trata este video?**

- **Qué es MLOps:** la definición, y qué tiene un sistema de ML que no alcanzaba con lo que ya existía.
- **Los tres niveles de madurez:** 0, 1 y 2, con sus características y ventajas.
- **Dónde se para cada equipo:** cómo se decide, y en cuál nos paramos nosotros.

[Layout: tres bloques que aparecen de a uno]

---

## Diapositiva 3 — Hook

**Si mañana les piden reentrenar el modelo con los datos de este mes y dejarlo funcionando…**

# ¿cuánto tardarían?

[Layout: la pregunta grande y sola en pantalla. Dejarla unos segundos en silencio antes de seguir]

---

## Diapositiva 4 — La respuesta no habla del modelo

**Puede ser "una tarde". Puede ser "dos semanas".**

**Puede ser "no sabría por dónde empezar".**

> Esa respuesta no dice nada sobre la calidad del modelo.
> Dice todo sobre la calidad del **proceso**.

[Layout: las tres respuestas aparecen de a una; la cita al final, en color de acento]

---

## Diapositiva 5 — Sección: Qué es MLOps

**Qué es MLOps y por qué hizo falta**

[Layout: diapositiva de sección]

---

## Diapositiva 6 — Definición

**MLOps**

> Una cultura y una práctica de ingeniería que busca **unificar el desarrollo de los sistemas
> de aprendizaje automático con su operación.**

Con automatización y monitoreo en **todos** los pasos: integración, pruebas, publicación, despliegue e infraestructura.

[Layout: definición grande, centrada]

---

## Diapositiva 7 — La intersección de tres mundos

**MLOps vive entre tres mundos**

- **Aprendizaje automático** — aporta los modelos
- **Ingeniería de software** — aporta las prácticas de construcción
- **Operaciones** — aporta lo necesario para que el sistema se mantenga en pie

[Layout: diagrama de Venn de tres círculos, con MLOps en la intersección]

---

## Diapositiva 8 — De DevOps a MLOps

**Viene de DevOps**

DevOps resolvió el muro entre quienes escribían el código y quienes lo ponían a funcionar.

Automatizando construcción, pruebas y despliegue se logró:

- Ciclos de desarrollo más cortos
- Desplegar más seguido
- Publicaciones confiables

**MLOps hereda todo eso.**

[Layout: un muro que se rompe entre dos figuras]

---

## Diapositiva 9 — Pero un sistema de ML es distinto

**Cinco cosas que hacen distinto a un sistema de ML**

[Layout: diapositiva de transición. Los cinco puntos vienen en las siguientes]

---

## Diapositiva 10 — Diferencia 1: el equipo

**1. El equipo**

Trabajan perfiles centrados en la **experimentación**, que no necesariamente tienen experiencia construyendo software de producción.

> No es una crítica: es consecuencia de cómo se forma cada rol, y explica buena parte de las fricciones que aparecen después.

[Layout: iconos de los roles del video 1, para enganchar]

---

## Diapositiva 11 — Diferencia 2: el desarrollo

**2. El desarrollo es experimental por naturaleza**

Se prueban features distintas, algoritmos distintos, configuraciones distintas.

> El desafío no es probar mucho —eso es lo fácil— sino **saber después qué funcionó y poder reproducirlo.**

[Layout: muchas ramas de experimentos, una sola marcada]

---

## Diapositiva 12 — Diferencia 3: las pruebas

**3. Las pruebas son más que pruebas de código**

Además de los tests de siempre, hace falta:

- **Validar los datos**
- **Evaluar la calidad** del modelo entrenado
- **Validar el modelo** antes de dejarlo pasar a producción

[Layout: tres capas de validación apiladas sobre el test unitario clásico]

---

## Diapositiva 13 — Diferencia 4: el despliegue

**4. El despliegue no es subir un artefacto**

No se despliega un modelo: se despliega **un pipeline de varios pasos que reentrena y publica el modelo automáticamente.**

[Layout: contrastar "copiar un archivo a un servidor" contra un pipeline completo]

---

## Diapositiva 14 — Diferencia 5: la degradación

**5. Los modelos se degradan de más formas que el software convencional**

Un servicio que nadie toca hace **exactamente lo mismo** el año que viene.

**Un modelo que nadie toca funciona peor** — sin que nadie cambie una línea, porque el mundo del que aprendió cambió.

> Por eso hay que monitorear las estadísticas de los datos, no solo si el servicio responde.

[Layout: dos curvas en el tiempo — una plana, otra descendente. Es la diapositiva más importante del bloque]

---

## Diapositiva 15 — CI, CD y CT

**Las tres piezas**

- **Integración continua (CI)** — probar y validar el código, los componentes, **los datos, los esquemas y los modelos**
- **Entrega continua (CD)** — desplegar **el sistema de ML completo**, el pipeline, no un paquete suelto
- **Entrenamiento continuo (CT)** — volver a entrenar y publicar el modelo automáticamente

> **CT es una propiedad nueva, exclusiva de los sistemas de ML.** No tiene equivalente en el software tradicional.

[Layout: tres siglas grandes. Al llegar a CT, resaltarla]

---

## Diapositiva 16 — Sección: los niveles

**Los tres niveles de madurez**

[Layout: diapositiva de sección]

---

## Diapositiva 17 — Vista general

**Tres niveles, según cuánta automatización hay implementada**

- **Nivel 0** — proceso manual
- **Nivel 1** — pipeline de ML automatizado
- **Nivel 2** — CI/CD del propio pipeline

[Layout: los tres como escalones. Se van a recorrer de a uno]

---

## Diapositiva 18 — Nivel 0

**Nivel 0 — Proceso manual**

- Proceso **manual, guiado por scripts e interactivo**
- Código **monolítico**: uno o pocos notebooks, reusabilidad muy limitada
- El objetivo del trabajo es **el modelo y sus métricas**, no un pipeline
- **Desconexión** entre quien entrena y quien despliega
- Publicaciones **poco frecuentes**
- **No hay CI** — se asume que el modelo casi no cambia
- **No hay CD** — se despliega el servicio de predicción, no el sistema completo
- **No hay monitoreo activo**

[Layout: el diagrama base de etapas, con un ícono de intervención manual en CADA transición]

---

## Diapositiva 19 — Cuándo el nivel 0 está bien

**El nivel 0 no está mal por definición**

Para un proyecto personal, una prueba de concepto, o para validar rápido si una idea sirve, **es exactamente lo que corresponde**: lo más rápido y lo más barato.

**El problema aparece cuando ese mismo proceso sostiene algo de lo que el negocio depende todos los días.**

[Layout: dos escenarios lado a lado — POC (verde) y producción (rojo)]

---

## Diapositiva 20 — El síntoma del nivel 0

**El modelo no se adapta**

No se adapta a los cambios del entorno, ni a los cambios en los datos que describen ese entorno.

Se degrada. Y nadie se entera hasta que alguien se queja.

[Layout: curva de métrica cayendo lentamente, sin ninguna alarma]

---

## Diapositiva 21 — Nivel 1

**Nivel 1 — Automatización del pipeline de ML**

El objetivo es lograr el **entrenamiento continuo**, automatizando el pipeline.

> **El cambio de mentalidad más importante de la materia:**
> lo que se entrega deja de ser un modelo y pasa a ser **un pipeline.**

[Layout: la cita, grande. Es la idea central del video]

---

## Diapositiva 22 — Nivel 1: características

**Qué caracteriza al nivel 1**

- **Experimentación rápida** — los pasos están orquestados, las transiciones son automáticas
- **Entrenamiento continuo** en producción, con datos frescos
- **Simetría entre experimentación y operación** — el mismo pipeline corre en desarrollo y en producción
- **Componentes reutilizables**, componibles y compartibles
- **Entrega continua de modelos**
- Se despliega **el pipeline completo**, no un modelo
- La salida es un **artefacto de inferencia que ya contiene el preprocesamiento**

[Layout: el diagrama base ahora SIN íconos manuales en el ciclo de entrenamiento; queda uno solo sobre el despliegue del pipeline]

---

## Diapositiva 23 — Los componentes nuevos

**Cuatro piezas que en el nivel 0 no existían**

- **Validación de datos** — ¿cambió el esquema? ¿se movieron las propiedades estadísticas?
- **Validación del modelo** — comparar contra **el que está en producción** y decidir si lo reemplaza
- **Repositorio centralizado de features** — una sola definición, para entrenar y para predecir
- **Gestión de metadata** — qué versión corrió, cuándo, con qué parámetros, dónde quedaron los artifacts

[Layout: las cuatro piezas se enchufan al diagrama del pipeline]

---

## Diapositiva 24 — Los disparadores

**¿Qué hace que el pipeline arranque?**

1. **A demanda** — alguien lo ejecuta
2. **Por calendario** — todos los días, todas las semanas
3. **Por datos nuevos** — llega un lote fresco
4. **Por degradación del modelo** — el monitoreo detecta que las métricas cayeron
5. **Por cambios en la distribución de los datos** — *concept drift*

> Los dos últimos cierran el ciclo: **el monitoreo deja de ser un informe que alguien mira y pasa a disparar acciones.**

[Layout: los cinco disparadores apuntando al inicio del pipeline. Los dos últimos, en color de acento]

---

## Diapositiva 25 — Ventajas del nivel 1

**Qué se gana al pasar del 0 al 1**

- **Estandarización** — el proceso deja de depender de cómo lo hace cada persona
- **Prototipado más rápido** — los componentes se reutilizan
- **Menos tiempo hasta producción**
- **Capacidad de responder a la degradación** antes de que sea un problema del negocio

[Layout: cuatro bloques]

---

## Diapositiva 26 — Lo que sigue siendo manual

**En el nivel 1 todavía hay algo manual**

El cambio **al pipeline mismo**. Si modificás su código, alguien lo tiene que actualizar a mano en producción.

**Eso es lo que resuelve el nivel siguiente.**

[Layout: el diagrama con el único ícono manual restante, resaltado]

---

## Diapositiva 27 — Nivel 2

**Nivel 2 — Automatización del pipeline de CI/CD**

Pensado para organizaciones con **varios pipelines ya funcionando en producción.**

El foco se corre: ya no se trata de construir el pipeline, sino de **mejorar sus componentes** de forma continua.

[Layout: varios pipelines en paralelo, no uno]

---

## Diapositiva 28 — Las seis etapas

**El ciclo completo del nivel 2**

1. **Desarrollo y experimentación** → código al repositorio
2. **Integración continua del pipeline** → componentes listos para desplegar
3. **Entrega continua del pipeline** → desplegados en el entorno destino
4. **Disparo automatizado** → el pipeline corre y produce **un modelo entrenado**
5. **Entrega continua del modelo** → publicado como servicio de predicción
6. **Monitoreo** → estadísticas sobre datos reales, que generan los disparadores

[Layout: dos ciclos anidados — el del pipeline y el del modelo. Es el único diagrama que necesita esa complejidad]

---

## Diapositiva 29 — Qué se testea en el CI de un sistema de ML

**"Pruebas" acá significa bastante más de lo habitual**

- La **lógica de construcción de features**
- Que **los métodos del modelo** hagan lo que dicen
- Que el **entrenamiento converja** y no aparezcan valores inválidos
- La **integración entre componentes**
- Que el **servicio de predicción** sea compatible y responda con la performance esperada

[Layout: lista, aparece de a una]

---

## Diapositiva 30 — Los niveles no son una medalla

**El nivel más alto no es "el correcto"**

Depende de cuánto cambian los datos, cada cuánto hay que actualizar, cuántos modelos se mantienen y cuánta gente los toca.

> Un nivel 2 montado para un solo modelo que se actualiza una vez por año **es plata tirada.**

[Layout: frase de cierre del bloque, centrada]

---

## Diapositiva 31 — Dónde estamos

**Hoy están en nivel 0**

Y está perfecto: hasta ahora el objetivo era aprender a modelar, y para eso el nivel 0 es el adecuado.

**Esta materia los lleva a un nivel 1 sólido**, con algunas piezas del nivel 2 —integración continua desde temprano— porque conviene tenerlas desde el principio y no agregarlas al final.

[Layout: los tres escalones, con una marca en el 0 y una flecha hacia el 1]

---

## Diapositiva 32 — Cuatro preguntas de diagnóstico

**Para saber en qué nivel está un equipo, no mires las herramientas. Preguntá:**

1. **¿Cuánto tardan en reentrenar el modelo con datos nuevos?**
2. **¿Alguien sabe con certeza qué versión está corriendo, y con qué datos se entrenó?**
3. **Si la persona que lo entrenó se va mañana, ¿alguien más puede reproducirlo?**
4. **Cuando el modelo empieza a fallar, ¿se enteran ustedes o el cliente?**

[Layout: las cuatro aparecen de a una, con aire para que el alumno las piense. Diapositiva para dejar quieta]

---

## Diapositiva 33 — Cierre e ideas clave

**Ideas clave de este video**

1. **MLOps** unifica el desarrollo de los sistemas de ML con su operación, mediante automatización y monitoreo en todos los pasos.
2. **No alcanzaba con DevOps:** desarrollo experimental, pruebas sobre datos y modelo, se despliega un pipeline, y el sistema se degrada solo. De ahí el **CT**.
3. **Nivel 0:** manual. Correcto para pruebas de concepto, riesgoso para producción.
4. **Nivel 1:** el entregable pasa a ser **un pipeline automatizado**. El salto que da más valor por unidad de esfuerzo.
5. **Nivel 2:** CI/CD del propio pipeline. El nivel más alto no siempre es el correcto.

[Layout: lista numerada, cada punto aparece de a uno]

---

## Diapositiva 34 — Despedida

**¡Muchas gracias!**

Nos vemos en el próximo video.

[Layout: fondo oscuro, logo centrado]
