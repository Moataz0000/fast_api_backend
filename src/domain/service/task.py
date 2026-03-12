from sqlalchemy.orm import Session

from src.db.models import Task
from src.schema import TaskCreateSchema, TaskUpdateSchema


class TaskService:
    @staticmethod
    def create_task(db: Session, task_data: TaskCreateSchema) -> Task:
        db_task = Task(title=task_data.title, description=task_data.description)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def update_task(
        db: Session, task_id: int, task_data: TaskUpdateSchema
    ) -> Task | None:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        # exclude_unset=True: ensures only the fields the client actually sent get updated
        for field, value in task_data.model_dump(exclude_unset=True).items():
            setattr(task, field, value)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db: Session, task: Task) -> None:
        db.delete(task)
        db.commit()
