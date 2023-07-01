from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Vendors as VendorsSchema
from app.models import Vendor as VendorModel
from app.database import get_db

router = APIRouter()

@router.get("/vendors", response_model=List[VendorsSchema], tags=["Vendor"])
def get_all_vendors(db: Session = Depends(get_db)):
    vendors = db.query(VendorModel).all()
    if not vendors:
        raise HTTPException(status_code=404, detail="Vendor data not found")
    return vendors

@router.post("/vendors", response_model=List[VendorsSchema], tags=["Vendor"])
def create_vendor(vendor: VendorsSchema, db: Session = Depends(get_db)):
    db_vendor = VendorModel(**vendor.dict())
    db.add(db_vendor)
    db.commit()
    db.refresh(db_vendor)
    return [vendor]

@router.get("/vendors/{vendor_id}", response_model=List[VendorsSchema], tags=["Vendor"])
def get_vendors_by_vendor_id(vendor_id: str, db: Session = Depends(get_db)):
    vendors = db.query(VendorModel).filter(VendorModel.vendor_id == vendor_id).all()
    if not vendors:
        raise HTTPException(status_code=404, detail="Vendor data not found for the vendor ID")
    return vendors

@router.put("/vendors/{vendor_id}", response_model=VendorsSchema, tags=["Vendor"])
def update_vendor_by_id(vendor_id: str, updated_vendor: VendorsSchema, db: Session = Depends(get_db)):
    vendor = db.query(VendorModel).filter(VendorModel.vendor_id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor data not found for the vendor ID")
    for attr, value in updated_vendor.dict(exclude_unset=True).items():
        setattr(vendor, attr, value)
    db.commit()
    db.refresh(vendor)
    return vendor

@router.delete("/vendors/{vendor_id}", response_model=VendorsSchema, tags=["Vendor"])
def delete_vendor_by_id(vendor_id: str, db: Session = Depends(get_db)):
    vendor = db.query(VendorModel).filter(VendorModel.vendor_id == vendor_id).first()
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found.")
    db.delete(vendor)
    db.commit()
    return vendor
