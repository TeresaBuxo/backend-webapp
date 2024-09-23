from fastapi import APIRouter,Depends,Response, HTTPException,security
from typing import List
from ..schemas import user_schema as schema
from ..models import model
from sqlalchemy.orm import Session
from ..config.db_setup import get_db
from ..services import user_functions
import passlib.hash as hash

user_route = APIRouter(prefix="/api/users")

@user_route.get("/users/",response_model=List[schema.User],tags = ['users'])
def show_users(db:Session=Depends(get_db)):
    users = db.query(model.User).all()
    return users

@user_route.post("/create_user",response_model=schema.User,tags = ['users'])
async def create_users(input:schema.UserCreate,db:Session=Depends(get_db)):
    db_user = await user_functions.get_user_by_email(input.email,db)
    if db_user:
        raise HTTPException(status_code=400, detail= "Email already in use")
    else:
        user_obj = model.User(email=input.email,
                          hashed_password = hash.bcrypt.hash(input.password))
        db.add(user_obj)
        db.commit()
        db.refresh(user_obj)
        return user_obj


@user_route.delete("/{user_id}",tags = ['users'])
def delete_users(user_id_to_delete:int,db:Session=Depends(get_db)):
    user = db.query(model.User).filter_by(user_id=user_id_to_delete).first()
    db.delete(user)
    return HTTPException(status_code=204,details= "Deleted user") 

@user_route.post("/token",tags = ['users'])#, response_model=schema.Token)
async def generate_token(form_data:security.OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = await user_functions.authenticate_user(form_data.username,form_data.password,db)
    print(user)
    if not user:
        raise HTTPException(status_code = 401,detail = "Invalid Credentials")
    access_token = await user_functions.create_token(user)
    return  {"access_token": access_token, "token_type": "bearer"}
    

@user_route.get("/me",tags = ['users'])
async def get_user(user:schema.User = Depends(user_functions.get_current_user)):
    return user