from pydantic import BaseModel

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