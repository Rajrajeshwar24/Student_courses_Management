from fastapi import Depends, HTTPException

def get_current_user():
    return {"role": "ADMIN", "student_id": 1}

def admin_required(user=Depends(get_current_user)):
    if user["role"] != "ADMIN":
        raise HTTPException(status_code=403, detail="Admin access required")

def student_required(user=Depends(get_current_user)):
    if user["role"] != "STUDENT":
        raise HTTPException(status_code=403, detail="Student access required")
