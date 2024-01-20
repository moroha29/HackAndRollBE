from ..models.questions import QuestionModel
from ..models.users import UserModel
from ..auth.jwt import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import Annotated
from ..gpt.upload import fetch_generated

router = APIRouter()


@router.get("/generated_question/", status_code=status.HTTP_200_OK)
async def get_generated_question(user: Annotated[UserModel, Depends(get_current_user)]):
    if user._id is None:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    question= await fetch_generated()
    if question is None:
        return None
    return question

