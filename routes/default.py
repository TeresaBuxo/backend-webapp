from fastapi import APIRouter
from starlette.responses import RedirectResponse

default = APIRouter()

@default.get('/')
def default_route():
    return RedirectResponse(url="/docs")