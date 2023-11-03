from pydantic import BaseModel, Extra, validator
from typing import Optional

class Users2FA(BaseModel):
    user_id: Optional[int] = None
    ota_code: Optional[int] = None

    @validator('ota_code')
    def check_ota_code(cls, v):
        if v is not None and not (isinstance(v, int) and 1000 <= v <= 9999):
            raise ValueError('OTA code must be a 4-digit integer')
        return v

    class Config:
        extra = Extra.forbid