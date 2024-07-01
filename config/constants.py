import os

# DATABASE settings
HOST = os.getenv('LOCAL_DB')
USER = os.getenv('LOCAL_DB_USER')
PASSWORD = os.getenv('LOCAL_DB_PASSWORD')
SCHEMA = "careagain"
PORT = '3306'