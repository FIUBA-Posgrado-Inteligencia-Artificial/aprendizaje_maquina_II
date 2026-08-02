# Entorno de desarrollo y entorno productivo

**Clase 01 — Introducción a MLOps y ciclo de vida de un proyecto de ML**
**Duración estimada:** 14–16 min

## De qué trata este video / Agenda (1 min)

En este video vamos a definir una palabra que se usa todo el tiempo sin definirse: **producción**.
- **Desarrollo y producción:** qué es cada uno y las cinco dimensiones en las que se diferencian.
- **Los entornos propios de un sistema de ML:** por qué entrenar y predecir necesitan cosas distintas.
- **La brecha entre entornos:** de dónde sale el "en mi máquina andaba" y cómo se cierra.

**[Slide: De qué trata este video]**

---

## Introducción (1–2 min)

"Poner en producción". "Esto todavía no está en producción". "Se rompió en producción". Es una expresión que van a escuchar todos los días, y que casi nunca se define.

Así que empecemos por ahí, con una pregunta que parece tonta y no lo es.

**[Slide: ¿esto está en producción?]**

Supongan un notebook que corren a mano todos los martes, y cuyo resultado alguien del área comercial usa para decidir a qué clientes llamar esa semana.

**¿Eso está en producción?**

La respuesta es **sí**. Y esto es lo importante: lo que define a producción **no es la tecnología, ni dónde corre, ni si está dockerizado**. Lo que la define es la **consecuencia de que falle**. Si alguien toma decisiones reales con esa salida, están en producción — con notebook y todo.

Esa confusión es cara, porque los equipos suelen tratar como "todavía es un experimento" a cosas de las que el negocio ya depende. Vamos a poner orden.

---

## Desarrollo

### Punto 1: Qué es desarrollo y qué es producción (5 min)

Primero, qué es un **entorno**. Es el conjunto de infraestructura, dependencias, configuración y datos donde corre el código. No es solo "la máquina": es todo lo que rodea al código y determina cómo se comporta.

**[Slide: los dos entornos]**

**El entorno de desarrollo** es donde se gestan los proyectos. Es donde se hacen los primeros análisis exploratorios y las pruebas de concepto. Su característica definitoria: **es un entorno donde uno puede equivocarse sin miedo**, porque una falla no afecta ningún proceso crítico.

**El entorno productivo** es donde se ejecutan los procesos que **ya fueron validados por el negocio**. Hay muchas más tareas corriendo de forma automática, y es un entorno considerablemente más **estable** que el de desarrollo.

Y hay un tercero que conviene conocer: el entorno de **preproducción** o *staging*, que es una copia lo más fiel posible de producción, donde se prueba lo que está por liberarse. Funciona como último filtro antes de que algo llegue a los usuarios.

**[Slide: las cinco dimensiones]**

Ahora, ¿en qué se diferencian concretamente? En cinco dimensiones.

**1. Propósito.** El entorno de desarrollo se usa para desarrollar y probar aplicaciones y funcionalidades nuevas. El de producción se usa para alojar las aplicaciones y servicios que **están siendo usados por los usuarios finales**.

**2. Escala.** Desarrollo suele correr en una sola máquina, o en un grupo chico. Producción suele tener múltiples máquinas y bastante más capacidad para manejar grandes volúmenes de datos.

**3. Configuración.** En desarrollo la configuración es flexible y poco rigurosa: quien desarrolla cambia y ajusta lo que necesita, cuando lo necesita. En producción la configuración es **rígida y estandarizada**, y eso no es burocracia: es lo que garantiza la estabilidad y la seguridad del sistema.

**4. Acceso.** En desarrollo el acceso es completo y libre — es la máquina de uno. En producción el acceso está **limitado a quienes lo necesitan para cumplir su rol**, y nada más.

**5. Mantenimiento.** En desarrollo, quien encuentra el error es quien lo arregla. En producción, el mantenimiento y la corrección de errores recaen en el equipo de operaciones y soporte, con un sistema en vivo del que dependen usuarios reales.

**[Slide: la asimetría de exigencia]**

**La clave: la diferencia de fondo entre los dos entornos es qué se está optimizando.** En desarrollo se optimiza la **velocidad de iteración**: que probar algo sea barato y rápido. En producción se optimiza la **confiabilidad**: que el sistema haga siempre lo mismo y no se caiga.

Son objetivos legítimos y opuestos, y por eso los dos entornos existen por separado. El problema —y de esto va el resto del video— es cuando esa separación se vuelve una **grieta**.

---

### Punto 2: Los entornos propios de un sistema de ML (4 min)

Todo lo anterior vale para cualquier sistema de software. Pero en un sistema de aprendizaje automático la división en dos no alcanza, porque **dentro de producción conviven dos cargas de trabajo con necesidades casi opuestas**.

**[Slide: entrenar vs. predecir — dos perfiles opuestos]**

**El entrenamiento** consume muchísimo cómputo y memoria, necesita acceso al histórico completo de datos, corre cada tanto, y **puede tardar horas sin que eso sea un problema**: no hay nadie esperando del otro lado. Además necesita todo el instrumental: librerías de exploración, de visualización, de evaluación.

**La inferencia** es lo contrario. No necesita el histórico, necesita el modelo. Tiene que responder rápido, con pocos recursos, y muchas veces bajo una restricción de tiempo estricta. Y no necesita nada del instrumental de exploración.

**Optimizar los dos con el mismo criterio es un error clásico.** El entorno de entrenamiento puede —y debe— ser pesado y completo. El de inferencia debería ser lo más chico y austero posible: cuanto menos tenga adentro, menos cosas pueden fallar y menos superficie hay para mantener.

**[Slide: los datos también son un entorno]**

Y hay una diferencia que en el software tradicional directamente no existe: **en ML, los datos también son parte del entorno.**

En desarrollo se trabaja con una muestra: más chica, muchas veces anonimizada, y casi siempre vieja. En producción llegan los datos **reales, completos, sucios y nuevos**. Un pipeline que anduvo perfecto con la muestra se puede romper con el volumen real, o con una categoría que en la muestra no aparecía, o con un formato de fecha que solo usa una de las sucursales.

Por eso, cuando hablamos de que los entornos tienen que parecerse, no hablamos solo de las librerías: hablamos también de que los datos de desarrollo sean **representativos** de los de producción.

Esto conecta directamente con algo que ya vimos: la **simetría entre experimentación y operación** que caracteriza al nivel 1 de madurez. Que el pipeline que corre en desarrollo sea el mismo que corre en producción es, justamente, la forma de que estas diferencias dejen de sorprender.

---

### Punto 3: La brecha entre entornos y cómo se cierra (4–5 min)

Llegamos al síntoma más conocido de toda la ingeniería de software.

**[Slide: "en mi máquina andaba"]**

Esa frase no es una excusa: es un **diagnóstico**. Significa que el entorno donde se desarrolló y el entorno donde se ejecutó no eran equivalentes, y que nadie se había ocupado de que lo fueran.

¿De dónde sale la diferencia? Casi siempre de la misma lista:

- La **versión del lenguaje** y las **versiones de las librerías**.
- El **sistema operativo** y sus librerías de bajo nivel.
- Las **variables de entorno** y las credenciales.
- Las **rutas** a los archivos, sobre todo cuando están escritas de forma absoluta.
- La **zona horaria** y la configuración regional, que cambian cómo se interpretan fechas y números.
- Los **recursos disponibles**: memoria y cómputo.
- Y, en ML, **los datos**.

**[Slide: el entorno que nadie estandariza]**

Ahora, acá hay algo que quiero que se lleven, porque es contraintuitivo.

Un entorno de producción, por lo general, **ya está muy estandarizado**: alguien se ocupó de que lo esté, porque ahí las fallas duelen. **El que se deja de lado es el entorno de desarrollo.** Cada persona del equipo instala lo que quiere, con la versión que le tocó el día que lo instaló.

Y esa asimetría es exactamente la que genera la brecha. Estandarizar el entorno de desarrollo debería ser, idealmente, una decisión de la empresa; como mínimo, del equipo.

**[Slide: cómo se cierra, de menor a mayor]**

¿Cómo se cierra? Hay cuatro medidas, de menor a mayor compromiso:

**1. Usar las mismas versiones que producción.** La misma versión del lenguaje, y las mismas versiones de cada librería, registradas con precisión. Ya vimos la herramienta conceptual para esto: el **lock file**. Acá se entiende para qué sirve de verdad — no es una comodidad, es lo que hace que el entorno de una persona sea el mismo que el de otra y el mismo que el de producción.

**2. Sacar la configuración del código.** El mismo código tiene que poder correr en los dos entornos; lo único que cambia es la configuración que se le inyecta desde afuera — rutas, credenciales, parámetros de conexión. **Si para pasar a producción hay que editar el código, la brecha está garantizada**, porque el código que se probó no es el código que corre.

**3. Sacar los secretos del código.** Nunca, bajo ninguna circunstancia, credenciales escritas en el repositorio. Se inyectan por entorno, y cada entorno tiene las suyas. Esto no es solo higiene: es lo que permite que desarrollo no tenga acceso a los datos de producción.

**4. Empaquetar el entorno completo.** La medida más fuerte: en lugar de pedirle a cada persona que **reproduzca** el entorno siguiendo instrucciones, se distribuye el entorno **ya armado**, con el sistema operativo, las librerías y todo adentro. Esa es la idea detrás de los **contenedores**, y es lo primero que vamos a ver en la próxima clase.

**[Slide: la regla]**

**La regla que resume todo: el entorno de desarrollo debe parecerse lo más posible al productivo.**

"Lo más posible" no quiere decir idéntico — no tiene sentido que cada persona tenga un clúster propio. Quiere decir idéntico **en todo aquello que pueda cambiar el comportamiento del código**: versiones, configuración, formato de los datos.

Y una advertencia final para que no se pase de rosca: **parecerse no significa usar datos productivos alegremente.** Los datos reales suelen tener restricciones legales y de privacidad, y el acceso a producción está restringido justamente por eso. Lo que se busca es una muestra representativa y anonimizada — parecida en forma y en estadística, no la misma.

---

## Cierre (1 min)

En este video definimos la palabra que da nombre a todo lo demás.

Las ideas clave para llevarse:
1. **Producción no se define por la tecnología, sino por la consecuencia.** Si alguien toma decisiones reales con esa salida, es producción — aunque sea un notebook que se corre a mano.
2. **Desarrollo y producción se diferencian en cinco dimensiones:** propósito, escala, configuración, acceso y mantenimiento. Desarrollo optimiza velocidad de iteración; producción, confiabilidad.
3. **En ML hay dos cargas productivas con perfiles opuestos:** entrenar necesita cómputo, memoria y tiempo; predecir necesita rapidez y austeridad. No se optimizan igual.
4. **Los datos también son parte del entorno**, y suelen ser la diferencia que más sorprende.
5. **"En mi máquina andaba" es un diagnóstico, no una excusa.** Se cierra estandarizando versiones, sacando configuración y secretos del código, y empaquetando el entorno completo. Y el entorno que casi siempre falta estandarizar es el de desarrollo.

Con esto cerramos el panorama conceptual de esta clase. En la próxima empezamos a construir: el primer paso es sacar el código del notebook.

---

## Notas de producción

- **Pantalla:** slides. El gancho inicial funciona mejor con una imagen concreta del notebook de los martes y una flecha hacia una decisión de negocio — que la pregunta "¿esto está en producción?" quede en pantalla unos segundos antes de responderla. Para las cinco dimensiones, una tabla de dos columnas que se va completando fila por fila; conviene que quede armada al final como imagen de resumen, porque es la diapositiva que los alumnos van a querer volver a mirar.
- **Animaciones:** para el bloque de entrenamiento vs. inferencia, dos barras opuestas (cómputo/memoria/tiempo tolerado alto en entrenamiento, bajo en inferencia; latencia exigida al revés) que se dibujan en simultáneo — el contraste visual ahorra medio minuto de explicación. Para la lista de fuentes de divergencia, que aparezcan de a una y queden acumuladas: el efecto de "cuántas cosas pueden diferir" es parte del mensaje.
- **Referencias:** Chip Huyen, _Designing Machine Learning Systems_ (O'Reilly) — cap. 10 para infraestructura y entornos de desarrollo; Google Cloud, *MLOps: Continuous delivery and automation pipelines in machine learning* para la simetría experimentación-operación; *The Twelve-Factor App* (<https://12factor.net>) para configuración por entorno y paridad dev/prod, que es la formulación clásica de los puntos 2 y 3 del cierre.
- **Continuidad:** retoma el lock file del video de pipelines —acá se ve su función real, la paridad entre entornos— y la simetría experimentación-operación del video de niveles. Entrega directamente al tema de contenedores, que es la respuesta completa a la brecha. La diferencia entre imagen de entrenamiento y de inferencia se retoma ahí en detalle, así que acá alcanza con plantearla.
- **Sobre el material previo:** las slides anteriores de la cátedra cerraban proponiendo estandarizar el entorno de desarrollo con scripts de entornos virtuales, y mencionaban entornos de desarrollo en la nube (IDE gestionado, máquinas remotas) como alternativa. El planteo del problema se conserva; la solución se actualizó al lock file y a los contenedores, que es el camino del curso. Si se quiere mencionar la alternativa cloud, va mejor como comentario en la clase sincrónica que en cámara, porque los productos concretos cambian rápido.
- **Criterio de agnosticismo:** no se nombra ninguna herramienta. "Contenedores" se usa como concepto, no la marca; el lock file se menciona sin la herramienta que lo genera.
