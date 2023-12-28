#!/usr/bin/env python3

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model.struct import arrival_struct, arrival_create_struct
from model.connection import get_db
from model.tables import Arrival
from sqlalchemy import Date

from . import CHUNK_SIZE


router = APIRouter()


# CRUD operations for arrival

@router.post("/", response_model=arrival_struct)
def create(data: arrival_create_struct, db: Session = Depends(get_db)):
    ar = Arrival(**data.dict())
    db.add(ar)
    db.commit()
    return ar

@router.get("/", response_model=list[arrival_struct])
def read(p: int = 0, db: Session = Depends(get_db)):
    skip = p * CHUNK_SIZE
    limit = CHUNK_SIZE
    return db.query(Arrival).order_by(Arrival.id).offset(skip).limit(limit).all()

def from_id(db: Session, id: int):
    return db.query(Arrival).filter(Arrival.id == id)


@router.put("/{id}")
def update(id: int, data: arrival_create_struct, db: Session = Depends(get_db)):
    ar = from_id(db, id).first()
    ar.berth_number = data.berth_number
    ar.arrival_date = data.arrival_date
    ar.departure_date = data.departure_date
    ar.arrival_purpose = arrival_purpose
    db.commit()
    return db

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    ar = from_id(db, id).delete()
    db.commit()
    return ar
