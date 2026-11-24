from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management API")
class Student(BaseModel):
    roll_no: str
    name: str
    branch: str
    year: int

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    branch: Optional[str] = None
    year: Optional[int] = None


students: list[Student] = []


def find_student(roll_no: str) -> Student:
    for s in students:
        if s.roll_no == roll_no:
            return s
    raise HTTPException(status_code=404, detail="Student not found")


@app.get("/")
def home():
    return {"message": "Student Management API"}


@app.get("/students")
def list_students():
    return students
# POST: add a new student
@app.post("/students", status_code=201)
def add_student(s: Student):
    for existing in students:
        if existing.roll_no == s.roll_no:
            raise HTTPException(status_code=400, detail="Roll number already exists")
    students.append(s)
    return s


# PUT: replace the whole record
@app.put("/students/{roll_no}")
def update_student(roll_no: str, s: Student):
    old = find_student(roll_no)
    students[students.index(old)] = s
    return s


# PATCH: change only the fields sent
@app.patch("/students/{roll_no}")
def patch_student(roll_no: str, changes: StudentUpdate):
    old = find_student(roll_no)
    updated = old.model_copy(update=changes.model_dump(exclude_unset=True))
    students[students.index(old)] = updated
    return updated


# DELETE: remove a student
@app.delete("/students/{roll_no}")
def delete_student(roll_no: str):
    s = find_student(roll_no)
    students.remove(s)
    return {"message": f"Student {roll_no} deleted"}
   