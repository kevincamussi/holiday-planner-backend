from typing import TypedDict, NotRequired

class UserDoc(TypedDict, total=False):
    _id: NotRequired[object]
    email: str
    name: str | None
    hashed_password: str

