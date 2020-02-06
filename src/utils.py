from flask import jsonify
from . import db
from .models import Book


def seed_books_table():
    """
    Populates the Book table if it is empty.

    Args:
    Returns:
    Raises:

    """

    titles = ['Dune', 'Blindsight', 'Anathem', 'Cryptonomicon',
              'Foundation']

    if Book.query.first() is None:
        for title in titles:
            print("Seeding book: ", title)
            db.session.add(Book(title=title))
            db.session.commit()
    else:
        print("INFO: Book table already seeded. Skipping.")


def check_book_exists(title):
    """
    Queries a book by title
    returns true if it exists in the DB.

    Args:
        title: String
    Returns:
        A boolean set to True if the book exists.
    Raises:

    """

    try:
        result = db.session.query(Book).filter(Book.title == title).one()
        return result is not None

    except Exception as e:
        # log e
        print(str(e))
        return False


def api_response(data=None):
    """
    Builds and returns a standardized json response
    following the jsend guidelines.

    https://github.com/omniti-labs/jsend

    Args:
        data: a dict containing the response data
                
    Returns:
        A json response in the format:

            {
                "data": {
                    "email": "email@gmail.com",
                    "title": "Example"
                },
                "status": "success"
            }

    Raises:

    """

    response = {
        "status": "success",
        "data": data
    }

    return jsonify(response)
