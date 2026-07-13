# Image de base legere avec Python
FROM python:3.12-slim

# Repertoire de travail dans le conteneur
WORKDIR /app

# Installer les dependances (mise en cache si requirements ne change pas)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du projet
COPY . .

# Port expose par l'application Flask
EXPOSE 5000

# Commande de demarrage du conteneur
CMD ["python", "app.py"]
