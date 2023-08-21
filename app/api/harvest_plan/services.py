from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersHarvestPlan

# CREATE USER HARVEST PLAN
def create_user_harvest_plan(db: Session, user_harvest_plan: UsersHarvestPlan):
    return user_harvest_plan

# DISPLAY USER HARVEST PLAN
def display_all_existing_user_harvest_plan(db: Session, user_id: int, user_harvest_plan: UsersHarvestPlan):
    return user_harvest_plan

# UPDATE USER HARVEST PLAN
def update_existing_user_harvest_plan_by_harvest_plan_id(db: Session, user_id: int, updated_user_harvest_plan: UsersHarvestPlan):
    return updated_user_harvest_plan

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
def delete_user_harvest_plan_by_harvest_plan_id(db: Session, user_id: int):
    return 

