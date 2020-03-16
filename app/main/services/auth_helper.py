from flask_jwt_extended import create_access_token, get_jwt_identity

from ..services.client_service import get_client


class Auth:

    @staticmethod
    def authenticate_client(data):
        client_id = data.get('client_id', None)
        client_secret = data.get('client_secret', None)

        if not client_id or not client_secret:
            return {
                'status_code': '400',
                'message': 'Missing parameter'
            }

        # Get the client for the client ID provided
        client = get_client(client_id)

        # Validate the client credentials
        if client is None or client_secret != client.secret:
            return {
                'status': '401',
                'message': 'Invalid credentials'
            }

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=client_id)
        return {
            'status': '200',
            "response": {
                'access_token': access_token
            }
        }

    @staticmethod
    def get_authenticated_client():
        client_id = get_jwt_identity()
        return client_id
