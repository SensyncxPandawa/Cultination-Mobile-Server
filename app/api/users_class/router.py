from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersClass, SetUsersClass
from app.database import get_db

router = APIRouter()

# DISPLAY USER DATA
@router.get("/users/{user_id}/class", response_model=UsersClass, tags=["Users' Class"])
def display_existing_user_class(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_class(db, user_id)

# SET USER DATA (ONLY NEED USER_ID ON THE PARAM AND THE ATTRIBUTE ON THE REQUEST BODY)
@router.put("/users/{user_id}/class", response_model=UsersClass, tags=["Users' Class"])
def update_user_class_by_user_id(user_id: int, updated_user_class: SetUsersClass, db: Session = Depends(get_db)):
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)
