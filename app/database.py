from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user import User
from fastapi import FastAPI
from contextlib import asynccontextmanager

MONGO_DETAILS = "mongodb://root:password@mongodb:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.auth_db

async def initialize_database():
    await init_beanie(
        database=database,
        document_models=[User]
    )
    
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    await initialize_database()
    print("Connected to MongoDB!")
    yield
    # Shutdown code
    client.close()
    print("Disconnected from MongoDB!") 