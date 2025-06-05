from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Messages(Base):
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, ForeignKey('chats.id'))
    text = Column(String, default=None)
    media_url = Column(String, default=None)
    date = Column(DateTime, default=datetime.now())
