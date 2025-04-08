#!/bin/bash

# Ruta del proyecto
PROYECTO_DIR="$HOME/mi_proyecto_python"
cd "$PROYECTO_DIR"

# Crea entorno virtual si no existe
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activa el entorno virtual
source venv/bin/activate

# Instala dependencias
pip install -r requirements.txt

echo "Dependencias instaladas correctamente."
