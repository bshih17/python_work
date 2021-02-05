cities = {
	'Spokane': {
	'country': 'the United States of America',
	'population': 217353,
	'fact': 'John G. Lake ministered in Spokane, Washington in the 1900s.'
	},
	'Thessalonica': {
	'country': 'Greece',
	'population': 315196,
	'fact': "They weren't as noble as those in Berea."
	},
	'Damascus': {
	'country': 'Syria',
	'population': 2079000,
	'fact': 'Paul met Jesus on the road to Damascus.'
	}
}

for city, info in cities.items():
	print(f"{city} is in {info['country']} "
		f"and has a population of approximately {info['population']}. "
		f"{info['fact']}")
