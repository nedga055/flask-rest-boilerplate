from unittest import TestCase

from app.main.models.employee import Employee

test_employee = Employee(
            FirstName="John",
            LastName="Doe",
            Email="john.doe@canada.ca",)

class TestEmployeeModel(TestCase):
    '''
    Unit tests for the Employee database model.
    '''

    def test_init(self):
        ''' Tests that the Employee model initializes correctly. '''
        # Check that properties are correct
        self.assertEqual(test_employee.FirstName, "John")
        self.assertEqual(test_employee.LastName, "Doe")
        self.assertEqual(test_employee.Email, "john.doe@canada.ca")

    def test_json(self):
        ''' Check that the JSON representation is correct. '''
        expected_json = {
            "FirstName": "John",
            "LastName": "Doe",
            "Email": "john.doe@canada.ca",
        }
        # Check that the json method returns the correct dict
        self.assertDictEqual(expected_json, test_employee.json())