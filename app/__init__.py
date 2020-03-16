from flask_restx import Api
from flask import Blueprint

blueprint = Blueprint('api/v1', __name__)

api = Api(blueprint,
          title="App Rest API V1",
          version="1.0",
          description="Boilerplate Flask Rest API for CDO Data Science Team projects"
          )

# TODO: Add namespaces
