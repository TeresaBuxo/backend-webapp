from sqlalchemy import Table,Boolean,Column, Integer, String,Float,DATE, ForeignKey,DATETIME
from sqlalchemy.orm import mapped_column,relationship
from sqlalchemy.ext.automap import automap_base
from ..config.db_setup import Base,engine
# from geopy.geocoders import Nominatim
import datetime as dt
import passlib.hash as hash

class User(Base):
    __tablename__='users'
    user_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(255))
    last_name1 = Column(String(255))
    last_name2 = Column(String(255))
    role = Column(String(255))
    email = Column(String(255),unique=True)
    hashed_password = Column(String(255))
    phone_number = Column(String(255)) 
    activation_date = Column(DATE,default=dt.date.today)
    active = Column(Boolean, default=True)
    deactivation_date = Column(DATE)
    image = Column(String(255))
    member_of = Column(Integer,ForeignKey("institutions.institution_id"))

    def verify_password(self,password:str):
        return hash.bcrypt.verify(password,self.hashed_password)


class Institution(Base):
    __tablename__='institutions'
    institution_id = Column(Integer,primary_key=True,index=True)
    intitution_name = Column(String(255))
    intitution_type = Column(String(255))
    address = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    logo = Column(String(255)) #url
    administrated_by = Column(Integer,ForeignKey("users.user_id"))

    #user=relationship("User",back_populates="user")

    def get_coordinates(self,address:str):
        # Initialize geolocator
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(address)
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
    user_id = Column(Integer,ForeignKey("users.user_id"))

class Video(Base):
    __tablename__= 'videos'
    video_id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100))
    description = Column(String(255))
    youtube_link = Column(String(255))
    created_by = Column(Integer,ForeignKey("users.user_id"))
