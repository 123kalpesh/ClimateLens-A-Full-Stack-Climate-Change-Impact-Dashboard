from sqlalchemy import Column, Integer, Float, String
from ..db.base import Base


class Temperature(Base):
    __tablename__ = "temperature"
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    year = Column(Integer, index=True)
    value = Column(Float)


class CO2(Base):
    __tablename__ = "co2"
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    year = Column(Integer)
    value = Column(Float)