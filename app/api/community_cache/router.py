from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import services
from .schemas import CommunityCache as CommunitySchema, SetCommunityCache as SetCommunitySchema
from app.database import get_db

router = APIRouter()

# COMMUNITY CACHE DATA IS REFRESHED EVERYTIME USER CREATE NEW HARVEST PLAN

# UPDATE COMMUNITY CACHE
@router.put(
    "/community/harvest_cache/update/{harvest_plan_id}",
    response_model=CommunitySchema,
    tags=["Community Cache"]
)
def update_community_cache_by_harvest_plan_id(harvest_plan_id: int, updated_community_cache: SetCommunitySchema, db: Session = Depends(get_db)):
    return services.update_community_cache_by_harvest_plan_id(db, harvest_plan_id, updated_community_cache)

# DISPLAY COMMUNITY CACHE
@router.get(
    "/community/harvest_cache",
    response_model=List[CommunitySchema],
    tags=["Community Cache"]
)
def display_community_cache_this_month(db: Session = Depends(get_db)):
    return services.display_community_cache_this_month(db)

@router.get(
    "/community/harvest_cache/province/{community_province}",
    response_model=List[CommunitySchema],
    tags=["Community Cache"]
)
def display_community_cache_this_month_by_province(community_province: str, db: Session = Depends(get_db)):
    return services.display_community_cache_this_month_by_province(db, community_province)

@router.get(
    "/community/harvest_cache/city/{community_city}",
    response_model=List[CommunitySchema],
    tags=["Community Cache"]
)
def display_community_cache_this_month_by_city(community_city: str, db: Session = Depends(get_db)):
    return services.display_community_cache_this_month_by_city(db, community_city)

@router.get(
    "/community/harvest_cache/fish_type/{community_fish_type}",
    response_model=List[CommunitySchema],
    tags=["Community Cache"]
)
def display_community_cache_this_month_by_fish_type(community_fish_type: str, db: Session = Depends(get_db)):
    return services.display_community_cache_this_month_by_fish_type(db, community_fish_type)

@router.get(
    "/community/harvest_cache/month/{community_month}",
    response_model=List[CommunitySchema],
    tags=["Community Cache"]
)
def display_community_cache_by_month(community_month: str, db: Session = Depends(get_db)):
    return services.display_community_cache_by_month(db, community_month)
