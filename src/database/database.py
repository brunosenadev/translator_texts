from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import path, mkdir, getcwd

SQLALCHEMY_DATABASE_URL = "sqlite:///./instance/translator_gpt.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_tables_and_database():
    path_to_database = path.join(getcwd(), 'instance')
    if not path.exists(path_to_database):
        mkdir(path_to_database)
        Base.metadata.create_all(bind=engine)