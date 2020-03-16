from flask import request, abort
from flask_restx import Resource
from ..services.auth_helper import Auth

from ..utils.dto import AuthDto

api = AuthDto.api
client_auth = AuthDto.client_auth
auth_resp = AuthDto.auth_resp


@api.route("")
@api.response(400, 'Missing parameter')
@api.response(401, 'Invalid credentials')
class ClientAuthentication(Resource):
    @api.doc('Client Authentication')
    @api.expect(client_auth, validate=True)
    @api.marshal_with(auth_resp)
    def post(self):
        # Get post data
        post_data = request.json
        auth_result = Auth.authenticate_client(post_data)

        if auth_result['status'] != '200':
            abort(auth_result['status'], auth_result['message'])

        return auth_result['response'], auth_result['status']
