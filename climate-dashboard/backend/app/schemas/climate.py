from pydantic import BaseModel
from typing import List, Optional

class TemperatureData(BaseModel):
    year: int
    value: float

class CO2Data(BaseModel):
    year: int
    value: float

class ForecastData(BaseModel):
    year: int
    value: float

class TemperatureResponse(BaseModel):
    data: List[TemperatureData]

class CO2Response(BaseModel):
    data: List[CO2Data]

class ForecastResponse(BaseModel):
    country: str
    forecast: List[ForecastData]

class AlertData(BaseModel):
    year: int
    message: str

class AlertResponse(BaseModel):
    country: str
    alerts: List[AlertData]