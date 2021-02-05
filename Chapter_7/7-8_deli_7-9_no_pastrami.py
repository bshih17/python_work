# 7-8 Deli
sandwich_orders = ['cuban sandwich', 'cheeseburger', 'chicken sandwich']
finished_sandwiches = []

print("The Sandwich Store")

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"\nMaking your sandwich now: {current_sandwich.title()}")
	finished_sandwiches.append(current_sandwich)

	print("Sandwiches made thus far:")
	for finished_sandwich in finished_sandwiches:
		print(f"{finished_sandwich.title()}")

# 7-9 No Pastrami
sandwich_orders = ['cuban sandwich', 'cheeseburger', 'chicken sandwich',
	'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print("\nThe Sandwich Store")

print("We're sorry. We have run out of pastrami...")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"\nMaking your sandwich now: {current_sandwich.title()}")
	finished_sandwiches.append(current_sandwich)

	print("Sandwiches made thus far:")
	for finished_sandwich in finished_sandwiches:
		print(f"{finished_sandwich.title()}")
