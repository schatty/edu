from fastapi import Header, HTTPException, status

import crud
from schemes import User


def get_user_by_auth_token(token: str = Header(..., description="User auth token.")):
    user = crud.get_user_by_token(token)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Invalid token!")
    