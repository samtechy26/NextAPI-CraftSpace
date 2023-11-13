from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from ..database import PyObjectId

class UserModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    email: str = EmailStr()
    username: str = Field()
    password: str = Field()

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
    owner: str = Field
    first_name: str = Field()
    last_name: str = Field()
    experience: int = Field()
    bio: str = Field()
    services: List[ServiceModel] 
    languages: List[LanguageModel] 
    education: List[EducationModel]
    experiences: List[ExperienceModel]


