from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import UsersHarvestPlan

# CREATE USER HARVEST PLAN
def create_user_harvest_plan(db: Session, user_id: int, user_harvest_plan: UsersHarvestPlan):

    user_exist = db.query(models.UsersAuth).filter_by(user_id=user_id).first()
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    latest_harvest_plan_id = db.query(func.max(models.UsersHarvestPlan.harvest_plan_id)).scalar() or 0
    new_harvest_plan_id = latest_harvest_plan_id + 1


    user_harvest_plan = models.UsersHarvestPlan(user_id=user_id, harvest_plan_id=new_harvest_plan_id, **user_harvest_plan.dict())

    db.add(user_harvest_plan)

    db.commit()

    return user_harvest_plan


# DISPLAY USER HARVEST PLAN
def display_all_existing_user_harvest_plan(db: Session, user_id: int):
    user_exist = db.query(models.UsersAuth).filter_by(user_id=user_id).first()
    if user_exist is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_harvest_plan = db.query(models.UsersHarvestPlan).filter_by(user_id=user_id)
    if user_harvest_plan.first() is None:
        raise HTTPException(status_code=404, detail="User's harvest plan not found")

    return user_harvest_plan

# UPDATE USER HARVEST PLAN
def update_existing_user_harvest_plan_by_harvest_plan_id(db: Session, user_id: int, harvest_plan_id: int, updated_user_harvest_plan: UsersHarvestPlan):
    user_harvest_plan = db.query(models.UsersHarvestPlan).filter(
        models.UsersHarvestPlan.user_id == user_id,
        models.UsersHarvestPlan.harvest_plan_id == harvest_plan_id
    ).first()

    if user_harvest_plan is None:
        raise HTTPException(status_code=404, detail="User's harvest plan not found")

    # Update only the provided fields from updated_user_harvest_plan
    if hasattr(updated_user_harvest_plan, 'user_province'):
        user_harvest_plan.user_province = updated_user_harvest_plan.user_province
    if hasattr(updated_user_harvest_plan, 'user_city'):
        user_harvest_plan.user_city = updated_user_harvest_plan.user_city
    if hasattr(updated_user_harvest_plan, 'harvest_plan_start'):
        user_harvest_plan.harvest_plan_start = updated_user_harvest_plan.harvest_plan_start
    if hasattr(updated_user_harvest_plan, 'harvest_plan_end'):
        user_harvest_plan.harvest_plan_end = updated_user_harvest_plan.harvest_plan_end
    if hasattr(updated_user_harvest_plan, 'harvest_plan_dayofcultivation'):
        user_harvest_plan.harvest_plan_dayofcultivation = updated_user_harvest_plan.harvest_plan_dayofcultivation
    if hasattr(updated_user_harvest_plan, 'harvest_plan_readyonmonth'):
        user_harvest_plan.harvest_plan_readyonmonth = updated_user_harvest_plan.harvest_plan_readyonmonth
    if hasattr(updated_user_harvest_plan, 'harvest_plan_pond_total'):
        user_harvest_plan.harvest_plan_pond_total = updated_user_harvest_plan.harvest_plan_pond_total
    if hasattr(updated_user_harvest_plan, 'harvest_plan_pond_size'):
        user_harvest_plan.harvest_plan_pond_size = updated_user_harvest_plan.harvest_plan_pond_size
    if hasattr(updated_user_harvest_plan, 'harvest_plan_fish_type'):
        user_harvest_plan.harvest_plan_fish_type = updated_user_harvest_plan.harvest_plan_fish_type
    if hasattr(updated_user_harvest_plan, 'harvest_plan_target_capacity'):
        user_harvest_plan.harvest_plan_target_capacity = updated_user_harvest_plan.harvest_plan_target_capacity
    if hasattr(updated_user_harvest_plan, 'harvest_plan_target_size'):
        user_harvest_plan.harvest_plan_target_size = updated_user_harvest_plan.harvest_plan_target_size
    if hasattr(updated_user_harvest_plan, 'harvest_plan_total_fish'):
        user_harvest_plan.harvest_plan_total_fish = updated_user_harvest_plan.harvest_plan_total_fish

    # Commit changes to the database
    db.commit()

    return user_harvest_plan

# DELETE ALL USER DATA TABLE (NOT ONLY AUTH)
def delete_user_harvest_plan_by_harvest_plan_id(db: Session, user_id: int, harvest_plan_id: int):
    # Delete related data from other tables based on user_id
    db.query(models.UsersHarvestPlan).filter(
        models.UsersHarvestPlan.user_id == user_id,
        models.UsersHarvestPlan.harvest_plan_id == harvest_plan_id
    ).delete()

    db.commit()

    return {"message": "User data and related records deleted successfully"}
