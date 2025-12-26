import numpy as np
from sklearn.linear_model import LinearRegression
from sqlalchemy.orm import Session
from ..models.climate import Temperature
from ..schemas.climate import ForecastResponse, ForecastData




def forecast_temperature(db: Session, country: str, years: int):
    rows = db.query(Temperature).filter(Temperature.country == country).all()
    if not rows:
        return ForecastResponse(country=country, forecast=[])
    X = np.array([r.year for r in rows]).reshape(-1, 1)
    y = np.array([r.value for r in rows])


    model = LinearRegression()
    model.fit(X, y)


    last_year = max(X)[0]
    future_years = np.array([last_year + i for i in range(1, years + 1)]).reshape(-1, 1)
    predictions = model.predict(future_years)
    forecast = [ForecastData(year=int(future_years[i][0]), value=float(predictions[i])) for i in range(len(predictions))]
    return ForecastResponse(country=country, forecast=forecast)