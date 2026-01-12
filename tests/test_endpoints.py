import requests


def test_get_all_books():
    response = requests.get(url="http://localhost:8000/api/book/list")

    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "author" in data
