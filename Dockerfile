# Image de base avec Python
FROM python:3.12-slim

# Dossier de travail dans le conteneur
WORKDIR /app

# Installer les dépendances en premier (meilleur cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code et le modèle
COPY main.py regression.joblib ./

# Port exposé par l'application
EXPOSE 8000

# Lancer le serveur
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]