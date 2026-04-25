# Propuesta de reestructuración — Operaciones de Aprendizaje Automático I

**Cátedra:** Operaciones de Aprendizaje Automático I — FIUBA, Especialización en Inteligencia Artificial
**Versión:** Borrador para coordinación
**Autor:** Facundo Lucianna

---

## Resumen ejecutivo

Esta propuesta reestructura la materia **Operaciones de Aprendizaje Automático I** para enfocarla en el ciclo completo de **entrenamiento reproducible y operacionalización** de modelos de Machine Learning bajo principios de MLOps, retirando los contenidos de **serving online** que pasan a ser cubiertos por una materia subsiguiente.

La idea central es que cada alumno **llegue con un notebook crudo** producido en la materia anterior (donde aprendieron modelos *shallow*) y **se vaya con un proceso reproducible** que entrena, versiona, testea y predice en lote ese mismo modelo, listo para ser consumido por el equipo que se encargue del serving.

Se mantiene Docker como tecnología transversal del curso, reposicionado desde "envoltura del modelo en producción" hacia "garantía de reproducibilidad del entrenamiento". El programa pasa a 8 clases e incorpora cuatro ejes nuevos que el programa actual no cubre con profundidad: **refactor de notebook a paquete**, **testing y validación de datos/modelos**, **versionado y CI/CD**, y **monitoreo de modelos y detección de drift**.

El dictado adopta un modelo **flipped classroom**: cada clase combina videos teóricos pregrabados (para consumo asincrónico) con una clase sincrónica online de ~1.5 horas dedicada a hands-on guiado y evacuación de dudas. Esto permite usar el tiempo sincrónico de forma intensiva en la práctica sobre el proyecto de cada grupo.

---

## 1. Justificación del cambio

### Contexto actual

El programa vigente dedica las clases 5, 6 y 7 a contenidos de deployment y serving online (batch prediction, APIs y microservicios con FastAPI, estrategias de serving en producción). Una materia posterior del programa absorberá los contenidos de **serving online**, lo que abre tres clases para profundizar en otros aspectos críticos del ciclo de MLOps que actualmente quedan tratados de manera superficial.

### Razones del rediseño

Los relevamientos de la industria y la práctica docente muestran que el principal cuello de botella para llevar modelos a producción no está en el serving sino **antes**: en la falta de procesos reproducibles para entrenar, validar y versionar modelos. El refactor de notebooks experimentales a paquetes mantenibles, el testing de datos y modelos, y la integración continua de proyectos de ML son competencias menos enseñadas y de altísimo valor profesional.

Liberar el espacio de serving online permite tratar estos temas con la profundidad que merecen, sin sacrificar Docker (que se mantiene central) ni la orquestación con Dagster (que pasa a ser el cierre integrador del curso a través de la predicción en lote).

### Conexión con las materias adyacentes

La reestructuración define un **flujo claro de tres etapas** dentro del posgrado:

- **Materia anterior (Aprendizaje de Maquina):** los alumnos producen un notebook que entrena un modelo *shallow* sobre un dataset propio.
- **Operaciones de Aprendizaje Automático I (esta materia):** los alumnos transforman ese notebook en un proceso productivo reproducible, versionado, testeado y orquestado, capaz de generar predicciones en lote de forma automatizada.
- **Materia siguiente (Serving):** los alumnos toman el modelo versionado producido en esta materia y aprenden a servirlo online.

Cada materia recibe un artefacto bien definido de la anterior y entrega uno bien definido a la siguiente. La frase que sintetiza el aporte de Operaciones de Aprendizaje Automático I queda:

> *"Los alumnos llegan con un notebook que entrena un modelo y se van con un proceso reproducible que entrena, versiona, testea, predice en lote y monitorea ese modelo en producción."*

### Conservación de Docker

Docker se mantiene como tecnología fundamental del curso, pero se reposiciona conceptualmente. En el programa actual aparece principalmente como envoltura del modelo de inferencia. En la propuesta nueva se utiliza desde la clase 3 como **garantía de reproducibilidad del entorno de entrenamiento**, y como infraestructura para levantar localmente el stack completo de MLOps (MLflow, Postgres, MinIO, Jupyter) vía Docker Compose. Es la herramienta que asegura que el pipeline corre igual en la máquina del alumno, en CI y en producción.

### Formato de dictado — flipped classroom

Cada clase se divide en cuatro componentes complementarios:

- **Videos teóricos pregrabados (asincrónico):** segmentos cortos de 8 a 15 minutos cada uno que cubren los conceptos estables de la clase. El alumno los consume a su propio ritmo antes de la clase sincrónica.
- **Materiales de lectura (Moodle, asincrónico):** guías prácticas sobre tooling específico del stack. Se separan de los videos porque son contenidos que cambian con el tiempo (herramientas, versiones, configuraciones concretas) y pueden actualizarse sin regrabar.
- **Actividades transversales (Moodle):** un evaluativo de 10 preguntas de opción múltiple por módulo (intentos ilimitados, requiere >8/10 para aprobar la materia), un foro de dudas previo a cada clase sincrónica, y un glosario colaborativo que los alumnos construyen a lo largo del curso.
- **Clase sincrónica online (~1.5 horas):** dedicada íntegramente a hands-on guiado sobre el proyecto de cada grupo. El docente llega habiendo revisado el foro y aprovecha el tiempo para desbloquear problemas en tiempo real.

Este formato permite usar el tiempo sincrónico de forma intensiva: los alumnos llegan con la teoría ya vista y aprovechan la clase para aplicar los conceptos sobre su propio modelo.

---

## 2. Programa nuevo — 8 clases

El hilo conductor del curso es **"de notebook a pipeline reproducible de entrenamiento y predicción en lote"**. Cada clase agrega una capa al pipeline que el alumno construye sobre su propio modelo de la materia anterior. La integración continua (CI/CD con GitHub Actions) atraviesa todas las clases en lugar de ser una clase aparte: cada nuevo concepto incorporado se traduce en un step adicional del workflow.

### Actividades transversales (todos los módulos)

Cada clase/módulo incluye las siguientes actividades fijas en Moodle:

**Foro de dudas:** un foro por clase donde los alumnos publican preguntas sobre los videos y lecturas antes de la sesión sincrónica. El docente llega a la clase sabiendo qué desbloquear.

**Evaluativo:** 10 preguntas de opción múltiple sobre los conceptos del módulo. Intentos ilimitados. Se requiere >8/10 en todos los evaluativos para aprobar la materia.

**Glosario colaborativo del curso:** actividad única compartida entre todas las clases. Los alumnos van incorporando y definiendo términos MLOps a medida que avanzan en el programa. Contribuir al glosario es parte de la cursada.

---

### Clase 1 — Introducción a MLOps y ciclo de vida de un proyecto de ML

Introducción al rol de MLOps en el ciclo de vida de un sistema de ML y setup del entorno de trabajo del curso.

**Videos teóricos:**

- Ciclo de vida de un proyecto de ML y roles (Data Engineer, Data Scientist, Data Analyst, ML Engineer)
- Pipelines de ML: componentes y artifacts
- MLOps: definición, niveles 0/1/2 de madurez y ventajas de cada nivel
- Entorno de desarrollo vs entorno productivo: propiedades y diferencias
- Contrato de interfaz entre AMq → MLOps1 → Serving (el flujo del posgrado)

**Materiales de lectura (Moodle):**

- Gestión moderna de dependencias con `uv`: instalación, entornos virtuales, lock files, semver *(se elige `uv` por ser la herramienta actual del stack; el concepto de lock file y semver se cubre en el video de pipelines)*
- Buenas prácticas de programación aplicadas a ML: guía de referencia con ejemplos de código *(introducción práctica; se profundiza en Clase 2)*

**Hands-on (clase sincrónica):** los alumnos crean su repo a partir del template de la cátedra vía GitHub Classroom y configuran su entorno local con `uv`.

### Clase 2 — De notebook a paquete Python

Refactorización sistemática de un notebook experimental hacia un paquete Python testeable y mantenible.

**Videos teóricos:**

- Estructura de proyecto Python (*src layout*, separación I/O / features / training / evaluación)
- Selección del tipo de modelo: 8 consejos (breve, como contexto del refactor)
- Las 4 fases del desarrollo de modelos
- Depuración de modelos: causas típicas de fallas y estrategias
- Introducción a CI/CD: qué es integración continua y por qué importa en ML

**Materiales de lectura (Moodle):**

- Manejo de configuración con Hydra/OmegaConf: guía de instalación y uso básico *(herramienta específica del stack; el concepto de configuración externalizada se cubre en el video de estructura de proyecto)*
- Logging estructurado, type hints y docstrings en Python: guía de referencia con ejemplos *(convenciones que cambian con versiones del lenguaje y herramientas)*
- Pre-commit hooks y linting con `ruff`: configuración paso a paso *(tooling que evoluciona; `ruff` reemplazó a `flake8`/`black`/`isort` pero el concepto de linting es estable)*
- Primer workflow de GitHub Actions: lint + tests en cada push *(implementación concreta de CI; el concepto se cubre en el video)*

**Hands-on (clase sincrónica):** los alumnos toman su notebook real de la materia anterior y lo refactorizan a un paquete con la estructura del template.

### Clase 3 — Docker para reproducibilidad de entrenamiento

Conceptos fundamentales de contenedores reposicionados como garantía de reproducibilidad del entorno de entrenamiento.

**Videos teóricos:**

- Contenedores vs máquinas virtuales: conceptos fundamentales
- Docker: Dockerfile, imágenes, contenedores, Docker Hub
- Dockerfile multi-stage para imágenes de training
- Diferencia entre imagen de desarrollo, training y producción
- El contenedor como contrato entre la máquina del alumno, CI y producción
- Capa de almacenamiento (breve): formatos de datos (CSV vs Parquet, row vs column), ETL/ELT
- Capa de cómputo (breve): escalamiento vertical y horizontal, clusters

**Materiales de lectura (Moodle):**

- Levantar el stack local de MLOps con Docker Compose (MLflow + Postgres + MinIO + Jupyter): guía paso a paso *(configuración concreta del stack del curso; los servicios y versiones pueden cambiar entre ediciones)*

**Hands-on (clase sincrónica):** dockerización del paquete refactorizado de la clase 2 y ejecución del entrenamiento dentro del contenedor. CI extendida: build automático de la imagen de training en cada push.

### Video transversal — Consideraciones para modelos grandes

Video complementario de 15 a 20 minutos, referenciado desde las clases 3, 4 y 7. El objetivo es que los alumnos tengan el mapa mental armado para cuando encuentren cargas intensivas de cómputo en otras materias del posgrado (deep learning, visión, NLP) o en su práctica profesional.

**Contenidos:**

- Cuándo aparece el problema (datos o modelo no entran en memoria, entrenamientos largos)
- Paralelismo de datos: SGD sincrónico vs asincrónico
- Paralelismo de modelo y de pipeline (conceptual)
- GPUs en contenedores: `nvidia-docker`, runtime de GPU, implicancias para imágenes
- Checkpointing y resuming de entrenamientos largos
- Implicancias para MLOps: tracking riguroso, orquestación asíncrona, reproducibilidad estricta

Formato conceptual, sin hands-on. Apunta a conectar estos conceptos con el resto del curso: tracking de runs caros con MLflow (clase 4), orquestación asíncrona con Dagster (clase 7), reproducibilidad estricta con DVC (clase 6).

### Clase 4 — Tracking de experimentos y Model Registry con MLflow

Tracking de experimentos y versionado de modelos como pilares de reproducibilidad.

**Videos teóricos:**

- Por qué trackear experimentos: reproducibilidad, comparación y auditoría de modelos
- MLflow: panorama de componentes (Tracking, Models, Registry, Projects)
- Tracking en profundidad: parámetros, métricas, artifacts
- Comparación de runs y reproducibilidad vía tracking riguroso
- Model Registry: versionado de modelos, stages (Staging / Production), aliases
- Empaquetado de modelos en formato MLflow

**Materiales de lectura (Moodle):**

- Configurar el servidor de MLflow Tracking con Docker Compose, Postgres y MinIO/R2: guía paso a paso *(configuración concreta del stack; las versiones y parámetros de MLflow cambian entre releases)*

**Hands-on (clase sincrónica):** los alumnos integran MLflow en su paquete de training y registran sus experimentos contra el servidor levantado con Docker Compose.

### Clase 5 — Testing y validación de datos y modelos

Testing formal aplicado al pipeline completo.

**Videos teóricos:**

- Por qué testear en ML: qué puede fallar y qué no alcanza con métricas
- Tests de código en proyectos de ML: organización, fixtures, parametrización
- Validación de datos: schemas, expectativas y contratos entre etapas del pipeline
- Tests de regresión de modelo
- ***Behavioral testing*** de modelos: tests de perturbación, invarianza, expectativa direccional, calibración, confianza y rangos

**Materiales de lectura (Moodle):**

- Pytest en proyectos de ML: guía de configuración y ejemplos de fixtures *(sintaxis y convenciones específicas de pytest, que evoluciona entre versiones)*
- Validación de datos con Pandera: guía práctica de schemas y contratos *(herramienta específica del stack; Great Expectations es la alternativa más pesada — se justifica la elección de Pandera)*
- CI extendida: correr tests y validación de datos en cada PR con GitHub Actions *(implementación concreta; el concepto de CI se cubrió en Clase 2)*

**Hands-on (clase sincrónica):** los alumnos escriben tests de código, schemas de datos y al menos un test de comportamiento sobre su propio modelo.

### Clase 6 — Versionado de datos y modelos, reproducibilidad

DVC y reproducibilidad estricta.

**Videos teóricos:**

- Por qué versionar datos: el problema de reproducibilidad que no resuelve Git
- Versionado de datos y pipelines declarativos: conceptos y patrones
- Lineage de datos: trazabilidad de extremo a extremo
- Integración entre versionado de datos y Model Registry
- Reproducibilidad estricta: lock de dependencias, fijación de semillas, hash de datos
- Object storage como backend para datos: API S3 y la separación código/datos

**Materiales de lectura (Moodle):**

- DVC: instalación, `dvc init`, `dvc add`, `dvc.yaml` y `dvc repro` — guía paso a paso *(comandos y sintaxis específicos de DVC, que cambian entre versiones)*
- Configurar MinIO local y Cloudflare R2 como remote de DVC: guía práctica *(configuración concreta de infraestructura; justifica por qué R2 en lugar de S3 para el curso)*
- CI extendida: validar que `dvc repro` corre limpio en cada push *(implementación concreta de la capa de CI para datos)*

**Hands-on (clase sincrónica):** los alumnos versionan los datos de su modelo con DVC y declaran su pipeline en `dvc.yaml`. CI extendida: validación de que `dvc repro` corre limpio.

### Clase 7 — Orquestación con Dagster y predicción en lote

Cierre integrador: orquestación de todo el pipeline y predicción en lote como patrón de despliegue.

**Videos teóricos:**

- Orquestación en ML: por qué no alcanza con un script y un cron
- Orquestadores vs sincronizadores: cuándo usar cada uno
- Grafos de activos como representación de flujos de trabajo
- Panorama de herramientas de orquestación (Airflow, Dagster, Prefect, Kubeflow, Metaflow)
- Patrón de predicción en lote: casos de uso, dimensiones de escalado
- Propiedades del entorno de ejecución: seguridad, validez, recuperación, feedback loops

**Materiales de lectura (Moodle):**

- Dagster: conceptos de assets, jobs, ops, schedules, sensors e IO managers — guía de referencia *(API y terminología específica de Dagster, que evoluciona activamente entre versiones)*
- Levantar Dagster con Docker Compose integrado al stack del curso: guía paso a paso *(configuración concreta; el stack puede cambiar entre ediciones)*
- CI/CD completa: build de imagen final, push al registry y deploy del job en cada merge *(implementación concreta del cierre de la pipeline de CI)*

**Hands-on (clase sincrónica):** los alumnos integran su pipeline en un job de Dagster que ejecuta entrenamiento y batch scoring de forma orquestada. CI completa: build de imagen final, push al registry, deploy del job.

### Clase 8 — Monitoreo de modelos y detección de drift

Cierre del loop MLOps: una vez que el pipeline genera predicciones en lote, hay que saber cuándo el modelo dejó de ser confiable.

**Videos teóricos:**

- El loop de feedback en MLOps: por qué entrenar una vez no alcanza
- Tipos de drift: drift de datos (covariable), drift de concepto y degradación de performance
- Estrategias de detección: tests estadísticos, ventanas temporales, comparación de distribuciones
- Monitoreo de datos vs monitoreo de modelo: qué medir y cuándo reentrenar
- Integración del monitoreo en el pipeline de batch prediction: dónde y cómo insertar el chequeo
- Feedback loops y gobierno del ciclo de reentrenamiento

**Materiales de lectura (Moodle):**

- Evidently AI: generación de reportes de drift y dashboards de monitoreo — guía práctica *(herramienta específica del stack; el ecosistema de monitoreo ML evoluciona rápido)*
- Integrar Evidently en un job de Dagster: monitoreo automatizado post-predicción *(implementación concreta sobre el stack del curso)*

**Hands-on (clase sincrónica):** los alumnos agregan un step de monitoreo a su job de Dagster que genera un reporte de drift sobre las predicciones producidas en la Clase 7 y dispara una alerta si se supera un umbral configurable.

---

## 3. Trabajo práctico final

### Enunciado

Cada grupo (de 2 a 6 alumnos) debe entregar un repositorio que implemente un **pipeline reproducible de entrenamiento y predicción en lote** para un modelo de su propiedad (típicamente el modelo desarrollado en Aprendizaje de Maquina). El pipeline debe estar versionado, testeado, dockerizado, integrado a un sistema de tracking y registry de modelos, y orquestado para ejecutarse de forma autónoma sobre datos nuevos.

El artefacto final del TP es un **modelo versionado en el Model Registry** acompañado de **predicciones en lote reproducibles**, listo para ser consumido por un equipo de serving (la materia subsiguiente).

### Niveles de aprobación

**Nivel local (nota 6 a 8):** el grupo entrega un pipeline reproducible que corre enteramente en local **sin Docker**. Incluye: paquete Python refactorizado con estructura `src`, MLflow tracking con backend local (SQLite + filesystem), tests automatizados, validación de datos con Pandera, DVC versionando datos con remote local, y un job de Dagster ejecutando training y batch prediction. CI verde con lint y tests en cada push. Documentación clara.

**Nivel container completo (nota 8 a 10):** además de lo anterior, el grupo dockeriza el pipeline completo y levanta el stack productivo con Docker Compose (Dagster + MLflow + Postgres + MinIO o R2). Secrets gestionados correctamente, modelos promovidos a `Production` en el registry vía pull request, CI/CD que valida la integridad del pipeline en cada cambio, y un step de monitoreo integrado al job de Dagster que genera un reporte de drift automático y dispara una alerta configurable cuando se supera el umbral.

### Entregables

Cada grupo entrega:

1. **Link al repositorio público** de GitHub creado mediante GitHub Classroom.
2. **Link al último run exitoso** del workflow de GitHub Actions.
3. **README** con descripción del problema heredado de Aprendizaje de Maquina, decisiones de diseño tomadas al adaptar el template, e instrucciones de uso.
4. **Demo en vivo** durante la última clase: levantar el stack, mostrar un run de Dagster ejecutando el pipeline end-to-end y exhibir las predicciones generadas.

### Cronograma

Los grupos declaran al inicio del curso qué nivel apuntan. Las entregas intermedias se evalúan según el track declarado.

**Track nivel local:**

- **Entrega 1 (Clase 3):** repo creado a partir del template, paquete refactorizado con estructura `src`, entorno configurado con `uv`, CI corriendo (lint + tests). La entrega se realiza como pull request. **Otro grupo asignado hace el review del PR** y determina si aprueba o solicita cambios; el grupo no puede avanzar a la Entrega 2 sin PR aprobado.
- **Entrega 2 (Clase 5):** MLflow tracking con backend local integrado, tests de código y schemas de datos con Pandera implementados, CI extendida con ejecución de tests en cada PR. **El profesor revisa y da el ok** para continuar.
- **Entrega final (7 días después de Clase 8):** DVC versionando datos con remote local, job de Dagster ejecutando training y batch prediction localmente, CI verde y demo preparada. **El profesor asigna la nota final.**

**Track nivel container completo:**

- **Entrega 1 (Clase 3):** repo creado a partir del template, paquete refactorizado con estructura `src`, entorno configurado con `uv`, Dockerfile de training funcionando y CI corriendo (lint + build de imagen). La entrega se realiza como pull request. **Otro grupo asignado hace el review del PR** y determina si aprueba o solicita cambios; el grupo no puede avanzar a la Entrega 2 sin PR aprobado.
- **Entrega 2 (Clase 5):** MLflow tracking levantado con Docker Compose (Postgres + MinIO/R2), tests de código y schemas de datos con Pandera implementados, CI extendida con ejecución de tests en cada PR. **El profesor revisa y da el ok** para continuar.
- **Entrega final (7 días después de Clase 8):** stack completo containerizado (Dagster + MLflow + Postgres + MinIO o R2), DVC versionando datos, job de Dagster con training, batch prediction y step de monitoreo, secrets gestionados, modelos promovidos a `Production` vía PR, CI/CD verde end-to-end y demo preparada. **El profesor asigna la nota final.**

### Criterios de evaluación

La evaluación se centra en el **proceso, no en la performance del modelo**. La tabla siguiente es orientativa: indica qué componentes tienen más peso en la nota final, pero el profesor pondera el conjunto con criterio holístico.

| Componente | Track | Peso orientativo |
|---|---|---|
| Refactor: estructura del paquete y calidad del código | Ambos | Alto |
| Testing de código y validación de datos (Pandera) | Ambos | Alto |
| Orquestación: job de Dagster (training + batch prediction) | Ambos | Alto |
| Versionado de datos con DVC | Ambos | Medio |
| Tracking de experimentos con MLflow | Ambos | Medio |
| CI/CD: workflows de GitHub Actions | Ambos | Medio |
| Dockerización y stack productivo completo | Container completo | Alto |
| Monitoreo y detección de drift con Evidently | Container completo | Medio |
| Gestión de secrets y promoción de modelos vía PR | Container completo | Medio |
| Documentación (README e instrucciones de uso) | Ambos | Bajo |
| Participación en peer review (Entrega 1) | Ambos | Bajo |

> **Nota explícita en el enunciado:** "No se evalúa cuán bueno es el modelo en términos de métricas predictivas. Eso fue evaluado en Aprendizaje de Maquina. Se evalúa cómo se lo puso a producción de forma reproducible, testeable y operable."

---

## 4. Stack tecnológico y logística

### Stack del curso

| Capa | Herramienta | Notas |
|---|---|---|
| Lenguaje | Python 3.10+ | |
| Gestión de dependencias | `uv` o `poetry` | |
| Refactor / configs | Hydra, OmegaConf | |
| Linting / formato | `ruff`, `pre-commit` | |
| Containerización | Docker, Docker Compose | |
| Tracking + Registry | MLflow | |
| Storage de artifacts | MinIO (local) / Cloudflare R2 (cloud) | API S3-compatible |
| Versionado de datos | DVC | |
| Testing | pytest, Pandera | |
| Monitoreo | Evidently AI | |
| CI/CD | GitHub Actions | |
| Orquestación | Dagster | |
| Base de datos | PostgreSQL | metadata de Dagster y MLflow |

### Gestión de repositorios — GitHub Classroom

Se recomienda utilizar **GitHub Classroom** en modo *group assignment* sobre una **GitHub Organization** dedicada al curso (por ejemplo `fiuba-amii-2026`). El flujo es:

1. La cátedra mantiene un **template repository** con el scaffold inicial (estructura `src`, Dockerfile base, `docker-compose.yml`, workflow de Actions inicial, `dvc.yaml` esqueleto, tests de ejemplo).
2. El docente crea un *group assignment* en Classroom apuntando al template.
3. Cada grupo (12 a 15 grupos esperados, asumiendo grupos de 3-4 alumnos sobre ~45 inscriptos) acepta el assignment y obtiene su propio repositorio bajo la org.
4. Los repos se configuran como **públicos** (los alumnos vienen con datasets y modelos distintos, lo que hace muy difícil la copia y permite usar GitHub Actions sin restricción de minutos).

### GitHub Actions

Repos públicos en GitHub Actions tienen **minutos ilimitados** en runners estándar de Linux (2 vCPU, 7 GB RAM), suficiente para entrenar los modelos *shallow* del curso. Los workflows pueden incluso ejecutar el entrenamiento completo como smoke test, lo que es una lección de MLOps en sí misma raramente posible cuando los modelos son *deep*.

Como respaldo en caso de querer repos privados, se sugiere aplicar a **GitHub Education / Teacher Toolbox** que provee acceso gratuito a GitHub Team para la organización académica.

### Object storage — Cloudflare R2

Cloudflare R2 ofrece API compatible con S3, **10 GB de almacenamiento gratis** por cuenta, **1 millón de operaciones Clase A** y **10 millones de operaciones Clase B** mensuales, y **cero cargos por egress**, lo que lo vuelve ideal para enseñanza (los alumnos pueden bajar datasets repetidamente sin generar costos).

Cada grupo crea su propia cuenta Cloudflare. Para grupos que no puedan o no quieran proveer tarjeta de crédito al activar R2, **MinIO** levantado por docker-compose es una alternativa local equivalente (la misma API S3 funciona contra ambos cambiando solo el endpoint, lo cual es en sí una lección sobre estándares).

### Corrección y demostraciones

Para no requerir credenciales de R2 al corregir, los workflows de CI deben subir un `predictions_sample.csv` como **artifact del run**, lo que permite verificar el funcionamiento del batch prediction sin acceso al bucket del grupo.

La cátedra mantiene un README en un repo coordinador con un **índice de los 12-15 repos** de los grupos, que funciona como dashboard para seguimiento durante el cuatrimestre.

### Resumen de costos

Bajo la configuración propuesta (repos públicos en una org de GitHub + R2 dentro del free tier + MinIO como fallback local), **el costo total de infraestructura del curso es cero** tanto para la cátedra como para los alumnos.

---

## Próximos pasos

1. Validación de la propuesta con coordinación.
2. Preparación del repositorio template con el scaffold inicial.
3. Creación de la GitHub Organization de la cátedra y configuración del Classroom.
4. Aplicación a GitHub Education como respaldo.
5. Reescritura de `CriteriosAprobacion.md` y del `README.md` del repo principal acorde al nuevo programa.
6. Comunicación con la cátedra de la materia siguiente para acordar el contrato de interfaz (qué artefacto recibe del modelo entregado por esta materia).
7. Producción del material asincrónico por clase: grabación de los videos teóricos, redacción de las guías de lectura Moodle, elaboración de los evaluativos (10 preguntas por módulo), y configuración de los foros y el glosario colaborativo en la plataforma.
