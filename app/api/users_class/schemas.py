from typing import Optional
from pydantic import BaseModel, Extra, constr

# USER AGE IS AUTOMATICALLY CREATED FROM USER_BIRTHDATE (USER_AUTH) DATA

class UsersClass(BaseModel):
    user_id: Optional[int] = None
    user_age: Optional[int] = None
    user_proficiency_level: Optional[constr(max_length=50)] = None
    user_pond_total: Optional[constr(max_length=50)] = None
    user_pond_size_range: Optional[constr(max_length=255)] = None
    user_fish_type: Optional[constr(max_length=255)] = None
    user_fish_size_preference: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetUsersClass(BaseModel):
    user_age: Optional[int] = None
    user_proficiency_level: Optional[constr(max_length=50)] = None
    user_pond_total: Optional[constr(max_length=50)] = None
    user_pond_size_range: Optional[constr(max_length=255)] = None
    user_fish_type: Optional[constr(max_length=255)] = None
    user_fish_size_preference: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid
