from services.dao.base import BaseDAO
from services.ai.models.usages import Usages


class UsagesDAO(BaseDAO):
    model = Usages