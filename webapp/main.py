"""
Este código define una API web que permite a los usuarios generar
texto utilizando el modelo GPT-2 de Hugging Face. La API tiene dos rutas: una
que devuelve un mensaje HTML simple y otra que genera texto basado en una
entrada proporcionada en una solicitud POST.
"""

# Importar librerias
"""
- pipeline de transformers: Se utiliza para crear un pipeline de generación
de texto con un modelo específico
- FastAPI y Response de fastapi: FastAPI es un framework para
construir APIs web rápidamente. Response se usa para devolver respuestas HTTP
personalizadas
- BaseModel de pydantic: Se usa para definir modelos de datos que validan
la entrada a las rutas de la API
"""
from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel

# Crea un pipeline de generación de texto
generator = pipeline('text-generation', model='gpt2')

# Se crea una instancia de la aplicación FastAPI llamada app
app = FastAPI()

# Esta clase se utiliza para validar los datos de entrada en las solicitudes POST
class Body(BaseModel):
    text: str
    
# Se define una ruta raíz '/' que devuelve una respuesta HTML simple.
# Esta ruta responde a las solicitudes GET con un mensaje de bienvenida.
@app.get('/')
def root():
    return Response("<h1>API autodocumentada que utiliza el marco FastAPI</h1>")
    
"""
- Se define una ruta POST '/generate' que toma un objeto Body como entrada
- La función predict utiliza el generator para generar texto basado en el body.text proporcionado,
con una longitud máxima de 35 caracteres y una secuencia de retorno.
- Devuelve el primer resultado generado.
"""
@app.post('/generate')
def predict(body: Body):
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
