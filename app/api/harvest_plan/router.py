from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import services
from .schemas import UsersHarvestPlan as HarvestSchema, SetUserHarvestPlan as SetHarvestSchema
from app.database import get_db

router = APIRouter()

# CREATE USER HARVEST PLAN
@router.post(
    "/users/{user_id}/harvest_plan",
    response_model=HarvestSchema,
    tags=["(DEPRECATED) Users' Harvest Plan"]
)
def create_user_harvest_plan(user_id: int, user_harvest_plan: SetHarvestSchema, db: Session = Depends(get_db)):
    return services.create_user_harvest_plan(db, user_id, user_harvest_plan)

# DISPLAY USER HARVEST PLAN
@router.get(
    "/users/{user_id}/harvest_plan",
    response_model=List[HarvestSchema],
    tags=["(DEPRECATED) Users' Harvest Plan"]
)
def display_all_existing_user_harvest_plan(user_id: int, db: Session = Depends(get_db)):
    return services.display_all_existing_user_harvest_plan(db, user_id)

# UPDATE USER HARVEST PLAN
@router.put(
    "/users/{user_id}/harvest_plan/{harvest_plan_id}",
    response_model=HarvestSchema,
    tags=["(DEPRECATED) Users' Harvest Plan"]
)
def update_existing_user_harvest_plan_by_harvest_plan_id(user_id: int, harvest_plan_id: int, updated_user_harvest_plan: SetHarvestSchema, db: Session = Depends(get_db)):
    return services.update_existing_user_harvest_plan_by_harvest_plan_id(db, user_id, harvest_plan_id, updated_user_harvest_plan)

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.delete(
    "/users/{user_id}/harvest_plan/{harvest_plan_id}",
    response_model=None,
    tags=["(DEPRECATED) Users' Harvest Plan"]
)
def delete_user_harvest_plan_by_harvest_plan_id(user_id: int, harvest_plan_id: int, db: Session = Depends(get_db)):
    return services.delete_user_harvest_plan_by_harvest_plan_id(db, user_id, harvest_plan_id)
