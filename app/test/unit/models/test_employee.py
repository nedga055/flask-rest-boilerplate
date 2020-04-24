from unittest import TestCase

from app.main.models.employee import Employee

test_employee = Employee(
            first_name="John",
            last_name="Doe",
            email="john.doe@canada.ca",)

class TestEmployeeModel(TestCase):
    '''
    Unit tests for the Employee database model.
    '''

    def test_init(self):
        ''' Tests that the Employee model initializes correctly. '''
        # Check that properties are correct
        self.assertEqual(test_employee.first_name, "John")
        self.assertEqual(test_employee.last_name, "Doe")
        self.assertEqual(test_employee.email, "john.doe@canada.ca")

    def test_json(self):
        ''' Check that the JSON representation is correct. '''
        expected_json = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@canada.ca",
        }
        # Check that the json method returns the correct dict
        self.assertDictEqual(expected_json, test_employee.json())