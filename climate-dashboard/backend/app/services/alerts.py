from sqlalchemy.orm import Session
from ..models.climate import Temperature
from ..schemas.climate import AlertResponse, AlertData
import numpy as np

def get_temperature_alerts(db: Session, country: str, threshold: float = 1.5):
    rows = db.query(Temperature).filter(Temperature.country == country).all()
    if not rows:
        return AlertResponse(country=country, alerts=[])
    
    # Calculate average temperature
    temps = [r.value for r in rows]
    avg_temp = np.mean(temps)
    
    alerts = []
    for row in rows:
        if row.value > avg_temp + threshold:
            alerts.append(AlertData(year=row.year, message=f"High temperature anomaly: {row.value:.2f}°C"))
    
    return AlertResponse(country=country, alerts=alerts)