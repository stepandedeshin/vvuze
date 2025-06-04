from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Bans(Base):
    __tablename__ = 'bans'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), autoincrement=True)
    registration_date = Column(DateTime, ForeignKey('users.registration_date'))
    ban_date = Column(DateTime, default=datetime.now())
    unbanned = Column(Boolean, default=False)