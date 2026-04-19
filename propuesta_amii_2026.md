# Propuesta de reestructuración — Aprendizaje de Máquina II

**Cátedra:** Aprendizaje de Máquina II — FIUBA, Especialización en Inteligencia Artificial
**Versión:** Borrador para coordinación
**Autor:** Facundo Lucianna

---

## Resumen ejecutivo

Esta propuesta reestructura la materia **Aprendizaje de Máquina II** para enfocarla en el ciclo completo de **entrenamiento reproducible y operacionalización** de modelos de Machine Learning bajo principios de MLOps, retirando los contenidos de **serving online** que pasan a ser cubiertos por una materia subsiguiente.

La idea central es que cada alumno **llegue con un notebook crudo** producido en la materia anterior (donde aprendieron modelos *shallow*) y **se vaya con un proceso reproducible** que entrena, versiona, testea y predice en lote ese mismo modelo, listo para ser consumido por el equipo que se encargue del serving.

Se mantiene Docker como tecnología transversal del curso, reposicionado desde "envoltura del modelo en producción" hacia "garantía de reproducibilidad del entrenamiento". Se preserva el formato de 7 clases y se incorporan tres ejes nuevos que el programa actual no cubre con profundidad: **refactor de notebook a paquete**, **testing y validación de datos/modelos**, y **versionado y CI/CD**.

El dictado adopta un modelo **flipped classroom**: cada clase combina videos teóricos pregrabados (para consumo asincrónico) con una clase sincrónica online de ~1.5 horas dedicada a hands-on guiado y evacuación de dudas. Esto permite usar el tiempo sincrónico de forma intensiva en la práctica sobre el proyecto de cada grupo.

---

## 1. Justificación del cambio

### Contexto actual

El programa vigente dedica las clases 5, 6 y 7 a contenidos de deployment y serving online (batch prediction, APIs y microservicios con FastAPI, estrategias de serving en producción). Una materia posterior del programa absorberá los contenidos de **serving online**, lo que abre tres clases para profundizar en otros aspectos críticos del ciclo de MLOps que actualmente quedan tratados de manera superficial.

### Razones del rediseño

Los relevamientos de la industria y la práctica docente muestran que el principal cuello de botella para llevar modelos a producción no está en el serving sino **antes**: en la falta de procesos reproducibles para entrenar, validar y versionar modelos. El refactor de notebooks experimentales a paquetes mantenibles, el testing de datos y modelos, y la integración continua de proyectos de ML son competencias menos enseñadas y de altísimo valor profesional.

Liberar el espacio de serving online permite tratar estos temas con la profundidad que merecen, sin sacrificar Docker (que se mantiene central) ni la orquestación con Airflow (que pasa a ser el cierre integrador del curso a través de la predicción en lote).

### Conexión con las materias adyacentes

La reestructuración define un **flujo claro de tres etapas** dentro del posgrado:

- **Materia anterior (Aprendizaje de Máquina I):** los alumnos producen un notebook que entrena un modelo *shallow* sobre un dataset propio.
- **Aprendizaje de Máquina II (esta materia):** los alumnos transforman ese notebook en un proceso productivo reproducible, versionado, testeado y orquestado, capaz de generar predicciones en lote de forma automatizada.
- **Materia siguiente (Serving):** los alumnos toman el modelo versionado producido en esta materia y aprenden a servirlo online.

Cada materia recibe un artefacto bien definido de la anterior y entrega uno bien definido a la siguiente. La frase que sintetiza el aporte de Aprendizaje de Máquina II queda:

> *"Los alumnos llegan con un notebook que entrena un modelo y se van con un proceso reproducible que entrena, versiona, testea y predice en lote ese modelo en producción."*

### Conservación de Docker

Docker se mantiene como tecnología fundamental del curso, pero se reposiciona conceptualmente. En el programa actual aparece principalmente como envoltura del modelo de inferencia. En la propuesta nueva se utiliza desde la clase 3 como **garantía de reproducibilidad del entorno de entrenamiento**, y como infraestructura para levantar localmente el stack completo de MLOps (MLflow, Postgres, MinIO, Jupyter) vía Docker Compose. Es la herramienta que asegura que el pipeline corre igual en la máquina del alumno, en CI y en producción.

### Formato de dictado — flipped classroom

Cada clase se divide en dos componentes complementarios:

- **Videos teóricos pregrabados (asincrónico):** segmentos cortos de 8 a 15 minutos cada uno que cubren los conceptos de la clase. El alumno los consume a su propio ritmo antes de la clase sincrónica. Se complementan con material textual (guías paso a paso, ejemplos de código) que el alumno puede revisar en paralelo.
- **Clase sincrónica online (~1.5 horas):** dedicada íntegramente a hands-on guiado sobre el proyecto de cada grupo, resolución de dudas sobre los videos y trabajo práctico acompañado. El docente está disponible para desbloquear problemas en tiempo real.

Este formato permite usar el tiempo sincrónico de forma intensiva: los alumnos llegan con la teoría ya vista y aprovechan la clase para aplicar los conceptos sobre su propio modelo, con el docente acompañando.

---

## 2. Programa nuevo — 7 clases

El hilo conductor del curso es **"de notebook a pipeline reproducible de entrenamiento y predicción en lote"**. Cada clase agrega una capa al pipeline que el alumno construye sobre su propio modelo de la materia anterior. La integración continua (CI/CD con GitHub Actions) atraviesa todas las clases en lugar de ser una clase aparte: cada nuevo concepto incorporado se traduce en un step adicional del workflow.

### Clase 1 — Introducción a MLOps y ciclo de vida de un proyecto de ML

Introducción al rol de MLOps en el ciclo de vida de un sistema de ML y setup del entorno de trabajo del curso.

**Videos teóricos:**

- Ciclo de vida de un proyecto de ML y roles (Data Engineer, Data Scientist, Data Analyst, ML Engineer)
- Pipelines de ML: componentes y artifacts
- MLOps: definición, niveles 0/1/2 de madurez y ventajas de cada nivel
- Entorno de desarrollo vs entorno productivo: propiedades y diferencias
- Contrato de interfaz entre AMq1 → AMq2 → Serving (el flujo del posgrado)
- Gestión moderna de dependencias: `uv` / `poetry`, lock files, semver
- Buenas prácticas de programación aplicadas a ML (introducción)

**Hands-on (clase sincrónica):** los alumnos crean su repo a partir del template de la cátedra vía GitHub Classroom y configuran su entorno local.

### Clase 2 — De notebook a paquete Python

Refactorización sistemática de un notebook experimental hacia un paquete Python testeable y mantenible.

**Videos teóricos:**

- Estructura de proyecto Python (*src layout*, separación I/O / features / training / evaluación)
- Selección del tipo de modelo: 8 consejos (breve, como contexto del refactor)
- Las 4 fases del desarrollo de modelos
- Depuración de modelos: causas típicas de fallas y estrategias
- Manejo de configuración con Hydra u OmegaConf
- Logging estructurado, type hints y docstrings
- Pre-commit hooks, linting con `ruff`, formateo automático
- Introducción a CI/CD: primer workflow de GitHub Actions (lint + tests en cada push)

**Hands-on (clase sincrónica):** los alumnos toman su notebook real de la materia anterior y lo refactorizan a un paquete con la estructura del template.

### Clase 3 — Docker para reproducibilidad de entrenamiento

Conceptos fundamentales de contenedores reposicionados como garantía de reproducibilidad del entorno de entrenamiento.

**Videos teóricos:**

- Contenedores vs máquinas virtuales: conceptos fundamentales
- Docker: Dockerfile, imágenes, contenedores, Docker Hub
- Dockerfile multi-stage para imágenes de training
- Diferencia entre imagen de desarrollo, training y producción
- Docker Compose y stack local de MLOps (MLflow + Postgres + MinIO + Jupyter)
- El contenedor como contrato entre la máquina del alumno, CI y producción
- Capa de almacenamiento (breve): formatos de datos (CSV vs Parquet, row vs column), ETL/ELT
- Capa de cómputo (breve): escalamiento vertical y horizontal, clusters

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

Formato conceptual, sin hands-on. Apunta a conectar estos conceptos con el resto del curso: tracking de runs caros con MLflow (clase 4), orquestación asíncrona con Airflow (clase 7), reproducibilidad estricta con DVC (clase 6).

### Clase 4 — Tracking de experimentos y Model Registry con MLflow

Tracking de experimentos y versionado de modelos como pilares de reproducibilidad.

**Videos teóricos:**

- MLflow: panorama de componentes (Tracking, Models, Registry, Projects)
- Tracking en profundidad: parámetros, métricas, artifacts
- Comparación de runs y reproducibilidad vía tracking riguroso
- Model Registry: versionado de modelos, stages (Staging / Production), aliases
- Empaquetado de modelos en formato MLflow
- Servidor de tracking en docker-compose conectado a Postgres y MinIO / R2

**Hands-on (clase sincrónica):** los alumnos integran MLflow en su paquete de training y registran sus experimentos.

### Clase 5 — Testing y validación de datos y modelos

Testing formal aplicado al pipeline completo.

**Videos teóricos:**

- Pytest aplicado a código de ML: organización de tests, fixtures, parametrización
- Validación de datos con Great Expectations o Pandera: schemas, expectativas, contratos entre etapas
- Tests de regresión de modelo
- ***Behavioral testing*** de modelos: tests de perturbación, invarianza, expectativa direccional, calibración, confianza y rangos
- CI extendida: ejecución de tests y validación de datos en cada PR

**Hands-on (clase sincrónica):** los alumnos escriben tests de código, schemas de datos y al menos un test de comportamiento sobre su propio modelo.

### Clase 6 — Versionado de datos y modelos, reproducibilidad

DVC y reproducibilidad estricta.

**Videos teóricos:**

- DVC: versionado de datos y pipelines declarativos
- `dvc.yaml`, `dvc repro`, lineage de datos
- Integración de DVC con MLflow Model Registry
- Reproducibilidad estricta: lock de dependencias, fijación de semillas, hash de datos
- Object storage para datos: MinIO local y Cloudflare R2 como opción cloud (API S3 común)

**Hands-on (clase sincrónica):** los alumnos versionan los datos de su modelo con DVC y declaran su pipeline en `dvc.yaml`. CI extendida: validación de que `dvc repro` corre limpio.

### Clase 7 — Orquestación con Airflow y predicción en lote

Cierre integrador: orquestación de todo el pipeline y predicción en lote como patrón de despliegue.

**Videos teóricos:**

- Administración de recursos: orquestadores vs sincronizadores
- DAGs como representación de flujos de trabajo
- Panorama de herramientas de workflow (Airflow, Argo, Prefect, Kubeflow, Metaflow)
- Apache Airflow en profundidad: arquitectura, DAGs, operators, schedules, sensors, XComs
- Patrón de predicción en lote: casos de uso, dimensiones de escalado
- Propiedades del entorno de ejecución: seguridad, validez, recuperación, feedback loops

**Hands-on (clase sincrónica):** los alumnos integran su pipeline en un DAG de Airflow que ejecuta entrenamiento y batch scoring de forma orquestada. CI completa: build de imagen final, push al registry, deploy del DAG.

---

## 3. Trabajo práctico final

### Enunciado

Cada grupo (de 2 a 6 alumnos) debe entregar un repositorio que implemente un **pipeline reproducible de entrenamiento y predicción en lote** para un modelo de su propiedad (típicamente el modelo desarrollado en Aprendizaje de Máquina I). El pipeline debe estar versionado, testeado, dockerizado, integrado a un sistema de tracking y registry de modelos, y orquestado para ejecutarse de forma autónoma sobre datos nuevos.

El artefacto final del TP es un **modelo versionado en el Model Registry** acompañado de **predicciones en lote reproducibles**, listo para ser consumido por un equipo de serving (la materia subsiguiente).

### Niveles de aprobación

**Nivel local (nota 6 a 8):** el grupo entrega un pipeline reproducible que corre en local con docker-compose, con MLflow tracking, tests automatizados, validación de datos, versionado con DVC y un DAG de Airflow ejecutando training y batch prediction. Documentación clara y workflow de CI verde.

**Nivel container completo (nota 8 a 10):** además de lo anterior, el grupo demuestra que el sistema corre con servicios containerizados de forma equivalente a un entorno productivo (Airflow + MLflow + Postgres + MinIO o R2), con secrets gestionados correctamente, modelos promovidos a `Production` en el registry vía pull request y CI/CD que valida la integridad del pipeline en cada cambio.

### Entregables

Cada grupo entrega:

1. **Link al repositorio público** de GitHub creado mediante GitHub Classroom.
2. **Link al último run exitoso** del workflow de GitHub Actions.
3. **README** con descripción del problema heredado de Aprendizaje de Máquina I, decisiones de diseño tomadas al adaptar el template, e instrucciones de uso.
4. **Demo en vivo** durante la última clase: levantar el stack, mostrar un run de Airflow ejecutando el pipeline end-to-end y exhibir las predicciones generadas.

### Cronograma

- **Pre-entrega (Clase 5):** repo iniciado con paquete refactorizado, primeros tests y workflow de CI corriendo.
- **Entrega final:** 7 días después de la última clase.

### Criterios de evaluación

La evaluación se centra en el **proceso, no en la performance del modelo**. Se evalúa: estructura y calidad del código (refactor), cobertura y pertinencia de tests, robustez de la validación de datos, correctitud del versionado de datos y modelos, integridad del pipeline reproducible, calidad del DAG de Airflow, calidad de la CI/CD, y claridad de la documentación.

> **Nota explícita en el enunciado:** "No se evalúa cuán bueno es el modelo en términos de métricas predictivas. Eso fue evaluado en Aprendizaje de Máquina I. Se evalúa cómo se lo puso a producción de forma reproducible, testeable y operable."

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
| Testing | pytest, Great Expectations o Pandera | |
| CI/CD | GitHub Actions | |
| Orquestación | Apache Airflow | |
| Base de datos | PostgreSQL | metadata de Airflow y MLflow |

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
7. Grabación de los videos teóricos y preparación del material textual que acompaña cada hands-on.
