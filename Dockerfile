# Establece la imagen de Docker, utilizará un entorno que tiene Python 3.8
FROM python:3.8

# Copia el archivo requirements.txt a la ruta /webapp/requirements.txt
COPY ./requirements.txt /webapp/requirements.txt

# Establece el directorio de trabajo 
WORKDIR /webapp

# Ejecuta el comando para instalar todas las dependencias
RUN pip install -r requirements.txt

# Copia todos los archivos de la aplicación desde el directorio local webapp al directorio /webapp 
COPY webapp/* /webapp

# Expone el puerto 8080
EXPOSE 8080

#  Establece el punto de entrada para el contenedor
ENTRYPOINT [ "main.py" ]

# indica que el servidor debe estar accesible desde cualquier dirección IP,
# y main:app especifica que uvicorn debe ejecutar la aplicación app definida en el archivo main.py.
CMD [ "python" ]
