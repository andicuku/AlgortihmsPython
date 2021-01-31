from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import DB_URI, APP_ENV


is_dev = APP_ENV == "development"

engine = create_engine(DB_URI, echo=is_dev)
Base = declarative_base(bind=engine)
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)
