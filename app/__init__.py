from flask_restx import Api
from flask import Blueprint

# Import namespace definitions
from .main.controllers.auth import api as auth_ns
from .main.controllers.client import api as client_ns
from .main.controllers.employee import api as employee_ns

blueprint = Blueprint('api/v1', __name__)

api = Api(blueprint,
          title="App Rest API V1",
          version="1.0",
          description="Boilerplate Flask Rest API for CDO Data Science Team projects",
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
api.add_namespace(client_ns, path='/api/v1/client')
api.add_namespace(employee_ns, path="/api/v1/employees")