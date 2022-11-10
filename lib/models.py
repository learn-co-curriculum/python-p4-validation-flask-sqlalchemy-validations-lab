from sqlalchemy import func
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    phone_number = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f'Author(id={self.id}'

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    content = Column(String())
    category = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f'Post(id={self.id}'
