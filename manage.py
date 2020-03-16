from flask_script import Manager

from app.main import create_app

# Create the app
app = create_app()

# Set up the manager
manager = Manager(app)


@manager.command
def run():
    app.run()


# TODO: Set up testing command

if __name__ == '__main__':
    manager.run()
