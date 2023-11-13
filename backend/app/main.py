from fastapi import FastAPI
from .routers import user, project


app = FastAPI()
app.include_router(user.router)
app.include_router(project.router)


@app.get("/")
async def root():
    return {"message": "Welcome aboard"}