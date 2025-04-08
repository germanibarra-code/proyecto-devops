#!/bin/bash

sudo apt update && sudo apt upgrade -y

# Instalar paquetes esenciales
sudo apt install -y git vim docker.io python3 python3-pip

# Habilitar e iniciar Docker
sudo systemctl enable docker
sudo systemctl start docker

# Agregar usuario ubuntu al grupo docker
sudo usermod -aG docker ubuntu
