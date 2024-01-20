from ..database.users import UserModel, add_user
from fastapi import APIRouter, Body, status

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserModel = Body(...)):
    """
    Registers a new user.
    """

    await add_user(user)
