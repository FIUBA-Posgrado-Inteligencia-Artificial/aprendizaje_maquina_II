# /// script
# requires-python = ">=3.11"
# dependencies = ["markdown>=3.6"]
# ///
"""
Convierte una lectura en Markdown a un fragmento HTML listo para pegar en Moodle.

Uso:
    uv run scripts/lectura_a_moodle.py <archivo.md> [más archivos...]
    uv run scripts/lectura_a_moodle.py --todas
    uv run scripts/lectura_a_moodle.py <archivo.md> --stdout

Salida:
    Por cada entrada genera <mismo_nombre>.moodle.html junto al original.

Por qué existe:
    Moodle no acepta Markdown en las páginas y su editor descarta las hojas de
    estilo: cualquier formato tiene que venir como atributo `style` en cada
    etiqueta. Este script hace esa traducción para no maquetar a mano.

Convenciones del Markdown de entrada:
    - El primer encabezado `#` es el título de la página. No se emite en el
      cuerpo (Moodle ya muestra el título por su cuenta): se informa por
      pantalla para copiarlo en el campo correspondiente.
    - Todo lo que esté entre `<!-- interno -->` y `<!-- /interno -->` se
      descarta. Ahí van las notas de cátedra que no se publican.
    - Las listas de tareas (`- [ ]`) se convierten en casillas visuales.
"""

import argparse
import html
import re
import sys
from pathlib import Path

import markdown

RAIZ = Path(__file__).resolve().parent.parent

# Paleta sobria, legible sobre el fondo blanco de Moodle.
AZUL = "#1a4f7a"
GRIS_BORDE = "#d9dee3"
GRIS_FONDO = "#f6f8fa"
GRIS_TEXTO = "#3c4043"
AMBAR_BORDE = "#e0a800"
AMBAR_FONDO = "#fff8e6"

# Estilos por etiqueta. Moodle descarta <style>, así que todo va inline.
ESTILOS = {
    "h2": (
        f"color:{AZUL};font-size:1.45em;font-weight:600;margin:1.8em 0 .6em;"
        f"padding-bottom:.25em;border-bottom:2px solid {GRIS_BORDE};"
    ),
    "h3": f"color:{AZUL};font-size:1.2em;font-weight:600;margin:1.4em 0 .5em;",
    "h4": f"color:{GRIS_TEXTO};font-size:1.05em;font-weight:600;margin:1.2em 0 .4em;",
    "p": f"color:{GRIS_TEXTO};line-height:1.65;margin:.8em 0;",
    "ul": f"color:{GRIS_TEXTO};line-height:1.65;margin:.8em 0;padding-left:1.6em;",
    "ol": f"color:{GRIS_TEXTO};line-height:1.65;margin:.8em 0;padding-left:1.6em;",
    "li": "margin:.35em 0;",
    "table": (
        "border-collapse:collapse;width:100%;margin:1.2em 0;font-size:.95em;"
    ),
    "th": (
        f"border:1px solid {GRIS_BORDE};padding:.6em .8em;background:{GRIS_FONDO};"
        f"color:{AZUL};text-align:left;font-weight:600;"
    ),
    "td": f"border:1px solid {GRIS_BORDE};padding:.6em .8em;color:{GRIS_TEXTO};vertical-align:top;",
    "blockquote": (
        f"margin:1.2em 0;padding:.9em 1.1em;background:{AMBAR_FONDO};"
        f"border-left:4px solid {AMBAR_BORDE};color:{GRIS_TEXTO};line-height:1.6;"
    ),
    "hr": f"border:0;border-top:1px solid {GRIS_BORDE};margin:2em 0;",
    "a": f"color:{AZUL};text-decoration:underline;",
}

ESTILO_PRE = (
    f"background:{GRIS_FONDO};border:1px solid {GRIS_BORDE};border-radius:6px;"
    "padding:.9em 1.1em;overflow-x:auto;margin:1.1em 0;"
    "font-family:ui-monospace,'SF Mono',Menlo,Consolas,monospace;"
    "font-size:.9em;line-height:1.5;white-space:pre;"
)
ESTILO_CODE_INLINE = (
    f"background:{GRIS_FONDO};border:1px solid {GRIS_BORDE};border-radius:3px;"
    "padding:.1em .35em;font-family:ui-monospace,'SF Mono',Menlo,Consolas,monospace;"
    "font-size:.9em;"
)

RE_INTERNO = re.compile(r"<!--\s*interno\s*-->.*?<!--\s*/interno\s*-->", re.DOTALL)
RE_TAREA = re.compile(r"^(\s*)-\s+\[([ xX])\]\s+", re.MULTILINE)


def extraer_titulo(texto: str) -> tuple[str, str]:
    """Separa el primer encabezado `#` del resto del documento."""
    lineas = texto.splitlines()
    for i, linea in enumerate(lineas):
        if linea.startswith("# "):
            titulo = linea[2:].strip()
            return titulo, "\n".join(lineas[:i] + lineas[i + 1 :])
    return "", texto


def preparar(texto: str) -> str:
    """Quita los bloques internos y traduce las listas de tareas."""
    texto = RE_INTERNO.sub("", texto)
    # Moodle no renderiza checkboxes de Markdown: usamos un carácter visible.
    texto = RE_TAREA.sub(lambda m: f"{m.group(1)}- ☐ ", texto)
    return texto


def aplicar_estilos(html_texto: str) -> str:
    """Inyecta un atributo `style` en cada etiqueta que lo necesite."""
    for etiqueta, estilo in ESTILOS.items():
        html_texto = re.sub(
            rf"<{etiqueta}(?=[\s>])",
            f'<{etiqueta} style="{estilo}"',
            html_texto,
        )
        # Etiquetas sin atributos previos (el caso más común).
        html_texto = html_texto.replace(f"<{etiqueta}>", f'<{etiqueta} style="{estilo}">')
    return html_texto


def estilar_codigo(html_texto: str) -> str:
    """Aplica estilos a los bloques y al código en línea.

    Los bloques vienen como <pre><code class="language-x">; Moodle no resalta
    sintaxis, así que se aplana a un solo <pre> con estilo.
    """

    def bloque(match: re.Match) -> str:
        cuerpo = match.group(1)
        return f'<pre style="{ESTILO_PRE}">{cuerpo}</pre>'

    html_texto = re.sub(
        r"<pre[^>]*>\s*<code[^>]*>(.*?)</code>\s*</pre>",
        bloque,
        html_texto,
        flags=re.DOTALL,
    )
    html_texto = re.sub(
        r"<code(?![^>]*style)",
        f'<code style="{ESTILO_CODE_INLINE}"',
        html_texto,
    )
    return html_texto


def convertir(texto_md: str) -> tuple[str, str]:
    """Devuelve (título, fragmento HTML listo para Moodle)."""
    titulo, cuerpo = extraer_titulo(texto_md)
    cuerpo = preparar(cuerpo)

    html_texto = markdown.markdown(
        cuerpo,
        extensions=["fenced_code", "tables", "sane_lists", "attr_list"],
    )
    html_texto = estilar_codigo(html_texto)
    html_texto = aplicar_estilos(html_texto)

    encabezado = (
        "<!-- Generado por scripts/lectura_a_moodle.py — no editar a mano. -->\n"
        f"<!-- Título para el campo 'Nombre' de Moodle: {html.escape(titulo)} -->\n"
    )
    envoltorio = (
        '<div style="max-width:860px;font-family:-apple-system,BlinkMacSystemFont,'
        "'Segoe UI',Roboto,Helvetica,Arial,sans-serif;font-size:16px;\">\n"
        f"{html_texto}\n</div>\n"
    )
    return titulo, encabezado + envoltorio


def mostrar(ruta: Path) -> str:
    """Ruta relativa al repo cuando se puede; si no, la ruta tal cual."""
    try:
        return str(ruta.resolve().relative_to(RAIZ))
    except ValueError:
        return str(ruta)


def procesar(ruta: Path, a_stdout: bool) -> Path | None:
    titulo, salida = convertir(ruta.read_text(encoding="utf-8"))

    if a_stdout:
        sys.stdout.write(salida)
        return None

    destino = ruta.with_suffix(".moodle.html")
    destino.write_text(salida, encoding="utf-8")
    print(f"  {mostrar(ruta)}")
    print(f"    -> {mostrar(destino)}")
    print(f"    título: {titulo}")
    return destino


def buscar_lecturas() -> list[Path]:
    return sorted(RAIZ.glob("clases/*/lecturas/lectura_*.md"))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Convierte lecturas en Markdown a HTML para pegar en Moodle.",
    )
    parser.add_argument("archivos", nargs="*", type=Path, help="Archivos .md a convertir")
    parser.add_argument("--todas", action="store_true", help="Convertir todas las lecturas del repo")
    parser.add_argument("--stdout", action="store_true", help="Imprimir el HTML en vez de escribir el archivo")
    args = parser.parse_args()

    rutas = buscar_lecturas() if args.todas else args.archivos
    if not rutas:
        parser.error("indicá al menos un archivo, o usá --todas")

    faltantes = [r for r in rutas if not r.is_file()]
    if faltantes:
        for r in faltantes:
            print(f"error: no existe {r}", file=sys.stderr)
        return 1

    if not args.stdout:
        print(f"Convirtiendo {len(rutas)} lectura(s):")
    for ruta in rutas:
        procesar(ruta, args.stdout)

    if not args.stdout:
        print(
            "\nPara publicar en Moodle: crear una página, abrir el editor en modo "
            "HTML (`<>`) y pegar el contenido del archivo generado."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
