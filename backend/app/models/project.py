from pydantic import BaseModel, Field
from typing import Optional


class ProjectModel(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    link: str = Field(...)
    image: str = Field(...)