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


class FormDto:
    api = Namespace('form', description="Form related operations")
    form = api.model('form', {
        "form_id": fields.String(required=True, description="The ID for the form"),
        "form_name": fields.String(required=True, description="The name of the form"),
        "pages": fields.Raw(required=True, description="The list of form pages"),
        "validation_state": fields.Integer(required=True, description="The form validation state"),
        "client_id": fields.String(description="The ID of the client who owns the form"),
    })
    filled_form = api.model('filled_form', {
        "file_id": fields.String(required=True, description="The ID for the file"),
        "form_id": fields.String(required=True, description="The ID for the form"),
        "filepage_to_formpage": fields.Raw(required=True, description="Mapping of filled form page to empty form page"),
        "pages": fields.Raw(required=True, description="The list of form pages"),
        "validation_state": fields.Integer(required=True, description="The form validation state"),
        "client_id": fields.String(description="The ID of the client who owns the form"),
    })
