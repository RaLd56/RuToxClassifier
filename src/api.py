from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post('/predict')
def predict_toxicity(input: InputText):
    label = predict(input.text)
    return {"label": label}