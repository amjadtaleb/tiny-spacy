from fastapi import FastAPI, Request
import spacy


nlp = spacy.load("en_core_web_md")

app = FastAPI()


@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    text = data.get("text", "")
    return nlp(text).to_json()


@app.get("/health")
def health():
    return {"status": "ok"}
