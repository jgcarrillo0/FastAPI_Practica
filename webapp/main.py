# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:08:25 2024

@author: jgcar

Este código define una API web que permite a los usuarios generar texto
utilizando el modelo GPT-2 de Hugging Face. La API tiene una ruta que genera
texto basado en una entrada proporcionada en una solicitud POST.
"""

################################################################################
# Importar librerias

from transformers import pipeline
from fastapi import FastAPI
from starlette.responses import RedirectResponse
from pydantic import BaseModel

"""
-pipeline de transformers: Se utiliza para crear un pipeline de generación
de texto con un modelo específico.

-FastAPI: se utiliza para crear aplicaciones web y APIs rápidas y eficientes
en Python.

-RedirectResponse de Starlette: Permite redirigir a los usuarios a una URL
diferente en una aplicación web.

- BaseModel de pydantic: Se usa para definir modelos de datos que validan
la entrada a las rutas de la API.
"""

################################################################################
# Modelo gpt

# Crea un pipeline de generación de texto
generator = pipeline('text-generation', model='gpt2')

################################################################################
# Aplicación

# Se crea una instancia de la aplicación FastAPI llamada app
app = FastAPI()

# Se utiliza para validar los datos de entrada en las solicitudes POST
class Body(BaseModel):
    """
    Representa una estructura de datos con un único atributo 'texto'
    de tipo str.
    
    Attributes:
    ----------
    text : str
        El contenido textual almacenado en el cuerpo.
    """
    text: str

# Se define una ruta raíz '/' para la aplicación FastAPI @app.get('/'). 
@app.get('/')
def root():
    """
    Redirige al usuario a la URL '/docs/'.

    Returns
    -------
    RedirectResponse :
        Redirecciona a la URL '/docs/'.
    """
    return RedirectResponse(url="/docs/")

# Se define una ruta POST '/generate' que toma un objeto Body como entrada
@app.post('/generate')
def predict(body: Body):
    """
    Genera una predicción basada en el texto de entrada utilizando un modelo
    de generación de texto.
    
    Parameters
    ----------
    body : Body
        Una instancia de la clase Body que contiene el texto de entrada.

    Returns
    -------
    results : str
        La predicción del texto generado.
    """
    results = generator(body.text, max_length=35, num_return_sequences=1)
    return results[0]
