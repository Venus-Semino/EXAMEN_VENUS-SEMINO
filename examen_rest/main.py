from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
import models
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

class LaptopCreate(BaseModel):
    marca: str
    modelo: str
    ram_gb: int

class LaptopResponse(BaseModel):
    id: int
    marca: str
    modelo: str
    ram_gb: int
    disponible: bool
    
    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def cargar_datos_iniciales():
    db = SessionLocal()
    if db.query(models.Laptop).count() == 0:
        laptops_iniciales = [
            models.Laptop(marca="Dell", modelo="Latitude 5440", ram_gb=16, disponible=True),
            models.Laptop(marca="Lenovo", modelo="ThinkPad E14", ram_gb=8, disponible=False),
            models.Laptop(marca="HP", modelo="ProBook 450", ram_gb=16, disponible=True)
        ]
        db.add_all(laptops_iniciales)
        db.commit()
    db.close()

cargar_datos_iniciales()

# Endpoints
@app.get("/")
def leer_raiz():
    return {"mensaje": "API del laboratorio de cómputo"}

@app.get("/laptops/disponibles", response_model=List[LaptopResponse])
def leer_laptops_disponibles(db: Session = Depends(get_db)):
    return db.query(models.Laptop).filter(models.Laptop.disponible == True).all()

@app.get("/laptops", response_model=List[LaptopResponse])
def leer_laptops(db: Session = Depends(get_db)):
    return db.query(models.Laptop).all()

@app.get("/laptops/{laptop_id}", response_model=LaptopResponse)
def leer_laptop(laptop_id: int, db: Session = Depends(get_db)):
    laptop = db.query(models.Laptop).filter(models.Laptop.id == laptop_id).first()
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop no encontrada")
    return laptop

@app.post("/laptops", response_model=LaptopResponse)
def crear_laptop(laptop: LaptopCreate, db: Session = Depends(get_db)):
    # El id se asigna por MySQL y disponible queda en true
    db_laptop = models.Laptop(**laptop.model_dump(), disponible=True)
    db.add(db_laptop)
    db.commit()
    db.refresh(db_laptop)
    return db_laptop