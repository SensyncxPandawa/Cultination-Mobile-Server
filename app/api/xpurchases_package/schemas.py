from pydantic import BaseModel

class Purchases(BaseModel):
    purchase_id: str
    total_amount: str
    purchase_date: str
    purchase_status: str

    class Config:
        orm_mode = True