from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from .schemas import KolamData


def post_kolam_data(db: Session, kolam_data: KolamData):
    try:
        latest_idk = db.query(func.max(models.KolamData.id)).scalar() or 0
        new_idk = latest_idk + 1
        kolam = models.KolamData(
            id=new_idk,
            id_kolam=kolam_data.id_kolam,
            airflow=kolam_data.airflow,
            ph=kolam_data.ph,
            tds=kolam_data.tds,
            temperature=kolam_data.temperature
        )
        db.add(kolam)
        db.commit()
        db.refresh(kolam)
        return kolam
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error during database operation: {str(e)}")


def fetch_certain_kolam_data(db: Session, id_kolam: str):
    kolam_data = db.query(models.KolamData).filter(
        models.KolamData.id_kolam == id_kolam).all()
    if not kolam_data:
        raise HTTPException(status_code=404, detail="Kolam Data not found")
    return kolam_data


def update_existing_kolam_data_by_id(db: Session, idk: int, updated_kolam_data: KolamData):
    try:
        kolam_data = db.query(models.KolamData).get(idk)
        if kolam_data is None:
            raise HTTPException(status_code=404, detail="Kolam Data not found")

        for attr, value in updated_kolam_data.dict().items():
            if attr != "id" and attr != "id_kolam" and hasattr(kolam_data, attr) and value is not None:
                setattr(kolam_data, attr, value)

        db.commit()
        db.refresh(kolam_data)
        return kolam_data
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error during database operation: {str(e)}")


def delete_kolam_data_by_id(db: Session, idk: int):
    try:
        kolam_data = db.query(models.KolamData).get(idk)

        if kolam_data is None:
            raise HTTPException(
                status_code=404, detail="User's pond not found")

        db.delete(kolam_data)
        db.commit()
        return {"message": "Kolam Data deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Error during database operation: {str(e)}")
