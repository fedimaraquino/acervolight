# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que o Django usará
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "biblioteca.wsgi:application"] 