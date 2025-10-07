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

origins=[
    "https://holiday-planner-frontend-five.vercel.app",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost",
    "http://127.0.0.1",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
