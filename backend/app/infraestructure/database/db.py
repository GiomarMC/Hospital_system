from sqlalchemy import create_engine
from app.config import settings


engine = None

def init_db():
    global engine
    if not settings.SQLALCHEMY_DATABASE_URL:
        raise ValueError("SQLALCHEMY_DATABASE_URL is not set in settings.")

    engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
