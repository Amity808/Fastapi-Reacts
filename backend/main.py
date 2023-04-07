from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db.database import engine
from models.base_class import Base
from api.routerBase import api_router

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]


def crosM(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def create_table():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)


def startApplication():
    app = FastAPI()
    create_table()
    include_router(app)
    crosM(app)
    return app


app = startApplication()