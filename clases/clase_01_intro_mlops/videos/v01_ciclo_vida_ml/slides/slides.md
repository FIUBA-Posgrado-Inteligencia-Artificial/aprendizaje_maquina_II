# Slides — v01: Ciclo de vida de un proyecto de ML y roles

> Cada sección separada por `---` es una diapositiva.
> Las notas de layout y animación están entre corchetes `[ ]`.

---

## Diapositiva 1 — Portada

**Operaciones de Aprendizaje Automático I**

Ciclo de vida de un proyecto de ML y roles

`Clase 01 — Video 1`

[Layout: fondo oscuro, título centrado, subtítulo en gris claro]

---

## Diapositiva 2 — De qué trata este video

**¿De qué trata este video?**

- **El ciclo de vida:** Las etapas desde que nace la idea hasta que el modelo está en producción.
- **Los roles clave:** Quién hace qué (Data Engineer, Data Scientist, Data Analyst y ML Engineer).
- **El objetivo de MLOps:** Por qué la puesta en producción es nuestra meta real.

[Layout: tres bloques con iconos o colores representativos que aparecen de a uno]

---

## Diapositiva 3 — Hook

**¿Y después qué?**

- Tenés un notebook que entrena un modelo
- Las métricas son razonables
- Pero... ¿cómo llega ese modelo a un usuario real?
- ¿Quién lo mantiene cuando los datos cambian?
- ¿Cómo lo actualiza alguien que no estuvo en el desarrollo?

[Layout: pregunta principal grande al centro, bullets aparecen de a uno]

---

## Diapositiva 4 — Sección: El ciclo de vida

**El ciclo de vida de un proyecto de ML**

[Layout: diapositiva de sección, fondo de color, texto centrado]

---

## Diapositiva 5 — Ciclo de vida: inicio vacío

**Las etapas de un proyecto de ML**

[Layout: círculo/diagrama vacío o con las 10 posiciones en gris — se irán iluminando en las diapositivas siguientes. Disposición circular u ovalada con flechas en sentido horario.]

---

## Diapositiva 6 — Ciclo: Problema de negocio

**1. Problema de negocio**

> Todo empieza con una necesidad: predecir, clasificar, detectar.

- ¿Qué problema se está resolviendo?
- ¿Qué valor genera resolverlo?
- Antes de tocar datos: entender el negocio

[Layout: diagrama del ciclo con el nodo "Problema de negocio" resaltado, resto en gris]

---

## Diapositiva 7 — Ciclo: Definición de objetivos

**2. Definición de objetivos**

> Traducir el problema de negocio a un objetivo de ML concreto.

- ¿Qué métrica vamos a optimizar?
- ¿Cuál es el criterio de éxito?

[Layout: diagrama del ciclo con nodos 1 y 2 resaltados]

---

## Diapositiva 8 — Ciclo: Recolección y preparación de datos

**3. Recolección de datos y preparación**

> La etapa más subestimada y la que más tiempo consume.

- Conseguir los datos
- Limpiarlos y unificarlos
- Integrar fuentes dispares

[Layout: diagrama del ciclo con nodos 1–3 resaltados]

---

## Diapositiva 9 — Ciclo: Feature engineering

**4. Feature engineering**

> Transformar datos crudos en variables que el modelo puede consumir.

- A veces requiere conocimiento de dominio profundo
- Puede ser la diferencia entre un modelo mediocre y uno bueno

[Layout: diagrama del ciclo con nodos 1–4 resaltados]

---

## Diapositiva 10 — Ciclo: Entrenamiento

**5. Entrenamiento del modelo**

> La parte que ya conocen.

- Ajustar el algoritmo
- Buscar hiperparámetros
- Entrenar sobre el conjunto de entrenamiento

[Layout: diagrama del ciclo con nodos 1–5 resaltados]

---

## Diapositiva 11 — Ciclo: Evaluación

**6. Evaluación del modelo**

> Validar que el modelo generaliza sobre datos que no vio.

- No solo métricas globales
- Validar en los segmentos críticos para el negocio

[Layout: diagrama del ciclo con nodos 1–6 HTTP/HTTPS o diagramas resaltados]

---

## Diapositiva 12 — Ciclo: Despliegue

**7. Despliegue del modelo**

> Poner el modelo donde pueda generar predicciones reales.

- Infraestructura y empaquetado
- Mucho más que "copiar el `.pkl`"

[Layout: diagrama del ciclo con nodos 1–7 resaltados]

---

## Diapositiva 13 — Ciclo: Servicio

**8. Servicio del modelo**

> El modelo está deployado y genera predicciones.

- Sistema automatizado
- Usuario final vía interfaz
- Job de batch nocturno

[Layout: diagrama del ciclo con nodos 1–8 resaltados]

---

## Diapositiva 14 — Ciclo: Monitoreo

**9. Monitoreo del modelo**

> ¿El modelo sigue funcionando bien?

- Los datos cambian
- Los usuarios cambian
- El mundo cambia
- Un modelo puede degradarse **silenciosamente** en producción

[Layout: diagrama del ciclo con nodos 1–9 resaltados]

---

## Diapositiva 15 — Ciclo: Mantenimiento

**10. Mantenimiento del modelo**

> Reentrenar, ajustar, corregir.

- El monitoreo detecta el problema
- El mantenimiento lo resuelve
- **Y el ciclo vuelve a empezar**

[Layout: diagrama del ciclo completo con los 10 nodos resaltados y la flecha de retroalimentación del nodo 10 al nodo 3 (o al 1) visible]

---

## Diapositiva 16 — Insight clave: el ciclo es cíclico

**Este ciclo es cíclico, no lineal**

[Diagrama completo con flecha de retroalimentación bien visible]

> Un modelo con **70% de exactitud en producción** genera mucho más valor que uno con **100% de exactitud que nunca llega a usarse.**

La puesta en producción no es un detalle: **es el objetivo.**

[Layout: diagrama del ciclo completo con flecha de retroalimentación, cita grande en la parte inferior o lateral. Color de acento en el 70% y 100%]

---

## Diapositiva 17 — Sección: Los roles

**Los roles en el ciclo de vida**

[Layout: diapositiva de sección, fondo de color, texto centrado]

---

## Diapositiva 18 — Rol: Data Engineer

**Data Engineer**

Responsable de los **datos**.

- Construye y mantiene pipelines de datos
- Diseña la infraestructura de almacenamiento
- Asegura que los datos lleguen limpios, completos y a tiempo

> Sin un Data Engineer, el Data Scientist trabaja sobre arena.

[Layout: ícono o avatar del rol a la izquierda, texto a la derecha. Las etapas del ciclo de vida correspondientes (recolección y preparación) resaltadas en un diagrama pequeño]

---

## Diapositiva 19 — Rol: Data Scientist

**Data Scientist**

Responsable del **modelo**.

- Selecciona algoritmos y entrena modelos
- Optimiza métricas
- Explora datos en busca de señales

> Es el rol que ejercieron previamente durante la carrera.

[Layout: mismo estilo. Etapas resaltadas: feature engineering, entrenamiento, evaluación]

---

## Diapositiva 20 — Rol: Data Analyst

**Data Analyst**

Responsable de que los datos sean **interpretables** para el negocio.

- Traduce números en insights
- Construye dashboards
- Detecta tendencias
- Trabaja cerca del negocio

[Layout: mismo estilo. Etapas resaltadas: definición de objetivos, evaluación (desde perspectiva de negocio)]

---

## Diapositiva 21 — Rol: ML Engineer

**ML Engineer**

Responsable de llevar el modelo a **producción** y mantenerlo ahí.

- Toma el modelo del Data Scientist
- Lo convierte en un proceso reproducible, versionado, testeado, monitoreable
- Diseña la infraestructura de despliegue
- Integra el modelo con el resto de los sistemas

> **Este es el rol que vamos a ejercer en esta materia.**

[Layout: mismo estilo pero con énfasis visual. Etapas resaltadas: despliegue, servicio, monitoreo, mantenimiento]

---

## Diapositiva 22 — Roles mapeados al ciclo

**¿Quién hace qué?**

[Layout: diagrama del ciclo de vida completo con los cuatro roles posicionados sobre las etapas que les corresponden. Pueden ser colores o iconos distintos por rol. Mostrar solapamiento entre roles en algunas etapas]

> No hay fronteras perfectas. En equipos pequeños una persona cubre varios roles.

---

## Diapositiva 23 — Cierre e Ideas Clave

**Ideas clave de este video**

1. El ciclo de vida de un proyecto de ML tiene 10 etapas — y es **cíclico**.
2. Cada etapa tiene roles responsables: Data Engineer, Data Scientist, Data Analyst, ML Engineer.
3. Un modelo en producción vale más que un modelo perfecto que no llega a usarse.
4. Esta materia los posiciona como **ML Engineers**: toman el trabajo del Data Scientist y lo convierten en algo productivo.

[Layout: lista numerada, cada punto aparece de a uno.]

---

## Diapositiva 24 — Despedida

**¡Muchas gracias!**

Nos vemos en el próximo video.

[Layout: fondo oscuro, logo de la universidad o de la materia en el centro, texto centrado]
