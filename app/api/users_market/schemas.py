from pydantic import BaseModel

class UsersMarket(BaseModel):
    user_id:int
    user_production_capacity_n:int
    user_production_capacity_unit: str
    user_production_capacity_cycle: str
    user_market_capacity_n: str
    user_market_capacity_unit: str
    user_market_capacity_cycle: str
    user_market_preference: str

    class Config:
        orm_mode = True