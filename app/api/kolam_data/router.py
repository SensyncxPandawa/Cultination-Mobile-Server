from fastapi import Depends, APIRouter
from typing import List
from sqlalchemy.orm import Session
from . import services
from .schemas import KolamData
from app.database import get_db

router = APIRouter()


@router.post(
    "/api/kolam_data",
    response_model=KolamData,
    tags=["Data Kolam"]
)
def post_kolam_data(kolam_data: KolamData, db: Session = Depends(get_db)):
    return services.post_kolam_data(db, kolam_data)


@router.get(
    "/api/kolam_data/{id_kolam}",
    response_model=List[KolamData],
    tags=["Data Kolam"]
)
def fetch_certain_kolam_data(id_kolam: str, db: Session = Depends(get_db)):
    return services.fetch_certain_kolam_data(db, id_kolam)


@router.put(
    "/api/kolam_data/{id}",
    response_model=KolamData,
    tags=["Data Kolam"]
)
def update_existing_kolam_data_by_id(idk: int, updated_kolam_data: KolamData, db: Session = Depends(get_db)):
    return services.update_existing_kolam_data_by_id(db, idk, updated_kolam_data)


@router.delete(
    "/api/kolam_data/{id}",
    response_model=None,
    tags=["Data Kolam"]
)
def delete_kolam_data_by_id(idk: int, db: Session = Depends(get_db)):
    return services.delete_kolam_data_by_id(db, idk)
