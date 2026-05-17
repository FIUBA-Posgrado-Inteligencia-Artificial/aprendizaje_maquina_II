# Ciclo de Vida de un Proyecto de ML y Roles

**Clase 01 — Introducción a MLOps y ciclo de vida de un proyecto de ML**
**Duración estimada:** 8–10 min

---

## Introducción (1–2 min)

Hasta ahora vienen trabajando sobre un mismo notebook en el que entrenan un modelo. Lo exploraron, lo ajustaron, midieron sus métricas y probablemente lograron algo razonable. Pero ahora viene la pregunta que esta materia va a responder: ¿y después qué?

¿Cómo llega ese modelo a un usuario real? ¿Quién lo mantiene cuando los datos cambian? ¿Cómo lo actualiza otra persona que no estuvo en el desarrollo original?

Para responder eso, primero necesitamos un mapa: qué etapas tiene un proyecto de ML desde que nace hasta que está en producción, y quién es responsable de cada parte. Ese es el objetivo de este video.

---

## Desarrollo

### Punto 1: El ciclo de vida de un proyecto de ML (4–5 min)

Un proyecto de ML no termina cuando el modelo da buenas métricas en el notebook. Tiene un ciclo de vida mucho más amplio que podemos dividir en etapas.

**[Slide: diagrama del ciclo — construir paso a paso]**

1. **Problema de negocio:** todo empieza con una necesidad. Alguien quiere predecir algo, clasificar algo, detectar algo. Antes de tocar datos hay que entender bien qué problema se está resolviendo y qué valor genera resolverlo.

2. **Definición de objetivos:** traducir ese problema de negocio a un objetivo de ML concreto. ¿Qué métrica vamos a optimizar? ¿Cuál es el criterio de éxito?

3. **Recolección de datos y preparación:** conseguir los datos, limpiarlos, unificarlos. Esta etapa suele ser la más subestimada y la que más tiempo consume en la práctica.

4. **Feature engineering:** transformar los datos crudos en las variables que el modelo va a consumir. A veces esto requiere conocimiento de dominio profundo.

5. **Entrenamiento del modelo:** la parte que conocen bien. Ajustar el algoritmo, buscar hiperparámetros, entrenar sobre el conjunto de entrenamiento.

6. **Evaluación del modelo:** validar que el modelo generaliza sobre datos que no vio. No solo métricas globales — también validar que el modelo se comporta bien en los segmentos críticos para el negocio.

7. **Despliegue del modelo:** poner el modelo en un entorno donde pueda generar predicciones reales. Esto implica infraestructura, empaquetado y mucho más que "copiar el `.pkl`".

8. **Servicio del modelo:** el modelo ya está deployado y está generando predicciones. Alguien lo usa: puede ser un sistema automatizado, puede ser un usuario final vía interfaz, puede ser un job de batch que corre de noche.

9. **Monitoreo del modelo:** ¿el modelo sigue funcionando bien? Los datos cambian, los usuarios cambian, el mundo cambia. El modelo que funcionó muy bien en la evaluación puede degradarse silenciosamente en producción.

10. **Mantenimiento del modelo:** reentrenar, ajustar, corregir. El monitoreo detecta el problema, el mantenimiento lo resuelve — y el ciclo vuelve a empezar.

**La clave: este ciclo es cíclico, no lineal.** El monitoreo alimenta de vuelta la recolección de datos y el reentrenamiento. Un modelo no es algo que se entrega una vez y listo. Es un proceso continuo.

**Un dato importante:** un modelo con 70% de exactitud que está en producción genera mucho más valor que uno con 100% de exactitud que nunca llega a ser usado. La puesta en producción no es un detalle: es el objetivo.

---

### Punto 2: Los roles en el ciclo (3–4 min)

A lo largo de ese ciclo intervienen distintos perfiles. En la práctica los límites entre roles varían según la organización, pero hay cuatro que aparecen de forma recurrente.

**[Slide: diagrama de roles con sus etapas de responsabilidad]**

**Data Engineer**
Responsable de los datos. Construye y mantiene los pipelines que mueven los datos desde las fuentes hasta donde pueden ser usados. Diseña la infraestructura de almacenamiento. Se encarga de que los datos lleguen limpios, completos y a tiempo. Sin un Data Engineer, el Data Scientist trabaja sobre arena.

**Data Scientist**
Responsable del modelo. Toma los datos preparados y los convierte en predicciones útiles. Selecciona algoritmos, entrena modelos, optimiza métricas, explora los datos en busca de señales. Es el rol que ejercieron en la materia anterior.

**Data Analyst**
Responsable de que los datos sean interpretables para quienes toman decisiones de negocio. Traduce los números en insights, construye dashboards, detecta tendencias. Trabaja muy cerca del negocio.

**ML Engineer**
Responsable de llevar el modelo a producción y mantenerlo ahí. Toma el modelo que entregó el Data Scientist y lo convierte en un proceso reproducible, versionado, testeado, monitoreable. Diseña la infraestructura de despliegue e integra el modelo con el resto de los sistemas.

**[Slide: dónde cae cada rol en el ciclo de vida]**

No existe una frontera perfecta. En equipos pequeños una sola persona cubre varios roles. Pero entender estas responsabilidades ayuda a saber qué está esperando quien recibe tu trabajo.

---

## Cierre (1 min)

En este video vieron el mapa completo: las etapas del ciclo de vida de un proyecto de ML y los roles que intervienen en cada parte.

Las ideas clave para llevarse:
1. El ciclo de vida de un proyecto de ML tiene 10 etapas — y es cíclico.
2. Cada etapa tiene roles responsables: Data Engineer, Data Scientist, Data Analyst, ML Engineer.
3. Un modelo en producción vale más que un modelo perfecto que no llega a usarse.
4. Esta materia los posiciona como ML Engineers: toman el trabajo del Data Scientist y lo convierten en algo productivo.

---

## Notas de producción

- **Pantalla:** slides con diagrama animado del ciclo de vida (construir etapa a etapa) y diagrama de roles con sus zonas de responsabilidad.
- **Animaciones:** el ciclo de vida se construye paso a paso; al llegar al monitoreo, mostrar la flecha de retroalimentación hacia recolección/entrenamiento. El diagrama de roles aparece con las etapas del ciclo de fondo para mostrar solapamiento.
- **Referencias:** Chip Huyen, _Designing Machine Learning Systems_ (O'Reilly) — cap. 1 y 2 para el ciclo de vida y los roles; Google MLOps whitepaper para la definición de etapas.
