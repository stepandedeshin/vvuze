from datetime import datetime

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey

from core.psql import Base


class Likes(Base):
    __tablename__ = 'likes'
    
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    date = Column(DateTime, default=datetime.now())
    