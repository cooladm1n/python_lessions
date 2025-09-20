from fastapi.testclient import TestClient
from tasks import app, UserRegistration, BulkDataItem


def test_user_registration():
    client = TestClient(app)
    
    # Test valid registration
    user_data = {
        "username": "alice",
        "email": "alice@example.com",
        "password": "password123",
        "confirm_password": "password123"
    }
    
    response = client.post("/register", json=user_data)
    assert response.status_code == 200
    assert "user_id" in response.json()
    
    # Test invalid registration
    invalid_data = {
        "username": "bob",
        "email": "invalid-email",
        "password": "short",
        "confirm_password": "different"
    }
    
    response = client.post("/register", json=invalid_data)
    assert response.status_code == 422


def test_file_upload():
    client = TestClient(app)
    
    # Test file upload
    files = {"file": ("test.txt", "Hello, World!", "text/plain")}
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    assert "filename" in response.json()


def test_bulk_data_processing():
    client = TestClient(app)
    
    # Test bulk processing
    bulk_data = [
        {"id": 1, "name": "Item 1", "value": 10.5},
        {"id": 2, "name": "Item 2", "value": 20.0}
    ]
    
    response = client.post("/bulk-process", json=bulk_data)
    assert response.status_code == 200
    assert "processed_count" in response.json()


def test_get_user():
    client = TestClient(app)
    
    response = client.get("/users/1")
    assert response.status_code == 200
    assert "user_id" in response.json()


def test_update_user():
    client = TestClient(app)
    
    update_data = {"username": "updated_user"}
    response = client.put("/users/1", json=update_data)
    assert response.status_code == 200
    assert "updated" in response.json()


