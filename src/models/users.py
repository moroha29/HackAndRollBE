from enum import Enum
from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from typing_extensions import Annotated


PyObjectId = Annotated[str, BeforeValidator(str)]


class AgeRangeEnum(str, Enum):
    one = "<18"
    two = "18-24"
    three = "25-29"
    four = "30-39"
    five = "40-49"
    six = "50+"


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    nonbinary = "nonbinary"


class MaritalStatusEnum(str, Enum):
    single = "single"
    attached = "attached"
    married = "married"


class UserModel(BaseModel):
    """
    Container for a single user record.
    """

    name: str = Field(...)
    hashed_password: str = Field(...)
    age_range: AgeRangeEnum = Field(...)
    gender: GenderEnum = Field(...)
    marital_status: MaritalStatusEnum = Field(...)


class UserCollection(BaseModel):
    """
    A container holding a list of `UserModel` instances.

    This exists because providing a top-level array in a JSON response can be a
    [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """

    students: list[UserModel]


class UserLoginModel(BaseModel):
    name: str = Field(...)
    hashed_password: str = Field(...)
