FROM python:3.11-slim

# Instalamos utilidades básicas que Reflex necesita para descargar Node.js/Next.js
RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Optimizamos la instalación de dependencias
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código
COPY . .

# Quitamos --frontend-only para que levante TANTO el puerto 3000 como el 8000
CMD reflex run --env prod
