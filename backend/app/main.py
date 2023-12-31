from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import user, project

origins = ["*"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)


app.include_router(user.router)
app.include_router(project.router)


@app.get("/")
async def root():
    return {"message": "Welcome aboard"}