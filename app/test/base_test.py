from unittest import TestCase

from app.main.config import DatabaseConfig
from app.main.utils.database import assemble_sqlalchemy_url

from manage import app
from app.main.db import db

class BaseTest(TestCase):
    '''
    A base test class with setup and teardown methods to create an
    application context/initialized database for testing purposes.
    '''
    @classmethod
    def setUpClass(cls):
        '''
        Set up method for the BaseTest class (sets any required testing configurations)
        '''
        # Create a separate testing database that is different from the development database.
        if DatabaseConfig.DB_TYPE == "sql":
            app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///../test/test.db'
        if DatabaseConfig.DB_TYPE == "mongo":
            raise NotImplementedError("Testing support for mongodb has not "
                                      "yet been implemented.")
    
    @classmethod
    def tearDownClass(cls):
        '''
        Reverts any changes set in the setUpClass method back to their original value.
        '''
        # Create a separate testing database that is different from the development database.
        if DatabaseConfig.DB_TYPE == "sql":
            app.config["SQLALCHEMY_DATABASE_URI"] = assemble_sqlalchemy_url(DatabaseConfig)
        if DatabaseConfig.DB_TYPE == "mongo":
            raise NotImplementedError("Testing support for mongodb has not "
                                      "yet been implemented.")

    def setUp(self):
        '''
        Set up the application context; runs once for every test method.
        '''
        # TODO: add support for testing with mongodb here
        if DatabaseConfig.DB_TYPE == "sql":
            # Initialized empty database for testing context
            with app.app_context():
                db.create_all()
        if DatabaseConfig.DB_TYPE == "mongo":
            raise NotImplementedError("Testing support for mongodb has not "
                                      "yet been implemented.")
        # All instances of children of BaseTest have access to the test
        # client and the application context.
        self.app = app.test_client
        self.app_context = app.app_context
    
    def tearDown(self):
        '''
        Clear database when each test is finished.
        '''
        with app.app_context():
            db.session.remove()
            db.drop_all()