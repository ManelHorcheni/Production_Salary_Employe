# Utilise une image officielle avec Python
FROM python:3.10-slim

# Crée un répertoire dans le conteneur
WORKDIR /app

# Copie le contenu du projet dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Expose le port Streamlit
EXPOSE 8501

# Commande pour lancer l'application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
