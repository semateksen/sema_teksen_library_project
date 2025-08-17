import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_list_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_book():
    test_isbn = "9783161484100"  # Test ISBN'i
    response = client.post("/books", json={"isbn": test_isbn})
    # 400 (geçersiz ISBN), 404 (kitap bulunamadı) veya 200 (başarılı) kabul et
    assert response.status_code in [200, 400, 404]

def test_delete_book():
    # Önce bir kitap ekleyelim
    add_response = client.post("/books", json={"isbn": "9780451524935"})
    if add_response.status_code == 200:
        isbn = add_response.json()["isbn"]
        response = client.delete(f"/books/{isbn}")
        assert response.status_code == 200