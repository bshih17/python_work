class User:
    """This is a user."""

    def __init__(self, first_name, last_name, username, age):
        """Initialize user with first name and last name."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Describe user."""
        print(f"{self.first_name} {self.last_name}'s username is "
            f"{self.username}, and {self.first_name} is {self.age} years old.")
    
    def greet_user(self):
        """Greet the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges():
    """A separate class just for admin privileges"""
    
    def __init__(self, privileges):
        """Initialize Privileges class and define privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """This is a method to show privileges in list form."""
        print(f"Privileges:")
        for privileges in self.privileges:
            print(f"- {privileges}")


class Admin(User):
    """This is the admin, which is a special user."""
    
    def __init__(self, first_name, last_name, username, age, privileges):
        """
        Initialize the admin with his first name, last name, and username.
        Also initialize with privileges.
        """
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges(privileges)