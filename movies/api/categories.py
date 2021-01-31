from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from movies import schemas, models
from movies.dependencies import get_db

router = APIRouter()


@router.get("/", response_model=List[schemas.Category])
def get_categories_list(db: Session = Depends(get_db)):
    """
    Gets the categories list
    """
    categories = db.query(models.Category).all()
    return categories


@router.get("/{category_id}", response_model=schemas.Category)
def get_category_details(category_id: int, db: Session = Depends(get_db)):
    """
    Get details for single category
    """
    category = db.query(models.Category).get(category_id)
    if category is None:
        raise HTTPException(404, "Category not found.")
    return category
