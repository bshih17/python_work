# 6-1 Person
person = {
	'first_name': 'Donald',
	'last_name': 'Trump',
	'city': 'West Palm Beach'
}

print(f"{person['first_name']} {person['last_name']} lives in {person['city']}.\n")

person1 = {
	'first_name': 'Mr',
	'last_name': 'Anderson',
	'city': 'Lower Downtown',
}

person2 = {
	'first_name': 'Agent',
	'last_name': 'Smith',
	'city': 'The Matrix',
}

# 6-7 People
people = [person, person1, person2]

for person in people:
	full_name = f"{person['first_name']} {person['last_name']}"
	location = person['city']
	print(f"{full_name} lives in {location}.")