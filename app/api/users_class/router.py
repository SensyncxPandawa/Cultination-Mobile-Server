from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Class as ClassSchema
from app.models import Class as ClassModel
from app.database import get_db

router = APIRouter()

# USERS_CLASS DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# DIPLAY USER DATA
@router.get("/users/class/proficiency_level/{user_id}", response_model=List[ClassSchema], tags=["Users' Class"])
def display_existing_user_proficiency_level(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/users/class/pond_total/{user_id}", response_model=List[ClassSchema], tags=["Users' Class"])
def display_existing_user_pond_total(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/users/class/pond_size_range/{user_id}", response_model=List[ClassSchema], tags=["Users' Class"])
def display_existing_user_pond_size_range(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/users/class/fish_type/{user_id}", response_model=List[ClassSchema], tags=["Users' Class"])
def display_existing_user_fish_type(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/users/class/fish_size_preference/{user_id}", response_model=List[ClassSchema], tags=["Users' Class"])
def display_existing_user_fish_size_preference(user_id: int, db: Session = Depends(get_db)):
    return

# SET USER DATA
@router.put("/users/class/{user_id}", response_model=ClassSchema, tags=["Users' Class"])
def update_user_class_by_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/class/proficiency_level/{user_id}", response_model=ClassSchema, tags=["Users' Class"])
def update_user_proficiency_level_by_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/class/pond_total/{user_id}", response_model=ClassSchema, tags=["Users' Class"])
def update_user_pond_total_by_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/class/pond_size_range/{user_id}", response_model=ClassSchema, tags=["Users' Class"])
def update_user_pond_size_range_by_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/class/fish_type/{user_id}", response_model=ClassSchema, tags=["Users' Class"])
def update_user_fish_type_by_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/class/fish_size_preference/{user_id}", response_model=ClassSchema, tags=["Users' Class"])
def update_user_fish_size_preference_by_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return