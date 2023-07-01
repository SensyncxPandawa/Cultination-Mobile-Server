from fastapi import Depends, APIRouter, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .schemas import Categories as CategoriesSchema
from app.models import Category as CategoryModel
from app.database import get_db

router = APIRouter()

@router.get("/categories", response_model=List[CategoriesSchema], tags=["Category"])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).all()
    if not categories:
        raise HTTPException(status_code=404, detail="Category data not found")
    return categories

@router.post("/categories", response_model=List[CategoriesSchema], tags=["Category"])
def create_category(category: CategoriesSchema, db: Session = Depends(get_db)):
    db_category = CategoryModel(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return [category]

@router.get("/categories/{category_id}", response_model=List[CategoriesSchema], tags=["Category"])
def get_categories_by_category_id(category_id: str, db: Session = Depends(get_db)):
    categories = db.query(CategoryModel).filter(CategoryModel.category_id == category_id).all()
    if not categories:
        raise HTTPException(status_code=404, detail="Category data not found for the category ID")
    return categories

@router.put("/categories/{category_id}", response_model=CategoriesSchema, tags=["Category"])
def update_category_by_id(category_id: str, updated_category: CategoriesSchema, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.category_id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category data not found for the category ID")
    for attr, value in updated_category.dict(exclude_unset=True).items():
        setattr(category, attr, value)
    db.commit()
    db.refresh(category)
    return category

@router.delete("/categories/{category_id}", response_model=CategoriesSchema, tags=["Category"])
def delete_category_by_id(category_id: str, db: Session = Depends(get_db)):
    category = db.query(CategoryModel).filter(CategoryModel.category_id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    db.delete(category)
    db.commit()
    return category
