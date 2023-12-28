from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from model.struct import ship_struct, port_struct, arrival_struct
from model.tables import Ship, Port, Arrival
from model.connection import get_db

from . import CHUNK_SIZE


router = APIRouter()


@router.get("/select", response_model=list[ship_struct])
def select(p: int = 0, key: int = id, db: Session = Depends(get_db)):
    skip = p * CHUNK_SIZE
    limit = CHUNK_SIZE
    query = (
        db.query(Ship)
        .where(Ship.name == "Ocean Explorer")
        .where(Ship.ship_type == "Container Ship")
    )
    match key:
        case "id":
            query = query.order_by(Ship.id)
        case "name":
            query = query.order_by(Ship.name)
        case "ship_type":
            query = query.order_by(Ship.ship_type)
    return query.offset(skip).limit(limit).all()

@router.get("/join", response_model=list[tuple[ship_struct, port_struct]])
def join(p: int = 0, key: int = id, db: Session = Depends(get_db)):
    skip = p * CHUNK_SIZE
    limit = CHUNK_SIZE
    query = (
        db.query(Arrival, Ship, Port)
        .join(Ship, Ship.id == Arrival.ship_id)
        .join(Port, Port.id == Arrival.port_id)
    )
    match key:
        case "port_id":
            query = query.order_by(Port.id)
        case "ship_id":
            query = query.order_by(Ship.id)
    query = query.offset(skip).limit(limit).all()
    return [(op, sub) for _, op, sub in query]


@router.get("/group_by", response_model=list[dict[str, float]])
def group_by(p: int = 0, db: Session = Depends(get_db)):
    skip = p * CHUNK_SIZE
    limit = CHUNK_SIZE
    query = (
        db.query(Ship.name, func.avg(Port.day_price))
        .group_by(Ship.name)
        .order_by(Port.day_price)
    )
    return [{"name": name, "average": average}
            for (name, average) in query.offset(skip).limit(limit).all()]


@router.put("/update")
def update(db: Session = Depends(get_db)):
    db.query(Port).filter(Port.day_price < 15000).update({"day_price": Port.day_price * 3})
    db.commit()
    return db
