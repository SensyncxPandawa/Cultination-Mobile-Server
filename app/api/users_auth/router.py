from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersAuth, UsersValidationAuth, DisplayUsersAuth, DisplayUsersValidationAuth
from app.database import get_db

router = APIRouter()

@router.post(
    "/users/register",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
)
def create_user(user_auth: UsersAuth, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using the user_phonenumber.
    \n If the user already exists based on the provided user_phonenumber, a 404 error is raised.
    \n If the user isn't exist, it proceed to generate new_user_id.
    \n It then generate hashed_password using the provided user_password.
    \n It then created the UsersAuth table with the provided attributes and values.
    \n It then created various related tables (Users2FA, UsersClass, UsersMarket, and UsersPrimaryAddress).
    \n The function returns the created user's authentication data.
    """
    return services.create_user(db, user_auth)

@router.post(
    "/users/login",
    response_model=DisplayUsersValidationAuth,
    tags=["Users' Auth"],
)
def validate_user_auth(user_validation_auth: UsersValidationAuth, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using the user_phonenumber.
    \n If no user is found, a 404 error is raised.
    \n If a user is found, it validates the given user_password against the stored password;
    \n if the password is incorrect, a 400 error is raised.
    \n The function returns the retrieved user authentication data.
    """
    return services.validate_user_auth(db, user_validation_auth)

@router.get(
    "/users/{user_id}",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
)
def display_existing_user_auth(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using a given user_id.
    \n If no user is found, a 404 error is raised.
    \n The function returns the retrieved user authentication data.
    """
    return services.display_existing_user_auth(db, user_id)

@router.put(
    "/users/{user_id}",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
)
def update_user_auth_by_id(user_id: int, updated_user_auth: UsersAuth, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using a given user_id.
    \n If no user is found, it raises a 404 error.
    \n If a user is found, the code updates only the provided attribute(s) and value(s).
    \n The function returns the retrieved user authentication data.
    """
    return services.update_user_auth_by_id(db, user_id, updated_user_auth)

@router.delete(
    "/users/{user_id}",
    response_model=None,
    tags=["Users' Auth"],
)
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using a given user_id.
    \n If no user is found, it raises a 404 error.
    \n If a user is found, delete related data from other tables (Users2FA, UsersClass, UsersMarket, and UsersPrimaryAddress) based on user_id
    \n It then query and delete all UsersPonds records with the given user_id
    \n It then query and delete all UsersHarvestPlan records with the given user_id
    \n It then delete the user auth data
    \n The function returns a success message.
    """
    return services.delete_user_by_id(db, user_id)
