from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersPrimaryAddress, UsersPondsAddress

# CREATE POND ADDRESS AND SET TO PRIMARY IF THERE IS NO PRIMARY ADDRESS
def create_pond_address(db: Session, users_ponds: UsersPondsAddress):
    return users_ponds

# DISPLAY USER PRIMARY ADDRESS
def display_existing_user_primary_address(db: Session, user_id: int, users_ponds: UsersPrimaryAddress):
    return users_ponds

# DISPLAY ALL USER POND ADDRESSES (TODO: LIST RESPONSE)
def display_all_existing_user_pond_address(db: Session, user_id: int, users_ponds: UsersPondsAddress):
    return users_ponds

# DISPLAY CERTAIN USER POND ADDRESS
def display_certain_existing_user_pond_address(db: Session, user_id: int, users_ponds: UsersPondsAddress):
    return users_ponds

# SET PRIMARY ADDRESS
def update_user_primary_address_by_user_id(db: Session, user_id: int, updated_user_primary_address: UsersPrimaryAddress):
    return updated_user_primary_address

# UPDATE USER POND ADDRESS
def update_user_pond_address_by_pond_id(db: Session, user_id: int, updated_user_pond_address: UsersPondsAddress):
    return updated_user_pond_address

# DELETE USER POND ADDRESS
def delete_user_pond_address_by_pond_id(db: Session, user_id: int):
    return 