from fastapi import APIRouter,Depends,Response
from typing import List
from schemas import schema
from models import model
from sqlalchemy.orm import Session
from config.db_setup import get_db
from starlette.status import HTTP_204_NO_CONTENT

user_route = APIRouter()

@user_route.get("/users/",response_model=List[schema.User])
def show_users(db:Session=Depends(get_db)):
    users = db.query(model.User).all()
    return users

@user_route.post("/users/",response_model=schema.User)
def create_users(input:schema.User,db:Session=Depends(get_db)):
    user = model.User(first_name = input.first_name,
                      last_name1 = input.last_name1,
                      longitude = input.longitude,
                      latitude = input.latitude)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@user_route.delete("/users/{user_id}")
def delete_users(user_id_to_delete:int,db:Session=Depends(get_db)):
    user = db.query(model.User).filter_by(user_id=user_id_to_delete).first()
    db.delete(user)
    return Response(status_code=HTTP_204_NO_CONTENT) 