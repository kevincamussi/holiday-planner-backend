"""
FastAPI application for managing holidays.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import holidays, auth

app = FastAPI(title="Holiday Management API")

app.include_router(auth.router, prefix="/auth", tags=["Auth"])     
app.include_router(holidays.router, prefix="/holidays", tags=["Holidays"])

# CORS for frontend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
