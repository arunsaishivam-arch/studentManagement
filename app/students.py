# app/students.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import models, schemas
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students")
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/students")
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()
