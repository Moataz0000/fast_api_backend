from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_tasks_endpoint():
    response = client.get("/tasks/")
    assert response.status_code == 200


def test_create_task_endpoint():
    mock_data = {"title": "Test Task", "description": "This is a test task."}

    response = client.post("/task/create/", json=mock_data)

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Test Task"
    assert body["description"] == "This is a test task."
    assert "id" in body
    assert "is_completed" in body
