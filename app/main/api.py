# -*- coding: utf-8 -*-
"""API entry point

@author: Nick Edgar
"""
import click
from flask import Flask, Blueprint
from flask_restx import Api
from flask_jwt_extended import JWTManager
from mongoengine import connect

# Import namespace definitions
from mart.controllers.auth import api as auth_ns
from mart.controllers.form import api as form_ns

# Import app config
from mart import config
from mart.config import DB_HOST, DB_USER, DB_PASS

# Import service helpers
from mart.services.client_service import create_client

# Initialize app
app = Flask(__name__)
app.secret_key = config.SECRET_KEY

# Connect DB
db_host_info = DB_HOST.split(':')
connect(
    db='MaRT',
    host=db_host_info[0],
    port=int(db_host_info[1]),
    username=DB_USER,
    password=DB_PASS
)

# Initialize JWT authorization
app.config['JWT_SECRET_KEY'] = config.SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 24 * 60 * 60
jwt = JWTManager(app)

# Create API Blueprint
blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          title="MaRT API",
          version="1.0",
          description="Restful API for the MaRT application",
          authorizations={
              'accessToken': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization',
                  'tokenUrl': '/access_token',
                  'description': 'Use the access token after the keyword <b>Bearer</b>'
              }
          })

# Add namespaces
api.add_namespace(auth_ns)
api.add_namespace(form_ns, path='/api/v1/form')

# Register API blueprint
app.register_blueprint(blueprint)

app.app_context().push()


@app.cli.command("create-client")
@click.argument("name")
def create_new_client(name):
    client = create_client(name)
    print(f"Details for client {name} - client_id: {client.id}, client_secret: {client.secret} ")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
