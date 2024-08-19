from fastapi import APIRouter,Depends,Response, HTTPException,security
from typing import List
from schemas import project_schema as schema
from models import model
from sqlalchemy.orm import Session
from config.db_setup import get_db
from services import user_functions
import passlib.hash as hash

project_route = APIRouter(prefix="/api")

@project_route.get("/projects/",response_model=List[schema.Project],tags = ['projects'])
def show_projects(db:Session=Depends(get_db)):
    users = db.query(model.Project).all()
    return users

@project_route.post("/new_project/",response_model=schema.Project,tags = ['projects'])
async def create_project(input:schema.Project,db:Session=Depends(get_db)):
    # db_user = await user_functions.get_user_by_email(input.email,db)
    # if db_user:
    #     raise HTTPException(status_code=400, detail= "Email already in use")
    # else:
    project_obj = model.Project(project_name=input.project_name,
                                link=input.link,
                                image=input.image,
                                description=input.description)
    db.add(project_obj)
    db.commit()
    db.refresh(project_obj)
    return project_obj 