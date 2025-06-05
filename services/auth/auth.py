from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr


from config import cnf
from services.auth.dao import UsersDAO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=cnf.jwt_token.TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, cnf.jwt_token.SECRET_KEY, cnf.jwt_token.ALGORITHM
    )

    return encoded_jwt


async def authenticate_user(login: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(login=login)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user