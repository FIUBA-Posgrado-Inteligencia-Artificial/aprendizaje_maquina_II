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
> **Requisitos que el template tiene que cumplir para que esta guía funcione:**
> - `.gitignore` que excluya `data/raw/` pero **no** `data/sample/`, y que excluya `.venv/`.
> - `data/raw/` y `data/sample/` existentes con `.gitkeep`, y un `data/README.md` con las secciones a completar (origen, cómo obtener los datos, restricciones de uso).
>
> El resto de la guía —tiempos, secuencia, puntos de atención— no depende del template y debería sobrevivir sin cambios.

---

## Antes de la clase (docente)

- [ ] Revisar el **foro de dudas**: es lo que define dónde poner el foco del hands-on.
- [ ] Tener a mano el enlace de registro de Cloudflare R2 (<https://dash.cloudflare.com/sign-up>), para la tarea del cierre.
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
├── data/
│   ├── README.md               # de dónde salen los datos y cómo obtenerlos
│   ├── raw/                    # dataset completo — IGNORADO por git
│   └── sample/                 # muestra chica — SÍ se versiona
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

Los tres puntos que sí importan hoy, y que conectan con los videos:

- **`pyproject.toml` y `uv.lock` son piezas distintas**: uno declara, el otro resuelve. Es exactamente la distinción del video de pipelines.
- **`src/` está vacío a propósito.** El contenido va a salir del notebook, y ese es el trabajo del módulo que viene.
- **`data/raw/` está ignorado por git y `data/sample/` no.** Vale la pena detenerse acá treinta segundos, porque es contraintuitivo y va a generar preguntas. Ver el paso siguiente.

#### 4. Traer el modelo al repositorio (15 min)

1. Copiar el notebook de la materia anterior a `notebooks/`.
2. Copiar el dataset completo a `data/raw/`. **Eso no se sube**: está ignorado por git.
3. Generar una **muestra** de unas pocas centenas de filas en `data/sample/`. Esa sí se versiona.
4. Completar `data/README.md`: de dónde salieron los datos, cómo se obtienen de nuevo, y cualquier restricción de uso que tengan.
5. Agregar con `uv add` las dependencias que el notebook necesita para correr (`pandas`, `scikit-learn`, lo que use cada uno).
6. Verificar que el notebook corre en el entorno nuevo: **reiniciar el kernel y ejecutar todo de arriba abajo**.

**Por qué el dataset no va al repositorio.** Es la pregunta que van a hacer, y conviene contestarla bien porque instala un tema del curso:

- **Git no está hecho para datos.** Guarda cada versión completa de cada archivo binario. Un CSV que cambia tres veces son tres copias enteras en el repositorio.
- **Y no hay vuelta atrás.** Todo lo que se commitea queda en el historial **para siempre**: borrar el archivo después no achica el repositorio, porque la copia sigue estando en la historia. Es una de las pocas decisiones de esta clase que no se deshace fácil.
- **Los datos pueden tener restricciones** de privacidad o de licencia que un repositorio público no respeta.
- Versionar datos en serio necesita otra herramienta: **DVC**, a la que le dedicamos un módulo entero más adelante. Por ahora convivimos con la incomodidad a propósito: cuando llegue esa clase, van a entender exactamente qué problema resuelve.

**Por qué sí va la muestra.** Con una muestra chica versionada, cualquiera puede clonar el repositorio y correr algo de punta a punta sin conseguir los datos completos. Es lo que va a permitir que los tests con pytest y los workflows de GitHub Actions se ejecuten sin acceso a los datos reales.

> **Este paso es el que más tiempo consume y el más valioso**, porque es donde aparecen los problemas reales: rutas absolutas a la carpeta de Descargas, dependencias que estaban en el entorno de conda y nadie declaró, y celdas que solo funcionaban en el orden en que se habían ejecutado ese día. Es la lectura de buenas prácticas encontrándose con la realidad.

Si un grupo no logra hacer correr el notebook completo, **no se frena la clase**: se anota como tarea y se sigue. Lo importante es que el repositorio exista.

#### 5. Primer commit (10 min)

```bash
git status          # mirar qué va a entrar ANTES de agregar
git add .
git commit -m "Agregar notebook y muestra de datos del modelo del grupo"
git push
```

**Insistir en el `git status` antes del `git add .`.** Es el hábito que evita el problema, y es el momento de instalarlo: mirar qué se va a subir antes de subirlo.

Antes de que hagan `push`, la verificación que importa:

```bash
git ls-files | grep -E "uv\.lock|\.venv|data/"
```

- `uv.lock` **tiene** que aparecer.
- Nada con `.venv/` puede aparecer.
- De `data/`, solo `README.md` y lo que esté en `sample/`. Si aparece algo de `data/raw/`, el `.gitignore` no está funcionando.

Si alguien ya commiteó el `.venv` o el dataset completo, **es mucho mejor arreglarlo ahora que después**: mientras no se haya hecho `push`, alcanza con `git rm -r --cached <ruta>` y rehacer el commit. Es el momento perfecto para explicar por qué el `.gitignore` existe y por qué el historial de git no perdona.

#### 6. Colchón (10 min)

Reservado a propósito. En esta clase **siempre** hay dos o tres personas trabadas con algo del sistema operativo, y este tiempo es para ellas. Si sobra, adelantar la mirada al notebook con los ojos de la lectura de buenas prácticas: buscar rutas absolutas y semillas sin fijar.

### Puntos de atención frecuentes

**Anaconda activada.** Si ven `(base)` en el prompt, `conda deactivate`. No rompe nada pero genera confusión sobre qué Python está corriendo, y es la causa de la mitad de los "a mí no me funciona" de esta clase.

**`uv` no está en el PATH.** Casi siempre es que no reiniciaron la terminal después de instalar. Cerrarla por completo y volver a abrir.

**Windows.** La activación del entorno y las rutas usan barras invertidas. Recordar que `uv run` evita todo el problema, porque no hay que activar nada.

**El notebook no corre en el entorno nuevo.** Casi siempre falta declarar una dependencia que en conda estaba instalada globalmente. Se resuelve con `uv add` a medida que aparecen los `ImportError`.

**El kernel del notebook apunta a Anaconda.** Se detecta con `import sys; print(sys.executable)`. Se resuelve levantando Jupyter desde el proyecto con `uv run jupyter lab`, o registrando el kernel.

**"¿Por qué no puedo subir el dataset?"** Es la pregunta garantizada de la clase. La respuesta corta: git guarda cada versión completa y no olvida nunca. La respuesta útil: para eso existe DVC, y le dedicamos un módulo entero. Conviene que la pregunta aparezca — es el mejor gancho para ese tema.

**Alguien commiteó el dataset completo igual.** Si todavía no hizo `push`, `git rm -r --cached data/raw` y rehacer el commit. Si ya lo pusheó y el archivo es grande, lo más práctico es rehacer el repositorio desde el template: reescribir historia con un grupo entero mirando no es buen uso del tiempo de clase.

**GitHub rechaza el push por tamaño.** El límite por archivo son 100 MB. Si aparece, es que el dataset se coló: revisar el `.gitignore` y el paso anterior.

**Un grupo sin modelo propio.** Si nadie del grupo trae un notebook utilizable, que elijan un dataset público simple y un modelo básico. No es lo ideal, pero es preferible a que el grupo no arranque.

---

## Cierre (5 min)

**Qué entregó esta clase al pipeline:**

- Un repositorio versionado, compartido por el grupo, con el notebook y una muestra de los datos.
- Un entorno reproducible: cualquier integrante clona, corre `uv sync` y obtiene exactamente las mismas versiones.
- El punto de partida real del curso — de acá en adelante, todo se construye sobre este repo.

**Un pendiente declarado:** el dataset completo **no** está versionado, así que hoy el repositorio no alcanza para reproducir el modelo de punta a punta. Es una deuda consciente, y conviene decirlo en voz alta: la vamos a saldar cuando lleguemos a DVC: los datos van a vivir en un bucket de object storage y en el repositorio va a quedar solo un archivo de referencia, chiquito y versionable.

**Tarea de esta semana — crear la cuenta de almacenamiento (10 minutos, en casa):**

Cada grupo tiene que crear **una** cuenta de **Cloudflare R2**. No se usa hoy ni la semana que viene: se pide ahora porque es un trámite que a veces se traba, y así hay margen para resolverlo.

Registro: <https://dash.cloudflare.com/sign-up>, y después activar R2 desde el panel.

- R2 da **10 GB gratis** y **no cobra egress**, o sea que pueden bajar el dataset todas las veces que quieran sin generar costo. Por eso lo elegimos en lugar de S3, que sí cobra por transferencia de salida.
- **Cloudflare pide una tarjeta de crédito para activar R2**, aunque no cobre nada dentro de la capa gratuita. Si en el grupo nadie puede o quiere darla, avisen en el foro: la alternativa es **MinIO** levantado con Docker Compose en la propia máquina. Funciona igual, porque los dos exponen la misma API S3 y solo cambia el endpoint — que es, en sí, una buena lección sobre para qué sirven los estándares.
- **Guarden las credenciales donde el grupo pueda encontrarlas** — y no en el repositorio.

> **Importante, y decirlo explícitamente:** por ahora **no suban nada al bucket**. La estructura la administra DVC cuando lleguemos a ese módulo, y contenido cargado a mano antes solo genera trabajo de limpieza.

Los pasos concretos —crear el bucket, generar las credenciales, configurarlo como remote de DVC— vienen en la lectura del módulo de versionado de datos. Hoy alcanza con tener la cuenta creada y las credenciales guardadas.

**Preview:** el notebook está en el repositorio, pero sigue siendo un notebook. El próximo paso es convertirlo en código que se pueda testear, reutilizar y ejecutar sin abrir Jupyter.

**Tarea para quien quedó a mitad de camino:** dejar el entorno funcionando y el notebook corriendo de punta a punta antes de la próxima clase, y plantear en el foro lo que no haya salido.
