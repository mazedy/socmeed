from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class User(UserBase):
    uid: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Post Schemas
class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    uid: str
    author_uid: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Relationship Schemas
class FollowCreate(BaseModel):
    target_uid: str

class FriendshipCreate(BaseModel):
    friend_uid: str

class LikeCreate(BaseModel):
    post_uid: str