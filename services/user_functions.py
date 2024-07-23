# import model and db
from fastapi import security, Depends, HTTPException
from models import model
from schemas import schema
from config.db_setup import engine,Base,Session,get_db
import jwt
import os

JWT_SECRET = "myjwtsecret" #os.getenv("JWT_SECRET")
oauth2schema = security.OAuth2PasswordBearer(tokenUrl="/users/token")

async def get_user_by_email(email:str,db:Session):
    '''Return the email if exists in db'''
    return db.query(model.User).filter(model.User.email == email).first()


async def authenticate_user(email:str,password:str,db:Session):
    '''Checks if the email exist and verify the password and return the user if so'''
    user = await get_user_by_email(email,db)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def create_token(input:model.User):
    '''Create a token for each user when opening session'''
    user_obj =  schema.User.from_orm(input)
    token = jwt.encode(user_obj.dict(),JWT_SECRET)

    return dict(access_token = token, token_tyep="bearer")


async def get_current_user(db:Session=Depends(get_db),token:str = Depends(oauth2schema)):
    '''Get current user logged in'''
    try:
        payload = jwt.decode(token,JWT_SECRET,algorithms = ["HS256"])
        user = db.query(model.User).get(payload["id"])
    except:
        raise HTTPException(status_code=401,detail="Invalid Email or Password")

    return schema.UserCreate.from_orm(user)