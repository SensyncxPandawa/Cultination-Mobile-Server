from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersMarket, SetUsersMarket
from app.database import get_db

router = APIRouter()

# USERS_MARKET DATA TABLE IS CREATED AUTOMATICALLY WHEN USER_AUTH IS CREATED

# DISPLAY USER DATA
@router.get("/users/{user_id}/market", response_model=UsersMarket, tags=["Users' Market"])
def display_existing_user_market(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_market(db, user_id)

# SET USER DATA
@router.put("/users/{user_id}/market", response_model=UsersMarket, tags=["Users' Market"])
def update_user_market_by_id(user_id: int, updated_user_market: SetUsersMarket, db: Session = Depends(get_db)):
    return services.update_user_market_by_id(db, user_id, updated_user_market)
