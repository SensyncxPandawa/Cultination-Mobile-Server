from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersMarket, SetUsersMarket
from app.database import get_db

router = APIRouter()

@router.get(
    "/users/{user_id}/market",
    response_model=UsersMarket,
    tags=["Users' Market"]
)
def display_existing_user_market(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's market data using the user_id.
    \n If no user is found, a 404 error is raised.
    \n The function returns the retrieved user's market data.
    """
    return services.display_existing_user_market(db, user_id)

@router.put(
    "/users/{user_id}/market",
    response_model=UsersMarket,
    tags=["Users' Market"]
)
def update_user_market_by_id(user_id: int, updated_user_market: SetUsersMarket, db: Session = Depends(get_db)):
    """
    The function fetches a user's market data using a given user_id.
    \n If no user is found, it raises a 404 error.
    \n If a user is found, the code updates only the provided attribute(s) and value(s).
    \n The function returns the retrieved user's market data.
    """
    return services.update_user_market_by_id(db, user_id, updated_user_market)
