from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from ..database import PyObjectId
from bson import ObjectId

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    email: str = EmailStr()
    username: str = Field()
    password: str = Field()

    class config:
        json_encoders = {ObjectId: str}

class ServiceModel(BaseModel):
    title: str = Field()
    description: str = Field()
    image: str = Field

class LanguageModel(BaseModel):
    title: str = Field()
    level: int = Field()

class EducationModel(BaseModel):
    school_name: str = Field()
    start_year: int = Field()
    end_year: int = Field()
    on_going: bool = Field()

class ExperienceModel(BaseModel):
    company_name: str = Field()
    start_year: int = Field()
    end_year: int = Field()
    on_going: bool = Field()

class ProfileModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    owner: str = Field()
    image: Optional[str] = None
    first_name: str = Field()
    last_name: str = Field()
    bio: str = Field()
    services: list[ServiceModel]
    languages: list[LanguageModel]
    education: list[EducationModel]
    experiences: list[ExperienceModel]

    class config:
        json_encoders = {ObjectId: str}

class UserLogin(BaseModel):
    username: str = Field(...)
    password: str = Field(...)

class UploadProfile(BaseModel):
    image: str = Field(...)


class ProfileUpdate(BaseModel):
    bio: str = None
    first_name: str = None
    last_name: str = None

 


