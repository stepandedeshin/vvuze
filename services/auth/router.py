from fastapi import APIRouter, Depends, Response
from pydantic import TypeAdapter

from exceptions import APIException
from services.auth.auth import authenticate_user, create_access_token, get_password_hash
from services.auth.dao import UsersDAO
from services.user.dao import ProfilesDAO
from services.auth.dependencies import get_current_user
from services.auth.schemas.userauth import SUserAuth
from services.user.schemas.profiles import SProfiles


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

@router.post("/register")
async def register_user(
    user_data: SUserAuth,
    profile_data: SProfiles
    ):
    existing_user = await UsersDAO.find_one_or_none(login=user_data.login)
    if existing_user:
        raise APIException.UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(login=user_data.login, hashed_password=hashed_password)
    user = await UsersDAO.find_all(login=user_data.login)
    await ProfilesDAO.add(
        user_id=user[0].id, 
        **profile_data.model_dump()
    )  
    

@router.post("/login")
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.login, user_data.password)
    if not user:
        raise APIException.IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("active_token", access_token, httponly=True)
    return {"active_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("active_token")
    


# @router.get("/all")  # Реализация ролей
# async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
#     return await UsersDAO.find_all()
