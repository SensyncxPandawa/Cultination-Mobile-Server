from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersClass

# DISPLAY USER DATA
def display_existing_user_class(db: Session, user_id: int):
    users_class = db.query(models.UsersClass).filter_by(user_id=user_id).first()
    if users_class is None:
        raise HTTPException(status_code=404, detail="User ID not found")

    return users_class

# SET USER DATA
def update_user_class_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    user_class = db.query(models.UsersClass).filter_by(user_id=user_id).first()
    if user_class is None:
        raise HTTPException(status_code=404, detail="User class not found")

    # Update the user's data based on the provided input
    for attr, value in updated_users_class.dict().items():
        if attr != "user_id" and hasattr(user_class, attr) and value is not None:
            setattr(user_class, attr, value)

    # Commit changes to the database
    db.commit()

    return user_class
