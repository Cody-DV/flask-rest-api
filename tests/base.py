import factory

from src import db


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """Base class for factories"""

    class Meta:
        abstract = True
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "flush"
