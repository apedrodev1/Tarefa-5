# Usar uma imagem base do Python
FROM python:3.8

# Definir a pasta de trabalho no contêiner
WORKDIR /app

# Instalar o Flask
RUN pip install Flask

# Copiar o script do Flask para o contêiner
COPY ./app.py ./app.py

# Executar o app.py quando o contêiner iniciar
CMD ["python", "app.py"]
