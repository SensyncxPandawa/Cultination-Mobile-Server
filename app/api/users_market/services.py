from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersMarket

# DIPLAY USER DATA
def display_existing_user_market(db: Session, user_id: int, users_market: UsersMarket):
    return users_market

def display_existing_user_production_capacity(db: Session, user_id: int, users_market: UsersMarket):
    return users_market

def display_existing_user_market_capacity(db: Session, user_id: int, users_market: UsersMarket):
    return users_market

def display_existing_user_market_preference(db: Session, user_id: int, users_market: UsersMarket):
    return users_market

# SET USER DATA
def update_user_market_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    return updated_users_market

def update_user_production_capacity_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    return updated_users_market

def update_user_market_capacity_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    return updated_users_market

def update_user_market_preference_by_id(db: Session, user_id: int, updated_users_market: UsersMarket):
    return updated_users_market
