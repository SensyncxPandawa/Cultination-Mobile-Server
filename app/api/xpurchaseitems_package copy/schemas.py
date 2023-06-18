from pydantic import BaseModel

class PurchaseItems(BaseModel):
    purchase_item_id: str
    purchase_id: str
    product_id: str
    quantity: int

    class Config:
        orm_mode = True