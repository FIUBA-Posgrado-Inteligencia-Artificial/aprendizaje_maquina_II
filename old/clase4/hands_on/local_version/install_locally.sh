#!/bin/bash
set -e

# ------------------------------------------------------
# Configuración inicial
# ------------------------------------------------------

AIRFLOW_VERSION="3.0.2"
export AIRFLOW_HOME=~/airflow

AIRFLOW_CFG_SOURCE="$(pwd)/conf/airflow.cfg"
AIRFLOW_CFG_DEST="${AIRFLOW_HOME}/airflow.cfg"

PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

REQUIREMENTS_FILE="requirements.txt"

echo "Apache Airflow ${AIRFLOW_VERSION} - Instalador"
echo "🐍 Python version detectada: ${PYTHON_VERSION}"
echo

# ------------------------------------------------------
# Elegir método de instalación
# ------------------------------------------------------

echo "Seleccioná el método de instalación:"
echo "1) uv"
echo "2) pipx"
echo "3) venv (entorno virtual local)"
read -rp "Opción [1-3]: " OPTION

case "$OPTION" in
  1)
    echo "🔧 Instalando con uv..."
    uv pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
    if [[ -f "$REQUIREMENTS_FILE" ]]; then
      echo "📦 Instalando dependencias desde $REQUIREMENTS_FILE con uv..."
      uv pip install -r "$REQUIREMENTS_FILE"
    fi
    ;;
  2)
    echo "🔧 Instalando con pipx..."
    pipx install "apache-airflow==${AIRFLOW_VERSION}" --pip-args="--constraint ${CONSTRAINT_URL}"
    if [[ -f "$REQUIREMENTS_FILE" ]]; then
      echo "📦 Instalando dependencias desde $REQUIREMENTS_FILE con pipx inject..."
      pipx inject apache-airflow -r "$REQUIREMENTS_FILE"
    fi
    ;;
  3)
    echo "🔧 Instalando con entorno virtual (venv)..."
    VENV_DIR=".venv_airflow"
    python -m venv "${VENV_DIR}"
    source "${VENV_DIR}/bin/activate"
    pip install --upgrade pip
    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
    
    if [[ -f "$REQUIREMENTS_FILE" ]]; then
      echo "📦 Instalando dependencias desde $REQUIREMENTS_FILE en venv..."
      pip install -r "$REQUIREMENTS_FILE"
    fi
    echo "✅ Entorno virtual activado: ejecutá 'source ${VENV_DIR}/bin/activate' para usar Airflow"
    ;;
  *)
    echo "❌ Opción inválida. Abortando."
    exit 1
    ;;
esac

# ------------------------------------------------------
# Crear AIRFLOW_HOME si no existe
# ------------------------------------------------------

if [[ ! -d "$AIRFLOW_HOME" ]]; then
  echo "📁 Creando AIRFLOW_HOME en: $AIRFLOW_HOME"
  mkdir -p "$AIRFLOW_HOME"
else
  echo "✅ AIRFLOW_HOME ya existe: $AIRFLOW_HOME"
fi

if [[ ! -d "${AIRFLOW_HOME}/dags" ]]; then
  echo "📁 Creando dags en: $AIRFLOW_HOME"
  mkdir -p "${AIRFLOW_HOME}/dags"
  cp -r ./dags/* "${AIRFLOW_HOME}/dags/"
else
  echo "✅ dags ya existe en $AIRFLOW_HOME"
fi

AIRFLOW_HOME_ABS="$(cd "$AIRFLOW_HOME"; pwd)"

if [[ -f "$AIRFLOW_CFG_DEST" ]]; then
  echo "⚠️ Ya existe un archivo 'airflow.cfg' en $AIRFLOW_HOME. Se omite la copia y modificación."
elif [[ -f "$AIRFLOW_CFG_SOURCE" ]]; then
  echo "📄 Copiando configuración airflow.cfg desde 'conf/' a $AIRFLOW_HOME"
  cp "$AIRFLOW_CFG_SOURCE" "$AIRFLOW_CFG_DEST"

  echo "📝 Agregando configuración personalizada al final de airflow.cfg"

  cat <<EOF >> "$AIRFLOW_CFG_DEST"

# Configuración personalizada agregada por el instalador
plugins_folder = ${AIRFLOW_HOME_ABS}/plugins
sql_alchemy_conn = sqlite:///${AIRFLOW_HOME_ABS}/airflow.db
base_log_folder = ${AIRFLOW_HOME_ABS}/logs
dag_processor_child_process_log_directory = ${AIRFLOW_HOME_ABS}/logs/dag_processor
dags_folder = ${AIRFLOW_HOME_ABS}/dags
EOF
else
  echo "⚠️ No se encontró el archivo 'conf/airflow.cfg'. Se salta la copia."
fi

echo
echo "✅ Instalación completada correctamente."
echo "📂 AIRFLOW_HOME está configurado en: $AIRFLOW_HOME"
