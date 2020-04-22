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
        'ID': fields.Integer(required=True, primary_key=True, description="Identifies an employee; primary key of employees table"),
        'FirstName': fields.String(required=True, description="The employee's first name"),
        'LastName': fields.String(required=True, description="The employee's last name"),
        'Email': fields.String(required=True, description="The employee's email"),
    })
