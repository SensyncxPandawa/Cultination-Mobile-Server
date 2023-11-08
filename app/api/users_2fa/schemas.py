from pydantic import BaseModel, Extra
from typing import Optional


class OTPCode(BaseModel):
    otp_code: Optional[int] = None

    class Config:
        extra = Extra.forbid
