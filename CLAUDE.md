# CLAUDE.md

Material de la materia **Operaciones de Aprendizaje Automático I** (CEIA — FIUBA).

## Contexto del repositorio

El repositorio está en transición entre dos ediciones:

- **`clases/`** — programa nuevo de 8 módulos, en desarrollo. Es donde se trabaja.
- **`clase1/` … `clase7/`, `old/`** — edición anterior. Material de consulta, no se edita salvo pedido explícito.
- **`propuesta_amii_2026.md`** — fuente de verdad del programa nuevo: qué videos, lecturas, hands-on y evaluativos lleva cada módulo, y el stack técnico. **Consultarlo antes de escribir material nuevo**, para saber qué le toca cubrir a cada pieza y qué está asignado a otra.
- **`README.md`** — todavía describe el programa anterior.

El hilo conductor del curso es *"de notebook a pipeline reproducible de entrenamiento y predicción en lote"*, y el formato es **flipped classroom**: videos pregrabados + lecturas en Moodle + clase sincrónica de hands-on.

### Estructura de un módulo

```
clases/clase_NN_tema/
├── README.md                 # objetivos y checklist de producción
├── videos/vNN_tema/
│   ├── guion.md              # guion del video
│   ├── guion_teleprompter.md # versión para leer en cámara (QPrompt)
│   └── slides/slides.md      # una diapositiva por bloque separado con ---
├── lecturas/                 # guías de tooling, se publican en Moodle
├── clase_sincrónica/guia.md  # hands-on guiado
├── evaluativo/preguntas.yaml # 10 preguntas, >8/10 para aprobar
└── kahoot/preguntas.yaml     # apertura de la clase sincrónica
```

Muchos archivos son todavía plantillas vacías. Al completar uno, seguir la estructura del equivalente ya escrito en otro módulo en vez de inventar un formato nuevo.

---

## Nomenclatura: módulo, no clase

La unidad del curso se llama **módulo**. En todo texto que lea el alumno se escribe "Módulo 1", "Módulo 2", nunca "Clase 1". Es el término que usa Moodle, y el que ya aparece en los `preguntas.yaml` (`modulo: 1`).

| ❌ | ✅ |
|---|---|
| "material de lectura de la Clase 01" | "material de lectura del Módulo 1" |
| "lo vas a necesitar en la clase 4" | "lo vas a necesitar en el Módulo 4" |

**La palabra "clase" queda reservada para la clase sincrónica**, que es el encuentro en vivo: "antes de la clase sincrónica", "el hands-on de la clase". Ahí sí corresponde.

Dos aclaraciones:

- **Los nombres de directorios y archivos no cambian.** `clases/clase_01_intro_mlops/` se mantiene: la convención es sobre el texto, no sobre las rutas.
- **En los guiones de video sigue mandando la regla de más abajo:** no se nombra la unidad en absoluto, ni como clase ni como módulo. "Más adelante en el curso" vale también para "Módulo 4".

---

## Convenciones para guiones de video

Los videos son **pregrabados**. Todo lo que escribamos en un guion tiene que sobrevivir a que cambie el stack o el orden del programa: si no, hay que regrabar. De ahí salen las dos reglas siguientes, que son las más importantes de este archivo.

### 1. No ubicar los temas en el plan de estudios

Los temas que se ven después se anuncian como **"más adelante en el curso"** o **"más adelante en el posgrado"**, sin decir en qué módulo ni en qué materia caen.

| ❌ | ✅ |
|---|---|
| "Lo vamos a ver en la clase 5" | "Le vamos a dedicar una clase entera más adelante" |
| "lo implementamos en la clase 7, con Dagster" | "más adelante, cuando lleguemos a la orquestación" |
| "es el tema de la materia siguiente del posgrado" | "es un tema que van a ver más adelante en el posgrado" |

Mantener el **anclaje temático** (la orquestación, el versionado de datos, el serving online) para que el alumno igual ubique el tema.

Esto vale **también para el resto del posgrado**, y ahí con más razón: el plan de otras materias es aún menos previsible que el orden de nuestros módulos — pueden cambiar de nombre, de contenido, de posición o dejar de existir, y nos enteramos tarde. Nunca nombrar otra materia ni afirmar que un tema es "de la que sigue". Única excepción: el video dedicado al contrato de interfaz entre materias, donde el flujo del posgrado *es* el contenido.

### 2. Ser agnóstico a las herramientas

Se nombra **lo que hace** la herramienta, no la marca.

| ❌ | ✅ |
|---|---|
| "MLflow" | "un sistema de tracking de experimentos y registro de modelos" |
| "DVC" | "versionado de datos" |
| "Dagster" | "orquestación" |
| "`uv` / `uv.lock`" | "la herramienta de gestión de dependencias" / "el lock file" |
| "`StandardScaler`" | "un escalador ajustado" |

**Excepción:** cuando el nombre *es* el contenido del video. En un video sobre gestión de dependencias, `pyproject.toml`, `requirements.txt` o `pip` pueden quedar, porque son estándares del ecosistema y son el tema en sí. La prueba a aplicar: *si mañana cambiamos esta herramienta, ¿hay que regrabar?* Si la respuesta es sí y el tema no lo exige, sacarla.

**Dónde sí van los nombres propios:** en las **lecturas de Moodle**, en la **guía de la clase sincrónica** y en la sección **Notas de producción** del guion (material interno, no se lee en cámara). Todo eso se actualiza sin regrabar.

⚠️ **Esta regla aplica solo a los guiones de video.** En las lecturas y en la clase sincrónica, ser vago con las herramientas no protege de nada y le quita utilidad al material: ahí van `uv`, `ruff`, `DVC`, `Cloudflare R2`, con sus comandos, sus URLs y sus límites de plan. Si el stack cambia, se edita el archivo y listo.

### Estructura del `guion.md`

Tomar como referencia [`clases/clase_01_intro_mlops/videos/v01_ciclo_vida_ml/guion.md`](clases/clase_01_intro_mlops/videos/v01_ciclo_vida_ml/guion.md):

1. Título, módulo y duración estimada.
2. **De qué trata este video / Agenda (1 min)** — tres bullets con lo que se va a ver.
3. **Introducción (1–2 min)** — el gancho: por qué le importa al alumno, conectado con el pipeline que está construyendo.
4. **Desarrollo** — 2 o 3 puntos, cada uno con su duración estimada.
5. **Cierre (1 min)** — las ideas clave numeradas, y con qué se conecta.
6. **Notas de producción** — pantalla, animaciones, referencias, continuidad.

Los cambios de diapositiva se marcan en el cuerpo como `**[Slide: descripción]**`.

### Duración

La referencia son **8–15 min**, y sirve como orientación, no como límite duro: **algunos videos pueden ser más largos si el tema lo justifica** y no se parte bien. No recortar contenido valioso solo para entrar en el rango — sí declarar la duración real en el encabezado y anotar en las notas de producción por qué se decidió dejarlo largo.

Para estimarla: contar palabras del guion sin las notas de producción y dividir por ~130 (palabras por minuto habladas con pausas). De referencia, `v01_ciclo_vida_ml` tiene ~1050 palabras y dura 8–10 min.

### Registro

Español rioplatense, dirigido al alumno en **ustedes** ("vienen trabajando", "quédense con"). Tono conversacional pero no informal. El `guion.md` es más redactado; el `guion_teleprompter.md` es la bajada oral, con marcas `[CD]` (cambio de diapositiva), `[C]` (click), `[PAUSA]`, `[ÉNFASIS]`, y los números escritos en letras.

### Al escribir un video nuevo

- Verificar en `propuesta_amii_2026.md` qué temas tiene asignados **ese** video, y cuáles están asignados a las lecturas o a otros videos, para no pisarlos ni dejar huecos.
- No dar por sabido lo que se introduce después. En el Módulo 1 el alumno viene de un notebook: no conoce `pyproject.toml`, ni la estructura `src`, ni el stack. Entrar siempre desde lo que ya sabe.

---

## Preguntas: apertura de la clase sincrónica y evaluativo

Son dos actividades distintas, con restricciones distintas.

### Apertura de la clase sincrónica — AhaSlides

Se juega en **AhaSlides**, no en Kahoot. La carpeta se sigue llamando `kahoot/` por historia del repo; el nombre del directorio no importa, el contenido sí.

Dos límites duros que hay que respetar al escribir:

- **Máximo 5 preguntas.** Es el tope del plan gratuito, que es el que usamos. No proponer sets más largos: si sobra material, va al evaluativo.
- **Texto corto o se recorta en pantalla.** Regla de trabajo: **≤ 50 caracteres por opción** y enunciados de una sola línea, sin subordinadas. Conviene verificar los largos antes de dar por cerrado el archivo — es fácil pasarse sin darse cuenta.

Con 5 preguntas no entra todo el módulo, así que el criterio es **una por pieza** (video o lectura), priorizando los conceptos centrales. Cada pregunta lleva un campo `fuente` con la pieza de la que sale: si falla masivamente, indica qué material no se consumió, y la guía de la clase sincrónica usa eso para decidir dónde poner el foco.

AhaSlides admite más que opción múltiple —emparejar, respuesta escrita, ordenar—; usar variedad hace la apertura más entretenida y algunos conceptos entran mejor. El esquema YAML de cada tipo está documentado en el encabezado de `clases/clase_01_intro_mlops/kahoot/preguntas.yaml`.

### Evaluativo — Moodle

**10 preguntas de opción múltiple**, intentos ilimitados, se requiere >8/10 para aprobar la materia. No tiene límite de caracteres ni de cantidad de tipos, así que acá entra lo que no cupo en la apertura, y las opciones pueden ser más largas y más precisas.
