"""
Tasks for Lesson 02 (Advanced Relationships)
"""
from __future__ import annotations
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

# Association table for many-to-many relationship
post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # One-to-many relationship
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self):
        raise NotImplementedError


class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(1000))
    author_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Many-to-one relationship
    author = relationship("User", back_populates="posts")
    
    # Many-to-many relationship
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")
    
    def __repr__(self):
        raise NotImplementedError


class Tag(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Many-to-many relationship
    posts = relationship("Post", secondary=post_tags, back_populates="tags")
    
    def __repr__(self):
        raise NotImplementedError


class UserPost(Base):
    __tablename__ = 'user_posts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    rating = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User")
    post = relationship("Post")
    
    def __repr__(self):
        raise NotImplementedError


