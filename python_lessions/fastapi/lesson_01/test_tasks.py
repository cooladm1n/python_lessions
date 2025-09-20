from fastapi.testclient import TestClient
from tasks import create_app


def test_health():
    app = create_app()
    client = TestClient(app)
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_items_crud():
    app = create_app()
    client = TestClient(app)
    # create
    r = client.post("/items", json={"name": "Book", "price": 12.5})
    assert r.status_code == 200
    item = r.json()
    assert item["id"] == 1
    # read
    r = client.get("/items/1")
    assert r.status_code == 200
    assert r.json()["name"] == "Book"
    # not found
    r = client.get("/items/999")
    assert r.status_code == 404
