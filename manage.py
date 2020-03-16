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


# TODO: Set up testing command


if __name__ == '__main__':
    manager.run()
