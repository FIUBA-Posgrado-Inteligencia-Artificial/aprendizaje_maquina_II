# Buenas prácticas de programación aplicadas a ML

<!-- interno -->
> **Nota de cátedra (no se publica en Moodle).**
> Introducción práctica, pensada para aplicarse sobre el notebook que el alumno ya tiene, **antes** del refactor.
> **Deliberadamente fuera de alcance** para no pisar las lecturas del Módulo 2: gestión de configuración (Hydra/OmegaConf), logging estructurado, type hints y docstrings en profundidad, configuración de `ruff` y pre-commit, y workflows de CI. Acá se los menciona como "lo vas a ver en el Módulo 2" y nada más.
> El criterio "legible, simple y conciso" viene del material anterior de la cátedra; se conservó como hilo conductor.
> Para publicar: `uv run scripts/lectura_a_moodle.py clases/clase_01_intro_mlops/lecturas/lectura_02_buenas_practicas.md`
<!-- /interno -->

Esta guía es material de lectura del **Módulo 1**. Es una introducción práctica: son cosas que podés aplicar hoy mismo sobre el notebook que ya tenés, sin esperar a refactorizar nada.

Hasta ahora tu código tuvo un solo lector: vos, mientras lo escribías. A partir de ahora va a tener otros dos: **la persona que lo reciba** y **vos dentro de tres meses**, que para estos efectos es casi la misma persona. Todo lo que sigue apunta a eso.

El criterio general es el de siempre: el código que va a producción tiene que ser **legible, simple y conciso**. Lo que agregamos acá es qué significa eso concretamente cuando lo que escribís es un pipeline de aprendizaje automático.

---

## Parte 1 — Que se entienda

### Nombres que dicen qué son

Es la práctica con mejor relación entre esfuerzo y beneficio. Un nombre bien puesto ahorra un comentario.

```python
# ❌ Nadie sabe qué es esto dentro de dos semanas
df2 = df[df['a'] > 0]
x = df2.iloc[:, :-1]
y = df2.iloc[:, -1]
m = fit(x, y)
```

```python
# ✅
ventas_validas = ventas[ventas['monto'] > 0]
features = ventas_validas.drop(columns='compro')
etiquetas = ventas_validas['compro']
modelo = entrenar(features, etiquetas)
```

Tres reglas que cubren casi todos los casos:

- **Nada de `df`, `df2`, `df_final`, `df_final_v2`.** Si tenés varios, es porque cada uno es una cosa distinta: nombralos por lo que son.
- **Las funciones son verbos** (`cargar_datos`, `calcular_features`), **las variables son sustantivos** (`datos_crudos`, `matriz_features`).
- **Una sola letra solo para índices** en un bucle corto. `X` e `y` para features y etiquetas son una convención tan establecida que se aceptan, pero son la excepción, no la regla.

### Una función, una responsabilidad

El síntoma más común en un notebook es la celda de cuarenta líneas que carga, limpia, transforma, entrena y grafica.

```python
# ❌ Una sola cosa que hace cinco
datos = pd.read_csv('/Users/juan/Desktop/datos.csv')
datos = datos.dropna()
datos['edad_norm'] = (datos['edad'] - datos['edad'].mean()) / datos['edad'].std()
modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(datos[['edad_norm']], datos['target'])
print(modelo.score(datos[['edad_norm']], datos['target']))
```

```python
# ✅ Cada paso es una función con nombre, entradas y salidas
def cargar_datos(ruta):
    return pd.read_csv(ruta)

def limpiar(datos):
    return datos.dropna()

def construir_features(datos):
    ...

def entrenar(features, etiquetas, n_estimadores):
    ...

def evaluar(modelo, features, etiquetas):
    ...
```

Esto no es estética. Una función con entradas y salidas explícitas se puede **testear**, se puede **reutilizar** y se puede **volver a ejecutar sola** sin correr todo lo anterior. Una celda no.

Como regla práctica: **si una función no entra en la pantalla, probablemente hace más de una cosa.**

### Comentarios que expliquen el porqué

El código ya dice *qué* hace. El comentario tiene que decir lo que el código no puede decir.

```python
# ❌ No aporta nada
# Sumo 1 al contador
contador += 1

# ✅ Explica una decisión que no es obvia
# Los registros de 2020 se descartan: durante la pandemia el patrón de compra
# no es representativo y mete ruido en el entrenamiento.
ventas = ventas[ventas['anio'] != 2020]
```

En ML esto importa el doble, porque muchas decisiones —descartar un período, elegir un umbral, imputar de cierta forma— vienen de conocimiento del dominio que no está en ningún lado del código.

### Estilo: no lo discutas, automatizalo

Python tiene una guía de estilo oficial, **PEP 8**: cuatro espacios de indentación, `snake_case` para funciones y variables, líneas que no se van al infinito.

No hace falta que te la aprendas de memoria ni que discutas con nadie dónde va un espacio: **eso se automatiza con un formateador**, y lo vamos a configurar en el Módulo 2. Por ahora, alcanza con que sepas que existe y que tu editor probablemente ya puede aplicarla sola.

---

## Parte 2 — Que se pueda volver a correr

Esta parte es la que separa un experimento de un proceso.

### Nada hardcodeado en el medio del código

Los valores que definen el comportamiento —rutas, hiperparámetros, umbrales, semillas— no pueden estar desperdigados.

```python
# ❌ ¿Dónde cambio el tamaño del test? ¿Y si aparece otro 0.2 más abajo?
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = RandomForestClassifier(n_estimators=100, max_depth=8)
```

```python
# ✅ Todo junto y con nombre, arriba del archivo
TEST_SIZE = 0.2
SEMILLA = 42
N_ESTIMADORES = 100
PROFUNDIDAD_MAXIMA = 8

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=SEMILLA
)
modelo = RandomForestClassifier(
    n_estimators=N_ESTIMADORES,
    max_depth=PROFUNDIDAD_MAXIMA,
    random_state=SEMILLA,
)
```

Juntar las constantes arriba es el primer paso. El paso siguiente es sacarlas del código y ponerlas en un archivo de configuración aparte, que es lo que vamos a hacer en el Módulo 2.

### Rutas relativas, nunca absolutas

```python
# ❌ Funciona solo en tu computadora
datos = pd.read_csv('/Users/juan/Desktop/proyecto/datos/ventas.csv')
```

```python
# ✅ Funciona en cualquier lado
from pathlib import Path

DIRECTORIO_DATOS = Path('datos')
datos = pd.read_csv(DIRECTORIO_DATOS / 'ventas.csv')
```

Dos motivos para usar `pathlib` en lugar de concatenar texto: se encarga solo de las barras (que en Windows van al revés) y hace evidente qué parte de la ruta es un directorio.

### Fijá las semillas

Cualquier cosa que use azar necesita una semilla explícita: la división de los datos, la inicialización del modelo, el submuestreo de un ensamble.

```python
SEMILLA = 42

train_test_split(X, y, random_state=SEMILLA)
RandomForestClassifier(random_state=SEMILLA)
np.random.seed(SEMILLA)
```

Sin esto, dos corridas del mismo código sobre los mismos datos dan métricas distintas, y perdés la capacidad de saber si un cambio mejoró el modelo o simplemente tuviste suerte.

**La semilla es un parámetro del pipeline como cualquier otro**: va con los demás, arriba y con nombre.

### El notebook tiene estado oculto

Este es el problema más específico de trabajar en notebooks, y el más traicionero.

Cuando ejecutás celdas en cualquier orden, borrás una, editás otra y volvés a correr solo algunas, el estado que queda en memoria **deja de corresponderse con el código que está escrito**. El notebook anda, pero nadie —incluido vos— puede reproducir ese resultado.

La verificación es simple, y conviene que la hagas seguido:

> **Reiniciar el kernel y ejecutar todo de arriba hacia abajo.**
> Si no llega al final sin errores y con los mismos resultados, tu notebook no es reproducible.

En Jupyter es *Kernel → Restart Kernel and Run All Cells*. Hacelo antes de dar por terminado cualquier trabajo.

### No copies y pegues: parametrizá

Si te encontrás copiando una celda para cambiarle un valor, eso es una función esperando a nacer.

```python
# ❌ Tres bloques iguales con un número distinto
modelo_a = RandomForestClassifier(max_depth=4).fit(X_train, y_train)
print(modelo_a.score(X_test, y_test))
modelo_b = RandomForestClassifier(max_depth=8).fit(X_train, y_train)
print(modelo_b.score(X_test, y_test))
modelo_c = RandomForestClassifier(max_depth=16).fit(X_train, y_train)
print(modelo_c.score(X_test, y_test))
```

```python
# ✅
def entrenar_y_evaluar(profundidad):
    modelo = RandomForestClassifier(max_depth=profundidad, random_state=SEMILLA)
    modelo.fit(X_train, y_train)
    return modelo, modelo.score(X_test, y_test)

for profundidad in [4, 8, 16]:
    modelo, exactitud = entrenar_y_evaluar(profundidad)
    print(f"profundidad={profundidad}: {exactitud:.3f}")
```

El problema del copiar y pegar no es la cantidad de líneas: es que cuando haya que corregir algo, hay que acordarse de corregirlo en los tres lugares. Y siempre queda uno.

---

## Parte 3 — Que no falle en silencio

Un programa común, cuando algo anda mal, se rompe. **Un modelo, cuando algo anda mal, devuelve un número igual.** Por eso en ML hay que ser mucho más explícito.

### Fallá temprano y fuerte

```python
# ❌ Si la columna no existe, te enterás doscientas líneas más abajo,
# o directamente no te enterás
def construir_features(datos):
    datos['ratio'] = datos['monto'] / datos['cantidad']
    return datos
```

```python
# ✅ Si algo no está como esperabas, se corta acá
def construir_features(datos):
    columnas_requeridas = {'monto', 'cantidad'}
    faltantes = columnas_requeridas - set(datos.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas en los datos de entrada: {faltantes}")

    if (datos['cantidad'] == 0).any():
        raise ValueError("Hay filas con cantidad cero: la división daría infinito")

    datos = datos.copy()
    datos['ratio'] = datos['monto'] / datos['cantidad']
    return datos
```

Puede parecer excesivo para tres líneas de transformación. No lo es: **es la diferencia entre un error que aparece en la línea que lo causó y un modelo que entrena con valores infinitos y da métricas raras que nadie sabe explicar.**

Esto se formaliza más adelante con herramientas de validación de datos, pero un `raise` bien puesto ya te cubre el noventa por ciento de los casos.

### No uses `print` para todo

`print` sirve mientras explorás. Cuando el código pasa a correr sin que nadie lo mire, necesitás algo que registre **cuándo** pasó cada cosa y **qué tan grave** es, y que se pueda apagar sin editar el código.

Eso es *logging*, y tiene su propia guía en el Módulo 2. Por ahora quedate con la idea: los `print` desperdigados son deuda que vas a pagar.

### Cuidado con modificar lo que recibís

```python
# ❌ Esta función modifica el DataFrame de quien la llamó,
# sin avisar. Después nada cuadra.
def normalizar(datos):
    datos['edad'] = (datos['edad'] - datos['edad'].mean()) / datos['edad'].std()
    return datos
```

```python
# ✅ Trabajá sobre una copia y devolvé algo nuevo
def normalizar(datos):
    resultado = datos.copy()
    resultado['edad'] = (resultado['edad'] - resultado['edad'].mean()) / resultado['edad'].std()
    return resultado
```

Una función que recibe algo, lo devuelve transformado y no toca la entrada es **predecible**: la podés llamar dos veces y obtener lo mismo. Ese es exactamente el tipo de función que después se puede testear y encadenar en un pipeline.

---

## Parte 4 — Que no pierda ni filtre nada

### Guardá lo que produce tu código

Un resultado que vive solo en la memoria del kernel no existe: se pierde al cerrar el notebook.

Todo lo que tu código produce y alguien va a necesitar después —el modelo entrenado, las transformaciones ajustadas, las métricas, el archivo de predicciones— **tiene que quedar escrito en disco**.

Y prestá atención especial a las transformaciones ajustadas. El escalador y el codificador de categóricas **aprendieron de tus datos de entrenamiento**: si guardás el modelo pero no los guardás a ellos, el modelo es inservible, porque nunca vas a poder reproducir las features con las que aprendió.

### Nunca credenciales en el código

```python
# ❌ Y si esto se sube al repositorio, ya es tarde:
# queda en el historial de Git para siempre
conexion = conectar(usuario='admin', password='1234abcd')
```

```python
# ✅ Se leen del entorno
import os

conexion = conectar(
    usuario=os.environ['DB_USUARIO'],
    password=os.environ['DB_PASSWORD'],
)
```

Es la única práctica de esta guía cuya violación no se puede deshacer editando un archivo: una contraseña commiteada hay que darla por comprometida y rotarla, aunque después la borres.

---

## Checklist antes de la clase sincrónica

Aplicá esto sobre el notebook con el que venís trabajando. No hace falta que quede perfecto; sí que lo hayas mirado con estos ojos:

- [ ] Reiniciaste el kernel, corriste todo de arriba abajo y llegó al final sin errores
- [ ] No quedan rutas absolutas de tu computadora
- [ ] Las semillas están fijas y explícitas
- [ ] Los hiperparámetros y umbrales están juntos y con nombre, no desperdigados
- [ ] No hay contraseñas, tokens ni claves de acceso escritas en el código
- [ ] Al menos los pasos principales están en funciones y no en celdas sueltas
- [ ] Ninguna variable se llama `df2` ni `datos_final_v3`

Si alguno de estos puntos te resultó difícil de resolver, traelo al **foro de dudas**: suelen ser los mismos casos para casi todo el curso.

---

## Referencias

- PEP 8, guía de estilo de Python: <https://peps.python.org/pep-0008/>
- The Hitchhiker's Guide to Python, sobre estructura y estilo: <https://docs.python-guide.org/writing/style/>
- Google, *Rules of Machine Learning*: <https://developers.google.com/machine-learning/guides/rules-of-ml>
- Documentación de `pathlib`: <https://docs.python.org/es/3/library/pathlib.html>
