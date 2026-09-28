from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL_BASE_DATOS = "mysql+pymysql://laboratorio:laboratorio@mysql:3306/laboratorio"

engine = create_engine(URL_BASE_DATOS)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()