# GUION DE TELEPROMPTER (QPROMPT)

**Módulo 1: Introducción a MLOps y ciclo de vida de un proyecto de ML — Video 4**
**Duración aproximada:** 14 a 16 minutos
**Recomendaciones para lectura:**
- Mantener un ritmo pausado y conversacional.
- Hacer contacto visual constante con la cámara (la lente).
- Las indicaciones entre corchetes `[...]` y las líneas divisorias son guías visuales y NO deben leerse en voz alta.
- Los números importantes se han escrito en letras para facilitar la lectura fluida.
- Registro: **ustedes**.
- La pregunta del arranque ("¿está en producción?") necesita una **pausa real** antes de contestarla.

Nomenclatura:

- CD: Cambio de diapositiva
- C: Click

---

[CD]

[SONREÍR] ¡Hola! En este video vamos a definir una palabra que se usa todo el tiempo... y que casi nunca se define. Producción.
[CD] Vamos a ver tres cosas.
[C] Primero, qué es el entorno de desarrollo y qué es el productivo, y las cinco dimensiones en las que se diferencian.
[C] Después, los entornos propios de un sistema de Machine Learning: por qué entrenar y predecir necesitan cosas distintas.
[C] Y por último, la brecha entre entornos: de dónde sale el famoso "en mi máquina andaba"... y cómo se cierra.
[CD] Bueno. "Poner en producción". "Esto todavía no está en producción". "Se rompió en producción". Es una expresión que van a escuchar todos los días.
Así que empecemos por ahí, con una pregunta que parece tonta y no lo es.
[C] Supongan un notebook que corren a mano todos los martes. Y con el resultado de ese notebook, alguien del área comercial decide a qué clientes llamar esa semana.
[PAUSA CORTA] [C] [ÉNFASIS] ¿Eso está en producción?
[PAUSA DE ÉNFASIS]
[CD] La respuesta es sí.
[C] Y esto es lo importante: lo que define a producción [ÉNFASIS] no es la tecnología. Ni dónde corre. Ni si está containerizado o no.
[C] Lo que la define es la consecuencia de que falle.
[PAUSA CORTA] Si alguien toma decisiones reales con esa salida, están en producción. Con notebook y todo.
Y esa confusión es cara, porque los equipos suelen tratar como "todavía es un experimento" a cosas de las que el negocio ya depende. Así que vamos a poner orden.
[CD] Empecemos por lo básico.
[CD] ¿Qué es un entorno? Es el conjunto de infraestructura, dependencias, configuración y datos donde corre el código.
No es solo "la máquina": es todo lo que rodea al código y determina cómo se comporta.
[CD] El entorno de desarrollo es donde se gestan los proyectos. Es donde se hacen los primeros análisis exploratorios y las pruebas de concepto.
Y su característica definitoria es esta: [ÉNFASIS] es un entorno donde uno puede equivocarse sin miedo, porque una falla no afecta ningún proceso crítico.
[C] El entorno productivo, en cambio, es donde se ejecutan los procesos que ya fueron validados por el negocio. Hay muchas más tareas corriendo de forma automática, y es un entorno considerablemente más estable.
[CD] Y hay un tercero que conviene conocer: el entorno de preproducción, o staging.
Es una copia lo más fiel posible de producción, donde se prueba lo que está por liberarse. Funciona como último filtro antes de que algo llegue a los usuarios.
[CD] Ahora, ¿en qué se diferencian concretamente? En cinco dimensiones.
[C] Uno: el propósito. El entorno de desarrollo se usa para desarrollar y probar aplicaciones y funcionalidades nuevas. El de producción, para alojar las aplicaciones y servicios que [ÉNFASIS] están siendo usados por los usuarios finales.
[C] Dos: la escala. Desarrollo suele correr en una sola máquina, o en un grupo chico. Producción suele tener múltiples máquinas, y bastante más capacidad para manejar grandes volúmenes de datos.
[C] Tres: la configuración. En desarrollo es flexible y poco rigurosa: quien desarrolla cambia y ajusta lo que necesita, cuando lo necesita. En producción es rígida y estandarizada. Y eso no es burocracia: es lo que garantiza la estabilidad y la seguridad del sistema.
[C] Cuatro: el acceso. En desarrollo es completo y libre, es la máquina de uno. En producción está limitado a quienes lo necesitan para cumplir su rol. Y nada más.
[C] Y cinco: el mantenimiento. En desarrollo, quien encuentra el error es quien lo arregla. En producción, el mantenimiento y la corrección recaen en el equipo de operaciones y soporte, con un sistema en vivo del que dependen usuarios reales.
[CD] Ahora, la diferencia de fondo entre los dos entornos es qué se está optimizando.
[C] En desarrollo se optimiza la velocidad de iteración: que probar algo sea barato y rápido.
[C] En producción se optimiza la confiabilidad: que el sistema haga siempre lo mismo, y no se caiga.
[PAUSA CORTA] Son objetivos legítimos, y son opuestos. Por eso los dos entornos existen por separado.
[C] El problema —y de esto va el resto del video— es cuando esa separación se vuelve una grieta.
[CD] Pero antes, algo específico de nuestro campo.
[CD] Todo lo anterior vale para cualquier sistema de software. Pero en un sistema de aprendizaje automático la división en dos no alcanza. Porque adentro de producción conviven dos cargas de trabajo con necesidades casi opuestas.
[C] El entrenamiento consume muchísimo cómputo y memoria, necesita acceso al histórico completo de datos, corre cada tanto, y puede tardar horas sin que eso sea un problema: no hay nadie esperando del otro lado. Además necesita todo el instrumental: librerías de exploración, de visualización, de evaluación.
[C] La inferencia es lo contrario. No necesita el histórico, necesita el modelo. Tiene que responder rápido, con pocos recursos, y muchas veces bajo una restricción de tiempo estricta. Y no necesita nada del instrumental de exploración.
[CD] Y acá hay un error clásico: optimizar los dos con el mismo criterio.
El entorno de entrenamiento puede —y debe— ser pesado y completo. El de inferencia debería ser lo más chico y austero posible.
[PAUSA CORTA] Porque cuanto menos tenga adentro, menos cosas pueden fallar, y menos superficie hay para mantener.
[CD] Y hay una diferencia que en el software tradicional directamente no existe: [ÉNFASIS] en Machine Learning, los datos también son parte del entorno.
[C] En desarrollo se trabaja con una muestra: más chica, muchas veces anonimizada, y casi siempre vieja.
[C] En producción llegan los datos reales, completos, sucios y nuevos.
[PAUSA CORTA] Un pipeline que anduvo perfecto con la muestra se puede romper con el volumen real. O con una categoría que en la muestra no aparecía. O con un formato de fecha que solo usa una de las sucursales.
Por eso, cuando hablamos de que los entornos tienen que parecerse, no hablamos solo de las librerías: hablamos también de que los datos de desarrollo sean representativos de los de producción.
[CD] Y esto conecta directamente con algo que ya vimos: la simetría entre experimentación y operación, que caracteriza al nivel uno de madurez.
Que el pipeline que corre en desarrollo sea el mismo que corre en producción es, justamente, la forma de que estas diferencias dejen de sorprender.
[CD] Bueno, vamos al último bloque.
[CD] Llegamos al síntoma más conocido de toda la ingeniería de software. "En mi máquina andaba".
[PAUSA CORTA] Esa frase no es una excusa: [ÉNFASIS] es un diagnóstico. Significa que el entorno donde se desarrolló y el entorno donde se ejecutó no eran equivalentes, y que nadie se había ocupado de que lo fueran.
[CD] ¿Y de dónde sale la diferencia? Casi siempre de la misma lista.
[C] La versión del lenguaje, y las versiones de las librerías.
[C] El sistema operativo y sus librerías de bajo nivel.
[C] Las variables de entorno y las credenciales.
[C] Las rutas a los archivos, sobre todo cuando están escritas de forma absoluta.
[C] La zona horaria y la configuración regional, que cambian cómo se interpretan fechas y números.
[C] Los recursos disponibles: memoria y cómputo.
[C] Y, en Machine Learning, los datos.
[CD] Ahora, acá hay algo que quiero que se lleven, porque es contraintuitivo.
Un entorno de producción, por lo general, [ÉNFASIS] ya está muy estandarizado. Alguien se ocupó de que lo esté, porque ahí las fallas duelen.
[PAUSA CORTA] [C] El que se deja de lado es el entorno de desarrollo. Cada persona instala lo que quiere, con la versión que le tocó el día que lo instaló.
[C] Y esa asimetría es exactamente la que genera la brecha. Estandarizar el entorno de desarrollo debería ser, idealmente, una decisión de la empresa. Como mínimo, del equipo.
[CD] ¿Cómo se cierra? Hay cuatro medidas, de menor a mayor compromiso.
[C] La primera: usar las mismas versiones que producción. La misma versión del lenguaje, y las mismas versiones de cada librería, registradas con precisión. Ya vimos la herramienta conceptual para esto: el lock file. Acá se entiende para qué sirve de verdad: no es una comodidad, es lo que hace que el entorno de una persona sea el mismo que el de otra... y el mismo que el de producción.
[C] La segunda: sacar la configuración del código. El mismo código tiene que poder correr en los dos entornos; lo único que cambia es la configuración que se le inyecta desde afuera. Rutas, credenciales, parámetros de conexión.
[CD] Y esto merece una diapositiva propia, porque es el argumento más fuerte del bloque: [ÉNFASIS] si para pasar a producción hay que editar el código, la brecha está garantizada. Porque el código que se probó no es el código que corre.
[CD] La tercera medida: sacar los secretos del código. Nunca, bajo ninguna circunstancia, credenciales escritas en el repositorio. Se inyectan por entorno, y cada entorno tiene las suyas.
Y esto no es solo higiene: es lo que permite que desarrollo no tenga acceso a los datos de producción.
[CD] Y la cuarta, que es la más fuerte: empaquetar el entorno completo.
En lugar de pedirle a cada persona que [ÉNFASIS] reproduzca el entorno siguiendo instrucciones, se distribuye el entorno [ÉNFASIS] ya armado, con el sistema operativo, las librerías y todo adentro.
[C] Esa es la idea detrás de los contenedores. Y es lo primero que vamos a ver en la próxima clase.
[CD] Bien. La regla que resume todo esto: el entorno de desarrollo debe parecerse lo más posible al productivo.
"Lo más posible" no quiere decir idéntico. No tiene sentido que cada persona tenga un clúster propio. Quiere decir idéntico en todo aquello que pueda cambiar el comportamiento del código: versiones, configuración, formato de los datos.
[CD] Y una advertencia final, para que no se pase de rosca.
[ÉNFASIS] Parecerse no significa usar datos productivos alegremente. Los datos reales suelen tener restricciones legales y de privacidad, y el acceso a producción está restringido justamente por eso.
Lo que se busca es una muestra representativa y anonimizada. Parecida en forma y en estadística. No la misma.
[CD] Bueno, en este video definimos la palabra que le da nombre a todo lo demás. Y para cerrar, cinco ideas.
[C] Uno. Producción no se define por la tecnología, sino por la consecuencia. Si alguien toma decisiones reales con esa salida, es producción. Aunque sea un notebook que se corre a mano.
[C] Dos. Desarrollo y producción se diferencian en cinco dimensiones: propósito, escala, configuración, acceso y mantenimiento. Desarrollo optimiza velocidad de iteración; producción, confiabilidad.
[C] Tres. En Machine Learning hay dos cargas productivas con perfiles opuestos: entrenar necesita cómputo, memoria y tiempo; predecir necesita rapidez y austeridad. No se optimizan igual.
[C] Cuatro. Los datos también son parte del entorno. Y suelen ser la diferencia que más sorprende.
[C] Y cinco. "En mi máquina andaba" es un diagnóstico, no una excusa. Se cierra estandarizando versiones, sacando configuración y secretos del código, y empaquetando el entorno completo. Y el entorno que casi siempre falta estandarizar... es el de desarrollo.
[PAUSA] Con esto cerramos el panorama conceptual de esta clase. En la próxima empezamos a construir: el primer paso es sacar el código del notebook.
[CD] [SONREÍR / SALUDO FINAL] ¡Nos vemos en el próximo video!
