import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import DB_URI


engine = create_engine(DB_URI, echo=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


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

    def __str__(self):
        return f"{self.id}. {self.title}"

    def __repr__(self):
        return f"Movie(id={self.id}, title={self.title!r})"
