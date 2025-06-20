from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Chats(Base):
    __tablename__ = 'chats'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_from = Column(Integer, ForeignKey('users.id'))
    user_to = Column(Integer, ForeignKey('users.id'))
    creation_date = Column(DateTime, default=datetime.now())
