from ..auth.auth import get_password_hash, verify_password
from ..models.users import UserModel
from .connection import db
from bson.objectid import ObjectId
from fastapi import HTTPException, status


users = db.get_collection("users")


FAILED_REGISTER = "User already exists."


async def add_user(user: UserModel) -> str:
    # TODO: validation on username & password requirements

    user.hashed_password = get_password_hash(user.hashed_password)

    search_result = await users.find_one({"name": user.name})
    if search_result is not None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, FAILED_REGISTER)

    created_user = await users.insert_one(user.model_dump(by_alias=True))
    user_id = str(created_user.inserted_id)
    return user_id


FAILED_LOGIN = "User or password is invalid."


async def login_user(name: str, password: str) -> dict:
    user = await users.find_one({"name": name})
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, FAILED_LOGIN)

    if not verify_password(password, user["hashed_password"]):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, FAILED_LOGIN)

    return user


async def get_user(user_id: str) -> UserModel:
    """
    Gets user without requiring password validation.
    """
    user = await users.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, FAILED_LOGIN)

    return UserModel(**user)
