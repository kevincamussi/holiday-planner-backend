"""
Database connection setup for MongoDB (Motor async client).
"""

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URL:
    raise ValueError("MONGO_URL is not set in environment variables")

# Async client and DB/collection references
client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URL)
db = client["DB_NAME"]
holidays_collection = db["holidays"]
