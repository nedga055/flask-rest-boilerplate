import json

from app.main.tests.base_test import BaseTest

from app.main.services.employee_service import (get_employee_by_id, get_all_employees)
from app.main.models.employee import Employee

# Request headers
content_header = {
    "Content-Type": "application/json",
}

# Test data
test_employee = {
    "FirstName": "John",
    "LastName": "Doe",
    "Email": "john.doe@canada.ca",}


class EmployeeTest(BaseTest):
    '''
    Tests several endpoints of the employee resource.
    '''

    def test_post_employees(self):
        ''' Use case: user wants to add a new employee. '''
        with self.app() as client:
            with self.app_context():
                # User makes a GET request to /employees endpoint
                resp = client.post('/api/v1/employees',
                                   data=json.dumps(test_employee),
                                   headers=content_header,)
                # Check that employee was created successfully
                self.assertEqual(resp.status_code, 201)
    
    def test_get_employees(self):
        ''' Use case: user wants to get a list of all employees. '''
        with self.app() as client:
            with self.app_context():
                # Add a new employee to the database
                new_employee = Employee(**test_employee)
                new_employee.save_to_db()
                # User makes a request for the list of employees
                resp = client.get('/api/v1/employees')
                # Check that response is as expected
                self.assertEqual(resp.status_code, 200)
                # the /api/v1/employees endpoint returns a list, so get the (only)
                # employee at index position 0.
                self.assertEqual(json.loads(resp.data)[0], test_employee)
    
    def test_get_employee(self):
        ''' Use case: user wants to get a specific employee by their database ID. '''
        with self.app() as client:
            with self.app_context():
                # Add a new employee to the database
                new_employee = Employee(**test_employee)
                new_employee.save_to_db()
                # User makes a request for the list of employees
                resp = client.get('/api/v1/employees/1')
                # Check that response is as expected
                self.assertEqual(resp.status_code, 200)
                # the /api/v1/employees endpoint returns a list, so get the (only)
                # employee at index position 0.
                self.assertEqual(json.loads(resp.data), test_employee)