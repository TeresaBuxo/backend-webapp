# import model and db
from fastapi import security, Depends, HTTPException, status, Response
from ..models import model
from ..schemas import user_schema as schema
from ..config.db_setup import engine,Base,Session,get_db
from ..config.constants import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from jose import JWTError, jwt
from passlib.context import CryptContext
import os

oauth2schema = security.OAuth2PasswordBearer(tokenUrl="api/users/token")

async def get_user_by_email(email:str,db:Session,):
    '''Return the email if exists in db'''
    user = db.query(model.User).filter(model.User.email == email).first()
    return user


async def authenticate_user(email:str,password:str,db:Session):
    '''Checks if the email exist and verify the password and return the user if so'''
    user = await get_user_by_email(email,db)
    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user


async def create_token(user:model.User): #expires_delta = ACCESS_TOKEN_EXPIRE_MINUTES):
    '''Create a token for each user when opening session'''
    user_obj =  {"user_id":user.user_id}
    # if expires_delta:
    #     expire = datetime.utcnow + expires_delta
    
    token = jwt.encode(user_obj,SECRET_KEY,algorithm=ALGORITHM)

    # # Set token in cookie (HTTP-only and secure)
    # response.set_cookie(
    #     key="access_token",  # Name of the cookie
    #     value=token,  # The token itself
    #     httponly=True,       # Prevents JavaScript access to the cookie (for security)
    #     secure=True,         # Ensures the cookie is only sent over HTTPS
    #     samesite="lax"       # Protects against CSRF
    # )

    # # Return a success response (or return any data you need)
    # print("message Token set in cookie")

    return token #dict(access_token = token, token_type="bearer")


async def get_current_user(db:Session=Depends(get_db),token:str = Depends(oauth2schema)):
    '''Get current user logged in'''
    credential_exception = HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                                         detail = "Could not validate credentials",
                                         headers = {"WWW-Authenticate": "Bearer"})

    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms = [ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise credential_exception

        #token_data = schema.User(user_id=user_id)

    except JWTError:
        raise credential_exception
    
    user = db.query(model.User).filter(model.User.user_id == user_id).first()

    return user

# async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
#     if current_user.disabled:
#         raise HTTPException(status_code=400,detail = "Inactive user")
#     return current_user