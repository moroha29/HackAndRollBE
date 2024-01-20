from ..auth.jwt import create_access_token, get_current_user
from ..database.users import add_user, login_user
from ..models.users import UserModel, UserLoginModel
from fastapi import APIRouter, Body, Depends, status
from typing_extensions import Annotated

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserModel = Body(...)):
    """
    Registers a new user.
    """

    user_id = await add_user(user)
    token = create_access_token(user.name, user_id)
    return token


@router.post("/login", status_code=status.HTTP_201_CREATED)
async def login(user: UserLoginModel = Body(...)):
    """
    Logins the user.
    """

    loggedin_user = await login_user(user.name, user.hashed_password)
    user_id = str(loggedin_user["_id"])
    token = create_access_token(user.name, user_id)
    return token


# TODO: remove this test endpoint
@router.get("/cook", status_code=status.HTTP_200_OK)
async def cook(user: Annotated[UserModel, Depends(get_current_user)]):
    return user.name
