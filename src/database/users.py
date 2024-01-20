from ..auth.auth import get_password_hash, verify_password
from ..models.users import UserModel, UserLoginModel
from .connection import db
from fastapi import HTTPException, status


users = db.get_collection("users")


FAILED_REGISTER = "User already exists."


async def add_user(user: UserModel) -> str:
    # TODO: validation on username & password requirements

    user.hashed_password = get_password_hash(user.hashed_password)

    search_result = await users.find_one({"name": user.name})
    if search_result is not None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, FAILED_REGISTER)

    created_result = await users.insert_one(user.model_dump(by_alias=True))
    user_id = str(created_result.inserted_id)
    return user_id


FAILED_LOGIN = "User or password is invalid."


async def login_user(login_info: UserLoginModel) -> str:
    user = await users.find_one({"name": login_info.name})
    if user is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, FAILED_LOGIN)

    if not verify_password(login_info.hashed_password, user["hashed_password"]):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, FAILED_LOGIN)

    user_id = str(user["_id"])
    return user_id
