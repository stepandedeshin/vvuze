from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Messages(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_from = Column(Integer, ForeignKey('users.id'))
    user_to = Column(Integer, ForeignKey('users.id'))
    text = Column(String, default=None)
    media_url = Column(String, default=None)
    date = Column(DateTime, default=datetime.now())
