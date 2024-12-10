import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True, index=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String)
    email = Column(String, nullable=False, unique=True)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='post')

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref='comment')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', backref='comment')

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    from_id = Column(Integer, ForeignKey('user.id'))
    to_id = Column(Integer, ForeignKey('user.id'))
    user_from_id = relationship('User', foreign_keys=[from_id], backref='Follower')
    user_to_id = relationship('User', foreign_keys=[to_id], backref='Followed')

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
