# Guía de clase sincrónica — Módulo 1: Introducción a MLOps y ciclo de vida de un proyecto de ML

**Duración total:** ~90 minutos

> ## ⚠️ PENDIENTE — revisar cuando exista el repositorio template
>
> Esta guía está escrita contra un **scaffold propuesto**, no contra el template real: al momento de escribirla, el repositorio template de la cátedra y la GitHub Organization con Classroom **todavía no existen** (son los puntos 2 y 3 de "Próximos pasos" en `propuesta_amii_2026.md`).
>
> **Qué hay que revisar cuando el template esté armado:**
> - El árbol de archivos de la sección "Recorrida del repositorio" — hoy es una propuesta.
> - Los nombres concretos de los módulos dentro de `src/`.
> - El comando exacto del smoke test (acá se asume `uv run pytest`).
> - Si el template trae o no `uv.lock` ya generado. Cambia el paso 2: con lock, `uv sync`; sin lock, `uv add` de las dependencias iniciales.
> - La URL del assignment de Classroom y el nombre de la organización.
>
> El resto de la guía —tiempos, secuencia, puntos de atención— no depende del template y debería sobrevivir sin cambios.

---

## Antes de la clase (docente)

- [ ] Revisar el **foro de dudas**: es lo que define dónde poner el foco del hands-on.
- [ ] Verificar que el *assignment* de GitHub Classroom está publicado y que el template clona bien desde una cuenta limpia.
- [ ] Tener a mano la URL del assignment para pegarla en el chat.
- [ ] Probar el flujo completo una vez, en el sistema operativo menos familiar (habitualmente Windows).

---

## Kahoot de apertura (10–15 min)

Preguntas sobre los cinco videos y las dos lecturas del módulo.

Además de repasar, sirve como **diagnóstico**: si varias preguntas sobre `uv` salen mal, conviene asumir que buena parte del curso no hizo la lectura y dedicarle más tiempo al paso 2 del hands-on.

---

## Hands-on guiado (~70 min)

### Contexto

Esta es la clase de **puesta en marcha**. No se construye nada de MLOps todavía: el objetivo es que al final de los noventa minutos **cada grupo tenga su repositorio, su entorno funcionando y su primer commit hecho**.

Suena modesto, y es la clase con más riesgo de todo el curso: es donde chocan los tres sistemas operativos, las instalaciones previas de Anaconda, los permisos de GitHub y las diferencias de experiencia previa con la línea de comandos. Si esto queda resuelto hoy, el resto del curso avanza; si queda a medias, arrastra.

Los alumnos llegan con dos cosas de la materia anterior: **un notebook que entrena un modelo** y **el dataset con el que lo entrenaron**. Eso es la materia prima del curso entero.

### Paso a paso

#### 1. Grupos y GitHub Classroom (15 min)

Los grupos son de 3 o 4 personas y **se mantienen durante todo el curso**, porque el trabajo práctico final es la acumulación de lo que se construye clase a clase.

1. Formar los grupos y definir un nombre.
2. Cada grupo decide **qué modelo va a trabajar**: uno solo, de alguno de sus integrantes. Conviene elegir el que tenga los datos más accesibles y el problema más simple — el foco del curso es el proceso, no la sofisticación del modelo.
3. Aceptar el assignment de Classroom. El **primer** integrante crea el equipo; los demás se suman al equipo ya creado.
4. Verificar que el repositorio aparece bajo la organización de la cátedra y que todos tienen acceso de escritura.

> **El error más común de este paso:** que cada integrante cree su propio equipo en vez de sumarse al existente, y el grupo termine con cuatro repos. Conviene decirlo antes de que empiecen, y pedir que **una sola persona** cree el equipo mientras los demás esperan.

#### 2. Clonar y levantar el entorno (10 min)

```bash
git clone <url-del-repo-del-grupo>
cd <repo>
conda deactivate          # si aparece (base) en el prompt
uv sync
```

Verificación:

```bash
uv run python -c "import sys; print(sys.executable)"
```

Tiene que apuntar al `.venv` **dentro del repositorio**. Si apunta a algo con `anaconda3` o `miniconda3` en la ruta, el entorno está mal.

#### 3. Recorrida del repositorio (10 min)

Mostrar la estructura y decir en voz alta para qué sirve cada cosa. **La mayoría de estos archivos no se tocan hoy**, y conviene aclararlo: la idea es que sepan que están ahí y que reconozcan los nombres cuando aparezcan.

```
repo-del-grupo/
├── .github/workflows/ci.yml    # integración continua (vacío o mínimo por ahora)
├── data/                       # los datos NO se versionan acá todavía
├── notebooks/                  # el notebook de la materia anterior
├── src/<paquete>/              # acá va a vivir el código refactorizado
│   ├── __init__.py
│   ├── data.py
│   ├── features.py
│   ├── train.py
│   └── evaluate.py
├── tests/                      # tests automáticos
├── .gitignore
├── .python-version
├── Dockerfile                  # reproducibilidad del entorno
├── docker-compose.yml          # el stack local
├── dvc.yaml                    # versionado de datos
├── pyproject.toml              # dependencias declaradas
├── uv.lock                     # dependencias resueltas
└── README.md
```

Los dos puntos que sí importan hoy, y que conectan con los videos:

- **`pyproject.toml` y `uv.lock` son piezas distintas**: uno declara, el otro resuelve. Es exactamente la distinción del video de pipelines.
- **`src/` está vacío a propósito.** El contenido va a salir del notebook, y ese es el trabajo del módulo que viene.

#### 4. Traer el modelo al repositorio (15 min)

1. Copiar el notebook de la materia anterior a `notebooks/`.
2. Copiar el dataset a `data/`.
3. Agregar con `uv add` las dependencias que el notebook necesita para correr (`pandas`, `scikit-learn`, lo que use cada uno).
4. Verificar que el notebook corre en el entorno nuevo: **reiniciar el kernel y ejecutar todo de arriba abajo**.

> **Este paso es el que más tiempo consume y el más valioso**, porque es donde aparecen los problemas reales: rutas absolutas a la carpeta de Descargas, dependencias que estaban en el entorno de conda y nadie declaró, y celdas que solo funcionaban en el orden en que se habían ejecutado ese día. Es la lectura de buenas prácticas encontrándose con la realidad.

Si un grupo no logra hacer correr el notebook completo, **no se frena la clase**: se anota como tarea y se sigue. Lo importante es que el repositorio exista.

#### 5. Primer commit (10 min)

```bash
git status          # mirar qué va a entrar ANTES de agregar
git add .
git commit -m "Agregar notebook y datos del modelo del grupo"
git push
```

Antes de que hagan `push`, la verificación que importa:

```bash
git ls-files | grep -E "uv.lock|.venv"
```

- `uv.lock` **tiene** que aparecer.
- Nada con `.venv/` puede aparecer.

Si alguien commiteó el `.venv`, es el momento de arreglarlo —`git rm -r --cached .venv`— y de explicar por qué el `.gitignore` existe.

#### 6. Colchón (10 min)

Reservado a propósito. En esta clase **siempre** hay dos o tres personas trabadas con algo del sistema operativo, y este tiempo es para ellas. Si sobra, adelantar la mirada al notebook con los ojos de la lectura de buenas prácticas: buscar rutas absolutas y semillas sin fijar.

### Puntos de atención frecuentes

**Anaconda activada.** Si ven `(base)` en el prompt, `conda deactivate`. No rompe nada pero genera confusión sobre qué Python está corriendo, y es la causa de la mitad de los "a mí no me funciona" de esta clase.

**`uv` no está en el PATH.** Casi siempre es que no reiniciaron la terminal después de instalar. Cerrarla por completo y volver a abrir.

**Windows.** La activación del entorno y las rutas usan barras invertidas. Recordar que `uv run` evita todo el problema, porque no hay que activar nada.

**El notebook no corre en el entorno nuevo.** Casi siempre falta declarar una dependencia que en conda estaba instalada globalmente. Se resuelve con `uv add` a medida que aparecen los `ImportError`.

**El kernel del notebook apunta a Anaconda.** Se detecta con `import sys; print(sys.executable)`. Se resuelve levantando Jupyter desde el proyecto con `uv run jupyter lab`, o registrando el kernel.

**Datos demasiado grandes para GitHub.** Si el dataset supera los 100 MB, GitHub rechaza el push. Por hoy: trabajar con una muestra y dejar el dataset completo afuera. Es la motivación perfecta para el versionado de datos, que llega más adelante — vale la pena nombrarlo cuando pase.

**Un grupo sin modelo propio.** Si nadie del grupo trae un notebook utilizable, que elijan un dataset público simple y un modelo básico. No es lo ideal, pero es preferible a que el grupo no arranque.

---

## Cierre (5 min)

**Qué entregó esta clase al pipeline:**

- Un repositorio versionado, compartido por el grupo, con el modelo y los datos adentro.
- Un entorno reproducible: cualquier integrante clona, corre `uv sync` y obtiene exactamente las mismas versiones.
- El punto de partida real del curso — de acá en adelante, todo se construye sobre este repo.

**Preview:** el notebook está en el repositorio, pero sigue siendo un notebook. El próximo paso es convertirlo en código que se pueda testear, reutilizar y ejecutar sin abrir Jupyter.

**Tarea para quien quedó a mitad de camino:** dejar el entorno funcionando y el notebook corriendo de punta a punta antes de la próxima clase, y plantear en el foro lo que no haya salido.
