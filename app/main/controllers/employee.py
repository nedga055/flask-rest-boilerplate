from flask import request
from flask_restx import Resource

from ..utils.dto import EmployeeDto
from ..services.employee_service import get_user_by_id, get_all_employees

from ..models.employee import Employee

api = EmployeeDto.api
_employee = EmployeeDto.employee

# TODO: add argument parsing functionality. Note that Flasks's reqparse is depricated,
# so should use marshmallow or similar instead.

@api.route("",
           doc={
               "description": "Retreive a list of employees."
           })
class Employees(Resource):
    def get(self):
        return "test"


@api.route("/<employee_id>",
           doc={
               "description": "Retreives an employee, given the employee's ID"
           })
@api.param('employee_id', 'The ID of the employee in the employees table')
class Employee(Resource):
    def get(self, employee_id):
        return "employee id is " + str(employee_id)

    def post(self):
        # Get request body
        post_data = request.json
        # Create a new instance of Employee model
        new_employee = Employee(**post_data)
        print("employee is ", new_employee)
