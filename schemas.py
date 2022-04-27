from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


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

    class Config:
        """This will tell pydantic to read our value from sqlachemy"""
        orm_mode = True


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


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None