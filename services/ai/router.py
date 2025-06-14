from fastapi import APIRouter, Depends

from services.auth.models.users import Users
from services.auth.dependencies import get_current_user
from services.ai.schemas import SRequest
from services.ai.request import answer
from services.auth.auth import authenticate_user
from services.ai.dao import UsagesDAO
from exceptions import APIException
from services.ai.data.parser import startup


router = APIRouter(
    prefix='/ai',
    tags=['ИИ ассистент']
)


@router.get('/parse')
async def start_parse():
    startup()
    return 'Парсинг завершен'


@router.post('/start')
async def get_ai_answer(
    request: SRequest,
    user: Users = Depends(get_current_user)
    ):
    response = answer(text=request.text)
    if response:
        await UsagesDAO.add(user_id=user.id, request_text=request.text, response_text=response)
        return response
    return None
    