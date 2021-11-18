import factory

from .base import BaseFactory
from src import models


class BookFactory(BaseFactory):
    class Meta:
        model = models.Book

    title = factory.sequence(lambda n: 'Book %s' % n)


class RequestFactory(BaseFactory):
    class Meta:
        model = models.Request

    title = factory.Faker('sentence', nb_words=3)
    email = factory.Faker("email")
