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
def update_enumerator_by_enum_name(enum_name: str, enum_data: Dict):
    return services.update_enumerator_by_enum_name(enum_name, enum_data)

# FETCH LATEST ENUMS
@router.get(
    "/enum/get/all",
    tags=["Enumerator"]
)
def get_all_latest_enumerator():
    return services.get_all_latest_enumerator()

# FETCH ENUM
@router.get(
    "/enum/get/{enum_name}",
    tags=["Enumerator"]
)
def get_specific_latest_enumerator_by_enum_name(enum_name: str):
    return services.get_specific_latest_enumerator_by_enum_name(enum_name)
