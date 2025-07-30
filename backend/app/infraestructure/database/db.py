from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


engine = None
SessionLocal = None

def init_db():
    global engine, SessionLocal
    if not settings.SQLALCHEMY_DATABASE_URL:
        raise ValueError("SQLALCHEMY_DATABASE_URL is not set in settings.")

    engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
