from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersClass

# DISPLAY USER DATA
def display_existing_user_class(db: Session, user_id: int):
    # The function fetches a user's data using the user_id.
    users_class = db.query(models.UsersClass).filter_by(user_id=user_id).first()
    
    # If no user is found, a 404 error is raised.
    if users_class is None:
        raise HTTPException(status_code=404, detail="User ID not found")

    return users_class

# SET USER DATA
def update_user_class_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    # The function fetches a user's data using a given user_id.
    user_class = db.query(models.UsersClass).filter_by(user_id=user_id).first()

    # If no user is found, it raises a 404 error.
    if user_class is None:
        raise HTTPException(status_code=404, detail="User class not found")

    # If a user is found, the code updates only the provided attribute(s) and value(s).
    for attr, value in updated_users_class.dict().items():
        if attr != "user_id" and hasattr(user_class, attr) and value is not None:
            setattr(user_class, attr, value)

    db.commit()
    return user_class
