from fastapi import FastAPI
from db import database
from users.router import router as userrouter
from nlp.router import router as nlprouter
from starlette.middleware.cors import CORSMiddleware 
from starlette.requests import Request

# import logging
# logging.basicConfig()
# logging.getLogger("nlp.decoder").setLevel(level=logging.DEBUG)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(userrouter)
app.include_router(nlprouter)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    reponse = await call_next(request)
    return reponse
    