from typing import Optional

from sqlalchemy.orm import Session

from src.db.models import Task


class TaskSelector:
    @staticmethod
    def get_all_tasks(
        db: Session, skip: int = 0, limit: int = 10, q: Optional[str] = None
    ) -> list[type[Task]]:
        if q is None:
            return db.query(Task).offset(skip).limit(limit).all()
        return (
            db.query(Task)
            .filter(Task.title.ilike(f"%{q}%"))
            .offset(skip)
            .limit(limit)
            .all()
        )

    @staticmethod
    def get_task_by_id(db: Session, task_id: int) -> Task | None:
        return db.query(Task).filter(Task.id == task_id).first()
