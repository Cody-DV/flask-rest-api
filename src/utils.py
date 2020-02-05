from flask import jsonify
from . import db
from .models import Book


def seed_books_table():
    """
    Populates the Book table if it is empty

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
    returns true if it exists in the DB

    """

    result = False

    try:
        result = db.session.query(Book).filter(Book.title == title).one()
        return result is not None

    except Exception as e:
        # log e
        print(str(e))

    return result


def api_response(status, data):
    """
    Returns a json response
    following the jsend guidelines.

    https://github.com/omniti-labs/jsend

    """

    # TODO: Handle exceptions

    response = ''

    if status == "fail" or status == "success":
        response = {
            "status": status,
            "data": data
        }

    if status == "error":
        response = {
            "status": "error",
            "message": data
        }

    return jsonify(response)
