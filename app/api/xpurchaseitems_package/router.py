from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import PurchaseItems as PurchaseItemsSchema
from app.models import PurchaseItem as PurchaseItemModel
from app.database import get_db

router = APIRouter()

@router.get("/purchaseitems", response_model=List[PurchaseItemsSchema], tags=["Purchase"])
def get_all_purchase_items(db: Session = Depends(get_db)):
    purchase_items = db.query(PurchaseItemModel).all()
    if not purchase_items:
        raise HTTPException(status_code=404, detail="Purchase item data not found")
    return purchase_items

@router.post("/purchaseitems", response_model=List[PurchaseItemsSchema], tags=["Purchase"])
def create_purchase_item(purchase_item: PurchaseItemsSchema, db: Session = Depends(get_db)):
    db_purchase_item = PurchaseItemModel(**purchase_item.dict())
    db.add(db_purchase_item)
    db.commit()
    db.refresh(db_purchase_item)
    return [purchase_item]

@router.get("/purchaseitems/{purchase_item_id}", response_model=List[PurchaseItemsSchema], tags=["Purchase"])
def get_purchase_items_by_purchase_item_id(purchase_item_id: str, db: Session = Depends(get_db)):
    purchase_items = db.query(PurchaseItemModel).filter(PurchaseItemModel.purchase_item_id == purchase_item_id).all()
    if not purchase_items:
        raise HTTPException(status_code=404, detail="Purchase item data not found for the purchase_item ID")
    return purchase_items

@router.get("/purchaseitems/purchase/{purchase_id}", response_model=List[PurchaseItemsSchema], tags=["Purchase"])
def get_purchase_items_by_purchase_id(purchase_id: str, db: Session = Depends(get_db)):
    purchase_items = db.query(PurchaseItemModel).filter(PurchaseItemModel.purchase_id == purchase_id).all()
    if not purchase_items:
        raise HTTPException(status_code=404, detail="Purchase item data not found for the purchase ID")
    return purchase_items

@router.get("/purchaseitems/user/{user_id}", response_model=List[PurchaseItemsSchema], tags=["Purchase"])
def get_purchase_items_by_user_id(user_id: str, db: Session = Depends(get_db)):
    purchase_items = db.query(PurchaseItemModel).filter(PurchaseItemModel.user_id == user_id).all()
    if not purchase_items:
        raise HTTPException(status_code=404, detail="Purchase item data not found for the user ID")
    return purchase_items


@router.put("/purchaseitems/{purchase_item_id}", response_model=PurchaseItemsSchema, tags=["Purchase"])
def update_purchase_item_by_id(purchase_item_id: str, updated_purchase_item: PurchaseItemsSchema, db: Session = Depends(get_db)):
    purchase_item = db.query(PurchaseItemModel).filter(PurchaseItemModel.purchase_item_id == purchase_item_id).first()
    if not purchase_item:
        raise HTTPException(status_code=404, detail="Purchase item data not found for the pond ID")
    for attr, value in updated_purchase_item.dict(exclude_unset=True).items():
        setattr(purchase_item, attr, value)
    db.commit()
    db.refresh(purchase_item)
    return purchase_item

@router.delete("/purchaseitems/{purchase_item_id}", response_model=PurchaseItemsSchema, tags=["Purchase"])
def delete_purchase_item_by_id(purchase_item_id: str, db: Session = Depends(get_db)):
    purchase_item = db.query(PurchaseItemModel).filter(PurchaseItemModel.purchase_item_id == purchase_item_id).first()
    if not purchase_item:
        raise HTTPException(status_code=404, detail="Purchase item not found.")
    db.delete(purchase_item)
    db.commit()
    return purchase_item
