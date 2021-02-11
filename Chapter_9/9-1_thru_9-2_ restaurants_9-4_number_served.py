# 9-1 Restaurant
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


restaurant = Restaurant('Chow Time Buffet', 'Chinese')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-2 Three Restaurants
restaurant_1 = Restaurant('Las Vegas Cuban Cuisine', 'Cuban')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('McDonalds', 'American')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('Chipotle', 'Mexican')
restaurant_3.describe_restaurant()


# 9-4 Number Served
restaurant = Restaurant("Chick-Fil-A", "American")
restaurant.describe_restaurant()
print(f"Number of people served: {restaurant.number_served}")
restaurant.set_number_served(40)
print(f"Number of people served: {restaurant.number_served}")

restaurant.increment_number_served(5)
print(f"Number of people served: {restaurant.number_served}")