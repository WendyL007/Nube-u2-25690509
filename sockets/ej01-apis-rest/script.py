import os
import time
import requests
from dotenv import load_dotenv
from tabulate import tabulate

# Cargar variables de entorno
load_dotenv()
WEATHER_KEY = os.getenv("OPENWEATHER_API_KEY", "CLAVE_INVALIDA")

resultados_tabla = []

def ejecutar_peticion(metodo, url, params=None, json_data=None, headers=None):
    """Ejecuta peticiones HTTP y mide tiempo (ms) y bytes transferidos."""
    inicio = time.perf_counter()
    respuesta = requests.request(metodo, url, params=params, json=json_data, headers=headers, timeout=10)
    duracion_ms = (time.perf_counter() - inicio) * 1000
    tamano_bytes = len(respuesta.content)
    
    resultados_tabla.append([
        url[:45] + "..." if len(url) > 48 else url,
        metodo,
        respuesta.status_code,
        f"{duracion_ms:.1f} ms",
        f"{tamano_bytes} B"
    ])
    return respuesta

print("=== 1. JSONPlaceholder ===")
# GET: Listar publicaciones
res_get = ejecutar_peticion("GET", "https://jsonplaceholder.typicode.com/posts")
publicaciones = res_get.json()
print(f"Total de posts recibidos: {len(publicaciones)}")

# POST: Crear publicación[cite: 16, 17]
nuevo_post = {"title": "Prueba de API", "body": "Contenido para el ejercicio", "userId": 1}
res_post = ejecutar_peticion("POST", "https://jsonplaceholder.typicode.com/posts", json_data=nuevo_post)
print(f"Respuesta creación POST ID: {res_post.json().get('id')}\n")


print("=== 2. PokéAPI ===")
# GET: Consultar Pokémon
res_poke = ejecutar_peticion("GET", "https://pokeapi.co/api/v2/pokemon/pikachu")
data_poke = res_poke.json()
habilidades = [a["ability"]["name"] for a in data_poke["abilities"]]
print(f"Nombre: {data_poke['name']} | Altura: {data_poke['height']} | Habilidades: {', '.join(habilidades)}\n")


print("=== 3. OpenWeatherMap ===")
# GET: Pronóstico de Ciudad Valles
url_weather = "https://api.openweathermap.org/data/2.5/weather"
params_weather = {"q": "Ciudad Valles,MX", "appid": WEATHER_KEY, "units": "metric"}
res_weather = ejecutar_peticion("GET", url_weather, params=params_weather)

if res_weather.status_code == 200:
    data_clima = res_weather.json()
    print(f"Clima en Ciudad Valles: {data_clima['weather'][0]['description']}, Temp: {data_clima['main']['temp']}°C\n")
else:
    print(f"Estado de la petición: {res_weather.status_code}\n")


print("=== 4. Errores Provocados ===")
# Error 404: Recurso no existente[cite: 13, 17]
res_404 = ejecutar_peticion("GET", "https://jsonplaceholder.typicode.com/posts/999999")
print(f"Código 404 obtenido: {res_404.status_code}")

# Error 401: No autorizado (API Key errónea)[cite: 13, 17]
res_401 = ejecutar_peticion("GET", url_weather, params={"q": "Ciudad Valles,MX", "appid": "KEY_ERRONEA"})
print(f"Código 401 obtenido: {res_401.status_code}\n")


print("=== TABLA DE REGISTRO DE EVIDENCIA ===")
headers_tabla = ["URL", "Método", "Código", "Tiempo (ms)", "Bytes"]
print(tabulate(resultados_tabla, headers=headers_tabla, tablefmt="github"))