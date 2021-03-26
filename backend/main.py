from fastapi import FastAPI
from db import database
from users.router import router as userrouter
from starlette.middleware.cors import CORSMiddleware 
from starlette.requests import Request

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(userrouter)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.connection = database
    reponse = await call_next(request)
    return reponse
    