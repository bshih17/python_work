rivers = {
	'nile': 'egypt',
	'mississippi': 'the united states of america',
	'huang he': 'china'
}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

print("\nList of 3 major rivers:")
for river in rivers:
	print(river.title())

print("\nList of 3 countries with have major rivers:")
for country in rivers.values():
	print(country.title())