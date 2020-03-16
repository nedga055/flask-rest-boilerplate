from flask import Flask

from .config import FlaskConfig


def create_app():
    # Initialize flask app
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    # TODO: Initialize database
    return app
