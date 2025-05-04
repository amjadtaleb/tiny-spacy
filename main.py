from fastapi import FastAPI, Request
import spacy

nlp = None

app = FastAPI()


@app.post("/analyze")
async def analyze(request: Request):
    global nlp
    if nlp is None:
        nlp = spacy.load("en_core_web_md")
    data = await request.json()
    text = data.get("text", "")
    return nlp(text).to_json()


@app.get("/health")
def health():
    return {"status": "ok"}
