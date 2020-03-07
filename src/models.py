import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone = Column(String(250), nullable=False)
  


class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    photo_id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    mention = Column(String(250))
    address = Column(String(250), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    usuario = relationship(Usuario)

class Profile(Base):
    __tablename__ = 'Profile'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    profile_id = Column(Integer, primary_key=True)
    photo = Column(String(250))
    followers = Column(String(250))
    following = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)

class Timeline(Base):
    __tablename__ = 'Timeline'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    Followers = Column(Integer, primary_key=True)
    Adds = Column(String(250))
    Post = Column(String(250))
    Likes = Column(String(250), nullable=False)
    profile_id= Column(Integer, ForeignKey('profile.id'))
    profile = relationship(Profile)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')