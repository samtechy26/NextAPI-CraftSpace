import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated

load_dotenv()

client = AsyncIOMotorClient(os.environ['DB_URL'])
db = client.get_database(os.environ['DB_NAME'])
user_collection = db.get_collection('users')
project_collection = db.get_collection('projects')
profile_collection = db.get_collection('profile')

# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]