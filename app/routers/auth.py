"""
Authentication endpoints: register, login, me
"""

from fastapi import APIRouter, HTTPException, status, Depends
from datetime import timedelta
from bson import ObjectId

from app.core.database import users_collection
from app.core.security import (
    hash_password, verify_password, create_access_token, get_current_user
)
from app.models.users import UserCreate, UserLogin, Token, UserOut
from app.types.users import UserDoc  # se não usar o types, pode remover

router = APIRouter()

@router.post("/register", response_model=Token)
async def register(user: UserCreate):
    exists = await users_collection.find_one({"email": user.email})
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    doc: UserDoc = {
        "email": user.email,
        "name": user.name,
        "hashed_password": hash_password(user.password),
    }
    result = await users_collection.insert_one(doc)
    token = create_access_token(str(result.inserted_id), timedelta(minutes=60))
    return Token(access_token=token)

@router.post("/login", response_model=Token)
async def login(credentials: UserLogin):
    user = await users_collection.find_one({"email": credentials.email})

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    hashed = user.get("hashed_password")
    if not hashed or not verify_password(credentials.password, hashed):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")

    user_id = str(user.get("_id"))
    if not user_id:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="User ID missing")

    token = create_access_token(user_id, timedelta(minutes=60))
    return Token(access_token=token)


@router.get("/me", response_model=UserOut)
async def me(current: UserOut = Depends(get_current_user)):
    return current
