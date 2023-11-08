from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersAuth, UsersValidationAuth
from .encrypt import create_hashed_password, verify_password
from datetime import date


def create_user(db: Session, user_auth: UsersAuth):
    # The function fetches a user's data using the user_phonenumber.
    existing_user = db.query(models.UsersAuth).filter(
        models.UsersAuth.user_phonenumber == user_auth.user_phonenumber).first()

    # If the user already exists based on the provided user_phonenumber, a 404 error is raised.
    if existing_user:
        raise HTTPException(
            status_code=400, detail="User with this phone number already exists")

    # If the user isn't exist, it proceed to generate new_user_id.
    latest_user_id = db.query(func.max(models.UsersAuth.user_id)).scalar() or 0
    new_user_id = latest_user_id + 1

    # It then generate hashed_password using the provided user_password.
    hashed_password = create_hashed_password(user_auth.user_password)

    # It then created the UsersAuth table with the provided attributes and values.
    users_auth = models.UsersAuth(
        user_id=new_user_id,
        user_fullname=user_auth.user_fullname,
        user_birthdate=user_auth.user_birthdate,
        user_phonenumber=user_auth.user_phonenumber,
        user_email=user_auth.user_email,  # OPTIONAL
        user_password=hashed_password
    )
    db.add(users_auth)

    # It then created various related tables (Users2FA, UsersClass, UsersMarket, and UsersPrimaryAddress).
    users_2fa = models.Users2FA(user_id=users_auth.user_id)
    db.add(users_2fa)

    calc_user_age = (date.today() - users_auth.user_birthdate).days // 365
    users_class = models.UsersClass(
        user_id=users_auth.user_id, user_age=calc_user_age)
    db.add(users_class)

    users_market = models.UsersMarket(user_id=users_auth.user_id)
    db.add(users_market)

    users_primary_address = models.UsersPrimaryAddress(
        user_id=users_auth.user_id)
    db.add(users_primary_address)

    db.commit()
    return users_auth


def validate_user_auth(db: Session, user_validation_auth: UsersValidationAuth):
    # The function fetches a user's data using the user_phonenumber.
    existing_user = db.query(models.UsersAuth).filter_by(
        user_phonenumber=user_validation_auth.user_phonenumber).first()

    # If no user is found, a 404 error is raised.
    if existing_user is None:
        raise HTTPException(
            status_code=404, detail="User with this phone number not found")

    # If a user is found, it validates the given user_password against the stored password;
    # if the password is incorrect, a 400 error is raised.
    if not verify_password(user_validation_auth.user_password, existing_user.user_password):
        raise HTTPException(status_code=400, detail="Invalid password")

    return existing_user


def display_existing_user_auth(db: Session, user_id: int):
    # The function fetches a user's data using a given user_id.
    user = db.query(models.UsersAuth).filter_by(user_id=user_id).first()

    # If no user is found, a 404 error is raised.
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


def update_user_auth_by_id(db: Session, user_id: int, updated_user_auth: UsersAuth):
    # The function fetches a user's auth data using a given user_id.
    user = db.query(models.UsersAuth).filter_by(user_id=user_id).first()

    # If no user is found, it raises a 404 error.
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # If a user is found, it then checks if user_phonenumber is the edited attribute.
    if updated_user_auth.user_phonenumber:
        # If yes, it fetches a user's data using the user_phonenumber.
        existing_user = db.query(models.UsersAuth).filter(
            models.UsersAuth.user_phonenumber == updated_user_auth.user_phonenumber).first()

        # If the user already exists based on the provided user_phonenumber, a 404 error is raised.
        if existing_user:
            raise HTTPException(
                status_code=400, detail="User with this phone number already exists")

    # It then check if user_password is the edited attribute.
    if updated_user_auth.user_password:
        # If yes, it converts user_password into hashed_user_password.
        updated_user_auth.user_password = create_hashed_password(
            updated_user_auth.user_password)

    # It then updates only the provided attribute(s) and value(s).
    for attr, value in updated_user_auth.dict().items():
        if attr != "user_id" and hasattr(user, attr) and value is not None:
            setattr(user, attr, value)

    db.commit()
    db.refresh(user)
    return user


def delete_user_by_id(db: Session, user_id: int):
    # The function fetches a user's data using a given user_id.
    user = db.query(models.UsersAuth).filter_by(user_id=user_id).first()

    # If no user is found, it raises a 404 error.
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # If a user is found, delete related data from other tables (Users2FA, UsersClass, UsersMarket, and UsersPrimaryAddress) based on user_id
    db.query(models.Users2FA).filter_by(user_id=user_id).delete()
    db.query(models.UsersClass).filter_by(user_id=user_id).delete()
    db.query(models.UsersMarket).filter_by(user_id=user_id).delete()
    db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).delete()

    # It then query and delete all UsersPonds records with the given user_id
    users_ponds = db.query(models.UsersPonds).filter_by(user_id=user_id).all()
    for user_pond in users_ponds:
        db.delete(user_pond)

    # It then query and delete all UsersHarvestPlan records with the given user_id
    users_harvest_plans = db.query(
        models.UsersHarvestPlan).filter_by(user_id=user_id).all()
    for users_harvest_plan in users_harvest_plans:
        db.delete(users_harvest_plan)

    # It then delete the user auth data
    db.delete(user)

    db.commit()
    return {"message": "User data and related records deleted successfully"}
