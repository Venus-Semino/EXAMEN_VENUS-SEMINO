from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Laptop(Base):
    __tablename__ = "laptops"

    id = Column(Integer, primary_key=True, index=True) # Autoincremental
    marca = Column(String(50))
    modelo = Column(String(50))
    ram_gb = Column(Integer)
    disponible = Column(Boolean, default=True)
