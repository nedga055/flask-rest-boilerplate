import unittest

from app import blueprint
from app.main import create_app, create_manager

# Create the app
app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

# Set up the manager
manager = create_manager(app)


@manager.command
def run():
    app.run()


@manager.command
def test():
    ''' Runs the test suite in app/tests. '''
    tests = unittest.TestLoader().discover('app/test/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
