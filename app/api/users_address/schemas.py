from pydantic import BaseModel

class Primary(BaseModel):
    user_id:int
    pond_address_id:int

    class Config:
        orm_mode = True

class Ponds(BaseModel):
    pond_address_id:int
    user_id:int
    user_address_full: str
    user_address_province: str
    user_address_city: str
    user_address_subdistrict: str
    user_address_zipcode: str
    user_address_coordinates: str

    class Config:
        orm_mode = True
