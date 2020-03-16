from flask import abort
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from ..utils.dto import ClientDto
from ..services.client_service import get_all_clients, get_client

api = ClientDto.api
_client = ClientDto.client


@api.route("",
           doc={"description": "Retrieve a list of clients<br>Requires an Authorization Bearer Token be set with an "
                               "access token retrieved by providing client credentials to the <b>authorize</b> "
                               "endpoint.",
                "security": "accessToken"})
class Clients(Resource):
    @api.doc('list_of_clients')
    @jwt_required
    @api.marshal_list_with(_client)
    def get(self):
        return list(get_all_clients())


@api.route("/<client_id>",
           doc={"description": "Retrieve the client given the client id. <br>Requires an Authorization Bearer Token "
                               "be set with an access token retrieved by providing client credentials to the "
                               "<b>authorize</b> endpoint.",
                "security": "accessToken"})
@api.param('client_id', 'The client ID of the empty form')
@api.response(401, 'Client not found.')
class Client(Resource):
    @api.doc('client')
    @jwt_required
    @api.marshal_list_with(_client)
    def get(self, client_id):
        # Verify the client exists
        client = get_client(client_id)
        if not client:
            abort(404, 'Client not found')

        return client
