from typing import Optional
from pydantic import BaseModel, Extra, constr

class CommunityCache(BaseModel):
    community_id: Optional[int] = None
    community_province: Optional[constr(max_length=255)] = None
    community_city: Optional[constr(max_length=255)] = None
    community_month: Optional[constr(max_length=255)] = None
    community_fish_type: Optional[constr(max_length=255)] = None
    community_production_total: Optional[int] = None
    community_user_total: Optional[int] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class CommunityCacheQuery(BaseModel):
    community_province: Optional[constr(max_length=255)] = None
    community_city: Optional[constr(max_length=255)] = None
    community_month: Optional[constr(max_length=255)] = None
    community_fish_type: Optional[constr(max_length=255)] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid

class SetCommunityCache(BaseModel):
    community_province: Optional[constr(max_length=255)] = None
    community_city: Optional[constr(max_length=255)] = None
    community_month: Optional[constr(max_length=255)] = None
    community_fish_type: Optional[constr(max_length=255)] = None
    community_production_total: Optional[int] = None
    community_user_total: Optional[int] = None

    class Config:
        from_attributes = True
        extra = Extra.forbid
