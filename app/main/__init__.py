from flask import Flask
from flask_script import Manager
from mongoengine import connect
from flask_jwt_extended import JWTManager

from .config import FlaskConfig, DatabaseConfig

from app.main.commands.client import CreateNewClient

from app.main.db import db

def create_app():
    # Initialize flask app
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
    # Initialize database based on the type specified in the config
    if DatabaseConfig.DB_TYPE == "mongo":
        # Set up the mongodb connection
        connect(
            db=DatabaseConfig.DB_NAME,
            host=DatabaseConfig.DB_HOST,
            port=DatabaseConfig.DB_PORT,
            username=DatabaseConfig.DB_USER,
            password=DatabaseConfig.DB_PASS
        )
    if DatabaseConfig.DB_TYPE == "sql":
        # Set up the SQLAlchemy connection
        db.init_app(app)
        @app.before_first_request
        def create_tables():
            db.create_all()
    
    # Initialize JWT authorization
    JWTManager(app)
    return app


def create_manager(app):
    # Set up the manager
    manager = Manager(app)
    # Add CLI commands
    manager.add_command('createnewclient', CreateNewClient())
    return manager
