from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/users/", json={"name": "John Doe", "email": "john@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }

def test_get_user():
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }

def test_get_user_not_found():
    response = client.get("/api/v1/users/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found in PostgreSQL"}