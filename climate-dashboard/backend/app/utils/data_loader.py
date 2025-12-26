import pandas as pd
from sqlalchemy.orm import Session
from ..models.climate import Temperature, CO2
import os

def load_temperature_data(db: Session):
    file_path = os.path.join(os.path.dirname(__file__), '../../data/sample_temperature.csv')
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        temp = Temperature(country=row['country'], year=int(row['year']), value=float(row['value']))
        db.add(temp)
    db.commit()

def load_co2_data(db: Session):
    file_path = os.path.join(os.path.dirname(__file__), '../../data/sample_co2.csv')
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        co2 = CO2(country=row['country'], year=int(row['year']), value=float(row['value']))
        db.add(co2)
    db.commit()

def load_all_data(db: Session):
    load_temperature_data(db)
    load_co2_data(db)