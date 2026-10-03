curl -s https://jsonplaceholder.typicode.com/posts/1
curl -s -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title": "hola", "body": "desde curl", "userId": 1}'