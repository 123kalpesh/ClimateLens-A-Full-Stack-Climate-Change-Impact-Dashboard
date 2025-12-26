from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    project_name: str = "ClimatePulse Dashboard"
    version: str = "1.0.0"
    api_v1_str: str = "/api/v1"

    # Database
    database_url: str = "sqlite:///./climate_data.db"

    # API Keys
    nasa_api_key: Optional[str] = None
    openweather_api_key: Optional[str] = None

    # Server
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
