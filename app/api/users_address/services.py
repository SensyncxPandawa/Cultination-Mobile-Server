from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersPrimaryAddress, UsersPondsAddress

# CREATE POND ADDRESS AND SET TO PRIMARY IF THERE IS NO PRIMARY ADDRESS
def create_pond_address(db: Session, users_ponds: UsersPondsAddress):
    existing_pond_id = db.query(models.UsersPondsAddress).filter_by(pond_address_id=users_ponds.pond_address_id).first()

    if existing_pond_id:
        raise HTTPException(status_code=409, detail="Pond already exists")

    users_auth = models.UsersPondsAddress(**users_ponds.dict())
    db.add(users_auth)

    db.commit()

    return users_ponds

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