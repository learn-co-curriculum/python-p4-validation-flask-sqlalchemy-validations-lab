import pytest
from sqlalchemy.exc import IntegrityError, CompileError
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app import app
from models import db, Author, Post


class TestAuthor:
    '''Class Author in models.py'''

    def test_requires_name(self):
        '''requires each record to have a name.'''
        
        with app.app_context():
            with pytest.raises(ValueError):
                author = Author(name = '', phone_number = '1231144321')
            db.session.query(Author).delete()
            db.session.query(Post).delete()
            db.session.commit()

    def test_requires_unique_name(self):
        '''requires each record to have a unique name.'''
        with app.app_context():

            author_a = Author(name = 'Ben', phone_number = '1231144321')
            author_b = Author(name = 'Ben', phone_number = '1231144321')
            with pytest.raises(IntegrityError):
                db.session.add(author_a)
                db.session.add(author_b)
                db.session.commit()
                db.session.query(Author).delete()
                db.session.commit()


    def test_requires_ten_digit_phone_number(self):
        '''requires each phone number to be exactly ten digits.'''

        with app.app_context():

            with pytest.raises(ValueError):
                author = Author(name="Jane Author", phone_number="3311")
                author2 = Author(name="Jane Author", phone_number="3312212121212121")

                db.session.add(author)
                db.session.add(author2)

                db.session.commit()


class TestPost:
    '''Class Post in models.py'''

    def test_requires_title(self):
        '''requires each record to have a title.'''

        with app.app_context():
            post = Post()
            with pytest.raises(IntegrityError):
                db.session.add(post)
                db.session.commit()
                db.session.query(Post).delete()
                db.session.commit()

    def test_content_length(self):
        '''requires each record to have a title.'''

        with app.app_context():
            content_string = "This is content" * 2

            with pytest.raises(ValueError):
                post = Post(title='Secret, Why I love programming.', content=content_string, category='Non-Fiction')
                db.session.add(post)
                db.session.commit()
                db.session.query(Post).delete()
                db.session.commit()

    def test_content_length(self):
        '''Content too short test. Less than 250 chars.'''

        with app.app_context():
            content_string = "This is content" * 2
            with pytest.raises(ValueError):
                post = Post(title='Secret, Why I love programming.', content=content_string, category='Non-Fiction')
                db.session.add(post)
                db.session.commit()

    def test_summary_length(self):
        '''Summary too long test. More than 250 chars.'''

        with app.app_context():
            content_string = "This is content" * 150
            summary_string = "This is summary" * 150
            with pytest.raises(ValueError):
                post = Post(title='Secret, Why I love programming.', content=content_string, summary= summary_string, category='Non-Fiction')
                db.session.add(post)
                db.session.commit()

    def test_category(self):
        '''Incorrect category test.  '''

        with app.app_context():
            content_string = "This is content" * 150
            with pytest.raises(ValueError):
                post = Post(title='Secret, Why I love programming.', content=content_string, category='Banana')
                db.session.add(post)
                db.session.commit()


    def test_clickbait(self):
        '''Test clickbait validator for title.'''
        with app.app_context():
            content_string = "This is content" * 150
            with pytest.raises(ValueError):
                post = Post(title='Why I love programming.', content=content_string, category='Fiction')
                db.session.add(post)
                db.session.commit()