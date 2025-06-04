from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Friends(Base):
    __tablename__ = 'friends'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_from = Column(Integer, ForeignKey('users.id'))
    user_to = Column(Integer, ForeignKey('users.id'))
    accepted = Column(Boolean, default=False)
    date = Column(DateTime, default=datetime.now())
    