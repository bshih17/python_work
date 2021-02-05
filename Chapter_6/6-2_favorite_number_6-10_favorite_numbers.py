# 6-2 Favorite Number
favorite_numbers = {
	'Noah': 7,
	'Euler': 2.71828,
	'Archimedes': 3.14,
	'Moses': 10,
	'Thomas': 2,
	'David': 1,
	'Mary': 1,
}

# the key is stored in the variable "key", not the value
# this for loop seems to treat the dictionary as a list
for key in favorite_numbers:
	# slice off the last letter and store it as last_letter
	last_letter = key[-1:]

	if last_letter == 's':
		print(f"{key}' favorite number is {favorite_numbers[key]}.")
	else:
		print(f"{key}'s favorite number is {favorite_numbers[key]}.")

# 6-10 Favorite Numbers
favorite_numbers = {
	'Noah': [7,2],
	'Euler': [2.71828, 'e'],
	'Archimedes': [3.14, 'pi'],
	'Moses': [10,613],
	'Thomas': [2,12],
	'David': [1,10000],
	'Mary': [1,0]
}

print("\nMore than 1 favorite number?")
for person, number in favorite_numbers.items():
	last_letter = person[-1:]

	if last_letter == 's':
		print(f"{person}' favorite numbers are {number[0]} and {number[1]}.")
	else:
		print(f"{person}'s favorite numbers are {number[0]} and {number[1]}.")