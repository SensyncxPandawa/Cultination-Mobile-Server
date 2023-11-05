from pydantic import BaseModel, Extra, validator
from typing import Optional

class OTPCode(BaseModel):
    otp_code: Optional[int] = None

    @validator('otp_code')
    def check_otp_code(cls, v):
        if v is not None and not (isinstance(v, int) and 1000 <= v <= 9999):
            raise ValueError('OTP code must be a 4-digit integer')
        return v

    class Config:
        extra = Extra.forbid