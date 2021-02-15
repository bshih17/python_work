import json

filename = 'favorite_number_remembered.json'

def get_stored_favorite_number():
	"""Get stored favorite number if available."""

	try:
		with open(filename) as f:
			favorite_number = json.load(f)

	except FileNotFoundError:
		print("Sorry, you haven't inputted your favorite number.\n")
		get_favorite_number()

	else:
		print(f"I know your favorite number! It's {favorite_number}.")
		
		choice = input("Do you want to change your favorite number? (yes/no) ")
		
		if choice == 'yes':
			get_favorite_number()
		else:
			print(f"Ok, thank you. Your favorite number is still {favorite_number}.")


def get_favorite_number():
	"""Prompt to get favorite number"""
	
	while True:
		number = input("What is your favorite number? ")

		try:
			number = int(number)
			with open(filename, 'w') as f:
				json.dump(number, f)
			return number

		except:
			print("That's not a number! Enter a number.\n")
			continue

get_stored_favorite_number()




