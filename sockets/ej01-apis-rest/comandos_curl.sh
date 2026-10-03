echo "=== 1. JSONPlaceholder GET ==="
curl -s -w "\nCódigo: %{http_code} | Tiempo: %{time_total}s | Bytes: %{size_download}\n" \
  https://jsonplaceholder.typicode.com/posts/1

echo -e "\n=== 1. JSONPlaceholder POST ==="
curl -s -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "hola", "body": "desde curl", "userId": 1}' \
  -w "\nCódigo: %{http_code} | Tiempo: %{time_total}s | Bytes: %{size_download}\n"

echo -e "\n=== 2. PokéAPI ==="
curl -s -w "\nCódigo: %{http_code} | Tiempo: %{time_total}s | Bytes: %{size_download}\n" \
  https://pokeapi.co/api/v2/pokemon/pikachu

echo -e "\n=== 3. OpenWeatherMap ==="
source sockets/ej01-apis-rest/.env 2>/dev/null || source .env 2>/dev/null
curl -s -w "\nCódigo: %{http_code} | Tiempo: %{time_total}s | Bytes: %{size_download}\n" \
  "https://api.openweathermap.org/data/2.5/weather?q=Ciudad%20Valles,MX&appid=${OPENWEATHER_API_KEY}&units=metric"

echo -e "\n=== 4. Error 404 ==="
curl -s -w "\nCódigo: %{http_code}\n" https://jsonplaceholder.typicode.com/posts/999999

echo -e "\n=== 4. Error 401 ==="
curl -s -w "\nCódigo: %{http_code}\n" "https://api.openweathermap.org/data/2.5/weather?q=Ciudad%20Valles,MX&appid=INVALIDA"