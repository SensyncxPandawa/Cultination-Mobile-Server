from pydantic import BaseModel

# USER AGE IS AUTOMATICALLY CREATED FROM USER_BIRTHDATE (USER_AUTH) DATA

class UsersClass(BaseModel):
    user_id:int
    user_age: int
    user_proficiency_level: str
    user_pond_total: int
    user_pond_size_range: str
    user_fish_type: str
    user_fish_size_preference: str

    class Config:
        orm_mode = True