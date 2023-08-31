from typing import Optional
from pydantic import BaseModel, Extra, constr

# TODO UBAH SPESIFIKASI CHARVAR(25) JADI CHARVAR(50), BIKIN ENUM DISINI

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

class UserProductionCapacity(BaseModel):
    user_id: Optional[int] = None
    user_production_capacity_n: Optional[int] = None
    user_production_capacity_unit: Optional[constr(max_length=25)] = None
    user_production_capacity_cycle: Optional[constr(max_length=25)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetUserProductionCapacity(BaseModel):
    user_production_capacity_n: Optional[int] = None
    user_production_capacity_unit: Optional[constr(max_length=25)] = None
    user_production_capacity_cycle: Optional[constr(max_length=25)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class UserMarketCapacity(BaseModel):
    user_id: Optional[int] = None
    user_market_capacity_n: Optional[int] = None
    user_market_capacity_unit: Optional[constr(max_length=25)] = None
    user_market_capacity_cycle: Optional[constr(max_length=25)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetUserMarketCapacity(BaseModel):
    user_market_capacity_n: Optional[int] = None
    user_market_capacity_unit: Optional[constr(max_length=25)] = None
    user_market_capacity_cycle: Optional[constr(max_length=25)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class UserMarketPreference(BaseModel):
    user_id: Optional[int] = None
    user_market_preference: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetUserMarketPreference(BaseModel):
    user_market_preference: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid