class Restaurant:
    """This is a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe this restaurant."""
        print(f"{self.restaurant_name} is a restaurant of {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Open the restaurant"""
        print(f"Grand Opening: {self.restaurant_name} is open!")

restaurant = Restaurant('Chow Time Buffet', 'Chinese')

print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant('Las Vegas Cuban Cuisine', 'Cuban')
restaurant_2 = Restaurant('McDonalds', 'American')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()