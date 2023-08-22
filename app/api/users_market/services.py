from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersMarket

# DISPLAY USER DATA
def display_existing_user_market(db: Session, user_id: int):
    users_market = db.query(models.UsersMarket).filter_by(user_id=user_id).first()
    if users_market is None:
        raise HTTPException(status_code=404, detail="User ID not found")

    return users_market

# SET USER DATA
def update_user_market_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    users_market = db.query(models.UsersMarket).filter_by(user_id=user_id).first()
    if users_market is None:
        raise HTTPException(status_code=404, detail="User class not found")

    # Update only the provided fields from updated_users_class
    if hasattr(updated_users_market, 'user_production_capacity_n'):
        users_market.user_production_capacity_n = updated_users_market.user_production_capacity_n
    if hasattr(updated_users_market, 'user_production_capacity_unit'):
        users_market.user_production_capacity_unit = updated_users_market.user_production_capacity_unit
    if hasattr(updated_users_market, 'user_production_capacity_cycle'):
        users_market.user_production_capacity_cycle = updated_users_market.user_production_capacity_cycle
    if hasattr(updated_users_market, 'user_market_capacity_n'):
        users_market.user_market_capacity_n = updated_users_market.user_market_capacity_n
    if hasattr(updated_users_market, 'user_market_capacity_unit'):
        users_market.user_market_capacity_unit = updated_users_market.user_market_capacity_unit
    if hasattr(updated_users_market, 'user_market_capacity_cycle'):
        users_market.user_market_capacity_cycle = updated_users_market.user_market_capacity_cycle
    if hasattr(updated_users_market, 'user_market_preference'):
        users_market.user_market_preference = updated_users_market.user_market_preference

    # Commit changes to the database
    db.commit()

    return users_market

