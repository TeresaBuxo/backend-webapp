from pydantic import BaseModel
from typing import Optional
import datetime as dt

class Project(BaseModel):
    project_id: Optional[int]
    project_name: str
    link: Optional[str]
    description: Optional[str]
    image: Optional[str]
    user_id: Optional[int]
