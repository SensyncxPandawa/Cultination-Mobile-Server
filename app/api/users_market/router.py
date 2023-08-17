from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Market as MarketSchema
from app.models import Market as MarketModel
from app.database import get_db

router = APIRouter()

# USERS_MARKET DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# DIPLAY USER DATA
@router.get("/users/market/production_capacity/{user_id}", response_model=List[MarketSchema], tags=["Users' Market"])
def display_existing_user_production_capacity(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/users/market/market_capacity/{user_id}", response_model=List[MarketSchema], tags=["Users' Market"])
def display_existing_user_market_capacity(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/users/market/market_preference/{user_id}", response_model=List[MarketSchema], tags=["Users' Market"])
def display_existing_user_market_preference(user_id: int, db: Session = Depends(get_db)):
    return

# SET USER DATA
@router.put("/users/market/{user_id}", response_model=MarketSchema, tags=["Users' Market"])
def update_user_market_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/market/production_capacity/{user_id}", response_model=MarketSchema, tags=["Users' Market"])
def update_user_production_capacity_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/market/market_capacity/{user_id}", response_model=MarketSchema, tags=["Users' Market"])
def update_user_market_capacity_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return

@router.put("/users/market/market_preference/{user_id}", response_model=MarketSchema, tags=["Users' Market"])
def update_user_market_preference_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return
