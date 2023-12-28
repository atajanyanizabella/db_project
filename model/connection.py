#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL


url = URL.create(drivername="postgresql",
                 username="admin",
                 password="secret",
                 host="localhost",
                 database="port_register",
                 port=5432)

engine = create_engine(url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
