from sqlalchemy import Table,Boolean,Column, Integer, String,Float,DATE, ForeignKey
from sqlalchemy.orm import mapped_column,relationship
from sqlalchemy.ext.automap import automap_base
from config.db_setup import Base,engine

class User(Base):
    __tablename__='user'
    user_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(255))
    last_name1 = Column(String(255))
    last_name2 = Column(String(255))
    role = Column(String(255))
    email = Column(String(255))
    phone_number = Column(String(255)) 
    activation_date = Column(DATE)
    active = Column(Boolean, default=True)
    deactivation_date = Column(DATE)
    institution_id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)


class Institution(Base):
    __tablename__='institution'
    institution_id = Column(Integer,primary_key=True,index=True)
    intitution_name = Column(String(255))
    address = Column(String(255))
    latitude = Column(Float)
    longitude = Column(Float)
    intitution_type = Column(String(255))
    logo = Column(String(255)) #url
