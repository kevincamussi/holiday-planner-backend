"""
FastAPI application for managing holidays.
"""

from fastapi import FastAPI, HTTPException, Query
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from datetime import timedelta, date
from .models.holidays import HolidayCreate, HolidayOut
from .database import holidays_collection
from .types.holidays import HolidayInsert

app = FastAPI()

@app.get("/autocomplete")
async def get_autocomplete(
    field: str = Query(..., regex="^(employee_name|department)$")
):  
    """
    Return distinct values from MongoDB for autocomplete fields.
    Allowed fields: employee_name, department.
    """

    values = await holidays_collection.distinct(field)
    return values


@app.get("/holidays", response_model=list[HolidayOut])
async def get_holidays():
    """Return all holidays from MongoDB."""
    cursor = holidays_collection.find()
    holidays: list[HolidayOut] = []

    async for h in cursor:
        holidays.append(HolidayOut(
            id=str(h["_id"]),
            employee_name=h["employee_name"],
            department=h["department"],
            start_date=h["start_date"],
            end_date=h["end_date"],
            days=h.get("days", [])
        ))
    return holidays

@app.post("/holidays")
async def create_holiday(holiday: HolidayCreate):
    """Insert a new holiday and return it."""
    doc: HolidayInsert = {
        "employee_name": holiday.employee_name,
        "department": holiday.department,
        "start_date": holiday.start_date.isoformat(),
        "end_date": holiday.end_date.isoformat(),
        "days": [
            (holiday.start_date + timedelta(days=i)).isoformat()
            for i in range((holiday.end_date - holiday.start_date).days +1)
        ]
    }
    result = await holidays_collection.insert_one(doc)
    return HolidayOut(
        id=str(result.inserted_id),
        employee_name=doc["employee_name"],
        department=doc["department"],
        start_date=date.fromisoformat(doc["start_date"]),
        end_date=date.fromisoformat(doc["end_date"]),
        days=doc["days"]
    )

@app.delete("/holidays/{holiday_id}")
async def delete_holiday(holiday_id: str):
    """Delete holiday by id."""
    try:
        oid = ObjectId(holiday_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Invalid ID format")

    result = await holidays_collection.delete_one({"_id": oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Holiday not found")

    return {"message": "Holiday deleted"}

# CORS for frontend (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
