from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersClass as ClassSchema
from app.database import get_db

router = APIRouter()

# USERS_CLASS DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# DIPLAY USER DATA
@router.get("/users/{user_id}/class", response_model=ClassSchema, tags=["Users' Class"])
def display_existing_user_class(user_id: int, users_class: ClassSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id, users_class)

@router.get("/users/{user_id}/class/proficiency_level", response_model=ClassSchema, tags=["Users' Class"])
def display_existing_user_proficiency_level(user_id: int, users_class: ClassSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_proficiency_level(db, user_id, users_class)

@router.get("/users/{user_id}/class/pond_total", response_model=ClassSchema, tags=["Users' Class"])
def display_existing_user_pond_total(user_id: int, users_class: ClassSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_pond_total(db, user_id, users_class)

@router.get("/users/{user_id}/class/pond_size_range", response_model=ClassSchema, tags=["Users' Class"])
def display_existing_user_pond_size_range(user_id: int, users_class: ClassSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_pond_size_range(db, user_id, users_class)

@router.get("/users/{user_id}/class/fish_type", response_model=ClassSchema, tags=["Users' Class"])
def display_existing_user_fish_type(user_id: int, users_class: ClassSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_fish_type(db, user_id, users_class)

@router.get("/users/{user_id}/class/fish_size_preference", response_model=ClassSchema, tags=["Users' Class"])
def display_existing_user_fish_size_preference(user_id: int, users_class: ClassSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_fish_size_preference(db, user_id, users_class)

# SET USER DATA
@router.put("/users/{user_id}/class", response_model=ClassSchema, tags=["Users' Class"])
def update_user_class_by_user_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/proficiency_level", response_model=ClassSchema, tags=["Users' Class"])
def update_user_proficiency_level_by_user_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return services.update_user_proficiency_level_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/pond_total", response_model=ClassSchema, tags=["Users' Class"])
def update_user_pond_total_by_user_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return services.update_user_pond_total_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/pond_size_range", response_model=ClassSchema, tags=["Users' Class"])
def update_user_pond_size_range_by_user_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return services.update_user_pond_size_range_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/fish_type", response_model=ClassSchema, tags=["Users' Class"])
def update_user_fish_type_by_user_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return services.update_user_fish_type_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/fish_size_preference", response_model=ClassSchema, tags=["Users' Class"])
def update_user_fish_size_preference_by_user_id(user_id: int, updated_user_class: ClassSchema, db: Session = Depends(get_db)):
    return services.update_user_fish_size_preference_by_user_id(db, user_id, updated_user_class)
