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
