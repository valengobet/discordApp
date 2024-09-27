import requests
import json

api_url = 'https://ws1.smn.gob.ar/v1/forecast/location/4864'


# Verifica el código de estado de la respuesta
if response.status_code == 200:
    # Imprime la respuesta en formato JSON
    print(response.json())
else:
    # Imprime el código de estado y el contenido de la respuesta en caso de error
    print(f"Error {response.status_code}: {response.text}")