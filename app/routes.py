# app/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Course, Student
from .schemas import CourseCreate, StudentCreate, StudentUpdate
from .dependencies import get_db
from .auth import admin_required, student_required, get_current_user

# ----------------- Courses Router -----------------
courses_router = APIRouter(prefix="/courses", tags=["Courses"])

@courses_router.post("/", dependencies=[Depends(admin_required)])
def add_course(course: CourseCreate, db: Session = Depends(get_db)):
    new_course = Course(**course.dict())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Course created successfully", "course": new_course}

@courses_router.get("/", dependencies=[Depends(admin_required)])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# ----------------- Students Router -----------------
students_router = APIRouter(prefix="/students", tags=["Students"])

@students_router.post("/")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):

    # Auto assign default course if not provided
    if student.course_id is None:
        student.course_id = 1   # default course_id

    # Check if course exists
    course = db.query(Course).filter(Course.course_id == student.course_id).first()
    if not course:
        raise HTTPException(status_code=400, detail="Course does not exist")

    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return {
        "message": "Student added successfully",
        "student": new_student
    }


@students_router.get("/", dependencies=[Depends(admin_required)])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@students_router.get("/course/{course_id}", dependencies=[Depends(admin_required)])
def students_by_course(course_id: int, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.course_id == course_id).all()

@students_router.get("/me", dependencies=[Depends(student_required)])
def my_profile(user=Depends(get_current_user), db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == user["student_id"]).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@students_router.put("/{student_id}", dependencies=[Depends(admin_required)])
def update_student(student_id: int, data: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    if data.course_id:
        course = db.query(Course).filter(Course.course_id == data.course_id).first()
        if not course:
            raise HTTPException(status_code=400, detail="Course does not exist")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)
    return {"message": "Student updated", "student": student}

@students_router.delete("/{student_id}", dependencies=[Depends(admin_required)])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return {"message": "Student deleted"}
