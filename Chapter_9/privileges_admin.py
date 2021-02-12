from user import User

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