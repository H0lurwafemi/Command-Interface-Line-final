from models import Author, Genre, Book
from db import session


def add_book(title, author_name, genre_name, rating):
    # Check if the author already exists, or create a new one
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)

    # Check if the genre already exists, or create a new one
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)

    # Create a new book
    new_book = Book(title=title, author=author, genre=genre, rating=rating)

    # Add the book to the database
    session.add(new_book)
    session.commit()

    print(f"Added book: {title} by {author_name}")


def view_books():
    books = session.query(Book).all()

    if not books:
        print("No books found.")
    else:
        print("List of Books:")
        for book in books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author.name}")
            print(f"Genre: {book.genre.name}")
            print(f"Rating: {book.rating}")
            print()


def search(attribute, value):
    if attribute == "title":
        books = session.query(Book).filter(
            Book.title.ilike(f'%{value}%')).all()
    elif attribute == "author":
        books = session.query(Book).join(Author).filter(
            Author.name.ilike(f'%{value}%')).all()
    elif attribute == "genre":
        books = session.query(Book).join(Genre).filter(
            Genre.name.ilike(f'%{value}%')).all()
    else:
        print("Invalid search attribute. Please use 'title', 'author', or 'genre'.")
        return

    if not books:
        print(f"No books found with {attribute} containing '{value}'.")
    else:
        print(f"Books found with {attribute} containing '{value}':")
        for book in books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author.name}")
            print(f"Genre: {book.genre.name}")
            print(f"Rating: {book.rating}")
            print()
