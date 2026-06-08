from pydantic import BaseModel

class Message(BaseModel):
    phone: str
    text: str
