from sqlalchemy import Table,Boolean,Column, Integer, String,Float,DATE, ForeignKey,DATETIME
from sqlalchemy.orm import mapped_column,relationship
from sqlalchemy.ext.automap import automap_base
from ..config.db_setup import Base,engine
from ..config import constants as cs
from geopy.geocoders import Nominatim
import certifi
import datetime as dt
import passlib.hash as hash
import ssl

class User(Base):
    __tablename__='users'
    user_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(255))
    last_name1 = Column(String(255))
    last_name2 = Column(String(255))
    country = Column(String(255))
    role = Column(String(255))
    email = Column(String(255),unique=True)
    hashed_password = Column(String(255))
    phone_number = Column(String(255)) 
    activation_date = Column(DATE,default=dt.date.today)
    active = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)
    visible = Column(Boolean, default=True)
    deactivation_date = Column(DATE)
    storage_path = Column(String(255),default=f'{cs.NO_SQL_PATH}/users/user_{str(user_id)}/')

    def verify_password(self,password:str):
        return hash.bcrypt.verify(password,self.hashed_password)
    
class User_Organization(Base):
    __tablename__='users_orgs'
    rel_uo_id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.user_id"))
    org_id = Column(Integer,ForeignKey("organizations.org_id"))
    member_type = Column(String(255))


class Organization(Base):
    __tablename__='organizations'
    org_id = Column(Integer,primary_key=True,index=True)
    org_name = Column(String(255))
    org_type = Column(String(255))
    address = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    logo = Column(String(255)) 
    web_link = Column(String(255)) 
    activation_date = Column(DATE,default=dt.date.today)
    active = Column(Boolean, default=True)
    verified = Column(Boolean, default=False)
    visible = Column(Boolean, default=True)
    storage_path  = Column(String(255))

    def get_coordinates(self):
        # Create a default SSL context
        ctx = ssl.create_default_context()

        # Load the certifi certificate file
        ctx.load_verify_locations(certifi.where())
        # Initialize geolocator
        geolocator = Nominatim(user_agent="geoapiExercises",ssl_context=ctx)
        location = geolocator.geocode(self.address)
        print(location)
        self.latitude = location.latitude
        self.longitude = location.longitude
        return location.latitude, location.longitude

# class Session(Base):
#     __tablename__='sessions'
#     session_id = Column(Integer,primary_key=True,index=True)
#     user_id = Column(Integer,ForeignKey("users.user_id"))
#     token = Column(String(255))
#     login_datetime = Column(DATETIME,default=dt.datetime.now)
#     logout_datetime = Column(DATETIME)

class Project(Base):
    __tablename__= 'projects'
    project_id = Column(Integer,primary_key=True,index=True)
    project_name = Column(String(100))
    link = Column(String(255))
    description = Column(String(255))
    image = Column(String(255))

class User_Project(Base):
    __tablename__= 'users_projects'
    rel_up_id = Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.user_id"))
    project_id = Column(Integer,ForeignKey("projects.project_id"))
    member_type = Column(String(255))

class Video(Base):
    __tablename__= 'videos'
    video_id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100))
    description = Column(String(255))
    youtube_link = Column(String(255))
    created_by = Column(Integer,ForeignKey("users.user_id"))
    deleted = Column(Boolean,default=False)

class Question(Base):
    __tablename__= 'questions'
    question_id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255))
    question = Column(String(255))
    file_link = Column(String(255))
    created_by = Column(Integer,ForeignKey("users.user_id"))
    deleted = Column(Boolean,default=False)