#!/usr/bin/env python3

from fastapi import FastAPI
from model import tables
from model.connection import engine
from routers.arrival import router as arrival_router
from routers.ship import router as ship_router
from routers.port import router as port_router

tables.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router=arrival_router, prefix="/arrival")
app.include_router(router=ship_router, prefix="/ship")
app.include_router(router=port_router, prefix="/port")
