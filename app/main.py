# app/main.py

from fastapi import FastAPI
from .database import engine
from . import models
from .students import router as student_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(student_router)

@app.get("/")
def home():
    return {"message": "Student Management API Running"}
