from ..auth.jwt import get_current_user
from ..database.questions import add_question, answer_question, fetch_all, fetch_random
from ..models.answers import AnswerInputModel
from ..models.questions import QuestionModel
from ..models.users import UserModel
from fastapi import APIRouter, Depends, HTTPException, status
from typing_extensions import Annotated


router = APIRouter()


@router.get("/random/", status_code=status.HTTP_200_OK)
async def get_random(user: Annotated[UserModel, Depends(get_current_user)]):
    if user._id is None:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

    question = await fetch_random(user._id)
    if question is None:
        return None
    question["_id"] = str(question["_id"])
    return question


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all(user: Annotated[UserModel, Depends(get_current_user)]):
    if user._id is None:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

    questions = await fetch_all(user._id)
    return questions


@router.post("/", status_code=status.HTTP_200_OK)
async def create_question(
    question: QuestionModel, user: Annotated[UserModel, Depends(get_current_user)]
):
    if user._id is None:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)
    question_id = await add_question(question)
    return question_id


@router.post("/answer/", status_code=status.HTTP_200_OK)
async def answer(
    answer_input: AnswerInputModel,
    user: Annotated[UserModel, Depends(get_current_user)],
) -> bool:
    if user._id is None:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR)

    question_id = answer_input.question_id
    option = answer_input.option

    answer = {
        "user_id": str(user._id),
        "option": option,
        "age_range": user.age_range,
        "gender": user.gender,
        "marital_status": user.marital_status,
    }
    result = await answer_question(question_id, answer)
    return result
