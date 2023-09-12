from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersPrimaryAddress, UsersPondsAddress

# CREATE POND ADDRESS AND SET TO PRIMARY IF THERE IS NO PRIMARY ADDRESS
def create_pond_address(db: Session, user_id: int, user_pond_address: UsersPondsAddress):
    user_exist = db.query(models.UsersAuth).filter_by(user_id=user_id).first()
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    latest_pond_address_id = db.query(func.max(models.UsersPondsAddress.pond_address_id)).scalar() or 0
    new_pond_address_id = latest_pond_address_id + 1

    user_pond = models.UsersPondsAddress(user_id=user_id, pond_address_id=new_pond_address_id, **user_pond_address.dict())
    db.add(user_pond)

    db.commit()

    return user_pond

# DISPLAY USER PRIMARY ADDRESS
def display_existing_user_primary_address(db: Session, user_id: int):
    primary_address = db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).first()
    if primary_address is None:
        raise HTTPException(status_code=404, detail="User's primary address not found")

    return primary_address

# DISPLAY ALL USER POND ADDRESSES (TODO: LIST RESPONSE)
def display_all_existing_user_pond_address(db: Session, user_id: int):
    pond_addresses = db.query(models.UsersPondsAddress).filter_by(user_id=user_id)
    if pond_addresses is None:
        raise HTTPException(status_code=404, detail="User's pond not found")

    return pond_addresses

# DISPLAY CERTAIN USER POND ADDRESS
def display_certain_existing_user_pond_address(db: Session, user_id: int, pond_address_id: int):
    pond_address = db.query(models.UsersPondsAddress).filter(
        models.UsersPondsAddress.user_id == user_id,
        models.UsersPondsAddress.pond_address_id == pond_address_id
    ).first()

    if pond_address is None:
        raise HTTPException(status_code=404, detail="Pond not found")

    return pond_address

# SET PRIMARY ADDRESS
def update_user_primary_address_by_user_id(db: Session, user_id: int, updated_user_primary_address: UsersPrimaryAddress):
    primary_address = db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).first()

    if primary_address is None:
        raise HTTPException(status_code=404, detail="User's primary address not found")

    primary_address.pond_address_id = updated_user_primary_address.pond_address_id

    # Commit changes to the database
    db.commit()

    return primary_address

# UPDATE USER POND ADDRESS
def update_user_pond_address_by_pond_id(db: Session, user_id: int, pond_address_id: int, updated_user_pond_address: UsersPondsAddress):
    pond_address = db.query(models.UsersPondsAddress).filter(
        models.UsersPondsAddress.user_id == user_id,
        models.UsersPondsAddress.pond_address_id == pond_address_id
    ).first()

    if pond_address is None:
        raise HTTPException(status_code=404, detail="User's primary address not found")

    # Update only the provided fields from updated_user_pond_address
    if hasattr(updated_user_pond_address, 'user_address_full'):
        pond_address.user_address_full = updated_user_pond_address.user_address_full
    if hasattr(updated_user_pond_address, 'user_address_province'):
        pond_address.user_address_province = updated_user_pond_address.user_address_province
    if hasattr(updated_user_pond_address, 'user_address_city'):
        pond_address.user_address_city = updated_user_pond_address.user_address_city
    if hasattr(updated_user_pond_address, 'user_address_subdistrict'):
        pond_address.user_address_subdistrict = updated_user_pond_address.user_address_subdistrict
    if hasattr(updated_user_pond_address, 'user_address_zipcode'):
        pond_address.user_address_zipcode = updated_user_pond_address.user_address_zipcode
    if hasattr(updated_user_pond_address, 'user_address_coordinates'):
        pond_address.user_address_coordinates = updated_user_pond_address.user_address_coordinates

    # Commit changes to the database
    db.commit()

    return pond_address

# DELETE USER POND ADDRESS
def delete_user_pond_address_by_pond_id(db: Session, user_id: int, pond_address_id: int):
    # Delete related data from other tables based on user_id
    db.query(models.UsersPondsAddress).filter(
        models.UsersPondsAddress.user_id == user_id,
        models.UsersPondsAddress.pond_address_id == pond_address_id
    ).delete()

    db.commit()

    return {"message": "User data and related records deleted successfully"}