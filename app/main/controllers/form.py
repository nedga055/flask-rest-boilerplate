from flask import abort
from flask_restx import Resource
from flask_jwt_extended import jwt_required

from ..utils.dto import FormDto
from ..services.auth_helper import Auth
from ..services.form_service import (
    get_all_client_forms,
    get_empty_form_images,
    get_empty_form,
    augment_forms_with_images,
    get_filled_forms,
    get_filled_form_images
)

api = FormDto.api
_form = FormDto.form
_filled_form = FormDto.filled_form


@api.route("",
           doc={"description": "Retrieve a list of forms that belong to the authenticated client.<br>Requires an "
                               "Authorization Bearer Token be set with an access token retrieved by providing client "
                               "credentials to the <b>authorize</b> endpoint.",
                "security": "accessToken"})
class Forms(Resource):
    @api.doc('list_of_forms')
    @jwt_required
    @api.marshal_list_with(_form)
    def get(self):
        # Get authorized client
        client_id = Auth.get_authenticated_client()

        forms = list(get_all_client_forms(client_id))

        # Augment forms with images for each page
        forms = augment_forms_with_images(forms, get_empty_form_images)

        # Return list of all forms for authorized client
        return forms


@api.route("/<form_id>",
           doc={"description": "Retrieve a the form given the form id. The form must belong to the authenticated"
                               "client. <br>Requires an Authorization Bearer Token be set with an access token "
                               "retrieved by providing client credentials to the <b>authorize</b> endpoint.",
                "security": "accessToken"})
@api.param('form_id', 'The form ID of the empty form')
@api.response(401, 'Form not found.')
@api.response(404, 'Not authorized to access this form')
class Form(Resource):
    @api.doc('form')
    @jwt_required
    @api.marshal_list_with(_form)
    def get(self, form_id):
        # Verify the form exists
        form = get_empty_form(form_id)
        if not form:
            abort(404, 'Form not found')

        # Get authorized client
        client_id = Auth.get_authenticated_client()

        # If the authenticated client does not own the form, return access denied
        if form.client_id != client_id:
            abort(404, 'Not authorized to access this form')

        return form


@api.route("/<form_id>/filled",
           doc={"description": "Retrieve a list of filled forms for a given form.  The form must belong to the "
                               "authenticated client.<br>Requires an Authorization Bearer Token be set with an access "
                               "token retrieved by providing client credentials to the <b>authorize</b> endpoint.",
                "security": "accessToken"})
@api.param('form_id', 'The form ID of the empty form')
@api.response(401, 'Form not found.')
@api.response(404, 'Not authorized to access this form')
class FilledForms(Resource):
    @api.doc('list_of_filled_forms')
    @jwt_required
    @api.marshal_list_with(_filled_form)
    def get(self, form_id):
        # Verify the form exists
        form = get_empty_form(form_id)
        if not form:
            abort(404, 'Form not found')

        # Get authorized client
        client_id = Auth.get_authenticated_client()

        # If the authenticated client does not own the form, return access denied
        if form.client_id != client_id:
            abort(404, 'Not authorized to access this form')

        # Get all filled forms for the given form
        filled_forms = list(get_filled_forms(form_id))

        # Augment forms with images for each page
        filled_forms = augment_forms_with_images(filled_forms, get_filled_form_images)

        # Return filled forms
        return filled_forms
