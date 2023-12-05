#!/usr/bin/env python3

from fastapi import FASTAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from db_setup import *


app = FastAPI()

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()


# CRUD operations for Ship

@app.post("/ships/", response_model=Ship)
def create_ship(ship: Ship, db: Session = Depends(get_db)):
    try:
        db_ship = Ship(**ship.dict())
        db.add(db_ship)
        db.commit()
        db.refresh(db_ship)
        return db_ship
    except IntegrityError:
        db.rollback() # rollback to the state before the changes were made
        raise HTTPException(status_code=400, detail="Duplicate entry")


@app.get("/ships/")
def read_all_ships(db: Session = Depends(get_db)):
    ships = db.query(Ship).all()
    return ships


@app.get("/ships/{ship_id}", response_model=Ship)
def read_ship(ship_id: int, db: Session = Depends(get_db)):
    ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if ship:
        return ship
    raise HTTPException(status_code=404, detail="Ship not found")


@app.put("/ships/{ship_id}", response_model=Ship)
def update_ship(ship_id: int, updated_ship: Ship, db: Session = Depends(get_db)):
    ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if ship:
        for field, value in updated_ship.dict().items():
            setattr(ship, field, value)
        db.commit()
        db.refresh(ship)
        return ship
    raise HTTPException(status_code=404, detail="Ship not found")


@app.delete("/ships/{ship_id}", response_model=dict)
def delete_ship(ship_id: int, db: Session = Depends(get_db)):
    ship = db.query(Ship).filter(Ship.id == ship_id).first()
    if ship:i
        db.delete(ship)
        db.commit()
        return {"message": "Ship deleted sucessfully"}
    raise HTTPException(status_code=404, detail="Ship not found")


@app.post("/ports/", response_model=Port)
def create_port(port: Port, db: Session = Depends(get_db)):
    try:
        db_port = Port(**port.dict())
        db.add(db_port)
        db.commit()
        db.refresh(db_port)
        return db_port
    except IntegrityError:
        db.rollback() # rollback to the state before the changes were made
        raise HTTPException(status_code=400, detail="Duplicate entry")


@app.get("/ports/")
def read_all_ports(db: Session = Depends(get_db)):
    ports = db.query(Port).all()
    return ports


@app.get("/ports/{port_id}", response_model=Port)
def read_port(port_id: int, db: Session = Depends(get_db)):
    port = db.query(Port).filter(Port.id == port_id).first()
    if port:
        return port
    raise HTTPException(status_code=404, detail="Port not found")


@app.put("/ports/{port_id}", response_model=Port)
def update_port(port_id: int, updated_port: Port, db: Session = Depends(get_db)):
    port = db.query(Port).filter(Port.id == port_id).first()
    if port:
        for field, value in updated_port.dict().items():
            setattr(port, field, value)
        db.commit()
        db.refresh(port)
        return port
    raise HTTPException(status_code=404, detail="Port not found")


@app.delete("/ports/{port_id}", response_model=dict)
def delete_port(port_id: int, db: Session = Depends(get_db)):
    port = db.query(Port).filter(Port.id == port_id).first()
    if port:
        db.delete(port)
        db.commit()
        return {"message": "Port deleted sucessfully"}
    raise HTTPException(status_code=404, detail="Port not found")


@app.post("/arrivals/", response_model=Arrival)
def create_arrival(port: Arrival, db: Session = Depends(get_db)):
    try:
        db_arrival = Arrival(**arrival.dict())
        db.add(db_arrival)
        db.commit()
        db.refresh(db_arrival)
        return db_arrival
    except IntegrityError:
        db.rollback() # rollback to the state before the changes were made
        raise HTTPException(status_code=400, detail="Duplicate entry")


@app.get("/arrivals/")
def read_all_arrivals(db: Session = Depends(get_db)):
    arrivals = db.query(Arrival).all()
    return arrivals


@app.get("/arrivals/{arrival_id}", response_model=Arrival)
def read_arrival(arrival_id: int, db: Session = Depends(get_db)):
    arrival = db.query(Arrival).filter(Arrival.id == arrival_id).first()
    if arrival:
        return arrival
    raise HTTPException(status_code=404, detail="Arrival not found")


@app.put("/arrivals/{arrival_id}", response_model=Arrival)
def update_arrival(arrival_id: int, updated_arrival: Arrival, db: Session = Depends(get_db)):
    arrival = db.query(Arrival).filter(Arrival.id == arrival_id).first()
    if arrival:
        for field, value in updated_arrival.dict().items():
            setattr(arrival, field, value)
        db.commit()
        db.refresh(arrival)
        return arrival
    raise HTTPException(status_code=404, detail="Arrival not found")


@app.delete("/arrivals/{arrival_id}", response_model=dict)
def delete_arrival(arrival_id: int, db: Session = Depends(get_db)):
    arrival = db.query(Arrival).filter(Arrival.id == arrival_id).first()
    if arrival:
        db.delete(arrival)
        db.commit()
        return {"message": "Arrival deleted sucessfully"}
    raise HTTPException(status_code=404, detail="Arrival not found")
