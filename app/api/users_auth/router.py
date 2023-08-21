from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersAuth, UsersValidationAuth, DisplayUsersAuth, DisplayUsersValidationAuth
from app.database import get_db

router = APIRouter()

# CREATE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.post(
    "/users/auth",
    response_model=DisplayUsersAuth,
    tags=["Users' Auth"],
    summary="REGISTERING NEW USER | CREATE ALL USER DATA TABLE (NOT ONLY USERS_AUTH)",
)
def create_user(user_auth: UsersAuth, db: Session = Depends(get_db)):
    """
    The code creates a new user's authentication data and related information in a database, checking if the user already exists based on the provided user_id.
    If not, it adds records to various related tables and returns the created user's authentication data (without the password).

    - **user_id**: integer (would also create users_2fa, users_class, users_market, users_primary_address row table with this user_id)
    - **user_fullname**: string with max_length=255
    - **user_birthdate**: date
    - **user_phonenumber**: PhoneNumber lib (automatically convert to 'tel:+62-811-1111-111' format)
    - **user_email**: EmailStr lib
    - **user_password**: string with max_length=255 (would be omitted in the successful response body)
    """
    return services.create_user(db, user_auth)

# VALIDATE LOGIN REQUEST
@router.post("/users/auth/{user_id}", response_model=DisplayUsersValidationAuth, tags=["Users' Auth"])
def validate_user_auth(user_validation_auth: UsersValidationAuth, db: Session = Depends(get_db)):
    return services.validate_user_auth(db, user_validation_auth)

# DISPLAY USER AUTHENTIFICATION DATA
@router.get("/users/auth/{user_id}", response_model=DisplayUsersAuth, tags=["Users' Auth"])
def display_existing_user_auth(user_id: int, db: Session = Depends(get_db)):
    return services.display_existing_user_auth(db, user_id)

# EDIT USER AUTHENTIFICATION DATA (IT CAN ALSO EDIT INDIVIDUAL ATTRIBUTE)
@router.put("/users/auth/{user_id}", response_model=DisplayUsersAuth, tags=["Users' Auth"])
def update_user_auth_by_id(user_id: int, updated_user_auth: UsersAuth, db: Session = Depends(get_db)):
    return services.update_user_auth_by_id(db, user_id, updated_user_auth)

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.delete("/users/auth/{user_id}", response_model=None, tags=["Users' Auth"])
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return services.delete_user_by_id(db, user_id)
