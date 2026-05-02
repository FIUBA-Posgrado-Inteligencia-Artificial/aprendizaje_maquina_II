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

## Diapositiva 2 — Hook

**¿Y después qué?**

- Tenés un notebook que entrena un modelo
- Las métricas son razonables
- Pero... ¿cómo llega ese modelo a un usuario real?
- ¿Quién lo mantiene cuando los datos cambian?
- ¿Cómo lo actualiza alguien que no estuvo en el desarrollo?

[Layout: pregunta principal grande al centro, bullets aparecen de a uno]

---

## Diapositiva 3 — Sección: El ciclo de vida

**El ciclo de vida de un proyecto de ML**

[Layout: diapositiva de sección, fondo de color, texto centrado]

---

## Diapositiva 4 — Ciclo de vida: inicio vacío

**Las etapas de un proyecto de ML**

[Layout: círculo/diagrama vacío o con las 10 posiciones en gris — se irán iluminando en las diapositivas siguientes. Disposición circular u ovalada con flechas en sentido horario.]

---

## Diapositiva 5 — Ciclo: Problema de negocio

**1. Problema de negocio**

> Todo empieza con una necesidad: predecir, clasificar, detectar.

- ¿Qué problema se está resolviendo?
- ¿Qué valor genera resolverlo?
- Antes de tocar datos: entender el negocio

[Layout: diagrama del ciclo con el nodo "Problema de negocio" resaltado, resto en gris]

---

## Diapositiva 6 — Ciclo: Definición de objetivos

**2. Definición de objetivos**

> Traducir el problema de negocio a un objetivo de ML concreto.

- ¿Qué métrica vamos a optimizar?
- ¿Cuál es el criterio de éxito?

[Layout: diagrama del ciclo con nodos 1 y 2 resaltados]

---

## Diapositiva 7 — Ciclo: Recolección y preparación de datos

**3. Recolección de datos y preparación**

> La etapa más subestimada y la que más tiempo consume.

- Conseguir los datos
- Limpiarlos y unificarlos
- Integrar fuentes dispares

[Layout: diagrama del ciclo con nodos 1–3 resaltados]

---

## Diapositiva 8 — Ciclo: Feature engineering

**4. Feature engineering**

> Transformar datos crudos en variables que el modelo puede consumir.

- A veces requiere conocimiento de dominio profundo
- Puede ser la diferencia entre un modelo mediocre y uno bueno

[Layout: diagrama del ciclo con nodos 1–4 resaltados]

---

## Diapositiva 9 — Ciclo: Entrenamiento

**5. Entrenamiento del modelo**

> La parte que ya conocen.

- Ajustar el algoritmo
- Buscar hiperparámetros
- Entrenar sobre el conjunto de entrenamiento

[Layout: diagrama del ciclo con nodos 1–5 resaltados]

---

## Diapositiva 10 — Ciclo: Evaluación

**6. Evaluación del modelo**

> Validar que el modelo generaliza sobre datos que no vio.

- No solo métricas globales
- Validar en los segmentos críticos para el negocio

[Layout: diagrama del ciclo con nodos 1–6 resaltados]

---

## Diapositiva 11 — Ciclo: Despliegue

**7. Despliegue del modelo**

> Poner el modelo donde pueda generar predicciones reales.

- Infraestructura y empaquetado
- Mucho más que "copiar el `.pkl`"

[Layout: diagrama del ciclo con nodos 1–7 resaltados]

---

## Diapositiva 12 — Ciclo: Servicio

**8. Servicio del modelo**

> El modelo está deployado y genera predicciones.

- Sistema automatizado
- Usuario final vía interfaz
- Job de batch nocturno

[Layout: diagrama del ciclo con nodos 1–8 resaltados]

---

## Diapositiva 13 — Ciclo: Monitoreo

**9. Monitoreo del modelo**

> ¿El modelo sigue funcionando bien?

- Los datos cambian
- Los usuarios cambian
- El mundo cambia
- Un modelo puede degradarse **silenciosamente** en producción

[Layout: diagrama del ciclo con nodos 1–9 resaltados]

---

## Diapositiva 14 — Ciclo: Mantenimiento

**10. Mantenimiento del modelo**

> Reentrenar, ajustar, corregir.

- El monitoreo detecta el problema
- El mantenimiento lo resuelve
- **Y el ciclo vuelve a empezar**

[Layout: diagrama del ciclo completo con los 10 nodos resaltados y la flecha de retroalimentación del nodo 10 al nodo 3 (o al 1) visible]

---

## Diapositiva 15 — Insight clave: el ciclo es cíclico

**Este ciclo es cíclico, no lineal**

[Diagrama completo con flecha de retroalimentación bien visible]

> Un modelo con **70% de exactitud en producción** genera mucho más valor que uno con **100% de exactitud que nunca llega a usarse.**

La puesta en producción no es un detalle: **es el objetivo.**

[Layout: diagrama del ciclo completo con flecha de retroalimentación, cita grande en la parte inferior o lateral. Color de acento en el 70% y 100%]

---

## Diapositiva 16 — Sección: Los roles

**Los roles en el ciclo de vida**

[Layout: diapositiva de sección, fondo de color, texto centrado]

---

## Diapositiva 17 — Rol: Data Engineer

**Data Engineer**

Responsable de los **datos**.

- Construye y mantiene pipelines de datos
- Diseña la infraestructura de almacenamiento
- Asegura que los datos lleguen limpios, completos y a tiempo

> Sin un Data Engineer, el Data Scientist trabaja sobre arena.

[Layout: ícono o avatar del rol a la izquierda, texto a la derecha. Las etapas del ciclo de vida correspondientes (recolección y preparación) resaltadas en un diagrama pequeño]

---

## Diapositiva 18 — Rol: Data Scientist

**Data Scientist**

Responsable del **modelo**.

- Selecciona algoritmos y entrena modelos
- Optimiza métricas
- Explora datos en busca de señales

> Es el rol que ejercieron en la materia anterior.

[Layout: mismo estilo. Etapas resaltadas: feature engineering, entrenamiento, evaluación]

---

## Diapositiva 19 — Rol: Data Analyst

**Data Analyst**

Responsable de que los datos sean **interpretables** para el negocio.

- Traduce números en insights
- Construye dashboards
- Detecta tendencias
- Trabaja cerca del negocio

[Layout: mismo estilo. Etapas resaltadas: definición de objetivos, evaluación (desde perspectiva de negocio)]

---

## Diapositiva 20 — Rol: ML Engineer

**ML Engineer**

Responsable de llevar el modelo a **producción** y mantenerlo ahí.

- Toma el modelo del Data Scientist
- Lo convierte en un proceso reproducible, versionado, testeado, monitoreable
- Diseña la infraestructura de despliegue
- Integra el modelo con el resto de los sistemas

> **Este es el rol que vamos a ejercer en esta materia.**

[Layout: mismo estilo pero con énfasis visual. Etapas resaltadas: despliegue, servicio, monitoreo, mantenimiento]

---

## Diapositiva 21 — Roles mapeados al ciclo

**¿Quién hace qué?**

[Layout: diagrama del ciclo de vida completo con los cuatro roles posicionados sobre las etapas que les corresponden. Pueden ser colores o iconos distintos por rol. Mostrar solapamiento entre roles en algunas etapas]

> No hay fronteras perfectas. En equipos pequeños una persona cubre varios roles.

---

## Diapositiva 22 — Sección: El contrato entre materias

**¿Dónde encaja esta materia?**

[Layout: diapositiva de sección, fondo de color, texto centrado]

---

## Diapositiva 23 — Flujo de materias: lo que ya vieron

**El camino recorrido**

| Materia | Qué aprendieron | Rol |
|---|---|---|
| Probabilidad y Estadística | Distribuciones, estimación, inferencia | Base matemática |
| Análisis de Datos | Exploración, visualización, patrones | Data Analyst |
| Aprendizaje de Máquina | Entrenar modelos, medir métricas | Data Scientist |

**Artefacto que entregan:** un notebook con un modelo entrenado.

[Layout: tabla o diagrama lineal de izquierda a derecha mostrando las tres materias ya cursadas, con sus artefactos de salida. La flecha apunta hacia esta materia]

---

## Diapositiva 24 — Flujo de materias: esta materia

**Operaciones de Aprendizaje Automático I**

Rol: **ML Engineer**

- Toman el notebook de AMq
- Lo convierten en un proceso reproducible:
  - Empaquetado como módulo Python
  - Testeado y validado
  - Versionado con DVC + MLflow
  - Orquestado con Dagster
  - Con monitoreo de drift

**Artefacto que entregan:** modelo versionado en un registry + pipeline de predicción en lote automatizado.

[Layout: caja central destacada con lista de transformaciones. Flecha de entrada desde AMq, flecha de salida hacia el futuro]

---

## Diapositiva 25 — Flujo de materias: lo que viene

**Lo que viene después**

- **Aprendizaje Profundo:** modelos de redes neuronales. Todo lo que aprendan acá sobre reproducibilidad aplica también ahí.

- **Serving _(maestría)_:** toman el modelo versionado de esta materia y aprenden a servirlo online, en tiempo real. Es el eslabón que cierra el ciclo hacia el usuario final.

[Layout: continuación del diagrama lineal, con las dos materias futuras a la derecha. "Serving" puede mostrarse con una nota "maestría" o con una línea punteada para indicar que es futuro/opcional según el recorrido del alumno]

---

## Diapositiva 26 — El flujo completo del posgrado

**El flujo completo**

```
PyE + Análisis de Datos
        ↓
Aprendizaje de Máquina  →  [notebook con modelo]
        ↓
MLOps I (esta materia)  →  [pipeline reproducible + modelo en registry]
        ↓                          ↓
   Aprendizaje Profundo       Serving (maestría)
```

> _Llegaron con un notebook que entrena un modelo. Se van con un proceso reproducible que entrena, versiona, testea, predice en lote y monitorea ese modelo en producción._

[Layout: diagrama de flujo vertical con flechas. La cita en itálica al pie, tipografía grande]

---

## Diapositiva 27 — Cierre

**Ideas clave de este video**

1. El ciclo de vida de un proyecto de ML tiene 10 etapas — y es **cíclico**.
2. Cada etapa tiene roles responsables: Data Engineer, Data Scientist, Data Analyst, ML Engineer.
3. Un modelo en producción vale más que un modelo perfecto que no llega a usarse.
4. Esta materia los posiciona como **ML Engineers**: toman el trabajo del Data Scientist y lo convierten en algo productivo.

**Próximo video →** Pipelines de ML: componentes y artefactos.

[Layout: lista numerada, cada punto aparece de a uno. Al final aparece el "próximo video" como call to action]
