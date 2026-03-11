from typing import List

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db.database import Base, SessionLocal, engine
from .db.models import Task
from .schema import TaskCreateSchema, TaskRetrieveSchema

Base.metadata.create_all(bind=engine)


app = FastAPI()


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
def create_task(task: TaskCreateSchema, db: Session = Depends(get_db)):
    db_task = Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=List[TaskRetrieveSchema])
def get_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks
