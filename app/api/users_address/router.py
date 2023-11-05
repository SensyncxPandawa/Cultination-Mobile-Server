from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersPondsAddress as PondsSchema, SetUsersPondsAddress as SetPondsSchema
from .schemas import UsersPrimaryAddress as PrimarySchema, SetUsersPrimaryAddress as SetPrimarySchema
from app.database import get_db

router = APIRouter()

@router.post(
    "/users/{user_id}/pond_address",
    response_model=PondsSchema,
    tags=["Users' Address"]
)
def create_pond_address(user_id: int, user_pond_address: SetPondsSchema, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using the user_id.
    \n If no user is found, a 404 error is raised.
    \n It then check if the user has a primary address
    \n If no primary address is found, a 404 error is raised.
    \n It then proceed to generate new_pond_address_id 
    \n It then fills the UsersPondsAdress table with the new_pond_address_id and the provided attributes and values.
    \n It then updates the primary address with the new_pond_address_id.
    \n The function returns the retrieved user address data.
    """
    return services.create_pond_address(db, user_id, user_pond_address)

@router.get(
    "/users/{user_id}/primary_address",
    response_model=PrimarySchema,
    tags=["Users' Address"]
)
def display_existing_user_primary_address(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's primary address data using a given user_id.
    \n If no primary address is found, a 404 error is raised.
    \n The function returns the retrieved user's primary address data.
    """
    return services.display_existing_user_primary_address(db, user_id)

@router.get(
    "/users/{user_id}/pond_address",
    response_model=List[PondsSchema],
    tags=["Users' Address"]
)
def display_all_existing_user_pond_address(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches all user's pond addresses data using a given user_id.
    \n If no pond addresses are found, a 404 error is raised.    
    \n The function returns the retrieved all user's pond addresses data.
    """
    return services.display_all_existing_user_pond_address(db, user_id)

@router.get(
    "/users/{user_id}/pond_address/{pond_address_id}",
    response_model=PondsSchema,
    tags=["Users' Address"]
)
def display_certain_existing_user_pond_address(user_id: int, pond_address_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's pond address data using a given user_id and pond_address_id.
    \n If no pond address is found, a 404 error is raised.    
    \n The function returns the retrieved user's pond address data.
    """
    return services.display_certain_existing_user_pond_address(db, user_id, pond_address_id)

@router.put(
    "/users/{user_id}/primary_address",
    response_model=PrimarySchema,
    tags=["Users' Address"]
)
def update_user_primary_address_by_user_id(user_id: int, updated_user_primary_address: SetPrimarySchema, db: Session = Depends(get_db)):
    """
    The function fetches a user's primary address data using a given user_id.
    \n If no primary address is found, it raises a 404 error.
    \n If a primary address is found, the code updates only the provided attribute(s) and value(s).    
    \n The function returns the retrieved user's primary address data.
    """
    return services.update_user_primary_address_by_user_id(db, user_id, updated_user_primary_address)

@router.put(
    "/users/{user_id}/pond_address/{pond_address_id}",
    response_model=PondsSchema,
    tags=["Users' Address"]
)
def update_user_pond_address_by_pond_id(user_id: int, pond_address_id: int, updated_user_pond_address: SetPondsSchema, db: Session = Depends(get_db)):
    """
    The function fetches a user's pond address data using a given user_id and pond_address_id.
    \n If no pond address is found, it raises a 404 error.
    \n If a pond address is found, the code updates only the provided attribute(s) and value(s).
    \n The function returns the retrieved user's primary address data.
    """
    return services.update_user_pond_address_by_pond_id(db, user_id, pond_address_id, updated_user_pond_address)

@router.delete(
    "/users/{user_id}/pond_address/{pond_address_id}",
    response_model=None,
    tags=["Users' Address"]
)
def delete_user_pond_address_by_pond_id(user_id: int, pond_address_id: int, db: Session = Depends(get_db)):
    """
    The function fetches pond address data using a given user_id and pond_address_id.
    \n If no pond address is found, it raises a 404 error.
    \n If a pond address is found, delete the data.
    \n The function returns a success message.
    """
    return services.delete_user_pond_address_by_pond_id(db, user_id, pond_address_id)
