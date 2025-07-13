# Hands-on - Usando MetaFlow para Sincronización de Tareas mediante servicio modo local

Dado que ejecutar Apache Airflow en local puede resultar algo pesado o complejo para algunas configuraciones, también se incluye una alternativa utilizando [MetaFlow](https://metaflow.org/) — una herramienta de código abierto desarrollada por Netflix para el desarrollo y orquestación de flujos de trabajo de ciencia de datos.

MetaFlow permite definir flujos de tareas mediante Python puro, sin necesidad de escribir código específico para una interfaz web o YAML. Su enfoque es centrado en el desarrollador, simple de usar y orientado a entornos tanto locales como en la nube.

## ¿Por qué usar MetaFlow?

- ✅ Sintaxis sencilla y declarativa con clases de Python
- ✅ Manejo automático de dependencias y versiones de datos
- ✅ Permite ejecutar en local, en AWS Batch o Kubernetes con mínimos cambios
- ✅ Excelente para flujos de trabajo lineales o con bifurcaciones controladas

## Instalación local de MetaFlow

Para usar MetaFlow localmente, podés instalarlo con:

```Bash
pip install metaflow
```

> Tambien lo podes instalar con conda, uv, poetry, pip, pipx, etc.

Asegurate de tener las dependencias necesarias en el entorno virtual, las podes instalar haciendo:

```Bash
pip install -r requirements.txt
```

No requiere servicios adicionales (como un scheduler o base de datos) para correr en local.

### ¿Cómo se usa en este hands-on?

Dentro de la carpeta local_metaflow vas a encontrar el mismo proceso ETL implementado en Apache Airflow en un `Flow` de MetaFlow. El DAG contiene los mismos pasos:

1. Obtener y limpiar los datos
1. Generar variables dummies
1. Separar en entrenamiento y test
1. Normalizar las variables numéricas
1. Verificar la forma de los datos

Podés verificar si el DAG está bien definido con:
```Bash
python etl_metaflow.py check
```

Podés ver como esta conformado el DAG con:
```Bash
python etl_metaflow.py show
```

Podés ejecutarlo con:
```Bash
python etl_metaflow.py run
```

Podés exportar para visualizar el DAG con graphviz con:
```Bash
python etl_metaflow.py output-dot
```

MetaFlow también guarda artefactos de los pasos (como datasets intermedios), lo cual te permite hacer debugging o volver a pasos anteriores sin repetir todo el flujo.