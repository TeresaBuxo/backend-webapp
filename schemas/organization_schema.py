from pydantic import BaseModel
from typing import Optional
import datetime as dt

class Organization(BaseModel):
    __tablename__='organizations'
    org_id: int
    org_name: str
    org_type: str
    address: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    logo: Optional[str]
    web_link: Optional[str]
    activation_date: dt.date
    active: bool
    verified: bool
    visible: bool
    storage_path: Optional[str]

    class Config:
        from_attributes = True
        json_encoders = {
            dt.date: lambda v: v.isoformat()
        }


class User_Org(BaseModel):
    __tablename__= 'users_orgs'
    rel_uo_id:int
    user_id:int
    org_id:int
    member_type: Optional[str]

class OrganizationUser(Organization):
    user_id:int

    class Config:
        from_attributes = True
        json_encoders = {
            dt.date: lambda v: v.isoformat()
        }