from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import Users2FA
from app.database import get_db

router = APIRouter()

# CREATE USER 2FA
@router.post(
    "/users/{user_id}/2fa",
    response_model=Users2FA,
    tags=["Users' 2FA"]
)
def generate_user_2fa(user_id: int, db: Session = Depends(get_db)):
    return services.generate_user_2fa(db, user_id)

# DISPLAY EXISTING OTA CODE
@router.get(
    "/users/{user_id}/2fa",
    response_model=Users2FA,
    tags=["Users' 2FA"]
)
def display_existing_user_2fa(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_2fa(db, user_id)