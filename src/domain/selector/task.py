from sqlalchemy.orm import Session

from src.db.models import Task


class TaskSelector:
    @staticmethod
    def get_all_tasks(db: Session, skip: int = 0, limit: int = 10):
        return db.query(Task).offset(skip).limit(limit).all()

    @staticmethod
    def get_task_by_id(db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()
