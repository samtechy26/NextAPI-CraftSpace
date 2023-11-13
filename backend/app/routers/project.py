import os
from dotenv import load_dotenv
from fastapi import APIRouter, status, UploadFile, File, Form
from ..models.project import ProjectBaseModel, ProjectModel, ProjectInfo, Technology
from ..database import project_collection
from ..authentication import Authorization
import cloudinary
import cloudinary.uploader

load_dotenv()
CLOUD_NAME = os.environ["CLOUD_NAME"]
CLOUD_API_KEY = os.environ["CLOUD_API_KEY"]
CLOUD_API_SECRET = os.environ["CLOUD_API_SECRET"]

cloudinary.config(
    cloud_name=CLOUD_NAME, api_key=CLOUD_API_KEY, api_secret=CLOUD_API_SECRET
)

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/",
            response_description="View all projects",
            status_code=status.HTTP_200_OK
            )
async def get_projects():
    query = project_collection.find()
    result = [ProjectBaseModel(**raw_data) async for raw_data in query]
    return result


# Add a new project
@router.post(
    "/new",
    response_description="Add a new Project",
    response_model=ProjectBaseModel,
    status_code=status.HTTP_201_CREATED,
)
async def add_project(
    title: str = Form("title"),
    description: str = Form("description"),
    link: str = Form("project link"),
    image: UploadFile = File(...),
    tags: str = Form("tags"),

):
    result = cloudinary.uploader.upload(
        image.file,
        folder='PROJECTS',
        crop='scale',
        width=800
    )
    url = result.get("url")
    project = ProjectBaseModel(
        title=title,
        description=description,
        link=link,
        image=url,
        tags=tags,
    )
    
    
    new_project = await project_collection.insert_one(project.model_dump(exclude="id", by_alias=True))
    created_project = await project_collection.find_one({"_id": new_project.inserted_id})
    return created_project
