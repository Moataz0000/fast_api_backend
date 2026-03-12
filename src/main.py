from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from .db.database import Base, SessionLocal, engine
from .domain.selector.task import TaskSelector
from .domain.service.task import TaskService
from .schema import TaskCreateSchema, TaskRetrieveSchema

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Todo Task Backend", version="1", description="This is a todo task api."
)


def get_db():
    """creates a new session for each request and closes it after"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def health_check():
    return {"Health": "Ok 200"}


@app.post("/task/create/", response_model=TaskRetrieveSchema)
async def create_task(task: TaskCreateSchema, db: Session = Depends(get_db)):
    return TaskService.create_task(db, task)


@app.get("/tasks/", response_model=List[TaskRetrieveSchema])
async def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = TaskSelector.get_all_tasks(db, skip, limit)
    return tasks


@app.get("/tasks/{task_id}/detail/", response_model=TaskRetrieveSchema)
async def get_task_detail(task_id: int, db: Session = Depends(get_db)):
    task_detail = TaskSelector.get_task_by_id(db, task_id)
    if not task_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with this '{task_id}' is not found!",
        )
    return task_detail


@app.delete("/task/{task_id}/delete/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_view(task_id: int, db: Session = Depends(get_db)):
    task = TaskSelector.get_task_by_id(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with this '{task_id}' is not found!",
        )
    TaskService.delete_task(db, task)
