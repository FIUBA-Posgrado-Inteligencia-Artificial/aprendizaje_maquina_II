# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml>=6.0"]
# ///
"""
Convierte un `preguntas.yaml` a Moodle XML, listo para importar al banco de preguntas.

Uso:
    uv run scripts/preguntas_a_moodle.py <preguntas.yaml>
    uv run scripts/preguntas_a_moodle.py <preguntas.yaml> --categoria "top/Evaluativos/Módulo 01"
    uv run scripts/preguntas_a_moodle.py --todos

Salida:
    <mismo_nombre>.moodle.xml junto al original.

Cómo importarlo en Moodle:
    Banco de preguntas -> Importar -> formato "Moodle XML" -> subir el archivo.
    La categoría de destino viene declarada adentro del XML, así que Moodle la
    crea sola si no existe. En la pantalla de importación hay que dejar
    destildado "Obtener categoría del archivo" solo si se la quiere sobrescribir.

Por qué Moodle XML y no GIFT:
    GIFT reserva los caracteres ~ = # { } y : , que aparecen naturalmente en
    enunciados con código y con rutas. Además no tiene un lugar limpio para la
    retroalimentación larga. Moodle XML lleva las explicaciones en
    `generalfeedback`, que es lo que el alumno ve al corregir el intento.
"""

import argparse
import re
import sys
from pathlib import Path
from xml.etree import ElementTree

import yaml

RAIZ = Path(__file__).resolve().parent.parent

RE_CODIGO = re.compile(r"`([^`]+)`")


def a_html(texto: str) -> str:
    """Pasa el texto del YAML a HTML de bloque: `código` y párrafos."""
    parrafos = [p.strip() for p in re.split(r"\n\s*\n", inline(texto)) if p.strip()]
    return "".join(f"<p>{p}</p>" for p in parrafos)


def inline(texto: str) -> str:
    """Igual, pero sin envolver en <p>: para las opciones de respuesta, que
    Moodle renderiza en línea y donde un párrafo agrega espacio de más."""
    return RE_CODIGO.sub(r"<code>\1</code>", texto.strip())


def campo_texto(padre: ElementTree.Element, etiqueta: str, contenido: str, html: bool = True):
    """Crea <etiqueta format="html"><text>...</text></etiqueta>."""
    nodo = ElementTree.SubElement(padre, etiqueta)
    if html:
        nodo.set("format", "html")
    texto = ElementTree.SubElement(nodo, "text")
    texto.text = contenido
    return nodo


def nombre_pregunta(modulo: int, pregunta: dict) -> str:
    """Nombre corto e identificable en el listado del banco."""
    plano = RE_CODIGO.sub(r"\1", pregunta["enunciado"]).strip()
    plano = " ".join(plano.split())
    if len(plano) > 70:
        plano = plano[:67].rsplit(" ", 1)[0] + "…"
    return f"M{modulo}-P{pregunta['id']:02d} · {plano}"


def construir_xml(datos: dict, categoria: str) -> ElementTree.ElementTree:
    modulo = datos["modulo"]
    quiz = ElementTree.Element("quiz")

    # Nodo de categoría: Moodle la crea si no existe.
    nodo_cat = ElementTree.SubElement(quiz, "question", {"type": "category"})
    campo_texto(nodo_cat, "category", categoria, html=False)
    campo_texto(nodo_cat, "info", a_html(datos.get("titulo", "")))

    omitidas = []
    for p in datos["preguntas"]:
        tipo = p.get("tipo", "opcion_multiple")
        if tipo != "opcion_multiple":
            omitidas.append((p["id"], tipo))
            continue

        correctas = [o for o in p["opciones"] if o.get("correcta")]
        if len(correctas) != 1:
            raise SystemExit(f"error: la pregunta {p['id']} tiene {len(correctas)} opciones correctas")

        q = ElementTree.SubElement(quiz, "question", {"type": "multichoice"})
        campo_texto(q, "name", nombre_pregunta(modulo, p), html=False)
        campo_texto(q, "questiontext", a_html(p["enunciado"]))
        campo_texto(q, "generalfeedback", a_html(p.get("explicacion", "")))

        ElementTree.SubElement(q, "defaultgrade").text = "1.0000000"
        ElementTree.SubElement(q, "penalty").text = "0.0000000"
        ElementTree.SubElement(q, "hidden").text = "0"
        ElementTree.SubElement(q, "single").text = "true"
        ElementTree.SubElement(q, "shuffleanswers").text = "true"
        ElementTree.SubElement(q, "answernumbering").text = "abc"

        for opcion in p["opciones"]:
            fraccion = "100" if opcion.get("correcta") else "0"
            ans = ElementTree.SubElement(q, "answer", {"fraction": fraccion, "format": "html"})
            ElementTree.SubElement(ans, "text").text = inline(opcion["texto"])
            campo_texto(ans, "feedback", "")

    if omitidas:
        for id_, tipo in omitidas:
            print(f"  aviso: pregunta {id_} omitida (tipo '{tipo}' no es de opción múltiple)",
                  file=sys.stderr)

    ElementTree.indent(quiz, space="  ")
    return ElementTree.ElementTree(quiz)


def mostrar(ruta: Path) -> str:
    try:
        return str(ruta.resolve().relative_to(RAIZ))
    except ValueError:
        return str(ruta)


def procesar(ruta: Path, categoria: str | None) -> None:
    datos = yaml.safe_load(ruta.read_text(encoding="utf-8"))
    modulo = datos["modulo"]
    titulo = datos.get("titulo", "")
    cat = categoria or f"$course$/top/Módulo {modulo:02d} — {titulo}"

    arbol = construir_xml(datos, cat)
    destino = ruta.with_suffix(".moodle.xml")
    arbol.write(destino, encoding="utf-8", xml_declaration=True)

    total = sum(1 for p in datos["preguntas"] if p.get("tipo", "opcion_multiple") == "opcion_multiple")
    print(f"  {mostrar(ruta)}")
    print(f"    -> {mostrar(destino)}")
    print(f"    {total} preguntas · categoría: {cat}")


def buscar() -> list[Path]:
    return sorted(RAIZ.glob("clases/*/evaluativo/preguntas.yaml"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convierte preguntas en YAML a Moodle XML para importar al banco de preguntas.",
    )
    parser.add_argument("archivos", nargs="*", type=Path, help="Archivos preguntas.yaml")
    parser.add_argument("--todos", action="store_true", help="Convertir todos los evaluativos del repo")
    parser.add_argument(
        "--categoria",
        help=(
            "Ruta de la categoría destino. Por defecto "
            "'$course$/top/Módulo NN — <título>'. Usar $system$ para el banco del sitio."
        ),
    )
    args = parser.parse_args()

    rutas = buscar() if args.todos else args.archivos
    if not rutas:
        parser.error("indicá al menos un archivo, o usá --todos")

    faltantes = [r for r in rutas if not r.is_file()]
    if faltantes:
        for r in faltantes:
            print(f"error: no existe {r}", file=sys.stderr)
        return 1

    print(f"Convirtiendo {len(rutas)} archivo(s):")
    for ruta in rutas:
        procesar(ruta, args.categoria)

    print(
        "\nPara importar: Banco de preguntas -> Importar -> 'Formato XML de Moodle' -> subir el archivo."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
