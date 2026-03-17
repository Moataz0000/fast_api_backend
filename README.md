# Todo Task API

A modern CRUD backend for managing tasks, built with FastAPI and SQLite.

## Run with Docker

1. Pull or clone the repository
   ```bash
   git clone https://github.com/Moataz0000/fast_api_backend.git
   cd FastAPI
   ```

2. Build the image
   ```bash
   docker build -t fastapi-todo .
   ```

3. Run the container
   ```bash
   docker run -p 8000:8000 fastapi-todo
   ```

4. Open http://localhost:8000/docs to see the interactive API docs

## API Endpoints

| Method   | Endpoint                     | Description                                    | Query Parameters      |
| -------- | ---------------------------- | ---------------------------------------------- | --------------------- |
| `GET`    | `/`                          | Health check to verify API is running          | —                     |
| `POST`   | `/tasks/create/`             | Create a new task with title and description   | —                     |
| `GET`    | `/tasks/`                    | Retrieve all tasks with pagination and search support | `skip`, `limit`, `q`  |
| `GET`    | `/tasks/{task_id}/detail/`   | Fetch a single task by its unique ID           | —                     |
| `PUT`    | `/tasks/{task_id}/update/`   | Update task details (title, description, status) | —                     |
| `DELETE` | `/tasks/{task_id}/delete/`   | Remove a task permanently by ID                | —                     |
