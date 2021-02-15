name = input("Welcome, please enter your name: ")

filename = 'guest.txt'

with open(filename, 'w') as file_object:
	file_object.write(f"Guest name: {name}")