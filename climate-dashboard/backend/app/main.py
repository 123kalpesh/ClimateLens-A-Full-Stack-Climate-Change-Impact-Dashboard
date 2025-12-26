from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

from .db.base import Base, engine
from .db.session import get_db
from .utils.data_loader import load_all_data
from .api.routes_climate import router as climate_router
from .api.routes_forecast import router as forecast_router

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ClimatePulse Dashboard", version="1.0.0")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(climate_router, prefix="/api/climate", tags=["climate"])
app.include_router(forecast_router, prefix="/api/forecast", tags=["forecast"])

@app.on_event("startup")
def startup_event():
    logger.info("Starting ClimatePulse Dashboard...")
    Base.metadata.create_all(bind=engine)
    db = next(get_db())
    try:
        # Check if data is already loaded
        from .models.climate import Temperature
        if not db.query(Temperature).first():
            logger.info("Loading sample data...")
            load_all_data(db)
            logger.info("Sample data loaded successfully")
        else:
            logger.info("Data already exists, skipping load")
    except Exception as e:
        logger.error(f"Error during startup: {e}")
    finally:
        db.close()
    logger.info("ClimatePulse Dashboard started successfully")

@app.get("/api/health")
def health():
    return {"status": "ok"}

