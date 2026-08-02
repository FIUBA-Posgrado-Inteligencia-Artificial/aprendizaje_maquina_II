# Slides — v04: Entorno de desarrollo y entorno productivo

> Cada sección separada por `---` es una diapositiva.
> Las notas de layout y animación están entre corchetes `[ ]`.

---

## Diapositiva 1 — Portada

**Operaciones de Aprendizaje Automático I**

Entorno de desarrollo y entorno productivo

`Módulo 1 — Video 4`

[Layout: fondo oscuro, título centrado, subtítulo en gris claro]

---

## Diapositiva 2 — De qué trata este video

**¿De qué trata este video?**

- **Desarrollo y producción:** qué es cada uno, y las cinco dimensiones en que se diferencian.
- **Los entornos propios de un sistema de ML:** por qué entrenar y predecir necesitan cosas distintas.
- **La brecha entre entornos:** de dónde sale el "en mi máquina andaba" y cómo se cierra.

[Layout: tres bloques que aparecen de a uno]

---

## Diapositiva 3 — Hook

**Un notebook que se corre a mano todos los martes.**

Con su resultado, el área comercial decide a qué clientes llamar esa semana.

# ¿Está en producción?

[Layout: dibujar el flujo — notebook → resultado → decisión de negocio. La pregunta grande abajo. Dejarla en pantalla unos segundos]

---

## Diapositiva 4 — La respuesta

# Sí

Lo que define a producción **no es la tecnología**, ni dónde corre, ni si está containerizado.

**Lo que la define es la consecuencia de que falle.**

> Si alguien toma decisiones reales con esa salida, están en producción — con notebook y todo.

[Layout: el "sí" grande, y el resto apareciendo debajo]

---

## Diapositiva 5 — Sección: los dos entornos

**Desarrollo y producción**

[Layout: diapositiva de sección]

---

## Diapositiva 6 — Qué es un entorno

**Entorno**

> El conjunto de **infraestructura, dependencias, configuración y datos** donde corre el código.

No es solo "la máquina": es todo lo que rodea al código y determina cómo se comporta.

[Layout: capas concéntricas alrededor de un bloque de código]

---

## Diapositiva 7 — Los dos entornos

**Desarrollo**

Donde se gestan los proyectos. Análisis exploratorios, pruebas de concepto.

> **Se puede equivocar sin miedo**: una falla no afecta ningún proceso crítico.

**Producción**

Donde se ejecutan los procesos **ya validados por el negocio**.

> Más tareas automáticas. Considerablemente más **estable**.

[Layout: dos columnas contrastadas, con paletas distintas que se van a mantener el resto del video]

---

## Diapositiva 8 — Y hay un tercero

**Preproducción (*staging*)**

Una copia lo más fiel posible de producción, donde se prueba lo que está por liberarse.

Es el último filtro antes de que algo llegue a los usuarios.

[Layout: la columna del medio, entre las dos anteriores]

---

## Diapositiva 9 — Las cinco dimensiones

**¿En qué se diferencian?**

| | Desarrollo | Producción |
|---|---|---|
| **Propósito** | Desarrollar y probar cosas nuevas | Alojar lo que usan los usuarios finales |
| **Escala** | Una máquina, o pocas | Múltiples máquinas, grandes volúmenes |
| **Configuración** | Flexible y poco rigurosa | Rígida y estandarizada |
| **Acceso** | Completo y libre | Limitado a quien lo necesita por su rol |
| **Mantenimiento** | Quien encuentra el error lo arregla | Equipo de operaciones y soporte |

[Layout: la tabla se completa fila por fila. **Dejarla armada al final como imagen de resumen** — es la diapositiva que los alumnos van a volver a mirar]

---

## Diapositiva 10 — La diferencia de fondo

**Qué se está optimizando en cada uno**

- **Desarrollo** optimiza la **velocidad de iteración**: que probar algo sea barato y rápido.
- **Producción** optimiza la **confiabilidad**: que el sistema haga siempre lo mismo y no se caiga.

> Son objetivos legítimos y opuestos. Por eso los dos entornos existen por separado.

**El problema es cuando esa separación se vuelve una grieta.**

[Layout: dos flechas en direcciones opuestas]

---

## Diapositiva 11 — Sección: lo específico de ML

**Los entornos propios de un sistema de ML**

[Layout: diapositiva de sección]

---

## Diapositiva 12 — Dentro de producción hay dos cargas

**Entrenar y predecir tienen perfiles opuestos**

| | Entrenamiento | Inferencia |
|---|---|---|
| **Cómputo y memoria** | Mucho | Poco |
| **Tiempo tolerado** | Horas: nadie espera | Milisegundos, o una ventana acotada |
| **Datos que necesita** | El histórico completo | Solo el modelo |
| **Instrumental** | Todo: exploración, gráficos, evaluación | Lo mínimo |

[Layout: dos barras opuestas que se dibujan en simultáneo. El contraste visual ahorra medio minuto de explicación]

---

## Diapositiva 13 — El error clásico

**Optimizar los dos con el mismo criterio**

El entorno de **entrenamiento** puede —y debe— ser pesado y completo.

El de **inferencia** debería ser lo más chico y austero posible.

> Cuanto menos tenga adentro, menos cosas pueden fallar y menos superficie hay que mantener.

[Layout: dos cajas de tamaños muy distintos]

---

## Diapositiva 14 — Los datos también son un entorno

**En ML, los datos son parte del entorno**

| Desarrollo | Producción |
|---|---|
| Una muestra | Los datos reales |
| Más chica | Completos |
| Muchas veces anonimizada | Sucios |
| Casi siempre vieja | Nuevos |

> Un pipeline que anduvo con la muestra se puede romper con el volumen real, con una categoría que no aparecía, o con un formato de fecha que usa una sola sucursal.

[Layout: tabla comparativa]

---

## Diapositiva 15 — Conexión con los niveles

**Simetría entre experimentación y operación**

Que el pipeline que corre en desarrollo sea **el mismo** que corre en producción es, justamente, la forma de que estas diferencias dejen de sorprender.

> Es una de las propiedades que caracterizan al nivel 1 de madurez.

[Layout: el mismo pipeline dibujado en los dos entornos, idéntico]

---

## Diapositiva 16 — Sección: la brecha

**La brecha entre entornos**

[Layout: diapositiva de sección]

---

## Diapositiva 17 — El síntoma

# "En mi máquina andaba"

**No es una excusa: es un diagnóstico.**

Significa que el entorno donde se desarrolló y el entorno donde se ejecutó no eran equivalentes — y que nadie se ocupó de que lo fueran.

[Layout: la frase grande arriba]

---

## Diapositiva 18 — De dónde sale la diferencia

**Todo esto puede diferir**

- La **versión del lenguaje** y las **versiones de las librerías**
- El **sistema operativo** y sus librerías de bajo nivel
- Las **variables de entorno** y las credenciales
- Las **rutas** a los archivos, sobre todo si son absolutas
- La **zona horaria** y la configuración regional
- Los **recursos disponibles**: memoria y cómputo
- Y, en ML, **los datos**

[Layout: que aparezcan de a una y queden acumuladas. El efecto de "cuántas cosas pueden diferir" es parte del mensaje]

---

## Diapositiva 19 — El entorno que nadie estandariza

**Contraintuitivo pero cierto**

Producción **ya está muy estandarizada**: alguien se ocupó, porque ahí las fallas duelen.

# El que se deja de lado es el entorno de desarrollo.

Cada persona instala lo que quiere, con la versión que le tocó el día que lo instaló.

> Y esa asimetría es la que genera la brecha.

[Layout: producción prolija y ordenada; desarrollo, cinco máquinas todas distintas]

---

## Diapositiva 20 — Cómo se cierra: cuatro medidas

**De menor a mayor compromiso**

1. **Usar las mismas versiones que producción** — el lenguaje y cada librería, registradas con precisión. Es el **lock file**.
2. **Sacar la configuración del código** — el mismo código en los dos entornos; cambia solo lo que se le inyecta.
3. **Sacar los secretos del código** — nunca credenciales en el repositorio.
4. **Empaquetar el entorno completo** — distribuirlo ya armado, no las instrucciones para reproducirlo.

[Layout: escalera de cuatro escalones, aparecen de a uno]

---

## Diapositiva 21 — Sobre la medida 2

**Si para pasar a producción hay que editar el código, la brecha está garantizada**

Porque el código que se probó **no es** el código que corre.

[Layout: frase única. Es el argumento más fuerte del bloque]

---

## Diapositiva 22 — Sobre la medida 3

**Los secretos nunca van en el código**

Se inyectan por entorno, y cada entorno tiene los suyos.

> No es solo higiene: es lo que permite que **desarrollo no tenga acceso a los datos de producción.**

[Layout: contrastar una credencial escrita en el código contra una variable de entorno]

---

## Diapositiva 23 — Sobre la medida 4

**Reproducir el entorno vs. distribuir el entorno**

En lugar de pedirle a cada persona que **reproduzca** el entorno siguiendo instrucciones, se distribuye el entorno **ya armado**: sistema operativo, librerías y todo adentro.

> Esa es la idea detrás de los **contenedores**, y es lo primero que vamos a ver en la próxima clase.

[Layout: a la izquierda, una receta con pasos; a la derecha, una caja cerrada lista para usar]

---

## Diapositiva 24 — La regla

**El entorno de desarrollo debe parecerse lo más posible al productivo**

"Lo más posible" no quiere decir idéntico —no tiene sentido que cada persona tenga un clúster propio—.

Quiere decir idéntico **en todo aquello que pueda cambiar el comportamiento del código**: versiones, configuración, formato de los datos.

[Layout: frase central]

---

## Diapositiva 25 — Una advertencia

**Parecerse no significa usar datos productivos alegremente**

Los datos reales suelen tener **restricciones legales y de privacidad**, y el acceso a producción está restringido justamente por eso.

Lo que se busca es una **muestra representativa y anonimizada**: parecida en forma y en estadística, no la misma.

[Layout: ícono de candado sobre los datos productivos]

---

## Diapositiva 26 — Cierre e ideas clave

**Ideas clave de este video**

1. **Producción no se define por la tecnología, sino por la consecuencia.** Si alguien decide con esa salida, es producción — aunque sea un notebook.
2. Se diferencian en **cinco dimensiones**: propósito, escala, configuración, acceso y mantenimiento. Desarrollo optimiza iteración; producción, confiabilidad.
3. En ML hay **dos cargas productivas opuestas**: entrenar necesita cómputo y tiempo; predecir, rapidez y austeridad.
4. **Los datos también son parte del entorno**, y suelen ser la diferencia que más sorprende.
5. **"En mi máquina andaba" es un diagnóstico.** Se cierra con versiones fijas, configuración y secretos fuera del código, y el entorno empaquetado. Y el entorno que falta estandarizar casi siempre es el de desarrollo.

[Layout: lista numerada, cada punto aparece de a uno]

---

## Diapositiva 27 — Despedida

**¡Muchas gracias!**

Nos vemos en el próximo video.

[Layout: fondo oscuro, logo centrado]
