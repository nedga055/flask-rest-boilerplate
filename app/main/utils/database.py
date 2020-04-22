def assemble_sqlalchemy_url(db_config):
    '''
    Assembles the URL expected by SQLAlchemy according to their documentation:
    https://docs.sqlalchemy.org/en/13/core/engines.html

    Args:
        db_config:
            A DatabaseConfig class defined in config/__init__.py.
    Returns:
        A string containing the assembled database url.
    '''
    # Unpacking config variables for readability
    dialect = db_config.DB_DIALECT
    user = db_config.DB_USER
    password = db_config.DB_PASS
    host = db_config.DB_HOST
    port = db_config.DB_PORT
    name = db_config.DB_NAME
    # If sqlite, create local database in the root of the project folder
    if dialect == 'sqlite':
        return f"sqlite:///{name}.db"
    else:
        # This url assumes the default DB API used by sqlalchemy.
        return f"{dialect}://{user}:{password}@{host}:{port}/{name}"