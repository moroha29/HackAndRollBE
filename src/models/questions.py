from pydantic import BaseModel, Field
from .answers import AnswerModel


class QuestionModel(BaseModel):
    question: str = Field(...)
    options: list[str] = Field(...)
    answers: list[AnswerModel] = []
    comments: list[str] = []


class QuestionCollection(BaseModel):
    """
    A container holding a list of `QuestionModel` instances.

    This exists because providing a top-level array in a JSON response can be a
    [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    students: list[QuestionModel]
