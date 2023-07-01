from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Products as ProductSchema
from app.models import Product as ProductModel
from app.database import get_db

router = APIRouter()

@router.get("/products", response_model=List[ProductSchema], tags=["Product"])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(ProductModel).all()
    if not products:
        raise HTTPException(status_code=404, detail="Product data not found")
    return products

@router.post("/products", response_model=List[ProductSchema], tags=["Product"])
def create_product(product: ProductSchema, db: Session = Depends(get_db)):
    db_product = ProductModel(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return [product]

@router.get("/products/{product_id}", response_model=List[ProductSchema], tags=["Product"])
def get_products_by_product_id(product_id: str, db: Session = Depends(get_db)):
    products = db.query(ProductModel).filter(ProductModel.product_id == product_id).all()
    if not products:
        raise HTTPException(status_code=404, detail="Product data not found for the product ID")
    return products

@router.get("/products/vendor/{vendor_id}", response_model=List[ProductSchema], tags=["Product"])
def get_products_by_vendor_id(vendor_id: str, db: Session = Depends(get_db)):
    products = db.query(ProductModel).filter(ProductModel.vendor_id == vendor_id).all()
    if not products:
        raise HTTPException(status_code=404, detail="Product data not found for the vendor ID")
    return products

@router.get("/products/category/{category_id}", response_model=List[ProductSchema], tags=["Product"])
def get_products_by_category_id(category_id: str, db: Session = Depends(get_db)):
    products = db.query(ProductModel).filter(ProductModel.category_id == category_id).all()
    if not products:
        raise HTTPException(status_code=404, detail="Product data not found for the category ID")
    return products

@router.put("/products/{product_id}", response_model=ProductSchema, tags=["Product"])
def update_product_by_id(product_id: str, updated_product: ProductSchema, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product data not found for the product ID")
    for attr, value in updated_product.dict(exclude_unset=True).items():
        setattr(product, attr, value)
    db.commit()
    db.refresh(product)
    return product

@router.delete("/products/{product_id}", response_model=ProductSchema, tags=["Product"])
def delete_product_by_id(product_id: str, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found.")
    db.delete(product)
    db.commit()
    return product
