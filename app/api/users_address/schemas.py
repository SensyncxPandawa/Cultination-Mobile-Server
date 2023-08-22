from typing import Optional
from pydantic import BaseModel, Extra, constr

class UsersPrimaryAddress(BaseModel):
    user_id: Optional[int] = None
    pond_address_id: Optional[int] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class UsersPondsAddress(BaseModel):
    pond_address_id: Optional[int] = None
    user_id: Optional[int] = None
    user_address_full: Optional[constr(max_length=255)] = None
    user_address_province: Optional[constr(max_length=255)] = None
    user_address_city: Optional[constr(max_length=255)] = None
    user_address_subdistrict: Optional[constr(max_length=255)] = None
    user_address_zipcode: Optional[constr(max_length=20)] = None
    user_address_coordinates: Optional[constr(max_length=100)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid
