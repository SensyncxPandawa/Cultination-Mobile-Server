from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersPonds

# CREATE USER PONDS
def create_user_ponds(db: Session, user_id: int, user_ponds: UsersPonds):
    user_exist = db.query(models.UsersAuth).filter(models.UsersAuth.user_id == user_id).first() or 0
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    latest_pond_id = db.query(func.max(models.UsersPonds.pond_id)).scalar() or 0
    new_pond_id = latest_pond_id + 1 if latest_pond_id is not None else 1

    user_ponds_model = models.UsersPonds(
        user_id=user_id,
        pond_id=new_pond_id,
        user_ponds_pond_name=user_ponds.user_ponds_pond_name,
        user_ponds_fish_type=user_ponds.user_ponds_fish_type,
        user_ponds_start_date=user_ponds.user_ponds_start_date,
        user_ponds_pond_diameter=user_ponds.user_ponds_pond_diameter,
        user_ponds_pond_density=user_ponds.user_ponds_pond_density,
        user_ponds_target_size=user_ponds.user_ponds_target_size
    )

    db.add(user_ponds_model)
    db.commit()

    return user_ponds_model

# DISPLAY USER PONDS
def display_all_existing_user_ponds(db: Session, user_id: int):
    user_exist = db.query(models.UsersAuth).filter(models.UsersAuth.user_id == user_id).first()
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_ponds = db.query(models.UsersPonds).filter(models.UsersPonds.user_id == user_id).all()
    if not user_ponds:
        raise HTTPException(status_code=404, detail="User's ponds not found")

    return user_ponds

# UPDATE USER PONDS BY POND ID
def update_existing_user_ponds_by_pond_id(db: Session, user_id: int, pond_id: int, updated_user_ponds: UsersPonds):
    user_ponds = db.query(models.UsersPonds).filter(
        models.UsersPonds.user_id == user_id,
        models.UsersPonds.pond_id == pond_id
    ).first()

    if user_ponds is None:
        raise HTTPException(status_code=404, detail="User's pond not found")

    # Update the user's data based on the provided input
    for attr, value in updated_user_ponds.dict().items():
        if attr != "user_id" and attr != "pond_id" and hasattr(user_ponds, attr) and value is not None:
            setattr(user_ponds, attr, value)
            
    # Update only the provided fields from updated_user_ponds
    # for field in updated_user_ponds.dict():
        # setattr(user_ponds, field, updated_user_ponds.dict()[field])

    # Commit changes to the database
    db.commit()

    return user_ponds

# DELETE USER PONDS BY POND ID
def delete_user_ponds_by_pond_id(db: Session, user_id: int, pond_id: int):
    # Delete related data from other tables based on user_id
    user_ponds = db.query(models.UsersPonds).filter(
        models.UsersPonds.user_id == user_id,
        models.UsersPonds.pond_id == pond_id
    ).first()

    if user_ponds is None:
        raise HTTPException(status_code=404, detail="User's pond not found")

    db.query(models.UsersPonds).filter(
        models.UsersPonds.user_id == user_id,
        models.UsersPonds.pond_id == pond_id
    ).delete()

    db.commit()

    return {"message": "User pond data deleted successfully"}
