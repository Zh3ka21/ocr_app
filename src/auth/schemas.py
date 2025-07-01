from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from uuid import UUID

# Shared fields
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

# Fields to receive on creation
class UserCreate(UserBase):
    username: str = Field(..., max_length=255)
    password: str = Field(..., min_length=8, max_length=40)

# Fields to receive on update
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8, max_length=40)

# Fields returned to client
class UserOut(UserBase):
    id: UUID
    username: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    sub: Optional[str] = None
