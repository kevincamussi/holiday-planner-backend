"""
FastAPI application for managing holidays.
"""

from fastapi import FastAPI
# from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
# from datetime import timedelta, date
# from .models.holidays import HolidayCreate, HolidayOut
# from .core.database import holidays_collection
# from .types.holidays import HolidayInsert
from app.routers import holidays

app = FastAPI(title="Holiday Management API")

app.include_router(holidays.router, prefix="/holidays", tags=["Holidays"])

# CORS for frontend (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
