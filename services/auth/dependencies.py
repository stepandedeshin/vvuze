from datetime import datetime, timezone
from fastapi import Depends, Request
from jose import jwt, JWTError

from config import cnf
from exceptions import APIException
from services.user.dao import UsersDAO 


def get_token(request: Request):
    token = request.cookies.get("active_token")
    if not token:
        raise APIException.TokenAbsentException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(
        token, cnf.jwt_token.SECRET_KEY, cnf.jwt_token.ALGORITHM
    )
    except JWTError:
        raise APIException.IncorrectTokenFormatException
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(timezone.utc).timestamp()):
        raise APIException.TokenExpiredException
    user_id: str = payload.get("sub")
    if not user_id:
        raise APIException.UserIsNotPresentException    
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise APIException.UserIsNotPresentException
    
    return user



# async def get_current_admin_user(current_user: Users = Depends(get_current_user)):   # Реализация ролей
#     # if current_user.role != "admin":
#     #     raise AccessRightsException
#     return