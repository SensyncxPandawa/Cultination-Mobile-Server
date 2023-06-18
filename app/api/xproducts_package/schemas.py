from pydantic import BaseModel

class Products(BaseModel):
    product_id: str
    vendor_id: str
    category_id: str
    product_name: str
    product_description: str
    product_images_path: str
    product_discount: str
    product_price: str
    product_stock: str

    class Config:
        orm_mode = True