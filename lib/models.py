from sqlalchemy import Column, Integer, String, DateTime, func, create_engine
from sqlalchemy.orm import validates, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///authors.db')
session = sessionmaker(bind=engine)()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer(), primary_key=True)
    name= Column(String())
    phone_number = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

    @validates('name')
    def validate_name(self, key, name):
        names = session.query(Author.name).all()
        if not name:
            raise ValueError("Name field is required.")
        elif name in names:
            raise ValueError("Name must be unique.")
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, phone_number):
        if len(phone_number) != 10:
            raise ValueError("Phone number must be 10 digits.")
        return phone_number

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    content = Column(String())
    category = Column(String())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title})'

Base.metadata.create_all(engine)
