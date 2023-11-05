from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersPrimaryAddress, UsersPondsAddress

def create_pond_address(db: Session, user_id: int, user_pond_address: UsersPondsAddress):
    # The function fetches a user's data using the user_id.
    user_exist = db.query(models.UsersAuth).filter_by(user_id=user_id).first()

    # If no user is found, a 404 error is raised.
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    # It then check if the user has a primary address
    primary_address = db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).first()

    # If no primary address is found, a 404 error is raised.
    if primary_address is None:
        raise HTTPException(status_code=404, detail="User's primary address not found")

    # It then proceed to generate new_pond_address_id 
    latest_pond_address_id = db.query(func.max(models.UsersPondsAddress.pond_address_id)).scalar() or 0
    new_pond_address_id = latest_pond_address_id + 1
    
    # It then fills the UsersPondsAdress table with the new_pond_address_id and the provided attributes and values.    
    user_pond = models.UsersPondsAddress(
        user_id=user_id,
        pond_address_id=new_pond_address_id,
        **user_pond_address.dict()
    )
    db.add(user_pond)

    # It then updates the primary address with the new_pond_address_id.
    primary_address.pond_address_id = new_pond_address_id

    db.commit()
    return user_pond

def display_existing_user_primary_address(db: Session, user_id: int):
    # The function fetches a user's primary address data using a given user_id.
    primary_address = db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).first()

    # If no primary address is found, a 404 error is raised.
    if primary_address is None:
        raise HTTPException(status_code=404, detail="User's primary address not found")

    return primary_address

def display_all_existing_user_pond_address(db: Session, user_id: int):
    # The function fetches all user's pond addresses data using a given user_id.
    pond_addresses = db.query(models.UsersPondsAddress).filter_by(user_id=user_id)

    # If no pond addresses are found, a 404 error is raised.
    if pond_addresses is None:
        raise HTTPException(status_code=404, detail="User's pond addresses not found")

    return pond_addresses

def display_certain_existing_user_pond_address(db: Session, user_id: int, pond_address_id: int):
    # The function fetches a user's pond address data using a given user_id and pond_address_id.
    pond_address = db.query(models.UsersPondsAddress).filter(
        models.UsersPondsAddress.user_id == user_id,
        models.UsersPondsAddress.pond_address_id == pond_address_id
    ).first()

    # If no pond address is found, a 404 error is raised.
    if pond_address is None:
        raise HTTPException(status_code=404, detail="User's pond address not found")

    return pond_address

def update_user_primary_address_by_user_id(db: Session, user_id: int, updated_user_primary_address: UsersPrimaryAddress):
    # The function fetches a user's primary address data using a given user_id.
    primary_address = db.query(models.UsersPrimaryAddress).filter_by(user_id=user_id).first()

    # If no primary address is found, it raises a 404 error.
    if primary_address is None:
        raise HTTPException(status_code=404, detail="User's primary address not found")

    # If a primary address is found, the code updates only the provided attribute(s) and value(s).
    primary_address.pond_address_id = updated_user_primary_address.pond_address_id

    db.commit()
    return primary_address

def update_user_pond_address_by_pond_id(db: Session, user_id: int, pond_address_id: int, updated_user_pond_address: UsersPondsAddress):
    # The function fetches a user's pond address data using a given user_id and pond_address_id.
    pond_address = db.query(models.UsersPondsAddress).filter(
        models.UsersPondsAddress.user_id == user_id,
        models.UsersPondsAddress.pond_address_id == pond_address_id
    ).first()

    # If no pond address is found, it raises a 404 error.
    if pond_address is None:
        raise HTTPException(status_code=404, detail="User's pond address not found")

    # If a pond address is found, the code updates only the provided attribute(s) and value(s).
    for attr, value in updated_user_pond_address.dict().items():
        if attr != "user_id" and attr != "pond_address_id" and hasattr(pond_address, attr) and value is not None:
            setattr(pond_address, attr, value)

    db.commit()
    return pond_address

def delete_user_pond_address_by_pond_id(db: Session, user_id: int, pond_address_id: int):
    # The function fetches a user's pond address data using a given user_id and pond_address_id.
    pond_address = db.query(models.UsersPondsAddress).filter(
        models.UsersPondsAddress.user_id == user_id,
        models.UsersPondsAddress.pond_address_id == pond_address_id
    )
    
    # If no pond address is found, it raises a 404 error.
    if pond_address is None:
        raise HTTPException(status_code=404, detail="User's pond address not found")
    
    # If a pond address is found, delete related data.
    pond_address.delete()

    db.commit()
    return {"message": "User's pond address deleted successfully"}