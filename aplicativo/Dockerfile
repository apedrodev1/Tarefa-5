# Use uma imagem base do Python
FROM python:3.8

# Definir a pasta de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de requisitos e instalar as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o projeto para a pasta de trabalho
COPY . .

# Executar o app.py quando o contêiner iniciar
CMD ["python", "app.py"]
