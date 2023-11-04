import pytest
from sqlalchemy.exc import IntegrityError
from app import app
from models import db, Author, Post
import logging
from faker import Faker


LOGGER = logging.getLogger(__name__)


class TestAuthor:
    '''Class Author in models.py'''

    def test_requires_name(self):
        '''requires each record to have a name.'''

        with app.app_context():
            # valid name
            author1 = Author(name = Faker().name(), phone_number = '1231144321')

            # missing name
            with pytest.raises(ValueError):
                author2 = Author(name = '', phone_number = '1231144321')

    def test_requires_unique_name(self):
        '''requires each record to have a unique name.'''
        
        with app.app_context():
            author_a = Author(name = 'Ben', phone_number = '1231144321')
            db.session.add(author_a)
            db.session.commit()
            
            with pytest.raises(ValueError):
                author_b = Author(name = 'Ben', phone_number = '1231144321')
                
            db.session.query(Author).delete()
            db.session.commit()

    def test_requires_ten_digit_phone_number(self):
        '''requires each phone number to be exactly ten digits.'''

        with app.app_context():

                
            with pytest.raises(ValueError):
                LOGGER.info('testing short phone number')
                author = Author(name="Jane Author", phone_number="3311")

            with pytest.raises(ValueError):
                LOGGER.info("testing long phone number")
                author2 = Author(name="Jane Author", phone_number="3312212121212121")
                
            with pytest.raises(ValueError):
                LOGGER.info("testing non-digit")
                author3 = Author(name="Jane Author", phone_number="123456789!")

class TestPost:
    '''Class Post in models.py'''

    def test_requires_title(self):
        '''requires each post to have a title.'''

        with app.app_context():
            with pytest.raises(ValueError):
                content_string = "HI" * 126
                post = Post(title = '', content=content_string, category='Non-Fiction')
                

    def test_content_length(self):
        '''Content too short test. Less than 250 chars.'''

        with app.app_context():
            
            #valid content length
            content_string1 = 'A' * 250
            post1 = Post(title='Secret Why I love programming.', content=content_string1, category='Non-Fiction')
            
            with pytest.raises(ValueError):
                #too short
                content_string2 = 'A' * 249
                post2 = Post(title='Guess Why I love programming.', content=content_string2, category='Non-Fiction')

    def test_summary_length(self):
        '''Summary too long test. More than 250 chars.'''

        with app.app_context():
            
            content_string = "A" * 250
            
            # valid summary string
            summary_string1 = "T" * 250
            post1 = Post(title='You Won\'t Believe Why I love programming..', content=content_string, summary= summary_string1, category='Non-Fiction')
            
            # too long
            summary_string2 = "T" * 251
            with pytest.raises(ValueError):
                post2 = Post(title='Top Reasons Why I love programming..', content=content_string, summary= summary_string2, category='Non-Fiction')


    def test_category(self):
        '''Incorrect category test'''

        with app.app_context():
            content_string = "A" * 251
            with pytest.raises(ValueError):
                post = Post(title='Top Ten Reasons I Love Programming.', content=content_string, category='Banana')


    def test_clickbait(self):
        '''Test clickbait validator for title.'''
        with app.app_context():
            content_string = "A" * 260
            with pytest.raises(ValueError):
                post = Post(title='Why I love programming.', content=content_string, category='Fiction')