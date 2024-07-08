# Usar una imagen base de Python
FROM python:3.9-slim

# Copia el archivo requirements.txt a la ruta /app/requirements.txt del contenedor
COPY ./requirements.txt /app/requirements.txt

# Copia todos los archivos de la aplicación desde el directorio local app al directorio /app del contenedor
COPY app/* /app

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación, se ejecuta cuando se inicia el contenedor
# "uvicorn": Usado para servir la aplicación FastAPI
# "main:app": Le dice a Uvicorn dónde encontrar la aplicación FastAP
  # main se refiere al archivo main.py
  # app se refiere a la instancia de la aplicación FastAPI dentro de main.py (app = FastAPI())
# "--host": Especifica la dirección IP en la que Uvicorn debe escuchar
# "0.0.0.0": Indica que el servidor debe aceptar conexiones desde cualquier IP
# "--port": especifica el puerto en el que Uvicorn debe escuchar
# 80 es el puerto estándar para el tráfico HTTP, lo que significa que la aplicación será accesible en el puerto 80 del contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
