"""
Pydantic models for holidays.
"""

from datetime import date
from pydantic import BaseModel, ConfigDict, field_validator

class HolidayBase(BaseModel):
    employee_name: str
    department: str
    start_date: date
    end_date: date

    @field_validator("end_date")
    @classmethod
    def check_end_after_start(cls, v, info):
        start = info.data.get("start_date")
        if start and v < start:
            raise ValueError("end_date cannot be before start_date")
        return v

class HolidayCreate(HolidayBase):
    pass

class HolidayOut(HolidayBase):
    id: str
    days: list[str]
    model_config = ConfigDict(from_attributes=True)
