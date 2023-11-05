from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import OTPCode
from app.database import get_db

router = APIRouter()

# CREATE USER 2FA
@router.get(
    "/users/{user_id}/2fa",
    response_model=None,
    tags=["Users' 2FA"]
)
def generate_and_send_otp_code(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's 2FA data using the user_id.
    \n If no user is found, a 404 error is raised.
    \n It then generate new otp_code.
    \n It then send the otp_code using Fonnta (WhatsApp) to the user_phonenumber.
    \n The function returns a success message.
    """
    return services.generate_and_send_otp_code(db, user_id)

# DISPLAY EXISTING OTA CODE
@router.post(
    "/users/{user_id}/2fa",
    response_model=None,
    tags=["Users' 2FA"]
)
def validate_otp_code(user_id: int, provided_otp_code: OTPCode, db: Session = Depends(get_db)):
    """
    The function fetches a user's 2FA data using the user_id.
    \n If no user is found, a 404 error is raised.
    \n If a user is found, it validates the given otp_code against the stored otp_code;
    \n If the otp_code is incorrect, a 400 error is raised.
    \n The function returns a success message.
    """
    return services.validate_otp_code(db, user_id, provided_otp_code)