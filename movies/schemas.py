from decimal import Decimal

from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


class Person(BaseModel):
    id: int
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class Movie(BaseModel):
    id: int
    title: str
    description: str
    year: int
    budget: int
    bo_returns: int
    rating: Decimal
    category: Category
    director: Person
    producer: Person

    class Config:
        orm_mode = True
