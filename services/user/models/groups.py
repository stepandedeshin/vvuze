from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Groups(Base):
    __tablename__ = 'groups'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, default=None)
    creator_id = Column(Integer, ForeignKey('users.id'))
    creation_date = Column(DateTime, default=datetime.now())
    