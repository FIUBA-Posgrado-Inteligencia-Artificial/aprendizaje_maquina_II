# Gestión de dependencias con uv

<!-- interno -->
> **Nota de cátedra (no se publica en Moodle).**
> Esta guía acompaña al video de pipelines y artifacts, donde se explican los conceptos de *lock file* y versionado semántico. Acá van la herramienta y los comandos concretos.
> Verificado contra **uv 0.12.1** (julio 2026). Si se actualiza uv entre ediciones, revisar sobre todo la sección "Crear el proyecto": `uv init` cambió su comportamiento por defecto en versiones recientes y hoy genera un proyecto empaquetado con layout `src/`.
> **Punto de partida asumido: Anaconda.** La guía está escrita para alumnos que vienen usando conda en las materias anteriores, no pip. Si en alguna edición eso cambia, hay que revisar la sección "Por qué cambiamos de herramienta", la tabla de equivalencias, la de notebooks y los errores frecuentes.
> Para publicar: `uv run scripts/lectura_a_moodle.py clases/clase_01_intro_mlops/lecturas/lectura_01_uv_dependencias.md`
<!-- /interno -->

Esta guía es material de lectura del **Módulo 1**. Al terminarla vas a poder crear el proyecto del curso, instalarle dependencias y dejarlo en un estado que cualquier otra persona pueda reproducir exactamente.

Trabajá con la guía abierta y la terminal al lado: todos los comandos están pensados para que los ejecutes vos.

---

## Por qué cambiamos de herramienta

Si venís de las materias anteriores, lo más probable es que hayas trabajado con **Anaconda**: creaste entornos con `conda create`, instalaste librerías con `conda install` y abriste los notebooks desde Anaconda Navigator o con `jupyter notebook`.

Anaconda hace bien varias cosas. Trae entornos aislados —que es exactamente la idea correcta— y resuelve un problema genuinamente difícil: instalar paquetes que no son solo Python, como bibliotecas de álgebra compiladas o soporte de GPU.

Pero para lo que necesitamos en esta materia tiene tres limitaciones.

**1. El entorno vive fuera del proyecto.** Los entornos de conda se guardan en un directorio central de la instalación de Anaconda, no al lado de tu código. Nada dentro de tu repositorio dice cuál de todos esos entornos le corresponde: esa información vive en la cabeza de quien lo creó.

**2. `environment.yml` no es un lock file.** Es el archivo que se suele compartir, y casi siempre se escribe a mano, con las librerías principales y sin versiones. Es una declaración de intenciones, no una descripción exacta del entorno. Se puede exportar el detalle completo con `conda env export`, pero esa exportación incluye identificadores de compilación propios de tu sistema operativo y en general no funciona en una máquina distinta.

**3. Mezclar `conda install` y `pip install` rompe el entorno.** Es la causa número uno de entornos de Anaconda que "dejaron de andar": conda no lleva registro de lo que instaló pip, así que puede pisarlo en la siguiente instalación.

**uv** resuelve las tres. Es un gestor de proyectos y dependencias de Python escrito en Rust, que reemplaza en una sola herramienta a `pip`, `venv`, `virtualenv`, `pip-tools`, `pipx` y `pyenv`. El entorno vive **dentro** del proyecto, genera un lock file de verdad, y no hay dos instaladores compitiendo. Además es notablemente rápido: instalaciones que tardaban minutos, acá tardan segundos.

**¿Anaconda deja de servir?** No. Sigue siendo la mejor opción cuando necesitás paquetes que no son de Python, y podés seguir usándola en otras materias sin ningún problema: **las dos herramientas conviven en la misma computadora.** Para el proyecto de esta materia vamos a usar uv.

Y lo importante: **no es la herramienta, son los conceptos.** El entorno aislado ya lo conocés de conda; lo que sumamos es la declaración versionada y el *lock file*, que existen en cualquier gestor moderno.

---

## De conda a uv: la traducción rápida

Antes de entrar en detalle, la tabla que probablemente más vas a usar. Casi todo lo que sabés hacer tiene un equivalente directo:

| En conda hacías | Acá hacés |
|---|---|
| `conda create -n mienv python=3.11` | `uv init mi-proyecto --python 3.11` |
| `conda activate mienv` | nada: se usa `uv run <comando>` |
| `conda install pandas` | `uv add pandas` |
| `pip install pytest` dentro del entorno | `uv add --dev pytest` |
| `conda remove pandas` | `uv remove pandas` |
| `conda list` | `uv tree` |
| `conda env export > environment.yml` | nada: `uv.lock` se escribe solo |
| `conda env create -f environment.yml` | `uv sync` |
| `conda env list` | no hace falta: hay un `.venv` por proyecto |

Las dos filas con "nada" son las que más cuesta incorporar, y son las dos mejores noticias: **no vas a tener que acordarte de activar el entorno, ni de exportar el archivo de dependencias.**

---

## Instalación

> **Si ya tenés Anaconda instalada** —que es lo más probable— uv convive con ella sin conflicto. Dos recomendaciones para evitarte confusiones:
> - Instalá uv con **el entorno de conda desactivado** (`conda deactivate` hasta que no veas `(base)` en el prompt). uv se instala a nivel del sistema, no adentro de un entorno.
> - Acostumbrate a correr `conda deactivate` antes de trabajar en el proyecto del curso. Un entorno de conda activo no rompe nada, pero hace difícil saber qué Python está corriendo.

### macOS y Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

En macOS, si usás Homebrew, también sirve:

```bash
brew install uv
```

### Windows

En PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Verificar la instalación

Cerrá y volvé a abrir la terminal, y después:

```bash
uv --version
```

Tenés que ver algo como `uv 0.12.1`. Si el comando no se encuentra, es que el instalador no llegó a agregar `uv` al PATH: cerrá la terminal por completo y volvé a probar.

Para actualizar uv más adelante:

```bash
uv self update
```

---

## Las cuatro piezas que vas a manejar

Antes de los comandos, cuatro nombres que van a aparecer todo el tiempo:

| Pieza | Qué es | ¿Se sube al repositorio? |
|---|---|---|
| `pyproject.toml` | Dónde **declarás** qué necesita tu proyecto, normalmente con rangos de versión | **Sí** |
| `uv.lock` | El resultado de **resolver** esa declaración: versión exacta de cada paquete, incluidas las transitivas, con sus hashes | **Sí** |
| `.venv/` | El entorno virtual: la carpeta donde uv instala realmente los paquetes | **No** |
| `.python-version` | Qué versión de Python usa el proyecto | **Sí** |

El `.venv/` es el equivalente de tu entorno de conda, con una diferencia que importa: **está adentro del proyecto**, no en un directorio central. Cada proyecto trae el suyo, y no hay que acordarse de cuál corresponde a cuál.

La regla a recordar: **se versiona lo que describe el entorno, nunca el entorno en sí.** El `.venv/` se puede regenerar en cualquier momento a partir del lock; por eso no se sube.

---

## Crear el proyecto del curso

```bash
uv init mi-proyecto-mlops
cd mi-proyecto-mlops
```

Vas a ver que se creó esto:

```
mi-proyecto-mlops/
├── .git/
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── src/
    └── mi_proyecto_mlops/
        └── __init__.py
```

Dos cosas para notar:

1. **uv ya inicializó un repositorio Git** y escribió un `.gitignore` que excluye `.venv/` y los archivos compilados de Python. No hace falta que lo hagas vos.
2. **El código va en `src/`.** uv crea por defecto un proyecto empaquetado con ese layout. Es exactamente la estructura que vamos a usar cuando convirtamos el notebook en un paquete, así que no la muevas.

Si querés fijar una versión de Python específica al crear el proyecto:

```bash
uv init mi-proyecto-mlops --python 3.12
```

---

## Agregar dependencias

Para agregar librerías al proyecto:

```bash
uv add pandas scikit-learn matplotlib
```

Ese comando hace cuatro cosas de una sola vez:

1. Agrega las librerías a `pyproject.toml`.
2. Resuelve el árbol completo de dependencias.
3. Escribe o actualiza `uv.lock`.
4. Crea el entorno virtual `.venv/` (si no existía) e instala todo adentro.

Para herramientas que necesitás para desarrollar pero que **no son parte de tu producto** —tests, linters, el kernel de Jupyter— usá el grupo `dev`:

```bash
uv add --dev pytest ruff ipykernel
```

Y para quitar algo:

```bash
uv remove matplotlib
```

Después de esos comandos, tu `pyproject.toml` se ve así:

```toml
[project]
name = "mi-proyecto-mlops"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "pandas>=3.0.5",
    "scikit-learn>=1.9.0",
]

[dependency-groups]
dev = [
    "pytest>=9.1.1",
    "ruff>=0.14.0",
    "ipykernel>=6.31.0",
]
```

---

## Cómo se leen las versiones

Fijate que `uv add pandas` no escribió `pandas`, escribió `pandas>=3.0.5`. Eso es un **rango**, y conviene entender qué significa.

Las versiones de Python siguen —en general— el **versionado semántico**: `MAJOR.MINOR.PATCH`.

| Cambio | Ejemplo | Qué significa |
|---|---|---|
| **PATCH** | `1.4.2` → `1.4.3` | Corrección de errores, sin cambios de interfaz |
| **MINOR** | `1.4.2` → `1.5.0` | Funcionalidad nueva, compatible con lo anterior |
| **MAJOR** | `1.4.2` → `2.0.0` | Cambios incompatibles: algo que funcionaba puede dejar de funcionar |

Los operadores que más vas a usar:

```toml
"pandas>=3.0.5"          # esa versión o cualquiera superior (lo que pone uv por defecto)
"pandas>=3.0,<4.0"       # acepta mejoras, frena antes del cambio incompatible
"pandas~=3.0.5"          # equivale a >=3.0.5,<3.1.0
"pandas==3.0.5"          # exactamente esa
```

Podés pedir un rango al agregar la librería:

```bash
uv add "scikit-learn>=1.7,<2.0"
```

> **Ojo con esto.** El versionado semántico es una **convención**, no una garantía: depende de que quien publica la librería la respete. Y aun respetándola, una corrección de errores legítima puede cambiar el tercer decimal de tus métricas. Por eso el rango declara tu intención, pero **lo que hace reproducible una corrida es el lock file**.

---

## El lock file

`uv.lock` es el archivo más importante de todos, y el que más se olvida.

Mientras `pyproject.toml` dice "quiero pandas 3.x o superior", `uv.lock` dice "pandas 3.0.5, numpy 2.4.6, scipy 1.17.1…", con el hash de cada paquete y para cada plataforma. Es lo único que garantiza que la instalación de hoy en tu máquina, la de mañana de tu compañero y la del mes que viene en el servidor sean **idénticas**.

**No lo edites a mano y no lo borres. Sí subilo al repositorio.**

Comandos relacionados:

```bash
uv lock                            # recalcula el lock desde pyproject.toml
uv lock --upgrade                  # actualiza todo a las versiones más nuevas permitidas
uv lock --upgrade-package pandas   # actualiza solo esa librería
```

Y del otro lado, cuando alguien clona tu repositorio:

```bash
uv sync
```

`uv sync` lee el lock y deja el entorno **exactamente** como dice ese archivo: instala lo que falta y quita lo que sobra. Es el comando que todo el mundo corre después de clonar.

Una variante útil, sobre todo para la integración continua:

```bash
uv sync --locked
```

Es igual, pero **falla si el lock no está actualizado** respecto de `pyproject.toml`, en vez de arreglarlo silenciosamente. Sirve para detectar que alguien editó las dependencias a mano y se olvidó de regenerar el lock.

---

## Ejecutar código

Acá viene el cambio de costumbre más grande viniendo de conda: **no hace falta activar nada.** No hay `uv activate`, y no es un olvido de la herramienta: no existe porque no hace falta.

```bash
uv run python entrenar.py
uv run pytest
uv run ruff check .
```

`uv run` se encarga de sincronizar el entorno con el lock y después ejecutar el comando adentro. Si alguien agregó una dependencia y vos hiciste `git pull`, `uv run` la instala sola antes de correr.

Si preferís activar el entorno a la manera tradicional, se puede:

```bash
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows
```

Pero la forma recomendada es `uv run`, porque garantiza que lo que corre es lo que dice el lock.

> **Si ves este mensaje:** `warning: VIRTUAL_ENV=... does not match the project environment path .venv and will be ignored`, significa que tenés activado el entorno de *otro* proyecto, o el de conda. No rompe nada —uv usa el correcto igual— pero conviene salir del otro con `deactivate` o `conda deactivate` según cuál sea.

---

## Versiones de Python

uv también administra los intérpretes de Python. No necesitás instalar Python por tu cuenta:

```bash
uv python list           # ver qué versiones hay disponibles e instaladas
uv python install 3.12   # instalar una
uv python pin 3.12       # fijarla para este proyecto (escribe .python-version)
```

Fijar la versión de Python del proyecto es parte de la reproducibilidad: el mismo código con dos versiones distintas de Python puede comportarse distinto.

---

## Trabajar con notebooks

Hasta ahora abrías los notebooks desde Anaconda Navigator, o con `jupyter notebook` desde el entorno de conda. Eso hay que ajustarlo, porque el notebook tiene que ejecutar con **el entorno del proyecto** y no con el de Anaconda: si no, vas a estar probando con versiones distintas de las que usa el resto de tu pipeline.

**Opción A — levantar Jupyter desde el proyecto (la más simple).**

```bash
uv add --dev jupyterlab ipykernel
uv run jupyter lab
```

Todo lo que abras desde ahí ya usa el entorno del proyecto. No hay nada más que configurar.

**Opción B — registrar el kernel, para verlo desde el Jupyter de siempre.** Si preferís seguir abriendo Jupyter como venías haciendo (desde Navigator, o desde el entorno de conda), registrá el entorno del proyecto como un kernel más:

```bash
uv add --dev ipykernel
uv run python -m ipykernel install --user \
    --name mi-proyecto-mlops \
    --display-name "Python (mi-proyecto-mlops)"
```

Después, en el menú de kernels del notebook vas a poder elegir **Python (mi-proyecto-mlops)**. Esto es lo que hace que un notebook abierto desde Anaconda ejecute con las librerías de tu proyecto.

**Para una prueba rápida**, sin instalar nada de forma permanente, `--with` agrega una librería solo para esa ejecución:

```bash
uv run --with jupyter jupyter lab
```

> **Cómo verificar que estás en el kernel correcto.** Ejecutá esto en una celda: si la ruta apunta al `.venv` de tu proyecto, estás bien; si apunta a algo con `anaconda3` o `miniconda3` en el medio, el notebook está usando el entorno viejo.
>
> ```python
> import sys; print(sys.executable)
> ```

---

## Migrar un proyecto que ya tenías

### Desde un entorno de conda

uv no lee `environment.yml`, así que el camino es averiguar **qué pediste vos** —no las cientos de dependencias que conda arrastró detrás— y volver a declararlo. Para eso sirve `--from-history`:

```bash
conda activate mi-entorno-viejo
conda env export --from-history
```

Ese comando lista solo los paquetes que instalaste explícitamente, que en general son un puñado. Con esa lista en la mano:

```bash
conda deactivate
uv init mi-proyecto-mlops
cd mi-proyecto-mlops
uv add pandas scikit-learn matplotlib   # lo que haya aparecido arriba
```

Dejá que uv resuelva el resto: no hace falta que copies las dependencias transitivas, justamente porque de eso se encarga el lock.

> Si el entorno viejo tenía paquetes instalados con `pip` además de con `conda`, revisá también `pip list` dentro de ese entorno: `--from-history` solo muestra lo que se instaló con conda.

### Desde un `requirements.txt`

```bash
uv init --bare               # crea solo el pyproject.toml, sin tocar tu código
uv add -r requirements.txt
```

Y al revés, si algún sistema te pide un `requirements.txt` (algunos servicios de despliegue todavía lo esperan):

```bash
uv export --format requirements-txt --no-hashes -o requirements.txt
```

Ese archivo pasa a ser un **producto derivado** del lock: se regenera, no se edita.

---

## Comandos de referencia rápida

| Comando | Para qué |
|---|---|
| `uv init <nombre>` | Crear un proyecto nuevo |
| `uv add <paquete>` | Agregar una dependencia |
| `uv add --dev <paquete>` | Agregar una dependencia de desarrollo |
| `uv remove <paquete>` | Quitar una dependencia |
| `uv sync` | Dejar el entorno igual al lock (después de clonar o de un `git pull`) |
| `uv sync --locked` | Igual, pero falla si el lock está desactualizado (para CI) |
| `uv lock --upgrade` | Actualizar las versiones dentro de los rangos declarados |
| `uv run <comando>` | Ejecutar algo dentro del entorno del proyecto |
| `uv tree` | Ver el árbol de dependencias |
| `uv python pin <versión>` | Fijar la versión de Python del proyecto |

---

## Errores frecuentes

**Subir `.venv/` al repositorio.** Son cientos de megas de archivos binarios que además solo sirven en tu sistema operativo. El `.gitignore` que genera `uv init` ya lo excluye; si venías de otro proyecto, verificá que esté.

**No subir `uv.lock`.** Es el error opuesto y es peor, porque anula todo el beneficio: sin el lock, cada persona resuelve las versiones por su cuenta. **El lock se commitea siempre.**

**Usar `pip install` o `conda install` dentro del proyecto.** Instalan el paquete pero no lo registran en ningún lado, así que el entorno deja de coincidir con el lock y el próximo `uv sync` lo va a borrar. Es la misma receta de desastre que mezclar conda y pip en un mismo entorno, y la regla es igual de simple: **dentro del proyecto del curso, todo se instala con `uv add`.**

**Trabajar con el entorno de conda activado.** Si ves `(base)` en el prompt, uv va a avisarte y va a usar igual el entorno correcto, así que no se rompe nada — pero vas a perder tiempo tratando de entender qué Python está corriendo. `conda deactivate` antes de empezar.

**Que el notebook siga apuntando al entorno de Anaconda.** Es el error más difícil de detectar, porque todo *parece* funcionar: el notebook corre, pero con otras versiones que tu pipeline. Verificá con `import sys; print(sys.executable)`.

**Editar `pyproject.toml` a mano y no regenerar el lock.** Es válido editarlo, pero después hay que correr `uv lock` (o `uv sync`) para que el lock refleje el cambio.

**Borrar `.venv` porque "algo se rompió".** Se puede, no es grave: `uv sync` lo reconstruye entero desde el lock en segundos. Es justamente la ventaja de tener el entorno descrito en un archivo.

---

## Antes de la clase sincrónica

Llegá con esto resuelto, así aprovechamos el tiempo para avanzar sobre tu proyecto:

- [ ] uv instalado y `uv --version` responde
- [ ] `conda deactivate` corrido: no ves `(base)` en el prompt
- [ ] Un proyecto creado con `uv init`
- [ ] Al menos una dependencia agregada con `uv add`
- [ ] `uv.lock` existe y está commiteado
- [ ] `.venv/` **no** está commiteado
- [ ] `uv run python -c "import pandas; print(pandas.__version__)"` funciona

Si algo de esto no te sale, dejalo planteado en el **foro de dudas** antes de la clase: así llegamos con los problemas identificados.

---

## Referencias

- Documentación oficial de uv: <https://docs.astral.sh/uv/>
- Guía de proyectos: <https://docs.astral.sh/uv/guides/projects/>
- Referencia de comandos: <https://docs.astral.sh/uv/reference/cli/>
- Especificación de versionado semántico: <https://semver.org/lang/es/>
- Especificadores de versión de Python (PEP 440): <https://peps.python.org/pep-0440/>
- Si venís de conda, la comparación oficial: <https://docs.astral.sh/uv/pip/compatibility/>
