from pydantic import BaseModel

class ToolInput(BaseModel):
    query: str
