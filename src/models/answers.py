from .users import AgeRangeEnum, GenderEnum, MaritalStatusEnum
from pydantic import BaseModel, Field


class AnswerInputModel(BaseModel):
    question_id: str = Field(...)
    option: str = Field(...)


class AnswerModel(BaseModel):
    user_id: str = Field(...)
    option: str = Field(...)
    age_range: AgeRangeEnum = Field(...)
    gender: GenderEnum = Field(...)
    marital_status: MaritalStatusEnum = Field(...)
