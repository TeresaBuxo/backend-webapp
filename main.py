# import fastAPI modules
from fastapi import FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
# import routes
from routes.default import default
from routes.user import user_route
# import model and db
from models import model
from config.db_setup import engine,Base,Session

# create table in the database
model.Base.metadata.create_all(bind=engine)
model.automap_base()

# initiate app
app = FastAPI()

# add all routes
app.include_router(default)
app.include_router(user_route)

# CORS middleware to allow communication between frontend and backend
origins = ['http://localhost:3000'] # specify the http where the api is going to run

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/", StaticFiles(directory="../frontend-webapp/build", html=True), name="frontend")