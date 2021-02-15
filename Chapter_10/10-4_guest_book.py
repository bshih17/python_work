filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
	file_object.write(f"List of Guests\n")

iteration = 0

while True:
	print("Enter 'q' to quit.")
	name = input("Hello user, please enter your name: ")

	iteration += 1

	if name == 'q':
		break
	else:
		print(f"Welcome {name}!")

		with open(filename, 'a') as file_object:
			file_object.write(f"Guest #{iteration}: {name}\n")