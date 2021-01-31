from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException

from . import schemas, models
from .dependencies import get_db
from .api.users import router as user_router
from .api.movies import router as movies_router


app = FastAPI()

app.include_router(user_router, prefix="/users")
app.include_router(movies_router, prefix="/movies")


@app.get("/categories", response_model=List[schemas.Category])
def get_categories_list(db: Session = Depends(get_db)):
    """
    Gets the categories list
    """
    categories = db.query(models.Category).all()
    return categories


@app.get("/categories/{category_id}", response_model=schemas.Category)
def get_category_details(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).get(category_id)
    if category is None:
        raise HTTPException(404, "Category not found.")
    return category
