from flask import request
from flask_restx import Resource

from ..utils.dto import EmployeeDto
from ..services.employee_service import (get_employee_by_id,
                                         get_all_employees)

from ..models.employee import Employee as EmployeeModel

api = EmployeeDto.api
_employee = EmployeeDto.employee
_new_employee = EmployeeDto.new_employee

# TODO: add argument parsing functionality. Note that Flasks's reqparse is depricated,
# so should use marshmallow or similar instead.

@api.route("",
           doc={
               "description": "A resource to get all employees or to post an employee.",
           })
class Employees(Resource):
    @api.doc('List of employees')
    @api.marshal_list_with(_employee)
    def get(self):
        return list(get_all_employees())

    @api.doc('Add employee')
    @api.expect(_new_employee, validate=True)
    @api.marshal_with(_employee, code=201)
    def post(self):
        # Get request body
        post_data = request.json
        # Create a new instance of Employee model
        new_employee = EmployeeModel(**post_data)
        # Save employee to database
        new_employee.save_to_db()
        return new_employee.json(), 201


@api.route("/<employee_id>",
           doc={
               "description": "Retreives an employee, given the employee's ID"
           })
@api.response(401, "Employee not found.")
class Employee(Resource):
    @api.doc(params={"employee_id": "The integer id assigned to the employee in the database."})
    @api.marshal_with(_employee, 200)
    def get(self, employee_id):
        if get_employee_by_id(employee_id):
            return get_employee_by_id(employee_id).json()
        return abort(401, "Employee not found.")

    
