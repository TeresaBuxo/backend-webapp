from pydantic import BaseModel
from typing import Optional
import datetime as dt

class Question(BaseModel):
    question_id: int
    title: str
    question: Optional[str]
    file_link: Optional[str]
    created_by: int
    deleted: bool

    class Config:
        from_attributes = True

