from fastapi import APIRouter, Depends, Response

from exceptions import APIException
from services.auth.auth import authenticate_user, create_access_token, get_password_hash
from services.auth.dao import UsersDAO
from services.auth.dependencies import get_current_user
from services.auth.models.users import Users
from services.auth.schemas.userauth import SUserAuth


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user





# @router.get("/all")  # Реализация ролей
# async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
#     return await UsersDAO.find_all()
