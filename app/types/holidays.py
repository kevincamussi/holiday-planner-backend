from typing import TypedDict

class HolidayDoc(TypedDict, total = False):
    _id: str
    employee_name: str
    department: str
    start_date: str
    end_date: str
    days: list[str]