import random
import json
import requests
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import OTPCode

# GENERATE OTA CODE


def generate_and_send_otp_code(db: Session, user_id: int):
    # The function fetches user's data using the user_id.
    existing_user = db.query(models.UsersAuth).filter(
        models.UsersAuth.user_id == user_id).first()

    # If no user is found, a 404 error is raised.
    if existing_user is None:
        raise HTTPException(
            status_code=404, detail="User with this user_id not found")

    # It then generate new otp_code
    generated_otp_code = generate_otp_code()
    existing_user_2fa = db.query(models.Users2FA).filter(
        models.Users2FA.user_id == user_id,).first()
    if existing_user_2fa:
        existing_user_2fa.otp_code = generated_otp_code
        db.commit()
        db.refresh(existing_user_2fa)

    # It then send the otp_code using Fonnte (WhatsApp) to the user_phonenumber.
    url = "https://api.fonnte.com/send"
    headers = {
        'Authorization': 'iA+BkdZMI_uMvXI_1!T5'
    }
    payload = {
        'target': existing_user.user_phonenumber,
        'message': f'OTP Cultination: {generated_otp_code}'
    }
    response = requests.request("POST", url, headers=headers, data=payload)

    return {"message": json.loads(response.text)}

# DISPLAY EXISTING OTA CODE


def validate_otp_code(db: Session, user_id: int, provided_otp_code: OTPCode):
    # The function fetches a user's data using the user_id.
    user_2fa = db.query(models.Users2FA).filter(
        models.Users2FA.user_id == user_id,
    ).first()

    # If no user is found, a 404 error is raised.
    if user_2fa is None:
        raise HTTPException(
            status_code=404, detail="User with this user_id not found")

    # If a user is found, it validates the given otp_code against the stored otp_code;
    if user_2fa.otp_code == provided_otp_code.otp_code:
        return "Success!"

    # If the otp_code is incorrect, a 400 error is raised
    else:
        raise HTTPException(status_code=400, detail="Incorrect OTP code")


def generate_otp_code():
    return random.randint(1000, 9999)
