from ..database.users import UserModel, UserLoginModel, add_user, login_user
from fastapi import APIRouter, Body, status

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserModel = Body(...)):
    """
    Registers a new user.
    """

    user_id = await add_user(user)
    return user_id


@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(user: UserLoginModel = Body(...)):
    """
    Logins a new user.
    """

    user_id = await login_user(user)
    return user_id
