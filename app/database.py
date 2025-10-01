"""
Database connection setup for MongoDB (Motor async client).
"""

from motor.motor_asyncio import AsyncIOMotorClient

# Connection string (use environment variable in production)
MONGO_URL = "mongodb+srv://kevin:FLxjLq9uEHt2ZRmO@cluster0.ujf3fpl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Async client and DB/collection references
client: AsyncIOMotorClient = AsyncIOMotorClient(MONGO_URL)
db = client["holiday_planner"]
holidays_collection = db["holidays"]
