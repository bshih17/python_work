import json

filename = 'favorite_number.json'

print("Enter 'end' to end the program.\n")

while True:
	number = input("What is your favorite number? ")

	if number == 'end':
		break

	try:
		number = int(number)
		with open(filename, 'w') as f:
			json.dump(number, f)
		break

	except:
		print("That's not a number! Enter a number.\n")
		continue

