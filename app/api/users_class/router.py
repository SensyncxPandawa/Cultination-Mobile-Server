from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersClass, SetUsersClass, UserProficiencyLevel, SetUserProficiencyLevel, UserPondTotal, SetUserPondTotal, UserPondSizeRange, SetUserPondSizeRange, UserFishType, SetUserFishType, UserFishSizePreference, SetUserFishSizePreference
from app.database import get_db

router = APIRouter()

# DISPLAY USER DATA
@router.get("/users/{user_id}/class", response_model=UsersClass, tags=["Users' Class"])
def display_existing_user_class(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

@router.get("/users/{user_id}/class/proficiency_level", response_model=UserProficiencyLevel, tags=["Users' Class"])
def display_existing_user_proficiency_level(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

@router.get("/users/{user_id}/class/pond_total", response_model=UserPondTotal, tags=["Users' Class"])
def display_existing_user_pond_total(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

@router.get("/users/{user_id}/class/pond_size_range", response_model=UserPondSizeRange, tags=["Users' Class"])
def display_existing_user_pond_size_range(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

@router.get("/users/{user_id}/class/fish_type", response_model=UserFishType, tags=["Users' Class"])
def display_existing_user_fish_type(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

@router.get("/users/{user_id}/class/fish_size_preference", response_model=UserFishSizePreference, tags=["Users' Class"])
def display_existing_user_fish_size_preference(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

# SET USER DATA (ONLY NEED USER_ID ON THE PARAM AND THE ATTRIBUTE ON THE REQUEST BODY)
@router.put("/users/{user_id}/class", response_model=UsersClass, tags=["Users' Class"])
def update_user_class_by_user_id(user_id: int, updated_user_class: SetUsersClass, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/proficiency_level", response_model=UserProficiencyLevel, tags=["Users' Class"])
def update_user_proficiency_level_by_user_id(user_id: int, updated_user_class: SetUserProficiencyLevel, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/pond_total", response_model=UserPondTotal, tags=["Users' Class"])
def update_user_pond_total_by_user_id(user_id: int, updated_user_class: SetUserPondTotal, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/pond_size_range", response_model=UserPondSizeRange, tags=["Users' Class"])
def update_user_pond_size_range_by_user_id(user_id: int, updated_user_class: SetUserPondSizeRange, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/fish_type", response_model=UserFishType, tags=["Users' Class"])
def update_user_fish_type_by_user_id(user_id: int, updated_user_class: SetUserFishType, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)

@router.put("/users/{user_id}/class/fish_size_preference", response_model=UserFishSizePreference, tags=["Users' Class"])
def update_user_fish_size_preference_by_user_id(user_id: int, updated_user_class: SetUserFishSizePreference, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)
