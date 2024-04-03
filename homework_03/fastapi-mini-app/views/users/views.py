from fastapi import APIRouter, status, HTTPException

from .crud import storage
from .schemas import UserCreate, UserOut, User


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
def get_users():
    return storage.get_users()


@router.post("", response_model=User)
def create_user(
        user_in: UserCreate,
):
    user = storage.create_user(user_in=user_in)
    return user


@router.get(
    "/{user_id",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User with id not found",
            "content": {
                "aplication/json": {
                    "example": {
                        "detail": "User with id #0 not found"
                    },
                },
            },
        },
    },
)
def get_user_by_id(user_id: int):
    user = storage.get_user(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id #{user_id} not found",
    )
