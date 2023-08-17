from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import CommunityCache as CommunitySchema
from app.models import CommunityCache as CommunityModel
from app.database import get_db

router = APIRouter()

# COMMUNITY CACHE DATA IS REFRESHED EVERYTIME USER CREATE NEW HARVEST PLAN

# UPDATE COMMUNITY CACHE
@router.put("/community/harvest_cache/update/{harvest_plan_id}", response_model=CommunitySchema, tags=["Community Cache"])
def update_community_cache_by_harvest_plan_id(user_id: int, updated_community_cache: CommunitySchema, db: Session = Depends(get_db)):
    return

# DIPLAY COMMUNITY CACHE
@router.get("/community/harvest_cache", response_model=List[CommunitySchema], tags=["Community Cache"])
def display_community_cache_this_month(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/community/harvest_cache/province/{community_province}", response_model=List[CommunitySchema], tags=["Community Cache"])
def display_community_cache_this_month_by_province(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/community/harvest_cache/city/{community_city}", response_model=List[CommunitySchema], tags=["Community Cache"])
def display_community_cache_this_month_by_city(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/community/harvest_cache/fish_type/{community_fish_type}", response_model=List[CommunitySchema], tags=["Community Cache"])
def display_community_cache_this_month_by_fish_type(user_id: int, db: Session = Depends(get_db)):
    return

@router.get("/community/harvest_cache/month/{community_month}", response_model=List[CommunitySchema], tags=["Community Cache"])
def display_community_cache_by_month(user_id: int, db: Session = Depends(get_db)):
    return
