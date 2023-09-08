from typing import Dict
from fastapi import APIRouter
from . import services

router = APIRouter()

'''
ENUM DATA IS FETCHED EVERYTIME USER OPEN APP
'''

# UPDATE ENUM
@router.put(
    "/enum/update/{enum_name}",
    tags=["Enumerator"]
)
async def update_enumerator_by_enum_name(enum_name: str, enum_data: Dict):
    return await services.update_enumerator_by_enum_name(enum_name, enum_data)

# FETCH LATEST ENUMS
@router.get(
    "/enum/get/all",
    tags=["Enumerator"]
)
async def get_all_latest_enumerator():
    return await services.get_all_latest_enumerator()

# FETCH ENUM
@router.get(
    "/enum/get/{enum_name}",
    tags=["Enumerator"]
)
async def get_specific_latest_enumerator_by_enum_name(enum_name: str):
    return await services.get_specific_latest_enumerator_by_enum_name(enum_name)
