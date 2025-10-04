from typing import TypedDict, NotRequired

class HolidayDoc(TypedDict, total = False):
    _id: str
    employee_name: str
    department: str
    start_date: str
    end_date: str
    days: list[str]

class HolidayInsert(HolidayDoc):
    _id: NotRequired[str]