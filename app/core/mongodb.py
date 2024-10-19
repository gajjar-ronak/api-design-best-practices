from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = AsyncIOMotorClient(settings.MONGODB_URI)
mongodb = client.fastapi_project

async def get_mongo_db():
    return mongodb