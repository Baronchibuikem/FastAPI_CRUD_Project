from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


# add all your routers
app.include_router(post.router)
app.include_router(user.router)