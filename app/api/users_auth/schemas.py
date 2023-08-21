from datetime import date
from typing import Optional
from pydantic import BaseModel, Extra, EmailStr, constr
from pydantic_extra_types.phone_numbers import PhoneNumber

class UsersAuth(BaseModel):
    user_id: Optional[int] = None
    user_fullname: Optional[constr(max_length=255)] = None
    user_birthdate: Optional[date] = None
    user_phonenumber: Optional[PhoneNumber] = None
    user_email: Optional[EmailStr] = None
    user_password: Optional[constr(max_length=255)] = None

    class Config:
        orm_mode = True
        extra = Extra.forbid

class UsersValidationAuth(BaseModel):
    user_phonenumber: Optional[PhoneNumber] = None
    user_email: Optional[EmailStr] = None
    user_password: constr(max_length=255)

class DisplayUsersAuth(BaseModel):
    user_id: Optional[int] = None
    user_fullname: Optional[constr(max_length=255)] = None
    user_birthdate: Optional[date] = None
    user_phonenumber: Optional[PhoneNumber] = None
    user_email: Optional[EmailStr] = None

class DisplayUsersValidationAuth(BaseModel):
    user_phonenumber: Optional[PhoneNumber] = None
    user_email: Optional[EmailStr] = None
