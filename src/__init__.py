from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    """ create and configure the app"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():

        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        # TODO: Seed book titles into database

        return app
