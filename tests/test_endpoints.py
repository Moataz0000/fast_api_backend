from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_get_tasks_endpoint():
    response = client.get("/tasks/")
    assert response.status_code == 200


def test_create_task_endpoint():
    mock_data = {"title": "Test Task", "description": "This is a test task."}

    response = client.post("/tasks/create/", json=mock_data)

    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Test Task"
    assert body["description"] == "This is a test task."
    assert "id" in body
    assert "is_completed" in body


def test_delete_task():
    mock_data = {"title": "Task to delete", "description": "Will be deleted"}
    create_response = client.post("/tasks/create/", json=mock_data)
    task_id = create_response.json()["id"]

    delete_response = client.delete(f"/tasks/{task_id}/delete/")
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    get_response = client.get(f"/tasks/{task_id}/detail/")
    assert get_response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_task_not_found():
    response = client.delete("/tasks/99999/delete/")
    assert response.status_code == status.HTTP_404_NOT_FOUND
