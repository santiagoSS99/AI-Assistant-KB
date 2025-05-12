# Soporte IA con Claude

Este proyecto utiliza Claude y RAG para responder preguntas de soporte técnico.

To use this repo please clone using

# 1. Clona el proyecto

git clone https://github.com/santiagoSS99/AI-Assistant-KB.git

# 2. Crea entorno virtual

python -m venv venv
source venv/bin/activate # o .\venv\Scripts\activate en Windows

# 3. Instala dependencias

pip install -r requirements.txt

# 4. Genera embeddings e índice

python src/embed_kb.py

# 5. Inicia el chatbot

python src/chatbot.py
