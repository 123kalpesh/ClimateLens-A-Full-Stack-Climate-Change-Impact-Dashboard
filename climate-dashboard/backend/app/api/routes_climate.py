from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..services.analytics import get_temperature_data, get_co2_data
from ..services.alerts import get_temperature_alerts

router = APIRouter()

@router.get("/temperature")
def temperature(country: str, start: int = 1980, end: int = 2023, db: Session = Depends(get_db)):
    try:
        return get_temperature_data(db, country, start, end)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching temperature data: {str(e)}")

@router.get("/co2")
def co2(country: str, db: Session = Depends(get_db)):
    try:
        return get_co2_data(db, country)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching CO2 data: {str(e)}")

@router.get("/alerts")
def alerts(country: str, threshold: float = 1.5, db: Session = Depends(get_db)):
    try:
        return get_temperature_alerts(db, country, threshold)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching alerts: {str(e)}")