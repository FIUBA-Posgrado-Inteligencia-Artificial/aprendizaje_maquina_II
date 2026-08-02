# Módulo 1 — Introducción a MLOps y ciclo de vida de un proyecto de ML

## Objetivos

Al terminar el módulo, el alumno tiene que poder:

1. Ubicar las etapas del ciclo de vida de un proyecto de ML y quién es responsable de cada una.
2. Explicar qué es un pipeline, qué es un artifact y por qué las transformaciones ajustadas viajan con el modelo.
3. Reconocer en qué nivel de madurez de MLOps está un equipo, y qué gana al subir de nivel.
4. Distinguir entorno de desarrollo de entorno productivo, y saber que producción se define por la consecuencia de una falla.
5. Entender qué se entrega junto con un modelo para que otro equipo pueda usarlo, incluso con otra tecnología.
6. Tener su repositorio de grupo creado y su entorno reproducible funcionando.

---

## Checklist de producción

### Videos — guiones
- [x] `videos/v01_ciclo_vida_ml/guion.md` — 8–10 min
- [x] `videos/v02_pipelines_artifacts/guion.md` — 18–20 min
- [x] `videos/v03_mlops_niveles/guion.md` — 18–20 min
- [x] `videos/v04_entornos/guion.md` — 14–16 min
- [x] `videos/v05_contrato_interfaz/guion.md` — 21–23 min

### Videos — teleprompter y slides
> Tomar como referencia `v01`, que es el único completo.

- [x] `v01_ciclo_vida_ml` — 24 diapositivas
- [x] `v02_pipelines_artifacts` — 36 diapositivas
- [x] `v03_mlops_niveles` — 34 diapositivas
- [x] `v04_entornos` — 27 diapositivas
- [x] `v05_contrato_interfaz` — 37 diapositivas
- [ ] Diapositivas **diseñadas** a partir de estos guiones de slides (hoy son texto y notas de layout)

### Videos — grabación
- [ ] v01 grabado y editado
- [ ] v02 grabado y editado
- [ ] v03 grabado y editado
- [ ] v04 grabado y editado
- [ ] v05 grabado y editado

### Lecturas (Moodle)
- [x] `lecturas/lectura_01_uv_dependencias.md` — verificada contra uv 0.12.1
- [x] `lecturas/lectura_02_buenas_practicas.md` — ejemplos de código verificados

### Evaluativo
- [x] `evaluativo/preguntas.yaml` — pool de 32 preguntas, Moodle sortea 10
- [ ] Importado al banco de preguntas (`uv run scripts/preguntas_a_moodle.py`)

### Apertura de la clase sincrónica (AhaSlides)
- [x] `kahoot/preguntas.yaml` — 5 preguntas (tope del plan gratuito)
- [ ] Cargadas en AhaSlides

### Clase sincrónica
- [x] `clase_sincrónica/guia.md` — secuencia y ejercicios definidos
- [ ] **Revisar la guía contra el repositorio template real.** Está escrita contra un scaffold propuesto, porque el template y la GitHub Organization todavía no existen. Hay que verificar el árbol de archivos, los nombres de los módulos de `src/`, el comando del smoke test, si el template trae `uv.lock` generado, y la URL del assignment de Classroom. El detalle está en el bloque ⚠️ PENDIENTE al inicio de la guía.

### Seguimiento entre módulos
- [ ] Verificar antes del módulo de versionado de datos que **todos los grupos crearon su cuenta de object storage** (se asigna como tarea en este módulo). Los que no hayan podido por el requisito de tarjeta de crédito van a la alternativa local con MinIO.

### Estado de publicación en Moodle
- [ ] Videos subidos y enlazados
- [ ] Lecturas publicadas como páginas (`uv run scripts/lectura_a_moodle.py`)
- [ ] Foro de dudas creado
- [ ] Evaluativo habilitado
- [ ] AhaSlides preparado

---

## Herramientas del repo

```bash
# Lecturas -> HTML para pegar en una página de Moodle
uv run scripts/lectura_a_moodle.py clases/clase_01_intro_mlops/lecturas/lectura_01_uv_dependencias.md

# Evaluativo -> XML para importar al banco de preguntas
uv run scripts/preguntas_a_moodle.py clases/clase_01_intro_mlops/evaluativo/preguntas.yaml
```
