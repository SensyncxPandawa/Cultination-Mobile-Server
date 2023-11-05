from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersMarket

def display_existing_user_market(db: Session, user_id: int):
    # The function fetches a user's data using the user_id.
    user_market = db.query(models.UsersMarket).filter_by(user_id=user_id).first()

    # If no user is found, a 404 error is raised.
    if user_market is None:
        raise HTTPException(status_code=404, detail="User ID not found")

    return user_market

def update_user_market_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    # The function fetches a user's data using a given user_id.
    user_market = db.query(models.UsersMarket).filter_by(user_id=user_id).first()

    # If no user is found, it raises a 404 error.
    if user_market is None:
        raise HTTPException(status_code=404, detail="User class not found")

    # If a user is found, the code updates only the provided attribute(s) and value(s).
    for attr, value in updated_users_market.dict().items():
        if attr != "user_id" and hasattr(user_market, attr) and value is not None:
            setattr(user_market, attr, value)

    db.commit()
    return user_market

