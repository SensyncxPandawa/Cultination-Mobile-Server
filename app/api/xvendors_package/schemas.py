from pydantic import BaseModel

class Vendors(BaseModel):
    vendor_id: str
    vendor_name: str
    vendor_contact: str
    vendor_address: int

    class Config:
        orm_mode = True