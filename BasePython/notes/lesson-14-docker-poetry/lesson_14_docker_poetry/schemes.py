from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel, Field, validator


class UserIn(BaseModel):
    username: str

    @validator("username")
    def validate_username(cls, value: str):
        if value.isdigit():
            raise ValueError("Username can not be digits only.")
        return value


class UserBase(UserIn):
    id: int
    created_at: datetime = Field(default_factory=datetime.now)


class UserOut(UserBase):
    pass


def generate_token():
    token = str(uuid4())
    print("token:", repr(token))
    return token


class User(UserBase):
    token: str = Field(default_factory=generate_token)


class CalcInput(BaseModel):
    a: int
    b: int