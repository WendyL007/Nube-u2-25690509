# Ejercicio 1 Portafolio: Consumir APIs REST Públicas

## 1. Tabla de Registro de Evidencia

| URL / Endpoint | Método | Código | Tiempo (ms) | Tamaño (Bytes) |
| :--- | :---: | :---: | :---: | :---: |
| `https://jsonplaceholder.typicode.com/posts` | GET | 200 | 210 ms | 27,520 B |
| `https://jsonplaceholder.typicode.com/posts` | POST | 201 | 185 ms | 65 B |
| `https://pokeapi.co/api/v2/pokemon/pikachu` | GET | 200 | 303 ms | 300,521 B |
| `https://api.openweathermap.org/data/2.5/weather?q=Ciudad...` | GET | 200 | 150 ms | 480 B |
| `https://jsonplaceholder.typicode.com/posts/999999` | GET | 404 | 120 ms | 2 B |
| `https://api.openweathermap.org/data/2.5/weather?appid=INVALIDA` | GET | 401 | 115 ms | 108 B |

---

## 2. Documentación de Errores Provocados

* **Error 404 (Not Found):** Se solicitó el recurso `/posts/999999` en JSONPlaceholder. La API respondió con código `404` indicando que la publicación no existe.
* **Error 401 (Unauthorized):** Se realizó una petición a OpenWeatherMap utilizando una API Key inválida (`appid=INVALIDA`). La API respondió con código `401` denegando el acceso por falta de autenticación válida.

---

## 3. Pregunta de Reflexión

### ¿Qué parte de la respuesta realmente usaste?
* **PokéAPI:** De la respuesta completa en JSON, únicamente se procesaron los campos `name`, `height` y la lista de nombres de `abilities`.
* **OpenWeatherMap:** Solamente se tomaron los datos de `weather[0].description` y `main.temp`.

### ¿Qué porcentaje de los bytes recibidos fue innecesario?
En la consulta a PokéAPI, la carga útil recibida fue de aproximadamente **300.5 KB** (300,521 bytes). La información utilizada en el script apenas representa unos **100 bytes**.

Esto significa que **más del 99.9% de los bytes recibidos fueron innecesarios** para la tarea. Este resultado evidencia el problema de sobre-descarga de datos característico de la arquitectura REST tradicional.