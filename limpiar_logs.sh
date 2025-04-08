daw# Elimina archivos .log de más de 7 días
find "$LOG_DIR" -name "*.log" -type f -mtime +7 -exec rm -f {} \;

echo "Logs eliminados correctamente en $LOG_DIR"#!/bin/bash

LOG_DIR="/var/log/mi_aplicacion"

# Crea el directorio si no existe (opcional)
mkdir -p "$LOG_DIR"

# Elimina archivos .log de más de 7 días
find "$LOG_DIR" -name "*.log" -type f -mtime +7 -exec rm -f {} \;

echo "$(date '+%Y-%m-%d %H:%M:%S') - Limpieza completada" >> /home/ubuntu/registro_limpieza.txt

