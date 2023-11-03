from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersPonds, SetUsersPonds
from app.database import get_db

router = APIRouter()

# CREATE USER Ponds
@router.post(
    "/users/{user_id}/ponds",
    response_model=UsersPonds,
    tags=["Users' Ponds"]
)
def create_user_ponds(user_id: int, user_ponds: SetUsersPonds, db: Session = Depends(get_db)):
    return services.create_user_ponds(db, user_id, user_ponds)

# DISPLAY USER Ponds
@router.get(
    "/users/{user_id}/ponds",
    response_model=List[UsersPonds],
    tags=["Users' Ponds"]
)
def display_all_existing_user_ponds(user_id: int, db: Session = Depends(get_db)):
    return services.display_all_existing_user_ponds(db, user_id)

# UPDATE USER Ponds
@router.put(
    "/users/{user_id}/ponds/{pond_id}",
    response_model=UsersPonds,
    tags=["Users' Ponds"]
)
def update_existing_user_ponds_by_pond_id(user_id: int, pond_id: int, updated_user_ponds: SetUsersPonds, db: Session = Depends(get_db)):
    return services.update_existing_user_ponds_by_pond_id(db, user_id, pond_id, updated_user_ponds)

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.delete(
    "/users/{user_id}/ponds/{pond_id}",
    response_model=None,
    tags=["Users' Ponds"]
)
def delete_user_ponds_by_pond_id(user_id: int, pond_id: int, db: Session = Depends(get_db)):
    return services.delete_user_ponds_by_pond_id(db, user_id, pond_id)
