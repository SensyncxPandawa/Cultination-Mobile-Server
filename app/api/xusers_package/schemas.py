from pydantic import BaseModel

class Users(BaseModel):
    user_id: str
    user_email: str
    user_password: str
    user_name: str
    user_contact: str
    user_address: str

    class Config:
        orm_mode = True