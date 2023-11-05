from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersClass, SetUsersClass
from app.database import get_db

router = APIRouter()

@router.get(
    "/users/{user_id}/class",
    response_model=UsersClass,
    tags=["Users' Class"]
)
def display_existing_user_class(user_id: int, db: Session = Depends(get_db)):
    """
    The function fetches a user's class data using the user_id.
    \n If no user is found, a 404 error is raised.
    \n The function returns the retrieved user's class data.
    """
    return services.display_existing_user_class(db, user_id)

@router.put(
    "/users/{user_id}/class",
    response_model=UsersClass,
    tags=["Users' Class"]
)
def update_user_class_by_user_id(user_id: int, updated_user_class: SetUsersClass, db: Session = Depends(get_db)):
    """
    The function fetches a user's class data using a given user_id.
    \n If no user is found, it raises a 404 error.
    \n If a user is found, the code updates only the provided attribute(s) and value(s).
    \n The function returns the retrieved user's class data.
    """
    return services.update_user_class_by_user_id(db, user_id, updated_user_class)
