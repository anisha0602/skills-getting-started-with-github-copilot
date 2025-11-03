from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Mergington High School" in response.text

def test_signup():
    response = client.post("/activities/soccer/signup", params={"email": "test@example.com"})
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up test@example.com for soccer"

def test_fetch_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)