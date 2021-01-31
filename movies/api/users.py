from typing import List

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from movies import schemas, models
from movies.dependencies import get_db


router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def get_user_list(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get("/{user_id}", response_model=schemas.User)
def get_user_details(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found.")
    return user
