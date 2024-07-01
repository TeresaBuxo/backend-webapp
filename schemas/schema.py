from pydantic import BaseModel
from typing import Optional
import datetime as dt

class User(BaseModel):
    user_id:Optional[int]
    first_name:str
    last_name1:str 
    last_name2:Optional[str] 
    role:Optional[str]
    email:Optional[str]
    phone_number:Optional[str]
    activation_date:Optional[dt.date]
    active:Optional[bool]
    deactivation_date:Optional[dt.date]
    institution_id:Optional[int]
    latitude:float
    longitude:float

    class Config:
        from_attributes = True

class UserCreate(User):
    first_name:str
    last_name1:str 


    

