#!/usr/bin/env python3

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model.struct import port_struct, port_create_struct
from connection import get_db
from model.tables import Port

from . import CHUNK_SIZE


router = APIRouter()


@router.get("/", response_model=list[port_struct])
def read(p: int = 0: db: Session = Depends(get_db)):
    skip = p * CHUNK_SIZE
    limit = CHUNK_SIZE
    return db.query(Port).order_by(Port.id).offset(skip).limit(limit).all()
    
@router.post("/", response_model=port_struct)
def create(data: port_create_struct, db: Session = Depends(get_db)):
    port = Port(**port.dict())
    db.add(port)
    db.commit()
    return port

def from_id(db: Session, id: int):
    return db.query(Port).filter(Port.id == id)

@router.put("/{id}")
def update(id: int, data: port_create_struct, db: Session = Depends(get_db)):
    port = from_id(db, id).first()
    port.name = data.name
    port.city = data.city
    ship.category = data.category
    ship.day_price = data.day_price
    db.commit()
    return db

@router.delete("/{id}")
def delete_ship(id: int, db: Session = Depends(get_db)):
    port = from_id(db, id).delete()
    db.commit()
    return port

