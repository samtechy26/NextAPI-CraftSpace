from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional, List
from bson import ObjectId
from ..database import PyObjectId

class Tags(str, Enum):
    UI =  'UI / Frontend'

class ProjectBaseModel(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    title: str = Field("Google Health Platform")
    category: str = Field("Web Application")
    description: str = Field("A basic health Application")
    tags: Optional[str] = None
    link: str = Field("...")
    image: Optional[str] = None
    
    class config:
        json_encoders = {ObjectId: str}

class CompanyInfo(BaseModel):
    title: str = Field("Google Incorporated")
    details: str = Field("Web application giant")
       
class ProjectInfo(BaseModel):
    client_heading: str  = Field("Tech Giant")
    company_info: List[CompanyInfo]
    
class Technology(BaseModel):
    title:str = Field("Python")
    techs: List[str] = Field(["FastAPI", "Django"])  
    
class ProjectModel(BaseModel):
    project: ProjectBaseModel
    project_info: ProjectInfo = None
    technologies: List[Technology]
    
    