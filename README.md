Build
```sh
docker build -t spacy-server .
```

Run
```sh
docker run --rm -p 8000:8000 -v .:/app spacy-server:latest
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
