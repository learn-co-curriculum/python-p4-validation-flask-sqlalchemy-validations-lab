import pytest
from sqlalchemy.exc import IntegrityError, CompileError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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
        '''requires each record to have a unique name.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        author = Author()
        with pytest.raises(IntegrityError):
            session.add(author)
            session.commit()

    def test_requires_unique_name(self):
        '''requires each record to have a unique name.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        author_a = Author(name='Ben', phone_number='1233231311')
        author_b = Author(name='Ben', phone_number='1233231311')
        with pytest.raises(IntegrityError):
            session.add(author_a)
            session.add(author_b)
            session.commit()

    def test_requires_ten_digit_phone_number(self):
        '''requires each phone number to be exactly ten digits.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()

        with pytest.raises(ValueError):
            author = Author(name="Jane Author", phone_number="3311")
            session.add(author)
            session.commit()


class TestPost:
    '''Class Post in models.py'''

    def test_requires_title(self):
        '''requires each record to have a title.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        post = Post()
        with pytest.raises(IntegrityError):
            session.add(post)
            session.commit()

    def test_content_length(self):
        '''requires each record to have a title.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        content_string = "This is content" * 2

        with pytest.raises(ValueError):
            post = Post(title='Secret, Why I love programming.', content=content_string, category='Non-Fiction')
            session.add(post)
            session.commit()

    def test_content_length(self):
        '''Content too short test. Less than 250 chars.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        content_string = "This is content" * 2
        with pytest.raises(ValueError):
            post = Post(title='Secret, Why I love programming.', content=content_string, category='Non-Fiction')
            session.add(post)
            session.commit()

    def test_summary_length(self):
        '''Summary too long test. More than 250 chars.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        content_string = "This is content" * 150
        summary_string = "This is summary" * 150
        with pytest.raises(ValueError):
            post = Post(title='Secret, Why I love programming.', content=content_string, summary= summary_string, category='Non-Fiction')
            session.add(post)
            session.commit()

    def test_category(self):
        '''Incorrect category test.  '''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        content_string = "This is content" * 150
        with pytest.raises(ValueError):
            post = Post(title='Secret, Why I love programming.', content=content_string, category='Banana')
            session.add(post)
            session.commit()


    def test_clickbait(self):
        '''Test clickbait validator for title.'''

        engine = create_engine('sqlite:///authors.db')
        Session = sessionmaker(bind=engine)
        session = Session()
        content_string = "This is content" * 150
        with pytest.raises(ValueError):
            post = Post(title='Why I love programming.', content=content_string, category='Fiction')
            session.add(post)
            session.commit()