from typing import Optional
from pydantic import BaseModel, Extra, constr

class UsersHarvestPlan(BaseModel):
    harvest_plan_id: Optional[int] = None
    user_id: Optional[int] = None
    user_province: Optional[constr(max_length=255)] = None
    user_city: Optional[constr(max_length=255)] = None
    harvest_plan_start: Optional[constr(max_length=255)] = None
    harvest_plan_end: Optional[constr(max_length=255)] = None
    harvest_plan_dayofcultivation:  Optional[int] = None
    harvest_plan_readyonmonth:  Optional[int] = None
    harvest_plan_pond_total:  Optional[int] = None
    harvest_plan_pond_size:  Optional[int] = None
    harvest_plan_fish_type: Optional[constr(max_length=255)] = None
    harvest_plan_target_capacity: Optional[constr(max_length=255)] = None
    harvest_plan_target_size: Optional[constr(max_length=255)] = None
    harvest_plan_total_fish: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class PostHarvestPlan(BaseModel):
    user_province: Optional[constr(max_length=255)] = None
    user_city: Optional[constr(max_length=255)] = None
    harvest_plan_start: Optional[constr(max_length=255)] = None
    harvest_plan_end: Optional[constr(max_length=255)] = None
    harvest_plan_dayofcultivation:  Optional[int] = None
    harvest_plan_readyonmonth:  Optional[int] = None
    harvest_plan_pond_total:  Optional[int] = None
    harvest_plan_pond_size:  Optional[int] = None
    harvest_plan_fish_type: Optional[constr(max_length=255)] = None
    harvest_plan_target_capacity: Optional[constr(max_length=255)] = None
    harvest_plan_target_size: Optional[constr(max_length=255)] = None
    harvest_plan_total_fish: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid
