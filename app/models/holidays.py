"""
Pydantic models for holidays.
"""

from datetime import date
from pydantic import BaseModel, ConfigDict, field_validator, Field
from pydantic_core.core_schema import FieldValidationInfo


class HolidayBase(BaseModel):
    employee_name: str = Field(..., alias="employeeName")
    department: str
    start_date: date = Field(..., alias="startDate")
    end_date: date = Field(..., alias="endDate")
    
    model_config = ConfigDict(populate_by_name=True)


    @field_validator("end_date")
    @classmethod
    def check_end_after_start(cls, v: date, info: FieldValidationInfo):
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
