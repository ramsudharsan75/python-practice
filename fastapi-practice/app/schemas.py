"""Pydantic Schemas"""
from datetime import datetime

from pydantic import BaseModel, EmailStr, validator


class UserCreate(BaseModel):
    """User Create Model"""

    email: EmailStr
    password: str


class UserOut(BaseModel):
    """User Response Model"""

    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        """Pydantic auto conversion configuration"""

        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None


class PostBase(BaseModel):
    """Base Post Model"""

    title: str
    content: str
    published: bool = True


class CreatePost(PostBase):
    """New post model"""


class UpdatePost(PostBase):
    """Update post model"""

    published: bool


class PostOut(PostBase):
    """Post Response Model"""

    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        """Pydantic auto conversion configuration"""

        orm_mode = True


class PostVoteOut(BaseModel):
    """Post Vote Response Model"""

    Post: PostOut
    votes: int

    class Config:
        """Pydantic auto conversion configuration"""

        orm_mode = True


class Vote(BaseModel):
    post_id: int
    direction: int

    @validator("direction")
    def direction_must_be_0_or_1(cls, value):
        if value not in (0, 1):
            raise ValueError("Value must be either 0 or 1")

        return value
