from configparser import ConfigParser

from ..utils.database import assemble_sqlalchemy_url

config = ConfigParser()
# Read in the default and local config files to populate our configuration
files_read = config.read(['./app/main/config/defaults.cfg', './app/main/config/local.cfg'])

class DatabaseConfig:
    DB_TYPE = config.get('database', 'type')
    DB_HOST = config.get('database', 'host')
    DB_DIALECT = config.get('database', 'dialect')  # Used to construct a SQLAlchemy URL
    DB_PORT = int(config.get('database', 'port'))
    DB_NAME = config.get('database', 'name')
    DB_USER = config.get('database', 'user')
    DB_PASS = config.get('database', 'pass')


class FlaskConfig:
    SERVER_NAME = "{}:{}".format(config.get('flask', 'host'), config.get('flask', 'port'))
    SECRET_KEY = config.get('flask', 'secret_key')
    DEBUG = config.get('flask', 'debug')
    JWT_SECRET_KEY = config.get('jwt', 'secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = int(config.get('jwt', 'access_token_expires'))
    # If a sql database is chosen, specify required flask-sqlalchemy configurations
    if config.get('database', 'type') == 'sql':
        SQLALCHEMY_DATABASE_URI = assemble_sqlalchemy_url(DatabaseConfig)
        SQLALCHEMY_TRACK_MODIFICATIONS = False

