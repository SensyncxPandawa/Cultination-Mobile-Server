from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersMarket as MarketSchema
from app.database import get_db

router = APIRouter()

# USERS_MARKET DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# DIPLAY USER DATA
@router.get("/users/{user_id}/market", response_model=MarketSchema, tags=["Users' Market"])
def display_existing_user_market(user_id: int, user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_market(db, user_id, user_market)

@router.get("/users/{user_id}/market/production_capacity", response_model=MarketSchema, tags=["Users' Market"])
def display_existing_user_production_capacity(user_id: int, user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_production_capacity(db, user_id, user_market)

@router.get("/users/{user_id}/market/market_capacity", response_model=MarketSchema, tags=["Users' Market"])
def display_existing_user_market_capacity(user_id: int, user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_market_capacity(db, user_id, user_market)

@router.get("/users/{user_id}/market/market_preference", response_model=MarketSchema, tags=["Users' Market"])
def display_existing_user_market_preference(user_id: int, user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.display_existing_user_market_preference(db, user_id, user_market)

# SET USER DATA
@router.put("/users/{user_id}/market", response_model=MarketSchema, tags=["Users' Market"])
def update_user_market_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.update_user_market_by_id(db, user_id, updated_user_market)

@router.put("/users/{user_id}/market/production_capacity", response_model=MarketSchema, tags=["Users' Market"])
def update_user_production_capacity_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.update_user_production_capacity_by_id(db, user_id, updated_user_market)

@router.put("/users/{user_id}/market/market_capacity", response_model=MarketSchema, tags=["Users' Market"])
def update_user_market_capacity_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.update_user_market_capacity_by_id(db, user_id, updated_user_market)

@router.put("/users/{user_id}/market/market_preference", response_model=MarketSchema, tags=["Users' Market"])
def update_user_market_preference_by_id(user_id: int, updated_user_market: MarketSchema, db: Session = Depends(get_db)):
    return services.update_user_market_preference_by_id(db, user_id, updated_user_market)
