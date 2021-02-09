def make_sandwich(*ingredients):
	print(f"\nMaking a sandwich for you with the following ingredients:")
	for ingredient in ingredients:
		print(f"- {ingredient}")

make_sandwich('bologne', 'cheese', 'mayonaise', 'lettuce')
make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('peanut butter', 'jelly')