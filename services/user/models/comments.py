from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from core.psql import Base


class Comments(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    text = Column(String, default=None)
    media_url = Column(String, default=None)
    date = Column(DateTime, default=datetime.now())
    