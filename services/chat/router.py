from fastapi import APIRouter, Depends

from services.auth.dependencies import get_current_user
from services.chat.dao import ChatsDAO, MessagesDAO
from services.chat.schemas.chats import SChats
from services.chat.schemas.messages import SMessages


router = APIRouter(
    prefix='/chats',
    tags=['Чаты']
)


@router.get('/')
async def get_user_chats(
        user = Depends(get_current_user)
    ):
    chats = await ChatsDAO.get_chat_pairs(user_id=user.id)
    chats_list = []
    for chat in chats:
        chat = SChats.model_validate(chat, from_attributes=True)
        chat = chat.model_dump()
        messages = await MessagesDAO.find_all(chat_id=chat['id'])
        chat['messages'] = messages
        chats_list.append(chat)
    return chats_list


@router.get('/cid={chat_id}')
async def get_chat(
        chat_id: int,
        user = Depends(get_current_user)
    ):
        messages = await MessagesDAO.find_all(chat_id=chat_id)
        return messages