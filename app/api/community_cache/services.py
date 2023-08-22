from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app import models
from .schemas import CommunityCache, UsersHarvestPlan

# UPDATE COMMUNITY CACHE
def update_community_cache_by_harvest_plan_id(db: Session, harvest_plan_id: int, updated_community_cache: CommunityCache):
    harvest_plan = db.query(models.UsersHarvestPlan).filter_by(harvest_plan_id=harvest_plan_id).first()

    if harvest_plan is None:
        raise HTTPException(status_code=409, detail="Harvest plan not found")

    community_cache = db.query(models.CommunityCache).filter(
        models.CommunityCache.community_city == harvest_plan.user_city,
        models.CommunityCache.community_month == harvest_plan.harvest_plan_readyonmonth,
        models.CommunityCache.community_fish_type == harvest_plan.harvest_plan_fish_type
    ).first()

    if community_cache:
        if hasattr(updated_community_cache, 'community_production_total'):
            community_cache.community_production_total = updated_community_cache.community_production_total
        if hasattr(updated_community_cache, 'community_user_total'):
            community_cache.community_user_total = updated_community_cache.community_user_total
    else:
        community_cache = models.CommunityCache(**community_cache.dict())
        db.add(community_cache)
        db.commit()

    return community_cache

# DISPLAY COMMUNITY CACHE
def display_community_cache_this_month(db: Session):
    current_month = datetime.now().month

    community_cache = db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == current_month
    ).first()

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

def display_community_cache_this_month_by_province(db: Session, community_province: str):
    current_month = datetime.now().month

    community_cache = db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == current_month,
        models.CommunityCache.community_province == community_province
    ).first()

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

def display_community_cache_this_month_by_city(db: Session, community_city: str):
    current_month = datetime.now().month

    community_cache = db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == current_month,
        models.CommunityCache.community_city == community_city
    ).first()

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

def display_community_cache_this_month_by_fish_type(db: Session, community_fish_type: str):
    current_month = datetime.now().month

    community_cache = db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == current_month,
        models.CommunityCache.community_fish_type == community_fish_type
    ).first()

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

def display_community_cache_by_month(db: Session, community_month: str):
    community_cache = db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == community_month
    ).first()

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache
