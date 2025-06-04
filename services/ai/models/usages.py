from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from core.psql import Base


class Usages(Base):
    __tablename__ = 'usages'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    request_text = Column(String, nullable=False)
    response_text = Column(String) 
    date = Column(DateTime, default=datetime.now())