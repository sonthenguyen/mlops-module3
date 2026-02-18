from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="ML Service", version="0.1.0")

class PredictRequest(BaseModel):
    value: float = Field(..., description="A numeric input")

class PredictResponse(BaseModel):
    prediction: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    # Minimal “model” logic (placeholder for real model)
    y = 2 * req.value + 1
    return {"prediction": y}