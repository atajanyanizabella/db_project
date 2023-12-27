#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, mapped_column
from sqlalchemy.dialects.postgresql import JSONB


Base = declarative_base()

# Define Arrival model
class Arrival(Base):
    __tablename__ = 'arrival'

    id = Column(Integer, primary_key=True, index = True)
    berth_number = Column(Integer, nullable=False)
    arrival_date = Column(Date, nullable=False)
    departure_date = Column(Date, nullable=False)
    arrival_purpose = Column(String(100), nullable=False)

    # Many-to-one
    ship_id = mapped_column(ForeignKey("ship.id", ondelete="CASCADE"))

    ship = relationship("Ship", back_populates="arrival")

    # Many-to-one
    port_id = mapped_column(ForeignKey("port.id", ondelete="CASCADE"))
    port = relationship("Port", back_populates="arrival", cascade="all,delete")


# Define ship model
class Ship(Base):
    __tablename__ = 'ship'

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(50))
    displacement = Column(Integer, default=0)
    home_port = Column(Integer)
    ship_type = Column(String(50))
    captain = Column(String(50))

    # One-to-many
    arrivals = relationship(Arrival, back_populates="ship")


# Define Port model
class Port(Base):
    __tablename__ = 'port'

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(50))
    city = Column(String(50))
    category = Column(String(50))
    day_price = Column(Numeric(10, 2))

    # One-to-many
    arrivals = relationship(Arrival, back_populates="port")

