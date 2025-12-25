from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:9665890982@localhost/student_course_management"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ This is the dependency FastAPI uses
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
