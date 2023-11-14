from pydantic import BaseModel, Extra
from typing import Optional


class KolamData(BaseModel):
    id_kolam: Optional[str] = None
    airflow: Optional[float] = None
    ph: Optional[float] = None
    tds: Optional[int] = None
    temperature: Optional[float] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid
