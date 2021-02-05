def city_country(city, country):
	"""Display the city with its country."""
	pair = print(f'"{city.title()}, {country.title()}"')
	return pair

city_country('jerusalem', 'israel')
city_country('rome', 'italy')
city_country('beijing', 'china')

# Using a dictionary, which is much more complicated
def city_country(city, country):
	"""Display the city with its country."""
	pairs = {'city': city, 'country': country}
	pair = f"{pairs['city'].title()}, {pairs['country'].title()}"

	return pair

place = city_country('jerusalem', 'israel')
print(f'"{place}"')
place = city_country('rome', 'italy')
print(f'"{place}"')
place = city_country('beijing', 'china')
print(f'"{place}"')