pizza = {
	'crust': 'thick',
	'toppings': ['mushroom', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

# 6-12 Extensions
pizza = {
	'crust': ['thick', 'thin', 'soggy', 'rock solid'],
	'toppings': ['mushroom', 'extra cheese', 'fish', 'kimchi', 'spinach'],
	'sauce': ['garlic', 'ranch', 'oily']
}

print(f"\nHere is our full menu:")
print("Make your own pizza!")

for key, value in pizza.items():
	print(f"\n{key.title()}:")
	for value in value:
		print(f"\t{value}")

print(f"Thanks for ordering a {pizza['crust'][3]} crust "
	f"with {pizza['toppings'][3]} and {pizza['sauce'][2]} sauce.")

