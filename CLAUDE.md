# CLAUDE.md

Material de la materia **Operaciones de Aprendizaje Automático I** (CEIA — FIUBA).

## Contexto del repositorio

El repositorio está en transición entre dos ediciones:

- **`clases/`** — programa nuevo de 8 clases, en desarrollo. Es donde se trabaja.
- **`clase1/` … `clase7/`, `old/`** — edición anterior. Material de consulta, no se edita salvo pedido explícito.
- **`propuesta_amii_2026.md`** — fuente de verdad del programa nuevo: qué videos, lecturas, hands-on y evaluativos lleva cada clase, y el stack técnico. **Consultarlo antes de escribir material nuevo**, para saber qué le toca cubrir a cada pieza y qué está asignado a otra.
- **`README.md`** — todavía describe el programa anterior.

El hilo conductor del curso es *"de notebook a pipeline reproducible de entrenamiento y predicción en lote"*, y el formato es **flipped classroom**: videos pregrabados + lecturas en Moodle + clase sincrónica de hands-on.

### Estructura de una clase

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

Muchos archivos son todavía plantillas vacías. Al completar uno, seguir la estructura del equivalente ya escrito en otra clase en vez de inventar un formato nuevo.

---

## Convenciones para guiones de video

Los videos son **pregrabados**. Todo lo que escribamos en un guion tiene que sobrevivir a que cambie el stack o el orden del programa: si no, hay que regrabar. De ahí salen las dos reglas siguientes, que son las más importantes de este archivo.

### 1. No ubicar los temas en el plan de estudios

Los temas que se ven después se anuncian como **"más adelante en el curso"** o **"más adelante en el posgrado"**, sin decir en qué clase ni en qué materia caen.

| ❌ | ✅ |
|---|---|
| "Lo vamos a ver en la clase 5" | "Le vamos a dedicar una clase entera más adelante" |
| "lo implementamos en la clase 7, con Dagster" | "más adelante, cuando lleguemos a la orquestación" |
| "es el tema de la materia siguiente del posgrado" | "es un tema que van a ver más adelante en el posgrado" |

Mantener el **anclaje temático** (la orquestación, el versionado de datos, el serving online) para que el alumno igual ubique el tema.

Esto vale **también para el resto del posgrado**, y ahí con más razón: el plan de otras materias es aún menos previsible que el orden de nuestras clases — pueden cambiar de nombre, de contenido, de posición o dejar de existir, y nos enteramos tarde. Nunca nombrar otra materia ni afirmar que un tema es "de la que sigue". Única excepción: el video dedicado al contrato de interfaz entre materias, donde el flujo del posgrado *es* el contenido.

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

**Dónde sí van los nombres propios:** en las **lecturas de Moodle**, en la **clase sincrónica** y en la sección **Notas de producción** del guion (material interno, no se lee en cámara). Todo eso se actualiza sin regrabar.

### Estructura del `guion.md`

Tomar como referencia [`clases/clase_01_intro_mlops/videos/v01_ciclo_vida_ml/guion.md`](clases/clase_01_intro_mlops/videos/v01_ciclo_vida_ml/guion.md):

1. Título, clase y duración estimada.
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
- No dar por sabido lo que se introduce después. En la clase 1 el alumno viene de un notebook: no conoce `pyproject.toml`, ni la estructura `src`, ni el stack. Entrar siempre desde lo que ya sabe.
