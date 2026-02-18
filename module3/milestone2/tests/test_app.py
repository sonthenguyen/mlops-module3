from fastapi.testclient import TestClient

# Import the FastAPI app object from app/app.py
from app.app import app

client = TestClient(app)

def test_health_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_predict_ok():
    r = client.post("/predict", json={"value": 5})
    assert r.status_code == 200
    body = r.json()
    assert "prediction" in body
    assert body["prediction"] == 11  # 2*5 + 1

def test_predict_rejects_bad_input():
    r = client.post("/predict", json={"wrong_key": 123})
    # FastAPI validation error
    assert r.status_code == 422