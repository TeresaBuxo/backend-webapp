# import fastAPI modules
from fastapi import FastAPI,Depends,security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
# import routes
from routes.default import default
from routes.user_routes import user_route
from routes.project_routes import project_route
# import model and db
from models import model
from config.db_setup import engine,Base,Session
from config.tags_metadata import tags_metadata

# create table in the database
model.Base.metadata.create_all(bind=engine)
model.automap_base()

# initiate app
app = FastAPI(openapi_tags=tags_metadata)

# add all routes
app.include_router(default)
app.include_router(user_route)
app.include_router(project_route)

# if __name__ == "__main__":
#     import uvicorn
#     import os
#     uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))

# # CORS middleware to allow communication between frontend and backend
# origins = ['http://localhost:3000'] # specify the http where the api is going to run

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=[origins],  # Change this in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.mount("/", StaticFiles(directory="../frontend-webapp/build", html=True), name="frontend")