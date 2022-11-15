from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from sqlalchemy.orm import validates, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///authors.db')
session = sessionmaker(bind=engine)()

class Author(Base):
    pass

class Post(Base):
    pass
Base.metadata.create_all(engine)
