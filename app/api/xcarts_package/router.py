from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Carts as CartSchema
from app.models import Cart as CartModel
from app.database import get_db

router = APIRouter()

@router.get("/carts", response_model=List[CartSchema], tags=["Cart"])
def get_all_carts(db: Session = Depends(get_db)):
    carts = db.query(CartModel).all()
    if not carts:
        raise HTTPException(status_code=404, detail="Cart data not found")
    return carts

@router.post("/carts", response_model=List[CartSchema], tags=["Cart"])
def create_cart(cart: CartSchema, db: Session = Depends(get_db)):
    db_cart = CartModel(**cart.dict())
    db.add(db_cart)
    db.commit()
    db.refresh(db_cart)
    return [cart]

@router.get("/carts/user/{user_id}", response_model=List[CartSchema], tags=["Cart"])
def get_carts_by_user_id(user_id: str, db: Session = Depends(get_db)):
    carts = db.query(CartModel).filter(CartModel.user_id == user_id).all()
    if not carts:
        raise HTTPException(status_code=404, detail="Cart data not found for the user ID")
    return carts

@router.get("/carts/vendor/{vendor_id}", response_model=List[CartSchema], tags=["Cart"])
def get_carts_by_vendor_id(vendor_id: str, db: Session = Depends(get_db)):
    carts = db.query(CartModel).filter(CartModel.vendor_id == vendor_id).all()
    if not carts:
        raise HTTPException(status_code=404, detail="Cart data not found for the vendor ID")
    return carts


@router.get("/carts/Cart/{cart_id}", response_model=List[CartSchema], tags=["Cart"])
def get_cart_by_cart_id(cart_id: str, db: Session = Depends(get_db)):
    carts = db.query(CartModel).filter(CartModel.cart_id == cart_id).all()
    if not carts:
        raise HTTPException(status_code=404, detail="Cart data not found for the user ID")
    return carts


@router.put("/carts/{cart_id}", response_model=CartSchema, tags=["Cart"])
def update_cart_by_id(cart_id: str, updated_cart: CartSchema, db: Session = Depends(get_db)):
    cart = db.query(CartModel).filter(CartModel.cart_id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart data not found for the pond ID")
    for attr, value in updated_cart.dict(exclude_unset=True).items():
        setattr(cart, attr, value)
    db.commit()
    db.refresh(cart)
    return cart

@router.delete("/carts/{cart_id}", response_model=CartSchema, tags=["Cart"])
def delete_cart_by_id(cart_id: str, db: Session = Depends(get_db)):
    cart = db.query(CartModel).filter(CartModel.cart_id == cart_id).first()
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found.")
    db.delete(cart)
    db.commit()
    return cart
