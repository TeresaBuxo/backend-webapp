import os

# DATABASE settings
HOST = os.getenv('LOCAL_DB')
USER = os.getenv('LOCAL_DB_USER')
PASSWORD = os.getenv('LOCAL_DB_PASSWORD')
SCHEMA = "careagain"
PORT = '3306'

# Secret key
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


#NO SQL
NO_SQL_PATH = "no_sql"