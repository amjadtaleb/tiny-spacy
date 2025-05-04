Build
```sh
docker build -t spacy-server .
```

Run
```sh
docker compose up
```

Usage
```sh
curl --request POST \
  --url http://localhost:8000/analyze \
  --header 'content-type: application/json' \
  --data '{
"text": "Tokenize this"
}'
```
