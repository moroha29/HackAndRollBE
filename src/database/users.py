from ..auth.auth import get_password_hash, verify_password
from ..models.users import UserModel
from .connection import db
from fastapi import HTTPException, status


users = db.get_collection("users")


async def add_user(user: UserModel) -> str:
    # TODO: validation on username & password requirements

    user.hashed_password = get_password_hash(user.hashed_password)

    search_result = await users.find_one({"name": user.name})
    if search_result is not None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "User already exists.")

    created_result = await users.insert_one(user.model_dump(by_alias=True))
    user_id = created_result.inserted_id
    return user_id
