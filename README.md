# FastAPI, Practica de despliegue de una app

## 📌 Objetivo de la practica

* Hacer uso del marco web FastAPI para desplegar un servicio
* Desplegar de forma sencilla un servicio que use el modelo GPT-2 para generar texto a partir de una entrada (texto inicial)
* Hacer uso del Uvicorn para implementar un servidor web ASGI

## 📚 Conceptos básicos

### 💡 ¿Qué es una API?

Una API, o Interfaz de Programación de Aplicaciones (Application Programming Interface, en inglés), es un conjunto de reglas, protocolos y herramientas que permiten a diferentes aplicaciones de software comunicarse entre sí. En esencia, una API especifica cómo interactuar con un software o servicio, proporcionando una serie de métodos, funciones y datos que otros programas pueden utilizar para realizar ciertas acciones o acceder a recursos específicos.


### 💡 ¿Qué es FastAPI?

FastAPI es un marco de desarrollo web de Python de alto rendimiento y fácil de usar para crear APIs web rápidas. Está construido sobre las capacidades de Starlette y Pydantic, lo que lo hace rápido, fácil de escribir y mantener, y altamente eficiente en el uso de recursos. FastAPI utiliza la tipificación de Python para proporcionar una documentación automática y precisa, así como una validación de datos, lo que hace que el desarrollo de APIs sea más rápido y seguro. Además, soporta la generación automática de documentación interactiva basada en el estándar OpenAPI y Swagger UI.

### 💡 ¿Qué es Uvicorn?

Uvicorn es un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento para aplicaciones web Python. Es ampliamente utilizado en el ecosistema de desarrollo web de Python, especialmente con marcos como FastAPI, Starlette y otros que admiten ASGI.

Uvicorn se destaca por su capacidad para manejar conexiones de red de forma asíncrona, lo que significa que puede manejar muchas solicitudes simultáneamente sin bloquear el hilo principal de ejecución. Esto lo hace ideal para aplicaciones web modernas que necesitan manejar un alto volumen de tráfico de manera eficiente.

Además de su rendimiento, Uvicorn es conocido por su facilidad de uso y su integración perfecta con otros componentes del ecosistema de Python, como asyncio y el ecosistema de herramientas de desarrollo web como FastAPI, lo que lo convierte en una opción popular para implementar aplicaciones web modernas y escalables.


