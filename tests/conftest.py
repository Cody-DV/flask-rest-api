import pytest
from src import db, create_app
from tests.factories import RequestFactory


@pytest.fixture()
def session():
    with create_app().app_context():
        db.session.begin()
        yield db.session
        db.session.rollback()


@pytest.fixture()
def book_request(session):
    book_request = RequestFactory.create()
    session.add(book_request)
    session.commit()
    return book_request
