#!/bin/bash

# Script de despliegue rápido para ai-shockpredictor
echo "🚀 Iniciando despliegue de ai-shockpredictor..."

# 1. Inicializar Git si no existe
if [ ! -d ".git" ]; then
    git init
    echo "✅ Repositorio Git inicializado."
fi

# 2. Añadir archivos
git add .

# 3. Commit inicial
git commit -m "Initial MVP: LSTM + CryptoQuant + Telegram Bot + Paywall"

# 4. Instrucciones para el usuario
echo "------------------------------------------------"
echo "¡Listo para subir! Ejecuta los siguientes comandos:"
echo "1. gh repo create ai-shockpredictor --public --source=. --remote=origin"
echo "2. git push -u origin main"
echo "------------------------------------------------"
