from flask import request, abort
from flask_restx import Resource

from ..utils.dto import ClientDto

api = ClientDto.api
_client = ClientDto.client


@api.route("")
class Client(Resource):
    def get(self):
        bp = 0
