from typing import List
from sqlalchemy.orm import Session, joinedload
from fastapi import APIRouter, Depends, HTTPException

from movies import schemas, models
from movies.dependencies import get_db


router = APIRouter()


@router.get("/", response_model=List[schemas.Movie])
def get_movies_list(db: Session = Depends(get_db)):
    movies = (
        db.query(models.Movie)
        .options(joinedload(models.Movie.category))
        .options(joinedload(models.Movie.director))
        .options(joinedload(models.Movie.producer))
        .all()
    )
    return movies
