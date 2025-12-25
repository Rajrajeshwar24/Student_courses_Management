# Student_courses_Management
Student–Course Management API
A FastAPI + PostgreSQL backend for managing students and courses using SQLAlchemy ORM.
________________________________________
Tech Stack
•	Backend: FastAPI
•	Database: PostgreSQL
•	ORM: SQLAlchemy
•	Migrations (optional): Postman
•	Server: Uvicorn
________________________________________
Prerequisites
•	Python 3.10+
•	PostgreSQL 13+
•	Git
________________________________________
Project Structure
app/
├── __pycache__/          # Python cache files
├── auth.py               # Authentication & authorization logic
├── database.py           # PostgreSQL connection & session handling
├── dependencies.py       # FastAPI dependencies (DB, auth, etc.)
├── main.py               # FastAPI application entry point
├── models.py             # SQLAlchemy ORM models
├── routes.py             # API route definitions
├── schemas.py            # Pydantic request/response schemas
├── venv/
├── requirements.txt
└── README.md

---

## Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd Student_course_backend
2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
requirements.txt (sample)
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
________________________________________
Database Setup (PostgreSQL)
4️⃣ Create Database
CREATE DATABASE student_course_management;
5️⃣ Configure Database Connection
Edit app/database.py:
DATABASE_URL = "postgresql://postgres:<password>@localhost/student_course_management"
________________________________________
Sample Database Schema
📘 courses table
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_months INT NOT NULL
);
👨‍🎓 students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL,
    course_id INT,
    CONSTRAINT fk_course
        FOREIGN KEY(course_id)
        REFERENCES courses(id)
        ON DELETE SET NULL
);
________________________________________
Sample Stored Procedures (Optional)
🔹 Insert Student Procedure
CREATE OR REPLACE PROCEDURE add_student(
    p_name VARCHAR,
    p_email VARCHAR,
    p_password VARCHAR,
    p_role VARCHAR,
    p_course_id INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO students(name, email, password, role, course_id)
    VALUES (p_name, p_email, p_password, p_role, p_course_id);
END;
$$;
🔹 Call Procedure
CALL add_student('Raj', 'raj@gmail.com', '123456', 'student', 1);
________________________________________
Running the Application
6️⃣ Start FastAPI Server
uvicorn app.main:app --reload
Server will run at:
http://127.0.0.1:8000
________________________________________
API Documentation
FastAPI provides automatic Swagger UI:
📌 PostMan:
http://127.0.0.1:8000/courses
http://127.0.0.1:8000/students
________________________________________
Sample API Endpoints
➕ Add Student
POST /students/
📄 Get All Students
GET /students/
🎓 Get Course by ID
GET /courses/{id}
________________________________________
Testing with Postman
•	Set Content-Type: application/json
•	Use POST, GET methods
•	Verify data using:
SELECT * FROM students;
SELECT * FROM courses;
         Notes
•	Folder structure follows FastAPI best practices (separation of concerns)
•	routes.py contains all endpoint routers
•	schemas.py is used for request validation and response models
•	models.py defines database tables using SQLAlchemy ORM
•	dependencies.py centralizes reusable dependencies (DB session, auth)
•	Passwords should be hashed before storing in production .


