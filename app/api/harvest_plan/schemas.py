from pydantic import BaseModel

class UsersHarvestPlan(BaseModel):
    harvest_plan_id:int
    user_id:int
    user_province:int
    user_city: str
    harvest_plan_start: str
    harvest_plan_end: str
    harvest_plan_dayofcultivation: int
    harvest_plan_readyonmonth: int
    harvest_plan_pond_total: int
    harvest_plan_pond_size: int
    harvest_plan_fish_type: str
    harvest_plan_target_capacity: str
    harvest_plan_target_size: str
    harvest_plan_total_fish: str

    class Config:
        orm_mode = True
