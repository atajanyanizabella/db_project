#!/usr/bin/env python3

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model.struct import ship_struct, ship_create_struct
from model.connection import get_db
from model.tables import Ship

from . import CHUNK_SIZE


router = APIRouter()


@router.get("/", response_model=list[ship_struct])
def read(p: int = 0, db: Session = Depends(get_db)):
    skip = p * CHUNK_SIZE
    limit = CHUNK_SIZE
    return db.query(Ship).order_by(Ship.id).offset(skip).limit(limit).all()

@router.post("/", response_model=ship_struct)
def create(data: ship_create_struct, db: Session = Depends(get_db)):
    ship = Ship(**ship.dict())
    db.add(ship)
    db.commit()
    return ship

def from_id(db: Session, id: int):
    return db.query(Ship).filter(Ship.id == id)

@router.put("/{id}")
def update(id: int, data: ship_create_struct, db: Session = Depends(get_db)):
    ship = from_id(db, id).first()
    ship.name = data.name
    ship.displacement = data.displacement
    ship.home_port = data.home_port
    ship.ship_type = data.ship_type
    ship.captain = data.captain
    db.commit()
    return db

@router.delete("/{id}")
def delete_ship(id: int, db: Session = Depends(get_db)):
    ship = from_id(db, id).delete()
    db.commit()
    return ship
