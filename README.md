# Proyecto DevOps

Este repositorio contiene scripts de automatización para servidores Linux, utilizados en prácticas de configuración en AWS CloudShell y EC2.

## Contenido

- `instalar_basicos.sh`: instala paquetes esenciales (`git`, `vim`, `docker`, `python3`)
- `instalar_dependencias.sh`: instala dependencias de Python desde `requirements.txt`
- `limpiar_logs.sh`: limpia archivos `.log` antiguos con `cron`
- `setup.sh`: script general para configuración inicial

## Cómo usar

```bash
chmod +x instalar_basicos.sh
./instalar_basicos.sh

