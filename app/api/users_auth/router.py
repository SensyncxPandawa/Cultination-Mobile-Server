from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersAuth, UsersValidationAuth, DisplayUsersAuth, DisplayUsersValidationAuth
from app.database import get_db

router = APIRouter()

# CREATE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.post(
    "/users",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
    summary="REGISTERING NEW USER | CREATE ALL USER DATA TABLE (NOT ONLY USERS_AUTH)",
)
async def create_user(user_auth: UsersAuth, db: Session = Depends(get_db)):
    """
    The function creates a new user's authentication data and related information in a database, checking if the user already exists based on the provided user_id.
    If not, it adds records to various related tables and returns the created user's authentication data (without the password).
    """
    return await services.create_user(db, user_auth)

# VALIDATE LOGIN REQUEST
@router.post(
    "/users/{user_id}",
    response_model=DisplayUsersValidationAuth,
    tags=["Users' Auth"],
    summary="LOGGING IN USER | VALIDATE LOGIN REQUEST",
)
async def validate_user_auth(user_validation_auth: UsersValidationAuth, db: Session = Depends(get_db)):
    """
    The function initially looks for the user_email attribute and queries the database for a matching email.
    If absent, it searches using the user_phonenumber attribute.
    If no user is located, a 404 error occurs.
    If a user is found, it validates the given user_password against the stored password; if incorrect, a 400 error emerges.
    In the end, the function yields the user object upon successful authentication.
    """
    return await services.validate_user_auth(db, user_validation_auth)

# DISPLAY USER AUTHENTIFICATION DATA
@router.get(
    "/users/{user_id}",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
    summary="DISPLAY USER AUTHENTIFICATION DATA",
)
async def display_existing_user_auth(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using a given user_id.
    If no user is found, a 404 error is raised.
    Otherwise, the function returns the retrieved user authentication data.
    """
    return await services.display_existing_user_auth(db, user_id)

# EDIT USER AUTHENTIFICATION DATA (IT CAN ALSO EDIT INDIVIDUAL ATTRIBUTE)
@router.put(
    "/users/{user_id}",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
    summary="EDIT USER AUTHENTIFICATION DATA (IT CAN ALSO EDIT INDIVIDUAL ATTRIBUTE)",
)
async def update_user_auth_by_id(user_id: int, updated_user_auth: UsersAuth, db: Session = Depends(get_db)):
    """
    The function fetches a user's data using a given user_id.
    If no user is found, it raises a 404 error.
    When a user is located, the code updates their information using provided attributes and values.
    It iterates through the attributes of the updated_user_auth object, assigning non-null values to the corresponding user attributes.
    """
    return await services.update_user_auth_by_id(db, user_id, updated_user_auth)

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.delete(
    "/users/{user_id}",
    response_model=None,
    tags=["Users' Auth"],
    summary="DELETE ALL USER DATA TABLE (NOT ONLY AUTH)",
)
async def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """
    The function starts by deleting associated data from different tables such as Users2FA, UsersClass, UsersMarket, and UsersPrimaryAddress based on the provided user_id.
    It then searches and deletes all records from the UsersHarvestPlan table associated with the given user_id.
    Next, the code searches for the user's data in the users_auth table.
    If the user isn't found, a 404 error is raised.
    If the user is located, their record is deleted, and changes are committed to the database.
    """
    return await services.delete_user_by_id(db, user_id)
