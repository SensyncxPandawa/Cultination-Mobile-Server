from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersAuth, UsersValidationAuth

# [POST] CREATE ALL USER DATA TABLE (NOT ONLY AUTH)
def create_user(db: Session, user_auth: UsersAuth):
    latest_user_id = db.query(func.max(models.UsersAuth.user_id)).scalar() or 0
    new_user_id = latest_user_id + 1

    users_auth = models.UsersAuth(user_id=new_user_id, **user_auth.dict())
    db.add(users_auth)

    users_2fa = models.Users2FA(user_id=users_auth.user_id)
    db.add(users_2fa)

    users_class = models.UsersClass(user_id=users_auth.user_id)
    db.add(users_class)

    users_market = models.UsersMarket(user_id=users_auth.user_id)
    db.add(users_market)

    users_primary_address = models.UsersPrimaryAddress(user_id=users_auth.user_id)
    db.add(users_primary_address)

    db.commit()

    return users_auth

# [POST] VALIDATE LOGIN REQUEST
def validate_user_auth(db: Session, user_validation_auth: UsersValidationAuth):
    if (user_validation_auth.user_email):
        # print(user_validation_auth.user_email)
        user = db.query(models.UsersAuth).filter_by(user_email=user_validation_auth.user_email).first()
    elif (user_validation_auth.user_phonenumber):
        # print(user_validation_auth.user_phonenumber)
        user = db.query(models.UsersAuth).filter_by(user_phonenumber=user_validation_auth.user_phonenumber).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user.user_password != user_validation_auth.user_password:
        raise HTTPException(status_code=400, detail="Invalid password")

    return user

# [GET] DISPLAY USER AUTHENTIFICATION DATA
def display_existing_user_auth(db: Session, user_id: int):
    user = db.query(models.UsersAuth).filter_by(user_id=user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user

# [PUT] EDIT USER AUTHENTIFICATION DATA
def update_user_auth_by_id(db: Session, user_id: int, updated_user_auth: UsersAuth):
    user = db.query(models.UsersAuth).filter_by(user_id=user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Update the user's data based on the provided input
    for attr, value in updated_user_auth.dict().items():
        if attr != "user_id" and hasattr(user, attr) and value is not None:
            setattr(user, attr, value)

    db.commit()
    db.refresh(user)

    return user

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
def delete_user_by_id(db: Session, user_id: int):
    # Delete related data from other tables based on user_id
    db.query(models.Users2FA).filter_by(user_id=user_id).delete()
    db.query(models.UsersClass).filter_by(user_id=user_id).delete()
    db.query(models.UsersMarket).filter_by(user_id=user_id).delete()
    db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).delete()

    # Query and delete all UsersHarvestPlan records with the given user_id
    users_harvest_plans = db.query(models.UsersHarvestPlan).filter_by(user_id=user_id).all()
    for users_harvest_plan in users_harvest_plans:
        db.delete(users_harvest_plan)

    # Query and delete user data from users_auth table
    user = db.query(models.UsersAuth).filter_by(user_id=user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User data and related records deleted successfully"}
