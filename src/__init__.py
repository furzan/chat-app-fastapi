from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from src.routes.router import router

@asynccontextmanager
async def life_span(app: FastAPI):
    print('server is starting')
    yield
    print('server has been stoped')

version = "v1"
app = FastAPI(
    title= "chat_app",
    description= "rest api for a chat app service", 
    version= version,
    lifespan= life_span
)


app.include_router(router, prefix=f"/app")

