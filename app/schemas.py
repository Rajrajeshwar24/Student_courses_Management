from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    course_name: str
    course_code: str
    course_duration: int


class StudentCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = "student"   # default role
    course_id: Optional[int] = None


class StudentUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    course_id: Optional[int]
