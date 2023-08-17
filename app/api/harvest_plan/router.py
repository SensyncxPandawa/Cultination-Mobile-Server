from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Harvest as HarvestSchema
from app.models import Harvest as HarvestModel
from app.database import get_db

router = APIRouter()

# CREATE USER HARVEST PLAN
@router.post("/users/harvest_plan/{user_id}", response_model=List[HarvestSchema], tags=["Users' Harvest Plan"])
def create_user_harvest_plan(user_auth: HarvestSchema, db: Session = Depends(get_db)):
    return

# DISPLAY USER HARVEST PLAN
@router.get("/users/harvest_plan/{user_id}", response_model=List[HarvestSchema], tags=["Users' Harvest Plan"])
def display_all_existing_user_harvest_plan(user_id: int, db: Session = Depends(get_db)):
    return

# UPDATE USER HARVEST PLAN
@router.put("/users/harvest_plan/{user_id}/{harvest_plan_id}", response_model=HarvestSchema, tags=["Users' Harvest Plan"])
def update_existing_user_harvest_plan_by_harvest_plan_id(user_id: int, updated_user_market: HarvestSchema, db: Session = Depends(get_db)):
    return

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
@router.delete("/users/harvest_plan/{user_id}/{harvest_plan_id}", response_model=HarvestSchema, tags=["Users' Harvest Plan"])
def delete_user_harvest_plan_by_harvest_plan_id(user_id: int, db: Session = Depends(get_db)):
    return
