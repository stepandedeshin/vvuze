from services.dao.base import BaseDAO
from services.auth.models.users import Users


class UsersDAO(BaseDAO):
    model = Users
