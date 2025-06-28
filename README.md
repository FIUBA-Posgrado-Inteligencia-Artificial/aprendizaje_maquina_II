[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

# Operaciones de Aprendizaje Automático I
Este repositorio contiene el material de clases (presentaciones, ejercicios y notebooks) para Operaciones de Aprendizaje Automático I (CEIA - FIUBA). 

Para revisar los criterios de aprobación, ver el [documento correspondiente](CriteriosAprobacion.md).

### Objetivo de la materia
El objetivo de la materia es acercar a los alumnos los conceptos necesarios para desarrollar productos de software relacionados a Machine Learning y análisis de datos de una manera escalable y siguiendo buenas prácticas de programación. También se trabaja sobre las tareas operativas de Machine Learning (MLOps) con distintas herramientas para disponibilizar los resultados en ambientes productivos 🚀.

### Organización del Repositorio
``` 
    clase#
        teoria
        hands-on
        README.md
```

### Requerimientos
* Lenguaje de Programación
    * Python >=3.10
    * Poetry / Pip / Conda para instalar librerías
* Librerías
    * MLflow
    * Librerias de manejo de datos y de modelos de aprendizaje automático.
    * Jupiter Notebook
* Herramientas
    * GitHub para repositorios
    * Docker
    * Apache Airflow
* IDE Recomendados 
    * Visual Studio Code
    * PyCharm Community Edition    

#### UV
Este repositorio contiene un archivo `pyproject.toml` para instalar las dependencias usando 
[uv](https://docs.astral.sh/uv/)

## Contenido

### [Clase 1](clase1/README.md) 
* Introducción a la Materia
* Ciclo de vida de un proyecto de Aprendizaje Automático
* Machine Learning Operations (MLOps)
* Buenas prácticas de programación

### [Clase 2](clase2/README.md) 

* Desarrollo de modelos
* Las 4 fases del desarrollo de modelos
* Contenedores y Docker

### [Clase 3](clase3/README.md)
* Infraestructura
* Plataforma de ML
* MLFlow

### [Clase 4](clase4/README.md)
* Orquestadores y sincronizadores
* Gestión del flujo de trabajo de ciencia de datos
* Apache Airflow

### [Clase 5](clase5/README.md)
* Despliegue de modelos
* Sirviendo modelos
* Predicción en lotes

### [Clase 6](clase6/README.md)
* Desplegado on-line
* APIs y Microservicios
* Implementación de REST APIs en Python

### [Clase 7](clase7/README.md)
* Sirviendo modelos en el mundo real
* Estrategias de implementación
* Ejemplo de servicios de modelos


## Bibliografia

- Designing Machine Learning Systems. An Iterative Process for Production-Ready Applications - Chip Huyen (Ed. O’Reilly)
- Machine Learning Engineering with Python: Manage the production life cycle of machine learning models using MLOps with practical examplesv - Andrew P. McMahon (Ed. Packt Publishing)
- Engineering MLOps: Rapidly build, test, and manage production-ready machine learning life cycles at scale - Emmanuel Raj (Ed. Packt Publishing)
- Introducing MLOps: How to Scale Machine Learning in the Enterprise -  Mark Treveil, Nicolas Omont, Clément Stenac, Kenji Lefevre, Du Phan, Joachim Zentici, Adrien Lavoillotte, Makoto Miyazaki, Lynn Heidmann (Ed. O’Reilly)
- Practical MLOps: Operationalizing Machine Learning Models -  Noah Gift, Alfredo Deza (Ed. O’Reilly)
- Machine Learning Engineering - Andriy Burkov (Ed. True Positive Inc.)
- Machine Learning Engineering in Action - Ben Wilson (Manning)

---
Esta obra está bajo una
[Licencia Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
