from datetime import datetime

from sqlalchemy import delete, insert, select, desc, or_, and_

from core.psql import async_session_maker
from services.dao.base import BaseDAO
from services.chat.models.messages import Messages
from services.chat.models.chats import Chats

    
class MessagesDAO(BaseDAO):
    model = Messages


class ChatsDAO(BaseDAO):
    model = Chats
    
    async def _find_chat_pairs(
        cls,
        user_id: int
    ):
        async with async_session_maker() as session:
            query = select(cls.model).where(
                or_(
                    cls.model.user_from == user_id,
                    cls.model.user_to == user_id
                )
            )
        result = await session.execute(query)
        await session.close()
        if result:
            return result.scalars().all()
        return None

    @classmethod
    async def get_chat_pairs(
        cls,
        user_id: int
    ):
        unique_pairs = {}
        pairs = await cls._find_chat_pairs(cls=cls, user_id=user_id)
        if not pairs:
            return None
        for pair in pairs:
            u1 = pair.user_from
            u2 = pair.user_to
            key = tuple(sorted([u1, u2]))
            if key not in unique_pairs:
                unique_pairs[key] = pair

        return list(unique_pairs.values())