from pydantic import BaseModel
from typing import Optional
import datetime as dt


class UserBase(BaseModel):
    user_id:Optional[int]
    first_name:Optional[str]
    last_name1:Optional[str]
    last_name2:Optional[str] 
    role:Optional[str]
    email:str
    hashed_password:str
    phone_number:Optional[str]
    activation_date:Optional[dt.date]
    active:Optional[bool]
    deactivation_date:Optional[dt.date]
    #institution_id:Optional[int]
    latitude:Optional[float]
    longitude:Optional[float]

    class Config:
        from_attributes = True
        json_encoders = {
            dt.date: lambda v: v.isoformat()
        }

class UserCreate(UserBase):
    email: str
    hashed_password: str
    activation_date: dt.date

class User(UserBase):
    user_id:Optional[int]

    class Config:
        from_attributes = True

class UserAuth(UserBase):
    email:str
    hashed_password:str



    

