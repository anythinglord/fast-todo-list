from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    description: str
    # With a default value will be optional in the JSON
    completed: bool = False

    # connfig optional, example in OpenAPI
    class Config:
        schema_extra = {
            "example": {
                "title": "Buy games",
                "description": "simple rts on steam",
                "completed": False
            }
        }

class TaskPatch(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    # With a default value will be optional in the JSON
    completed: Optional[bool] = False