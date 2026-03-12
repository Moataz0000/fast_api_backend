from pydantic import BaseModel, ConfigDict


class TaskCreateSchema(BaseModel):
    title: str
    description: str | None = None


class TaskRetrieveSchema(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)
