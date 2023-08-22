from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersPondsAddress as PondsSchema
from .schemas import UsersPrimaryAddress as PrimarySchema
from app.database import get_db

router = APIRouter()

# TODO: GET GAPERLU SCHEMA PARAMS, PUT DAN POST PERLU, DELETE GAPERLU
# USERS_PRIMARY_ADDRESS DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# CREATE POND ADDRESS AND SET TO PRIMARY IF THERE IS NO PRIMARY ADDRESS
@router.post("/users/{user_id}/address/pond_address", response_model=PondsSchema, tags=["Users' Address"])
def create_pond_address(user_pond_address: PondsSchema, db: Session = Depends(get_db)):
    return services.create_pond_address(db, user_pond_address)

# DISPLAY USER PRIMARY ADDRESS
@router.get("/users/{user_id}/address/primary_address", response_model=PrimarySchema, tags=["Users' Address"])
def display_existing_user_primary_address(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_primary_address(db, user_id)

# DISPLAY ALL USER POND ADDRESSES
@router.get("/users/{user_id}/address/pond_address", response_model=List[PondsSchema], tags=["Users' Address"])
def display_all_existing_user_pond_address(user_id: int, db: Session = Depends(get_db)):
    return services.display_all_existing_user_pond_address(db, user_id)

# DISPLAY CERTAIN USER POND ADDRESS
@router.get("/users/{user_id}/address/pond_address/{pond_address_id}", response_model=PondsSchema, tags=["Users' Address"])
def display_certain_existing_user_pond_address(user_id: int, pond_address_id: int, db: Session = Depends(get_db)):
    return services.display_certain_existing_user_pond_address(db, user_id, pond_address_id)

# SET PRIMARY ADDRESS
@router.put("/users/{user_id}/address/primary_address", response_model=PrimarySchema, tags=["Users' Address"])
def update_user_primary_address_by_user_id(user_id: int, updated_user_primary_address: PrimarySchema, db: Session = Depends(get_db)):
    return services.update_user_primary_address_by_user_id(db, user_id, updated_user_primary_address)

# UPDATE USER POND ADDRESS
@router.put("/users/{user_id}/address/pond_address/{pond_address_id}", response_model=PondsSchema, tags=["Users' Address"])
def update_user_pond_address_by_pond_id(user_id: int, pond_address_id: int, updated_user_pond_address: PondsSchema, db: Session = Depends(get_db)):
    return services.update_user_pond_address_by_pond_id(db, user_id, pond_address_id, updated_user_pond_address)

# DELETE USER POND ADDRESS
@router.delete("/users/{user_id}/address/pond_address/{pond_address_id}", response_model=None, tags=["Users' Address"])
def delete_user_pond_address_by_pond_id(user_id: int, pond_address_id: int, db: Session = Depends(get_db)):
    return services.delete_user_pond_address_by_pond_id(db, user_id, pond_address_id)
