from models import Session, Number, Server, User
from database import Base, engine
from os import path, mkdir, getcwd

def create_tables_and_database():
    path_to_database = path.join(getcwd(), 'instance')
    if not path.exists(path_to_database):
        mkdir(path_to_database)
        Base.metadata.create_all(bind=engine)