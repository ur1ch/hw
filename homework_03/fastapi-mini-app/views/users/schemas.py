from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Create a new user
    """


class UserOut(UserBase):
    id: int = Field(
        ...,
        description="User ID in DB automatically generated",
        example=123,
    )


class User(UserBase):
    id: int
