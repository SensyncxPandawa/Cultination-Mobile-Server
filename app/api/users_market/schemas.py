from typing import Optional
from pydantic import BaseModel, Extra, constr

class UsersMarket(BaseModel):
    user_id: Optional[int] = None
    user_production_capacity_n: Optional[int] = None
    user_production_capacity_unit: Optional[constr(max_length=25)] = None
    user_production_capacity_cycle: Optional[constr(max_length=25)] = None
    user_market_capacity_n: Optional[int] = None
    user_market_capacity_unit: Optional[constr(max_length=25)] = None
    user_market_capacity_cycle: Optional[constr(max_length=25)] = None
    user_market_preference: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetUsersMarket(BaseModel):
    user_production_capacity_n: Optional[int] = None
    user_production_capacity_unit: Optional[constr(max_length=25)] = None
    user_production_capacity_cycle: Optional[constr(max_length=25)] = None
    user_market_capacity_n: Optional[int] = None
    user_market_capacity_unit: Optional[constr(max_length=25)] = None
    user_market_capacity_cycle: Optional[constr(max_length=25)] = None
    user_market_preference: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid
