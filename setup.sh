#!/usr/bin/env bash
set -e
echo "🚀 Configurando entorno..."
command -v python3 >/dev/null 2>&1 || { echo "❌ Python3 requerido"; exit 1; }
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
[ ! -f .env ] && cp .env.example .env && echo "⚠️ Configura .env con tu QWEN_API_KEY"
echo "✅ Listo. Ejecuta: source venv/bin/activate && uvicorn main:app --reload"
