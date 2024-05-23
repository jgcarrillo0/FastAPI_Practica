# Establece la imagen de Docker, utilizará un entorno que tiene Python 3.8
FROM python:3.8

# Copia el archivo requirements.txt a la ruta /webapp/requirements.txt
COPY ./requirements.txt /webapp/requirements.txt

# Copia todos los archivos de la aplicación desde el directorio local webapp al directorio /webapp 
COPY webapp/* /webapp

# Establece el directorio de trabajo 
WORKDIR /webapp

# Ejecuta el comando para instalar todas las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 8080
EXPOSE 8080

CMD [ "main.py" ]

#  Establece el punto de entrada para el contenedor
ENTRYPOINT [ "python"]


