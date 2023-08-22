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

    # Update only the provided fields from updated_users_class
    if hasattr(updated_users_class, 'user_age'):
        user_class.user_age = updated_users_class.user_age
    if hasattr(updated_users_class, 'user_proficiency_level'):
        user_class.user_proficiency_level = updated_users_class.user_proficiency_level
    if hasattr(updated_users_class, 'user_pond_total'):
        user_class.user_pond_total = updated_users_class.user_pond_total
    if hasattr(updated_users_class, 'user_pond_size_range'):
        user_class.user_pond_size_range = updated_users_class.user_pond_size_range
    if hasattr(updated_users_class, 'user_fish_type'):
        user_class.user_fish_type = updated_users_class.user_fish_type
    if hasattr(updated_users_class, 'user_fish_size_preference'):
        user_class.user_fish_size_preference = updated_users_class.user_fish_size_preference

    # Commit changes to the database
    db.commit()

    return user_class
