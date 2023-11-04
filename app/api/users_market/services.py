from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersMarket

# DISPLAY USER DATA
def display_existing_user_market(db: Session, user_id: int):
    user_market = db.query(models.UsersMarket).filter_by(user_id=user_id).first()
    if user_market is None:
        raise HTTPException(status_code=404, detail="User ID not found")

    return user_market

# SET USER DATA
def update_user_market_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    user_market = db.query(models.UsersMarket).filter_by(user_id=user_id).first()
    if user_market is None:
        raise HTTPException(status_code=404, detail="User class not found")

    # Update the user's data based on the provided input
    for attr, value in updated_users_market.dict().items():
        if attr != "user_id" and hasattr(user_market, attr) and value is not None:
            setattr(user_market, attr, value)

    # Commit changes to the database
    db.commit()

    return user_market

