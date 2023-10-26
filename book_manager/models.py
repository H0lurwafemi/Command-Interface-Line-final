from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship with books
    books = relationship("Book", back_populates="author")


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Define the relationship with books
    books = relationship("Book", back_populates="genre")


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    rating = Column(Float, nullable=False)

    # Define the foreign keys for author and genre
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))

    # Define the relationships with author and genre
    author = relationship("Author", back_populates="books")
    genre = relationship("Genre", back_populates="books")
