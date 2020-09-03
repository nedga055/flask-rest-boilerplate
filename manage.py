import sys

from waitress import serve

from app import blueprint
from app.main import create_app, create_manager
from app.main.config import ServerConfig

from app.test.report import Report

# Create the app
app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

# Set up the manager
manager = create_manager(app)


@manager.command
def run():
    serve(app=app, host=ServerConfig.HOST, port=ServerConfig.PORT)


@manager.command
def run_dev():
    app.run(host=ServerConfig.HOST, port=ServerConfig.PORT)


@manager.command
def test():
    ''' Runs the test suite in app/tests. '''
    # Get the report created by ObjectTestRunner
    report = Report()
    report.generate_json_report()
    report.generate_markdown_report()
    if report.TESTS_PASSED:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    manager.run()
