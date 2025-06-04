from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime

from core.psql import Base


class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    registration_date = Column(DateTime, default=datetime.now())