from sqlalchemy.orm import Session

from src.db.models import Task
from src.schema import TaskCreateSchema


class TaskService:
    @staticmethod
    def create_task(db: Session, task_data: TaskCreateSchema) -> Task:
        db_task = Task(title=task_data.title, description=task_data.description)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def delete_task(db: Session, task: Task) -> None:
        db.delete(task)
        db.commit()
