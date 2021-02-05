def describe_city(city = 'athens', country = 'greece'):
	"""Display the city and the country it is in."""
	print(f"{city.title()} is in {country.title()}.")

describe_city('sparta')
describe_city('corinth')
describe_city('cairo','egypt')