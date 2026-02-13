# app/schemas.py

from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    email: str

class StudentResponse(StudentCreate):
    id: int

    class Config:
        orm_mode = True
