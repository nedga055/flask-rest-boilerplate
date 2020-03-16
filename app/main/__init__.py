from flask import Flask
from flask_script import Manager
from mongoengine import connect
from flask_jwt_extended import JWTManager

from .config import FlaskConfig, DatabaseConfig

from app.main.commands.client import CreateNewClient


def create_app():
    # Initialize flask app
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    # Initialize database
    # TODO: Would be nice to support other Database types
    connect(
        db=DatabaseConfig.DB_NAME,
        host=DatabaseConfig.DB_HOST,
        port=DatabaseConfig.DB_PORT,
        username=DatabaseConfig.DB_USER,
        password=DatabaseConfig.DB_PASS
    )
    # Initialize JWT authorization
    JWTManager(app)
    return app


def create_manager(app):
    # Set up the manager
    manager = Manager(app)
    # Add CLI commands
    manager.add_command('createnewclient', CreateNewClient())
    return manager
