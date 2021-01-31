import datetime
from sqlalchemy import create_engine
from sqlalchemy import (
    Table,
    Column,
    Integer,
    String,
    Numeric,
    Date,
    TIMESTAMP,
    ForeignKey,
)
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import CheckConstraint

from .config import DB_URI


engine = create_engine(DB_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

actors = Table(
    "actors",
    Base.metadata,
    Column("person_id", Integer, ForeignKey("people.id"), nullable=False),
    Column("movie_id", Integer, ForeignKey("movies.id"), nullable=False),
)


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False, unique=True)

    movies = relationship("Movie", back_populates="category")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Category(id={self.id}, name={self.name!r})"


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=True)
    birthdate = Column(Date, nullable=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_at = Column(
        TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    directed_movies = relationship(
        "Movie", foreign_keys="Movie.director_id", back_populates="director"
    )
    produced_movies = relationship(
        "Movie", foreign_keys="Movie.producer_id", back_populates="producer"
    )
    movies = relationship("Movie", secondary=actors, back_populates="actors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Person(id={self.id}, first_name={self.first_name!r})"


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    year = Column(Integer, nullable=False)
    budget = Column(Integer, nullable=True)
    bo_returns = Column(Integer, nullable=True)
    director_id = Column(Integer, ForeignKey(Person.id), nullable=False)
    producer_id = Column(Integer, ForeignKey(Person.id), nullable=False)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    rating = Column(
        Numeric(2, 1),
        CheckConstraint("rating >= 1 AND rating <= 10", name="chk_movies_rating"),
        nullable=True,
    )
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_at = Column(
        TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    director = relationship(
        Person, foreign_keys=[director_id], back_populates="directed_movies"
    )
    producer = relationship(
        Person, foreign_keys=[producer_id], back_populates="produced_movies"
    )
    category = relationship(Category, back_populates="movies")
    actors = relationship("Person", secondary=actors, back_populates="movies")
    reviews = relationship("Review", back_populates="movie")

    def __str__(self):
        return f"{self.id}. {self.title}"

    def __repr__(self):
        return f"Movie(id={self.id}, title={self.title!r})"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), nullable=False, unique=True)

    reviews = relationship("Review", back_populates="user")

    def __str__(self):
        return self.username

    def __repr__(self):
        return f'User(id={self.id}, username={self.username!r})'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    movie_id = Column(Integer, ForeignKey(Movie.id), nullable=False)
    rating = Column(
        Numeric(2, 1),
        CheckConstraint("rating >= 1 AND rating <= 10", name="chk_movies_rating"),
        nullable=True,
    )
    review = Column(String(500), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_at = Column(
        TIMESTAMP, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow
    )

    user = relationship(User, back_populates='reviews')
    movie = relationship(Movie, back_populates="reviews")
