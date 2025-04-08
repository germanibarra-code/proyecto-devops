#!/bin/bash

# Actualiza el sistema
sudo apt update && sudo apt upgrade -y

# Instala los paquetes esenciales
sudo apt install -y git vim docker.io python3 python3-pip

# Habilita e inicia Docker
sudo systemctl enable docker
sudo systemctl start docker

# Verifica versiones instaladas
echo "Versiones instaladas:"
git --version
vim --version | head -n 1
docker --version
python3 --version
