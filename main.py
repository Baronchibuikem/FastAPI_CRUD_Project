from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import post, user, auth


app = FastAPI()
Base.metadata.create_all(bind=engine)


# add all your routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)