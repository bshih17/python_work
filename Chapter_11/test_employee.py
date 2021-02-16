import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """
        Create an employee with attributes for all test methods.
        """
        self.new_employee = Employee('John', 'Smith', 40000)
    
    def test_give_default_raise(self):
        """Test that a default raise is given."""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.annual_salary, 45000)

    def test_give_custom_raise(self):
        """Test that a custom raise is given."""
        self.new_employee.give_raise(10000)
        self.assertEqual(self.new_employee.annual_salary, 50000)
    
if __name__ == '__main__':
    unittest.main()