from datetime import date
from pydantic import BaseModel, constr, Extra, validator
from typing import Optional

class UsersPonds(BaseModel):
    pond_id: Optional[int] = None
    user_id: Optional[int] = None
    user_ponds_pond_name:  Optional[constr(max_length=255)] = None
    user_ponds_fish_type: Optional[constr(max_length=255)] = None
    user_ponds_start_date: Optional[date] = None
    user_ponds_pond_diameter:  Optional[int] = None
    user_ponds_pond_density: Optional[constr(max_length=255)] = None
    user_ponds_target_size: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetUsersPonds(BaseModel):
    user_ponds_pond_name:  Optional[constr(max_length=255)] = None
    user_ponds_fish_type: Optional[constr(max_length=255)] = None
    user_ponds_start_date: Optional[date] = None
    user_ponds_pond_diameter:  Optional[int] = None
    user_ponds_pond_density: Optional[constr(max_length=255)] = None
    user_ponds_target_size: Optional[constr(max_length=255)] = None
    
    @validator('user_ponds_start_date', pre=True, always=True)
    def parse_date(cls, v):
        if isinstance(v, date):
            return v
        return date.fromisoformat(v)
    class Config:
        from_attributes = True
        extra = Extra.forbid
