from typing import Optional
from pydantic import BaseModel, Extra, constr

# TODO UBAH SPESIFIKASI CHARVAR(255) JADI CHARVAR(50), BIKIN ENUM DISINI

class UsersMarket(BaseModel):
    user_id: Optional[int] = None
    user_production_capacity_n: Optional[int] = None
    user_production_capacity_unit: Optional[constr(max_length=255)] = None
    user_production_capacity_cycle: Optional[constr(max_length=255)] = None
    user_market_capacity_n: Optional[constr(max_length=255)] = None
    user_market_capacity_unit: Optional[constr(max_length=255)] = None
    user_market_capacity_cycle: Optional[constr(max_length=255)] = None
    user_market_preference: Optional[constr(max_length=255)] = None

    class Config:
        orm_mode = True
        extra = Extra.forbid