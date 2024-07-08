# Usar una imagen base de Python
FROM python:3.9-slim

# Copia el archivo requirements.txt a la ruta /app/requirements.txt
COPY ./requirements.txt /app/requirements.txt

# Copia todos los archivos de la aplicación desde el directorio local webapp al directorio /app 
COPY app/* /app

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
