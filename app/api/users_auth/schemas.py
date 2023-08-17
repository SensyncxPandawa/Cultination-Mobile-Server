from datetime import date
from pydantic import BaseModel

class UsersAuth(BaseModel):
    user_id:int
    user_fullname: str
    user_birthdate: date
    user_phonenumber: str
    user_email: str
    user_password: str

    class Config:
        orm_mode = True