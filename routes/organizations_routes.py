from fastapi import APIRouter,Depends
from typing import List
from ..schemas import organization_schema as org_schema
from ..schemas import user_schema as schema
from ..models import model
from sqlalchemy.orm import Session
from ..config.db_setup import get_db
from ..services import user_functions

organization_route = APIRouter(prefix="/api/orgs")


@organization_route.post("/create_org",response_model=org_schema.Organization,tags = ['organizations'])
async def create_org(input:org_schema.Organization,
                     db:Session=Depends(get_db),
                     user:schema.User = Depends(user_functions.get_current_user)):

    org_obj = model.Organization(org_name = input.org_name,
                                 org_type=input.org_type,
                                 address = input.address,
                                 logo = input.logo,
                                 web_link = input.web_link)
    
    if org_obj.address is not None:
        try:
            org_obj.get_coordinates()   
        except:
            print("Error location")

    db.add(org_obj)
    db.commit()
    db.refresh(org_obj)

    rel_obj = model.User_Organization(user_id = user.user_id,
                                      org_id = org_obj.org_id,
                                      member_type = "admin")
    db.add(rel_obj)
    db.commit()
    db.refresh(rel_obj)
    return org_obj

@organization_route.get("/organizations",response_model=List[org_schema.Organization],tags = ['organizations'])
async def show_organizations(db:Session=Depends(get_db)):
    orgs = db.query(model.Organization).all()
    return orgs 

@organization_route.get("/my_organizations",tags = ['organizations'],
                        response_model=List[org_schema.OrganizationUser])
async def show_organizations(db:Session=Depends(get_db),
                             user:schema.User = Depends(user_functions.get_current_user)):
    my_orgs = db.query(model.Organization,
                       model.User_Organization.user_id) \
            .join(model.Organization, model.User_Organization.org_id == model.Organization.org_id) \
            .filter(model.User_Organization.user_id == user.user_id) \
            .all()
    print(my_orgs)
    return my_orgs

