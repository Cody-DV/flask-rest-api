from os import environ


class Config:

    # General
    FLASK_DEBUG = environ.get('FLASK_DEBUG')

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get(
        'SQLALCHEMY_TRACK_MODIFICATIONS')


# class DevConfig(Config):
#     # General
#     DEBUG = True
#     # Database
#     SQLALCHEMY_DATABASE_URI = 'dev.db'
