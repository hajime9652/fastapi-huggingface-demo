from pydantic import BaseModel

class Message(BaseModel):
    input: str
    output: str = None