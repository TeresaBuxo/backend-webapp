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
    user_id:int
    first_name:Optional[str]
    last_name1:Optional[str]
    last_name2:Optional[str] 
    role:Optional[str]
    email:str
    hashed_password:str
    phone_number:Optional[str]
    activation_date:dt.date
    active:bool
    deactivation_date:Optional[dt.date]
    verified: bool
    visible: bool
    storage_path: Optional[str]

    class Config:
        from_attributes = True
        json_encoders = {
            dt.date: lambda v: v.isoformat()
        }

class TokenData(BaseModel):
    user_id:int



    

