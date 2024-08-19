from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
import config.constants as cs

URL_DATABASE = f'mysql+pymysql://{cs.USER}:{cs.PASSWORD}@{cs.HOST}:{cs.PORT}/{cs.SCHEMA}'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit = False,autoflush = False, bind =engine)
Base = declarative_base()
conn = engine.connect()
meta = MetaData()

def get_db():
    try:
        db =SessionLocal()
        yield db
    finally:
        db.close()
