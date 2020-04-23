from unittest import TestCase

from app.main.utils.database import assemble_sqlalchemy_url

class TestDatabaseUtils(TestCase):
    '''
    A collection of unit tests for various database utilities
    '''

    def test_assemble_url(self):
        '''
        Checks that the assemble url function for SQLAlchemy works as expected.
        '''
        # Define a config class similar to that in app/main/config/__init__.py with
        # fixed values so that the test doesn't fail when the config changes.
        class PostgresDatabaseConfig:    
            DB_TYPE = "sql"
            DB_HOST = "localhost"
            DB_DIALECT = "postgresql"
            DB_PORT = 5432
            DB_NAME = "test_database"
            DB_USER = "john.doe"
            DB_PASS = "changeMe"
        
        class SQLiteDatabaseConfig:    
            DB_TYPE = "sql"
            DB_HOST = "localhost"
            DB_DIALECT = "sqlite"
            DB_PORT = 5432
            DB_NAME = "test_database"
            DB_USER = "john.doe"
            DB_PASS = "changeMe"
        
        # Define some expected results
        expected_sqlite_url = "sqlite:///test_database.db"
        expected_postgres_url = "postgresql://john.doe:changeMe@localhost:5432/test_database"

        # Generate actual urls for the two configs
        actual_sqlite_url = assemble_sqlalchemy_url(SQLiteDatabaseConfig)
        actual_postgres_url = assemble_sqlalchemy_url(PostgresDatabaseConfig)

        # Test that urls match
        self.assertEqual(expected_sqlite_url, actual_sqlite_url)
        self.assertEqual(expected_postgres_url, actual_postgres_url)