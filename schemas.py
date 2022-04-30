from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime

    class Config:
        """This will tell pydantic to read our value from sqlachemy"""
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    """For creating our Post"""
    pass


class PostResponse(PostBase):
    """A representation of what our post response look like"""
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse

    class Config:
        """This will tell pydantic to read our value from sqlachemy"""
        orm_mode = True

class PostVote(BaseModel):
    Post: PostResponse
    votes: int

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class VoteBase(BaseModel):
    post_id: int
    dir: conint(le=1)