from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Profiles(Base):
    __tablename__ = 'profiles'
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    picture_url = Column(String, default=None)
    bio = Column(String, default=None)
    gender = Column(String, default=None)
    phone = Column(String, default=None)
    email = Column(String, default=None)
    