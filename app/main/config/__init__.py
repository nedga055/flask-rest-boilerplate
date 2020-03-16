from configparser import ConfigParser

config = ConfigParser()
# Read in the default and local config files to populate our configuration
files_read = config.read(['./app/main/config/defaults.cfg', './app/main/config/local.cfg'])


class FlaskConfig:
    SERVER_NAME = "{}:{}".format(config.get('flask', 'host'), config.get('flask', 'port'))
    SECRET_KEY = config.get('flask', 'secret_key')
    DEBUG = config.get('flask', 'debug')
    JWT_SECRET_KEY = config.get('jwt', 'secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = config.get('jwt', 'access_token_expires')


class DatabaseConfig:
    DB_TYPE = config.get('database', 'type')
    DB_HOST = config.get('database', 'host')
    DB_PORT = config.get('database', 'port')
    DB_NAME = config.get('database', 'name')
    DB_USER = config.get('database', 'user')
    DB_PASS = config.get('database', 'pass')
