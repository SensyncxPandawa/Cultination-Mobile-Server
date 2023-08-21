from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from .schemas import CommunityCache

# UPDATE COMMUNITY CACHE
def update_community_cache_by_harvest_plan_id(db: Session, updated_community_cache: CommunityCache):
    return updated_community_cache

# DIPLAY COMMUNITY CACHE
def display_community_cache_this_month(db: Session, community_cache: CommunityCache):
    return community_cache

def display_community_cache_this_month_by_province(db: Session, community_province: str, community_cache: CommunityCache):
    return community_cache

def display_community_cache_this_month_by_city(db: Session, community_city: str, community_cache: CommunityCache):
    return community_cache

def display_community_cache_this_month_by_fish_type(db: Session, community_fish_type: str, community_cache: CommunityCache):
    return community_cache

def display_community_cache_by_month(db: Session, community_month: str, community_cache: CommunityCache):
    return community_cache
