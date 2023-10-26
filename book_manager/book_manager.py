
"""
Usage:
  book_manager.py add_book <title> <author> <genre> <rating>
  book_manager.py view_books
  book_manager.py search <attribute> <value>
  book_manager.py quit

Options:
  -h --help    Show this screen.

Commands:
  add_book    Add a new book to the database.
  view_books  View the list of all books.
  search      Search for books based on title, author, or genre.
  quit        Exit the application.

Examples:
  book_manager.py add_book "The Great Gatsby" "F. Scott Fitzgerald" "Classic" 4.5
  book_manager.py view_books
  book_manager.py search author "F. Scott Fitzgerald"
"""
import sys
from docopt import docopt
from commands import add_book, view_books, search


def main():
    args = docopt(__doc__)

    if args['add_book']:
        add_book(args['<title>'], args['<author>'],
                 args['<genre>'], float(args['<rating>']))
    elif args['view_books']:
        view_books()
    elif args['search']:
        search(args['<attribute>'], args['<value>'])
    elif args['quit']:
        sys.exit()


if __name__ == '__main__':
    main()
