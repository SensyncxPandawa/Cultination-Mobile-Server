from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersClass

# DIPLAY USER DATA
def display_existing_user_class(db: Session, user_id: int, users_class: UsersClass):
    return users_class

def display_existing_user_proficiency_level(db: Session, user_id: int, users_class: UsersClass):
    return users_class

def display_existing_user_pond_total(db: Session, user_id: int, users_class: UsersClass):
    return users_class

def display_existing_user_pond_size_range(db: Session, user_id: int, users_class: UsersClass):
    return users_class

def display_existing_user_fish_type(db: Session, user_id: int, users_class: UsersClass):
    return users_class

def display_existing_user_fish_size_preference(db: Session, user_id: int, users_class: UsersClass):
    return users_class

# SET USER DATA
def update_user_class_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    return updated_users_class

def update_user_proficiency_level_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    return updated_users_class

def update_user_pond_total_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    return updated_users_class

def update_user_pond_size_range_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    return updated_users_class

def update_user_fish_type_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    return updated_users_class

def update_user_fish_size_preference_by_user_id(db: Session, user_id: int, updated_users_class: UsersClass):
    return updated_users_class