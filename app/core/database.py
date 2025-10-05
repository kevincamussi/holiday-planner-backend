"""
Database connection setup for MongoDB (Motor async client).
"""

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from dotenv import load_dotenv
import os
from typing import Any
from ..types.holidays import HolidayDoc

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in environment variables")

if not DB_NAME:
    raise ValueError("DB_NAME is not set in environment variables")

# Async client and DB/collection references
client: AsyncIOMotorClient[dict[str, Any]] = AsyncIOMotorClient(MONGO_URL)
db: AsyncIOMotorDatabase[Any] = client[DB_NAME]
holidays_collection: AsyncIOMotorCollection[HolidayDoc] = db["holidays"]

