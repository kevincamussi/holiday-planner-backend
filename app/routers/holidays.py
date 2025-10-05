"""
Holiday-related endpoints (CRUD operations and autocomplete).
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from app.core.security import get_current_user
from bson import ObjectId
from datetime import timedelta, date

from app.models.holidays import HolidayCreate, HolidayOut
from app.core.database import holidays_collection
from app.types.holidays import HolidayInsert

router = APIRouter(dependencies=[Depends(get_current_user)])



@router.get("/autocomplete")
async def get_autocomplete(
    field: str = Query(..., regex="^(employee_name|department)$")
):  
    """
    Return distinct values from MongoDB for autocomplete fields.
    Allowed fields: employee_name, department.
    """

    field_map = {
        "employeeName": "employee_name",
        "department": "department"
    }

    mongo_field = field_map.get(field, field)
    values = await holidays_collection.distinct(mongo_field)
    return values


@router.get("/", response_model=list[HolidayOut])
async def get_holidays():
    """Return all holidays from MongoDB."""
    cursor = holidays_collection.find()
    holidays: list[HolidayOut] = []

    async for h in cursor:
        holidays.append(HolidayOut(
            id=str(h["_id"]),
            employeeName=h["employee_name"],
            department=h["department"],
            startDate=h["start_date"],
            endDate=h["end_date"],
            days=h.get("days", [])
        ))
    return holidays

@router.post("/")
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
        employeeName=doc["employee_name"],
        department=doc["department"],
        startDate=date.fromisoformat(doc["start_date"]),
        endDate=date.fromisoformat(doc["end_date"]),
        days=doc["days"]
    )

@router.delete("/{holiday_id}")
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
