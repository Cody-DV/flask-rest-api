import factory

from src import models


class BookFactory(factory.Factory):
    class Meta:
        model = models.Book

    title = factory.sequence(lambda n: 'Book%s' % n)
