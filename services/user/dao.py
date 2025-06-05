from datetime import datetime

from sqlalchemy import delete, insert, select, desc, or_, and_

from services.dao.base import BaseDAO
from services.user.models.comments import Comments
from services.user.models.friends import Friends
from services.user.models.group_members import GroupMembers
from services.user.models.groups import Groups
from services.user.models.likes import Likes
from services.chat.models.messages import Messages
from services.user.models.posts import Posts
from services.user.models.profiles import Profiles
from core.psql import async_session_maker


class CommentsDAO(BaseDAO):
    model = Comments


class FriendsDAO(BaseDAO):
    model = Friends
    
    async def _find_pairs(
        cls,
        user_id: int
    ):
        async with async_session_maker() as session:
            query = select(cls.model).where(
            and_(
                cls.model.accepted == True,
                or_(
                    cls.model.user_from == user_id,
                    cls.model.user_to == user_id
                    )
                )
            )
        result = await session.execute(query)
        await session.close()
        return result.scalars().all()

    @classmethod
    async def get_pairs(
        cls,
        user_id: int
    ):
        unique_pairs = {}
        pairs = await cls._find_pairs(cls=cls, user_id=user_id)
        for pair in pairs:
            u1 = pair.user_from
            u2 = pair.user_to
            key = tuple(sorted([u1, u2]))
            if key not in unique_pairs:
                unique_pairs[key] = pair

        return list(unique_pairs.values())


class GroupMembersDAO(BaseDAO):
    model = GroupMembers


class GroupsDAO(BaseDAO):
    model = Groups


class LikesDAO(BaseDAO):
    model = Likes
    

    
class PostsDAO(BaseDAO):
    model = Posts
    
    @classmethod
    async def find_recent_posts(cls):
        async with async_session_maker() as session:
            query = select(cls.model).order_by(desc(cls.model.creation_date)).limit(20)
            result = await session.execute(query)
            return result.scalars().all()
    
    
class ProfilesDAO(BaseDAO):
    model = Profiles
