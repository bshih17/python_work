class Employee:
    """This is an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee with his first and last name and his annual salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Give raise of a default of $5,000 or of your choice."""
        self.annual_salary += raise_amount

    def show_stats(self):
        print(f"Employee: {self.first_name} {self.last_name}")
        print(f"Annual Salary: ${self.annual_salary}")
