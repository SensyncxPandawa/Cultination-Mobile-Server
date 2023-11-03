import random
from sqlalchemy.orm import Session
from app import models
from .schemas import Users2FA

# GENERATE OTA CODE
def generate_user_2fa(db: Session, user_id: int):
    user_2fa = db.query(models.Users2FA).filter(
        models.Users2FA.user_id == user_id,
    ).first()
    
    if user_2fa:
        user_2fa.ota_code = generate_ota_code()
    else:
        user_2fa = models.Users2FA(user_id=user_id, ota_code=generate_ota_code())
        db.add(user_2fa)

    db.commit()
    db.refresh(user_2fa)
    return  user_2fa

# DISPLAY EXISTING OTA CODE
def display_existing_user_2fa(db: Session, user_id: int):
    user_2fa = db.query(models.Users2FA).filter(
        models.Users2FA.user_id == user_id,
    ).first()
    return user_2fa

def generate_ota_code():
    return random.randint(1000, 9999)