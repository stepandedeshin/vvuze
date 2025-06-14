from fastapi import APIRouter, Depends, Response
from fastapi_cache import FastAPICache
from pydantic import TypeAdapter
import asyncio

from exceptions import APIException
from services.auth.auth import authenticate_user, create_access_token, get_password_hash
from services.auth.dao import UsersDAO
from services.auth.dependencies import get_current_user
from services.auth.models.users import Users
from services.auth.schemas.userauth import SUserAuth
from services.user.dao import ProfilesDAO, PostsDAO, FriendsDAO, GroupMembersDAO, GroupsDAO
from services.user.schemas.profiles import SProfiles
from services.user.schemas.posts import SPosts
from services.user.schemas.friends import SFriends
from services.user.schemas.group_members import SGroupMembers
from core.redis import cache


router = APIRouter(
    prefix="/users",
    tags=["Пользователи"],
)


@router.get("/me")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    user_profile = await ProfilesDAO.find_all(user_id=current_user.id)
    return user_profile[0]


@router.get("/feed")
async def get_feed():
    posts = await PostsDAO.find_recent_posts()
    return posts


@router.get("/{user_id}")
@cache(key_pattern="profile_cached:{user_id}", ttl=30)
async def get_user_profile(user_id: int):
    try:
        groups = []
        group_member_in = await GroupMembersDAO.find_all(user_id=user_id)
        for group in group_member_in:
            group = (SGroupMembers.model_validate(group, from_attributes=True)).model_dump()
            groups.append(group)
        friends = await FriendsDAO.get_pairs(user_id=user_id)
        friends = [(SFriends.model_validate(friend, from_attributes=True)).model_dump() for friend in friends]
        posts = await PostsDAO.find_all(user_id=user_id)
        posts = [(SPosts.model_validate(post, from_attributes=True)).model_dump() for post in posts]
        profile = (await ProfilesDAO.find_all(user_id=user_id))[0]
        profile_validate = SProfiles.model_validate(profile, from_attributes=True)
        profile_dict = profile_validate.model_dump()
        profile_dict['posts'] = posts
        profile_dict['friends'] = friends
        profile_dict['groups'] = groups
        return profile_dict
    except Exception as e:
        print(e)
        raise APIException.BAD_REQUEST
    



# @router.get("/all")  # Реализация ролей
# async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
#     return await UsersDAO.find_all()
