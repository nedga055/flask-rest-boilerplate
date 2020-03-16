from configparser import ConfigParser

config = ConfigParser()
# Read in the default and local config files to populate our configuration
files_read = config.read(['./app/main/config/defaults.cfg', './app/main/config/local.cfg'])


class FlaskConfig:
    SERVER_NAME = "{}:{}".format(config.get('flask', 'host'), config.get('flask', 'port'))
    SECRET_KEY = config.get('flask', 'secret_key')
    DEBUG = config.get('flask', 'debug')
