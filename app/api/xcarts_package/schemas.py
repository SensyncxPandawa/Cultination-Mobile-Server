from pydantic import BaseModel

class Carts(BaseModel):
    cart_id: str
    product_id: str
    product_vendor_id: str
    user_id: str
    quantity: int

    class Config:
        orm_mode = True