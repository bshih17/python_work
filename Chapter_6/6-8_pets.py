pet = {
	'owner': 'Mr Anderson',
	'animal':'parrot',
	'color': 'green',
}

pet1 = {
	'owner': 'Agent Smith',
	'animal': 'german shepherd',
	'color': 'brown'
}

pet2 = {
	'owner': 'Batman',
	'animal': 'rottweiler',
	'color': 'black'
}

pet3 = {
	'owner': 'Captain',
	'animal': 'cockroach',
	'color': 'brown'
}

pets = [pet,pet1,pet2,pet3]

for pet in pets:
	print(f"{pet['owner'].title()} owns a {pet['color']} {pet['animal'].title()}.")