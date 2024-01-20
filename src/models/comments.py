from .users import AgeRangeEnum, GenderEnum, MaritalStatusEnum
from pydantic import BaseModel, Field


class QuestionCommentModel(BaseModel):
    question_id: str = Field(...)
    comment: str = Field(...)


class CommentModel(BaseModel):
    question_id: str = Field(...)
    comment: str = Field(...)
    age_range: AgeRangeEnum = Field(...)
    gender: GenderEnum = Field(...)
    marital_status: MaritalStatusEnum = Field(...)
