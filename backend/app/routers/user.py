from fastapi import (
    APIRouter,
    Body,
    Request,
    status,
    HTTPException,
    Depends,
    UploadFile,
    File,
    Form,
)
from typing import List
from pydantic import Field
from ..models.user import ProfileModel, UserModel, UserLogin
from ..authentication import Authorization
from fastapi.responses import JSONResponse
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


@router.post(
    "/",
    response_model=ProfileModel
)
async def create_profile(
    profile: ProfileModel = Body(...), userId=Depends(auth_handler.auth_wrapper)
):
    profile.owner = userId
    new_profile = await profile_collection.insert_one(
        profile.model_dump(exclude="id", by_alias=True)
    )
    created_profile = await profile_collection.find_one(
        {"_id": new_profile.inserted_id}
    )
    return created_profile


@router.post("/login", response_description="Login user")
async def login(loginUser: UserLogin = Body(...)):
    user = await user_collection.find_one({"username": loginUser.username})
    if user is None or (
        not auth_handler.verify_password(loginUser.password, user["password"])
    ):
        raise HTTPException(status_code=401, detail="Invalid username and/or password")
    token = auth_handler.encode_token(user["username"])
    response = JSONResponse(content={"token": token})
    return response

@router.get("/me")
async def me(username: str):
    user_profile = await profile_collection.find_one({"username": username})
    return user_profile

