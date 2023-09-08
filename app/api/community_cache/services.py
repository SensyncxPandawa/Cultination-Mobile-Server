import calendar
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app import models
from .schemas import CommunityCache, CommunityCacheQuery

# UPDATE COMMUNITY CACHE
async def update_community_cache_by_harvest_plan_id(db: Session, harvest_plan_id: int, updated_community_cache: CommunityCache):
    harvest_plan = await db.query(models.UsersHarvestPlan).filter_by(harvest_plan_id=harvest_plan_id).first()

    if harvest_plan is None:
        raise HTTPException(status_code=409, detail="Harvest plan not found")

    community_cache = await db.query(models.CommunityCache).filter(
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
        await db.add(community_cache)
        await db.commit()

    return community_cache

# DISPLAY COMMUNITY CACHE 
async def display_community_cache_by_query(db: Session, community_cache_query: CommunityCacheQuery):

    community_cache = await db.query(models.CommunityCache)

    if community_cache_query.community_month:
        community_cache = community_cache.filter_by(community_month=community_cache_query.community_month)
    else:
        current_month = datetime.now().month
        month_name = calendar.month_name[current_month]
        community_cache = community_cache.filter_by(community_month=month_name)

    if community_cache_query.community_province:
        community_cache = community_cache.filter_by(community_province=community_cache_query.community_province)
    if community_cache_query.community_city:
        community_cache = community_cache.filter_by(community_city=community_cache_query.community_city)
    if community_cache_query.community_fish_type:
        community_cache = community_cache.filter_by(community_fish_type=community_cache_query.community_fish_type)

    if community_cache is None:
        raise HTTPException(status_code=404, detail="Community cache not found")

    return community_cache

async def display_community_cache_this_month(db: Session):
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]

    community_cache = await db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == month_name
    )

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

async def display_community_cache_this_month_by_province(db: Session, community_province: str):
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]

    community_cache = await db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == month_name,
        models.CommunityCache.community_province == community_province
    )

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

async def display_community_cache_this_month_by_city(db: Session, community_city: str):
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]

    community_cache = await db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == month_name,
        models.CommunityCache.community_city == community_city
    )

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

async def display_community_cache_this_month_by_fish_type(db: Session, community_fish_type: str):
    current_month = datetime.now().month
    month_name = calendar.month_name[current_month]

    community_cache = await db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == month_name,
        models.CommunityCache.community_fish_type == community_fish_type
    )

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

async def display_community_cache_by_month(db: Session, community_month: str):
    community_cache = await db.query(models.CommunityCache).filter(
        models.CommunityCache.community_month == community_month
    )

    if community_cache is None:
        raise HTTPException(status_code=404, detail="This month's community cache not found")

    return community_cache

