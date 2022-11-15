#!/usr/bin/env python3
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Author, Post

if __name__ == '__main__':

    engine = create_engine('sqlite:///authors.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Author).delete() 
    session.query(Post).delete() 

    session.commit()

    # add author
    author = Author(name='Ben', phone_number='1233131111')
    session.add(author)

    # add post
    # You may change the number next to the content and summary string 
    # Variables to test different string lengths.
    content_string = "This is content" * 20
    summary_string = "This is a summary" * 2
    post = Post(title=' Secret, Why I love programming.', content=content_string, category='Non-Fiction', summary= summary_string)
    session.add(post)

    #commit author and post
    session.commit()

    print(session.query(Author).all())
    print(session.query(Post).all())

    import ipdb; ipdb.set_trace()
