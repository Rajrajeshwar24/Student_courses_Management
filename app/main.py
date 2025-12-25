from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Student, Course


app = FastAPI()

# Get all students
@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# Get student by id
@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# Get all courses
@app.get("/courses/")
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# Get course by id
@app.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
