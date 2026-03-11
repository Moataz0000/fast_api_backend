from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreateSchema(TaskBase):
    pass


class TaskRetrieveSchema(TaskBase):
    id: int
    is_completed: bool

    class Config:
        from_attributes = True
