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
            f"{self.username} and is {self.age} years old.")
    
    def greet_user(self):
        """Greet the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges():
"""A separate class just for admin privileges"""
    
    def __init__(self):
        """Initialize Privileges class and define privileges attribute."""
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can lock thread',]

    def show_privileges(self):
        """This is a method to show privileges in list form."""
        print(self.privileges)



class Admin(User):
    """This is the admin, which is a special user."""
    
    def __init__(self, first_name, last_name, username, age):
        """
        Initialize the admin with his first name, last name, and username.
        Also initialize with privileges.
        """

        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges()



special_user = Admin('John', 'Doe', 'Admin000', 10)
special_user.describe_user()
special_user.greet_user()

# self.privileges is an instance of Privileges, so it has access to every method in Privileges.
# special_user.privileges is an instance of Privileges, so it has access to show_privileges().
special_user.privileges.show_privileges()
