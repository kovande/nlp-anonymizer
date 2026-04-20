# src/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from .anonymizer import anonymize_spacy

app = FastAPI(title="NLP Anonymizer API")

class TextRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(request: TextRequest):
    anonymized = anonymize_spacy(request.text)
    return {"anonymized_text": anonymized}