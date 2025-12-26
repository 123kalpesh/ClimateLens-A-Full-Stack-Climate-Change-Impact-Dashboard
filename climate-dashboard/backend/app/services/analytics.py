from sqlalchemy.orm import Session
from ..models.climate import Temperature, CO2
from ..schemas.climate import TemperatureResponse, CO2Response, TemperatureData, CO2Data




def get_temperature_data(db: Session, country: str, start: int, end: int):
    rows = db.query(Temperature).filter(
        Temperature.country == country,
        Temperature.year.between(start, end)
    ).all()
    data = [TemperatureData(year=r.year, value=r.value) for r in rows]
    return TemperatureResponse(data=data)




def get_co2_data(db: Session, country: str):
    rows = db.query(CO2).filter(CO2.country == country).all()
    data = [CO2Data(year=r.year, value=r.value) for r in rows]
    return CO2Response(data=data)