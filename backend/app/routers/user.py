from fastapi import APIRouter, Body, Request, status, HTTPException, Depends, UploadFile, File, Form
from typing import List
from ..models.user import ProfileModel, UserModel
from ..authentication import Authorization
from ..database import user_collection, profile_collection
import cloudinary
import cloudinary.uploader

router = APIRouter(prefix="/users", tags=["users"])
auth_handler = Authorization()


# Register route
@router.post(
    "/register",
    response_model=UserModel,
    response_description="Register a User",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def register(newUser: UserModel = Body(...)):
    newUser.password = auth_handler.get_password_hash(newUser.password)

    if (
        existing_email := await user_collection.find_one({"email": newUser.email})
    ) is not None:
        raise HTTPException(
            status_code=409, detail=f"Email address {newUser.email} is taken"
        )
    if (
        existing_username := await user_collection.find_one(
            {"username": newUser.username}
        )
    ) is not None:
        raise HTTPException(
            status_code=409, detail=f"Username {newUser.username} is taken"
        )

    user = await user_collection.insert_one(
        newUser.model_dump(by_alias=True, exclude="id")
    )

    created_user = await user_collection.find_one({"_id": user.inserted_id})

    return created_user


# Add a new car  using forms
@router.post("/",
            response_description="Add new car with picture",
            response_model=ProfileModel,
            status_code=status.HTTP_201_CREATED,
            )
async def create_car_form(profile: ProfileModel = Form(),userId = Depends(auth_handler.auth_wrapper)):
    profile.owner = userId
    new_profile = await profile_collection.insert_one(profile.model_dump(exclude='id', by_alias=True))
    created_profile = await profile_collection.find_one({"_id": new_profile.inserted_id})
    return created_profile



# Return User Details
@router.get("/me")
async def get_user_info():
    pass