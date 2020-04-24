from app.test.base_test import BaseTest

from app.main.services.employee_service import (get_employee_by_id, get_all_employees)
from app.main.models.employee import Employee

test_employee = Employee(
            first_name="John",
            last_name="Doe",
            email="john.doe@canada.ca",)

expected_json = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@canada.ca",}

class TestEmployeeModel(BaseTest):
    '''
    Integration tests for the Employee database model.
    '''

    def test_crud(self):
        ''' Testing CRUD operations with the Employee model. '''
        with self.app_context():
            # Confirm that database table is empty
            self.assertListEqual(get_all_employees(), [],
            "Found an employee but expected not to.")
            # Save the test employee to the database
            test_employee.save_to_db()
            # Verify that the employee was successfully added to the database.
            # Note that test_employee should be the first and only database
            # entry, so its ID is 1.
            self.assertDictEqual(get_employee_by_id(1).json(), expected_json,
            "Did not find an employee with ID 1 but expected to")
            # Delete from database
            test_employee.delete_from_db()
            # Check that the employee was successfully deleted from the database.
            self.assertIsNone(get_employee_by_id(1),
            "Found the test employee, but expected not to.")