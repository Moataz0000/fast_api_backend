from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreateSchema(TaskBase):
    pass


class TaskRetrieveSchema(TaskBase):
    id: int
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)
