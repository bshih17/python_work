import json

filename = 'favorite_number.json'

try:
	with open(filename) as f:
		favorite_number = json.load(f)

except FileNotFoundError:
	print("Sorry, you haven't inputted your favorite number.")

else:
	print(f"I know your favorite number! It's {favorite_number}.")