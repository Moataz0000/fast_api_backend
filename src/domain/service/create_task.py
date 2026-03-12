from sqlalchemy.orm import Session

from db.models import Task
from schema import TaskCreateSchema


class TaskService:
    @staticmethod
    def create_task(db: Session, task_data: TaskCreateSchema):
        db_task = Task(title=task_data.title, description=task_data.description)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
