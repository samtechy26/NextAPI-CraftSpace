from fastapi import (
    APIRouter,
    Body,
    Request,
    status,
    HTTPException,
    Depends,
    UploadFile,
    File,
    BackgroundTasks,
    Form,
)
from typing import List
from pydantic import Field
from ..models.user import (
    ProfileModel,
    UserModel,
    UserLogin,
    UploadProfile,
    ProfileUpdate,
    ContactForm
)
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


# Create Profile
@router.post("/", response_model=ProfileModel)
async def create_profile(
    profile: ProfileModel = Body(...), userId=Depends(auth_handler.auth_wrapper)
):
    profile.owner = userId
    new_profile = await profile_collection.insert_one(
        profile.model_dump(
            exclude=["id", "email", "username", "password"], by_alias=True
        )
    )
    created_profile = await profile_collection.find_one(
        {"_id": new_profile.inserted_id}
    )
    return created_profile


# Login User
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


# Get profile information
@router.get("/me", response_model=ProfileModel, response_description="Get User Profile")
async def me(username: str):
    user_profile = await profile_collection.find_one({"owner": username})
    return user_profile


# Update profile
@router.put("/update/data")
async def update_profile_data(
    data: ProfileUpdate = Body(...), username=Depends(auth_handler.auth_wrapper)
):
    profile = await profile_collection.find_one({"owner": username})
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not available")

    updated_data = data.model_dump(exclude_unset=True)

    updated_profile = await profile_collection.update_one(
        {"owner": username}, {"$set": updated_data}
    )
    if updated_profile.modified_count == 0:
        raise HTTPException(status_code=400, detail="Field not updated")
    return {"message": "Fields updated successfully"}


# Update  profile picture
@router.put("/upload/profile")
async def upload_profile_pic(
    img: UploadFile = File(...), username=Depends(auth_handler.auth_wrapper)
):
    result = cloudinary.uploader.upload(
        img.file, folder="PROFILES", crop="scale", width=800
    )
    url = result.get("url")
    profile = await profile_collection.find_one({"owner": username})

    if profile is None:
        raise HTTPException(status_code=404, detail="profile is not available")

    # Update the field in the document
    updated_profile = await profile_collection.update_one(
        {"owner": username},
        {"$set": {"image": url}},
    )

    if updated_profile.modified_count == 0:
        raise HTTPException(status_code=400, detail="Field not updated")

    return {"message": "Field updated successfully"}

def send_my_email():
    print("Implementing background task")

@router.post("/email", response_description="Send Contact email")
async def send_contact_email(send_email: BackgroundTasks, contactinfo: ContactForm = Body(...)):
    received_info = contactinfo.model_dump()
    send_email.add_task(send_my_email)
    return ({"message": "Message sent!, I will get back to you as soon as possible"})