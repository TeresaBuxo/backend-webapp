from pydantic import BaseModel
from typing import Optional
import datetime as dt

class UserCreate(BaseModel):
    email:str
    password:str

    class Config:
        from_attributes = True
        json_encoders = {
            dt.date: lambda v: v.isoformat()
        }

class User(BaseModel):
    user_id:Optional[int]
    first_name:Optional[str]
    last_name1:Optional[str]
    last_name2:Optional[str] 
    role:Optional[str]
    email:str
    hashed_password:str
    phone_number:Optional[str]
    image:Optional[str]
    activation_date:Optional[dt.date]
    active:Optional[bool]
    deactivation_date:Optional[dt.date]
    member_of:Optional[int]

    class Config:
        from_attributes = True
        json_encoders = {
            dt.date: lambda v: v.isoformat()
        }

class TokenData(BaseModel):
    user_id:int



    

