from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Ponds as PondsSchema
from .schemas import Primary as PrimarySchema
from app.models import Ponds as PondsModel
from app.models import Primary as PrimaryModel
from app.database import get_db

router = APIRouter()

# USERS_PRIMARY_ADDRESS DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# CREATE POND ADDRESS AND SET TO PRIMARY IF THERE IS NO PRIMARY ADDRESS
@router.post("/users/address/pond_address/{user_id}", response_model=List[PondsSchema], tags=["Users"])
def create_pond_address(user_ponds: PondsSchema, db: Session = Depends(get_db)):
    return

# DISPLAY USER PRIMARY ADDRESS
@router.get("/users/address/primary_address/{user_id}", response_model=List[PrimarySchema], tags=["Users"])
def display_existing_user_primary_address(user_id: int, db: Session = Depends(get_db)):
    return

# DISPLAY ALL USER POND ADDRESSES
@router.get("/users/address/pond_address/{user_id}", response_model=List[PondsSchema], tags=["Users"])
def display_all_existing_user_pond_address(user_id: int, db: Session = Depends(get_db)):
    return

# DISPLAY CERTAIN USER POND ADDRESS
@router.get("/users/address/pond_address/{user_id}/{pond_address_id}", response_model=List[PondsSchema], tags=["Users"])
def display_certain_existing_user_pond_address(user_id: int, db: Session = Depends(get_db)):
    return

# SET PRIMARY ADDRESS
@router.put("/users/address/primary_address/{user_id}", response_model=PrimarySchema, tags=["Users"])
def update_user_primary_address_by_user_id(user_id: int, updated_user_primary_address: PrimarySchema, db: Session = Depends(get_db)):
    return

# UPDATE USER POND ADDRESS
@router.put("/users/address/pond_address/{user_id}/{pond_address_id}", response_model=PondsSchema, tags=["Users"])
def update_user_pond_address_by_pond_id(user_id: int, updated_user_pond_address: PondsSchema, db: Session = Depends(get_db)):
    return

# DELETE USER POND ADDRESS
@router.delete("/users/address/pond_address/{user_id}/{pond_address_id}", response_model=PondsSchema, tags=["Users"])
def delete_user_pond_address_by_pond_id(user_id: int, db: Session = Depends(get_db)):
    return
