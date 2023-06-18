from pydantic import BaseModel

class Categories(BaseModel):
    category_id: str
    category_name: str

    class Config:
        orm_mode = True