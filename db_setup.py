#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import declarative_base

DATABASE_URI = 'postgresql://admin:secret@localhost:5432/ship_registry'

Base = declarative_base()

# Define ship model
class Ship(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    displacement = Column(Integer, nullable=False)
    home_port = Column(String(30), nullable=False)
    ship_type = Column(String(30), nullable=False)
    captain = Column(String(30), nullable=False)

# Define Port model
class Port(Base):
    __tablename__ = 'ports'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    city = Column(String(30), nullable=False)
    category = Column(String(30), nullable=False)
    day_price = Column(Numeric(10, 2), nullable=False)

# Define Arrival model
class Arrival(Base):
    __tablename__ = 'arrivals'
    id = Column(Integer, primary_key=True)
    ship_id = Column(Integer, ForeignKey('ships.id'), nullable=False)
    port_id = Column(Integer, ForeignKey('ports.id'), nullable=False)
    berth_number = Column(Integer, nullable=False)
    arrival_date = Column(Date, nullable=False)
    departure_date = Column(Date, nullable=False)
    arrival_purpose = Column(String(100), nullable=False)

# Create engine and initialize the database
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
