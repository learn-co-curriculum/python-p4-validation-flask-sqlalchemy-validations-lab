import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

from models import Author, Post

engine = create_engine('sqlite:///authors.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Author).delete()
session.query(Post).delete()
session.commit()

class TestAuthor:
    '''Class Author in models.py'''

    def test_requires_name(self):
        '''requires each record to have a name.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        author = Author()
        with pytest.raises(ValueError):
            session.add(author)
            session.commit()

    # def test_requires_unique_name(self):
    #     '''requires each record to have a unique name.'''

    #     engine = create_engine('sqlite:///authors.db')
    #     Session = sessionmaker(bind=engine)
    #     session = Session()

    #     author_a = Author(name="John Author")
    #     author_b = Author(name="John Author")
    #     with pytest.raises(IntegrityError):
    #         session.add(author_a)
    #         session.add(author_b)
    #         session.commit()

    # def test_requires_ten_digit_phone_number(self):
    #     '''requires each phone number to be exactly ten digits.'''

    #     engine = create_engine('sqlite:///authors.db')
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
        
    #     author = Author(name="Jane Author", phone_number="555555555")
    #     with pytest.raises(ValueError):
    #         session.add(author)
    #         session.commit()

class TestPost:
    '''Class Post in models.py'''

    def test_performs_behavior(self):
        '''performs behavior when something happens.'''
        assert(True)
