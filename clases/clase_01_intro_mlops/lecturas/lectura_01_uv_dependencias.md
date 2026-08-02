# Gestión de dependencias con uv

<!-- interno -->
> **Nota de cátedra (no se publica en Moodle).**
> Esta guía acompaña al video de pipelines y artifacts, donde se explican los conceptos de *lock file* y versionado semántico. Acá van la herramienta y los comandos concretos.
> Verificado contra **uv 0.12.1** (julio 2026). Si se actualiza uv entre ediciones, revisar sobre todo la sección "Crear el proyecto": `uv init` cambió su comportamiento por defecto en versiones recientes y hoy genera un proyecto empaquetado con layout `src/`.
> Para publicar: `uv run scripts/lectura_a_moodle.py clases/clase_01_intro_mlops/lecturas/lectura_01_uv_dependencias.md`
<!-- /interno -->

Esta guía es material de lectura del **Módulo 1**. Al terminarla vas a poder crear el proyecto del curso, instalarle dependencias y dejarlo en un estado que cualquier otra persona pueda reproducir exactamente.

Trabajá con la guía abierta y la terminal al lado: todos los comandos están pensados para que los ejecutes vos.

---

## Por qué cambiamos de herramienta

Lo más probable es que hasta ahora hayas instalado tus librerías con `pip install`, y que si tuviste que compartir un proyecto hayas escrito un `requirements.txt` a mano. Eso funciona para trabajar solo, pero deja dos agujeros:

- **No queda registro de las versiones exactas.** Si el archivo dice `scikit-learn`, cada persona recibe la que esté publicada el día que instala.
- **Las dependencias transitivas quedan sueltas.** `scikit-learn` instala `numpy`, `scipy` y `joblib` por debajo, y nadie las escribió en ninguna lista.

**uv** resuelve las dos cosas. Es un gestor de proyectos y dependencias de Python escrito en Rust, que reemplaza en una sola herramienta a `pip`, `venv`, `pip-tools`, `pipx` y `pyenv`. Además es notablemente rápido: instalaciones que con `pip` tardan minutos, acá tardan segundos.

Lo elegimos porque es la herramienta actual del ecosistema, pero **lo importante no es la herramienta: son los conceptos**. El entorno virtual, el archivo de declaración y el *lock file* existen en cualquier gestor moderno.

---

## Instalación

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

Acá viene el cambio de costumbre más grande: **no hace falta activar el entorno virtual.**

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

> **Si ves este mensaje:** `warning: VIRTUAL_ENV=... does not match the project environment path .venv and will be ignored`, significa que tenés activado el entorno virtual de *otro* proyecto. No rompe nada —uv usa el correcto igual— pero conviene desactivarlo con `deactivate`.

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

Como venís de trabajar en notebooks, hay dos formas de conectarlos con el proyecto.

**Opción A — el kernel del proyecto (recomendada).** Agregás el kernel como dependencia de desarrollo y después elegís el intérprete `.venv` desde tu editor o desde Jupyter:

```bash
uv add --dev ipykernel
uv run jupyter lab
```

**Opción B — sin instalar nada permanente.** Para una prueba rápida, `--with` agrega una librería solo para esa ejecución:

```bash
uv run --with jupyter jupyter lab
```

La opción A es la que corresponde para el proyecto del curso: así el notebook usa exactamente las mismas versiones que el resto del pipeline.

---

## Migrar un proyecto que ya tenías

Si ya tenías un `requirements.txt`:

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

**Usar `pip install` dentro del `.venv`.** Instala el paquete pero no lo registra en ningún lado, así que el entorno deja de coincidir con el lock y el próximo `uv sync` lo va a borrar. Si necesitás algo, `uv add`.

**Editar `pyproject.toml` a mano y no regenerar el lock.** Es válido editarlo, pero después hay que correr `uv lock` (o `uv sync`) para que el lock refleje el cambio.

**Borrar `.venv` porque "algo se rompió".** Se puede, no es grave: `uv sync` lo reconstruye entero desde el lock en segundos. Es justamente la ventaja de tener el entorno descrito en un archivo.

---

## Antes de la clase sincrónica

Llegá con esto resuelto, así aprovechamos el tiempo para avanzar sobre tu proyecto:

- [ ] uv instalado y `uv --version` responde
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
