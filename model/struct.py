#!/usr/bin/env python3


from datetime import date
from pydantic import BaseModel

class arrival_create_struct(BaseModel):
    ship_id: int
    port_id: int
    berth_number: int
    arrival_date: date
    departure_date: date
    arrival_purpose: str

class arrival_struct(arrival_create_struct):
    id: int

    class Config:
        from_attributes = True


class ship_create_struct(BaseModel):
    name: str
    displacement: int
    home_port: int
    ship_type: str
    capitain: str

class ship_struct(ship_create_struct):
    id: int
    connections: list[arrival_struct]

    class Config:
        from_attributes = True

class port_create_struct(BaseModel):
    name: str
    city: str
    category: str
    day_price: float


class port_struct(port_create_struct):
    id: int
    connections: list[arrival_struct]

    class Config:
        from_attributes = True


