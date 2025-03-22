from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_prediction_valid():
    response = client.post("/prediction", json={"data": "Sample test text!"})
    assert response.status_code == 200
    assert "predictions" in response.json()
    assert isinstance(response.json()["predictions"], list)
