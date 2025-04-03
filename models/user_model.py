from sqlalchemy import Column,Integer,String,CheckConstraint,Text, DateTime, func
from config.data_base import Base

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, CheckConstraint('value > 5'),  index=True)
    email = Column(String, CheckConstraint('email ~* "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"'), nullable=False, unique=True, ) # type: ignore
    password = Column(String, CheckConstraint('LENGTH(password) > 6'), nullable=True)


class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    content = Column(Text, nullable=False)
    author_name = Column(String(100), nullable=False)  # Instead of author_id, storing author's name
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)