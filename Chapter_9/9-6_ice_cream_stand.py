class Restaurant:
    """This is a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe this restaurant."""
        print(f"{self.restaurant_name} is a restaurant of {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"GRAND OPENING: {self.restaurant_name} is NOW OPEN!")

    def set_number_served(self, number_served):
        """Number of people served"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant, specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """
        Initialize the child class with attributes of the parent class.
        Then initialize attributes of the ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Display the flavors available."""
        print("Flavors we currently have:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")

ice_cream_stand = IceCreamStand('Your Local Ice Cream Stand')
ice_cream_stand.flavors = ['chocolate', 'vanilla', 'pistachio']

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()