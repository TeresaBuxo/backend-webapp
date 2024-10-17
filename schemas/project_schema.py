from pydantic import BaseModel
from typing import Optional
import datetime as dt

class Project(BaseModel):
    project_id: Optional[int]
    project_name: str
    link: Optional[str]
    description: Optional[str]
    image: Optional[str]

    class Config:
        from_attributes = True


class CreateProject(BaseModel):
    project_name: str


class User_Project(BaseModel):
    __tablename__= 'users_projects'
    rel_up_id:int
    user_id:int
    org_id:int
    member_type: Optional[str]