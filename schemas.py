from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple,Union

import re

class Users(BaseModel):
    email: str
    password_hash: str
    phone: Optional[str]=None
    created_at: Optional[datetime.time]=None


class ReadUsers(BaseModel):
    email: str
    password_hash: str
    phone: Optional[str]=None
    created_at: Optional[datetime.time]=None
    class Config:
        from_attributes = True




class PutUsersUserId(BaseModel):
    user_id: Union[int, float] = Field(...)
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=150)
    created_at: Optional[Any]=None
    phone: Optional[str]=None
    password: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=150)
    created_at: Optional[str]=None
    phone: Optional[str]=None
    password: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetUsersUserIdQueryParams(BaseModel):
    """Query parameter validation for get_users_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True


class DeleteUsersUserIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_user_id"""
    user_id: int = Field(..., ge=1, description="User Id")

    class Config:
        populate_by_name = True
