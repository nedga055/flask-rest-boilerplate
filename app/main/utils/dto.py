from flask_restx import Namespace, fields


class AuthDto:
    api = Namespace('authorize', description="Authentication related operations")
    client_auth = api.model('auth_details', {
        'client_id': fields.String(required=True, description="The Client ID"),
        'client_secret': fields.String(required=True, description="The Client Secret"),
    })
    auth_resp = api.model('auth_resp', {
        'access_token': fields.String(required=True, description="The access token to be used in the Authentication "
                                                                 "header to validate subsequent requests.<br>Token "
                                                                 "expires in 24 hours")
    })


class ClientDto:
    api = Namespace('client', description="Client related operations")
    client = api.model('client', {
        'id': fields.String(required=True, description="The Client ID"),
        'name': fields.String(required=True, description="The Client name"),
        'secret': fields.String(required=True, description="The Client Secret"),
    })


class EmployeeDto:
    api = Namespace('employee', description="Employee related operations")
    employee = api.model('employee', {
        'first_name': fields.String(required=True, description="The employee's first name"),
        'last_name': fields.String(required=True, description="The employee's last name"),
        'email': fields.String(required=True, description="The employee's email"),
    })
    new_employee = api.model('new_employee', {
        'first_name': fields.String(required=True, description="The employee's first name"),
        'last_name': fields.String(required=True, description="The employee's last name"),
        'email': fields.String(required=True, description="The employee's email"),
    })