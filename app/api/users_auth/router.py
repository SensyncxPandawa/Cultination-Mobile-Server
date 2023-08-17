from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Auth as AuthSchema
from app.models import Auth as AuthModel
from app.database import get_db

router = APIRouter()

# CREATE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.post("/users/auth/", response_model=List[AuthSchema], tags=["Users' Auth"])
def create_user(user_auth: AuthSchema, db: Session = Depends(get_db)):
    return

# VALIDATE LOGIN REQUEST
@router.post("/users/auth/{user_id}", response_model=List[AuthSchema], tags=["Users' Auth"])
def validate_user_auth(user_auth: AuthSchema, db: Session = Depends(get_db)):
    return

# DISPLAY USER AUTHENTIFICATION DATA
@router.get("/users/auth/{user_id}", response_model=List[AuthSchema], tags=["Users' Auth"])
def display_existing_user_auth(user_id: int, db: Session = Depends(get_db)):
    return

# EDIT USER AUTHENTIFICATION DATA
@router.put("/users/auth/{user_id}", response_model=AuthSchema, tags=["Users' Auth"])
def update_user_auth_by_id(user_id: int, updated_user_auth: AuthSchema, db: Session = Depends(get_db)):
    return

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.delete("/users/auth/{user_id}", response_model=AuthSchema, tags=["Users' Auth"])
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return
