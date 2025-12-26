from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..services.forecasting import forecast_temperature

router = APIRouter()

@router.get("/temperature")
def temperature_forecast(country: str, years: int = 10, db: Session = Depends(get_db)):
    try:
        return forecast_temperature(db, country, years)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating forecast: {str(e)}")