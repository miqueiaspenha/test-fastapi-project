from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_users():
    reponse = client.get('/users')
    assert reponse.status_code == 200
    assert isinstance(reponse.json(), list)

def test_get_valid_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "user" in response.json()

def test_get_invalid_user():
    response = client.get("/users/999")
    assert response.status_code == 200
    assert "error" in response.json()