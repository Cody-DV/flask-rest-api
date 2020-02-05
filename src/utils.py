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
    Builds and returns a standardized json response
    following the jsend guidelines.

    https://github.com/omniti-labs/jsend

    Args:
        status: a string indicating status of the request
                'success', 'error', 'fail'
        data: a dict containing the response data for
                success and fail or a String with the error
                message if status is error.
    Returns:
        A json response in the format:

            {
                "data": {
                    "email": "email@gmail.com",
                    "title": "Example"
                },
                "status": "success"
            }

        or, on error:

            {
                "message": "Title with ID: 24 not found",
                "status": "error"
            }

    Raises:

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
