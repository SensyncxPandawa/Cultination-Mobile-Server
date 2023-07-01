from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Purchases as PurchaseSchema
from app.models import Purchase as PurchaseModel
from app.database import get_db

router = APIRouter()

@router.get("/purchases", response_model=List[PurchaseSchema], tags=["Purchase"])
def get_all_purchases(db: Session = Depends(get_db)):
    purchases = db.query(PurchaseModel).all()
    if not purchases:
        raise HTTPException(status_code=404, detail="Purchase data not found")
    return purchases

@router.post("/purchases", response_model=List[PurchaseSchema], tags=["Purchase"])
def create_purchase(purchase: PurchaseSchema, db: Session = Depends(get_db)):
    db_purchase = PurchaseModel(**purchase.dict())
    db.add(db_purchase)
    db.commit()
    db.refresh(db_purchase)
    return [purchase]

@router.get("/purchases/{purchase_id}", response_model=List[PurchaseSchema], tags=["Purchase"])
def get_purchases_by_purchase_id(purchase_id: str, db: Session = Depends(get_db)):
    purchases = db.query(PurchaseModel).filter(PurchaseModel.purchase_id == purchase_id).all()
    if not purchases:
        raise HTTPException(status_code=404, detail="Purchase data not found for the purchase ID")
    return purchases

@router.get("/purchases/user/{user_id}", response_model=List[PurchaseSchema], tags=["Purchase"])
def get_purchases_by_user_id(user_id: str, db: Session = Depends(get_db)):
    purchases = db.query(PurchaseModel).filter(PurchaseModel.user_id == user_id).all()
    if not purchases:
        raise HTTPException(status_code=404, detail="Purchase data not found for the user ID")
    return purchases


@router.put("/purchases/{purchase_id}", response_model=PurchaseSchema, tags=["Purchase"])
def update_purchase_by_id(purchase_id: str, updated_purchase: PurchaseSchema, db: Session = Depends(get_db)):
    purchase = db.query(PurchaseModel).filter(PurchaseModel.purchase_id == purchase_id).first()
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase data not found for the purchase ID")
    for attr, value in updated_purchase.dict(exclude_unset=True).items():
        setattr(purchase, attr, value)
    db.commit()
    db.refresh(purchase)
    return purchase

@router.delete("/purchases/{purchase_id}", response_model=PurchaseSchema, tags=["Purchase"])
def delete_purchase_by_id(purchase_id: str, db: Session = Depends(get_db)):
    purchase = db.query(PurchaseModel).filter(PurchaseModel.purchase_id == purchase_id).first()
    if not purchase:
        raise HTTPException(status_code=404, detail="Purchase not found.")
    db.delete(purchase)
    db.commit()
    return purchase
