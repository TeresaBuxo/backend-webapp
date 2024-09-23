from fastapi import APIRouter,Depends,Response, HTTPException,security
from typing import List
from ..schemas import project_schema as schema, user_schema
from ..models import model
from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..config.db_setup import get_db
from ..services import user_functions
import passlib.hash as hash

project_route = APIRouter(prefix="/api/projects")

@project_route.get("/",response_model=List[schema.Project],tags = ['projects'])
def show_projects(db:Session=Depends(get_db)):
    projects = db.query(model.Project).order_by(desc(model.Project.project_id)).all()
    return projects

@project_route.post("/new_project/",tags = ['projects'])#,response_model=schema.Project)
async def create_project(input:schema.Project,db:Session=Depends(get_db),
                         user:user_schema.User = Depends(user_functions.get_current_user)):
    #db_user = await user_functions.get_user_by_email(input.email,db)
    # if db_user:
    #     raise HTTPException(status_code=400, detail= "Email already in use")
    # else:
    project_obj = model.Project(project_name=input.project_name,
                                link=input.link,
                                description=input.description,
                                image=input.image,
                                user_id=user.user_id)
    db.add(project_obj)
    db.commit()
    db.refresh(project_obj)
    return project_obj 