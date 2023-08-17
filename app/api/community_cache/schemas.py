from pydantic import BaseModel

class CommunityCache(BaseModel):
    community_id: int
    community_province: str
    community_city: str
    community_month: str
    community_fish_type: str
    community_production_total: int
    community_user_total: int

    class Config:
        orm_mode = True
