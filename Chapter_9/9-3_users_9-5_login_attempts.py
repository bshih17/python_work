# 9-3 Users
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

user_0 = User('Hooligan', 'Jones', 'HooluhginJonez', 26)
user_0.describe_user()
user_0.greet_user()

user_1 = User('Luke', 'Skywalker', 'JediMaster123', 53)
user_1.describe_user()
user_1.greet_user()

user_2 = User('Thomas', 'Anderson', 'Neo', 20)
user_2.describe_user()
user_2.greet_user()

# 9-5 Login Attempts
new_user = User('Thunder', 'Bolt', 'Pikachu', 10)
new_user.increment_login_attempts()
print(f"Login attempts: {new_user.login_attempts}")
new_user.increment_login_attempts()
print(f"Login attempts: {new_user.login_attempts}")
new_user.increment_login_attempts()
print(f"Login attempts: {new_user.login_attempts}")
print("You have exhausted all your login attempts. Please wait 10,000 days to try again.")

new_user.reset_login_attempts()
print(f"Resetting login attempts: {new_user.login_attempts}")
