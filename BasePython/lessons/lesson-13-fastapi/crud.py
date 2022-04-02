from lib2to3.pgen2.token import OP
from typing import Optional
from schemes import UserIn, User


USER_ID_TO_USER: dict[int: User] = {}
USER_TOKEN_TO_USER: dict[str, User] = {}


def create_user(user_in: UserIn) -> User:
    new_id = len(USER_ID_TO_USER) + 1
    user = User(id=new_id, **user_in.dict())

    # db
    USER_ID_TO_USER[user.id] = user
    USER_TOKEN_TO_USER[user.token] = user

    return user


def list_users() -> list[User]:
    return list(USER_ID_TO_USER.values())


def get_user_by_id(user_id) -> Optional[User]:
    return USER_ID_TO_USER.get(user_id)


def get_user_by_token(user_token) -> Optional[User]:
    return USER_TOKEN_TO_USER.get(user_token)