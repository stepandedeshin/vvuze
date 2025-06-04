from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class GroupMembers(Base):
    __tablename__ = 'group_members'
    
    user_id = Column(Integer, ForeignKey('users.is'), primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.id'), primary_key=True)
    join_date = Column(DateTime, default=datetime.now())
    