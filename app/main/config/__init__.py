from configparser import ConfigParser

config = ConfigParser()
# Read in the default and local config files to populate our configuration
files_read = config.read(['./app/main/config/defaults.cfg', './app/main/config/local.cfg'])

class FlaskConfig:
    SERVER_NAME = "{}:{}".format(config.get('flask', 'host'), config.get('flask', 'port'))
    SECRET_KEY = config.get('flask', 'secret_key')
    DEBUG = config.get('flask', 'debug')
    JWT_SECRET_KEY = config.get('jwt', 'secret_key')
    JWT_ACCESS_TOKEN_EXPIRES = int(config.get('jwt', 'access_token_expires'))

class DatabaseConnection(object):
    ''' Defines a Database connection. '''
    def __init__(self, host, port, name, user, password):
        self.HOST = host
        self.PORT = port
        self.NAME = name
        self.USER = user
        self.PASS = password

class DataSourcesConfig:
    DATABASES = {}
    # If specified correctly, DATA_SOURCES should be a python list.
    db_connections = config.get('databases', 'supported_databases').split('\n')
    for source in db_connections:
        connection = config.get('database', source).split('\n')
        DATABASES[source] = DatabaseConnection(
            connection[0],
            connection[1],
            connection[2],
            connection[3],
            connection[4],)
    print("host is ", DATABASES["mongo"].HOST)

class DatabaseConfig:
    DB_TYPE = config.get('database', 'type')
    DB_HOST = config.get('database', 'host')
    DB_PORT = int(config.get('database', 'port'))
    DB_NAME = config.get('database', 'name')
    DB_USER = config.get('database', 'user')
    DB_PASS = config.get('database', 'pass')
