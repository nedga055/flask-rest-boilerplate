from flask import request
from flask_restx import Resource

from ..utils.dto import EmployeeDto
from ..services.employee_service import (get_employee_by_id,
                                         get_all_employees)

from ..models.employee import Employee as EmployeeModel

api = EmployeeDto.api
_employee = EmployeeDto.employee

# TODO: add argument parsing functionality. Note that Flasks's reqparse is depricated,
# so should use marshmallow or similar instead.

@api.route("",
           doc={
               "description": "Retreive a list of employees.",
           })
class Employees(Resource):
    def get(self):
        return list(get_all_employees())

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
@api.param('employee_id', 'The ID of the employee in the employees table')
class Employee(Resource):
    def get(self, employee_id):
        return get_employee_by_id(employee_id).json()

    
