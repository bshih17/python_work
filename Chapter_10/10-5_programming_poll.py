filename = 'programming_poll.txt'

with open(filename, 'w') as file_object:
	file_object.write("Reasons why people like programming:\n")

while True:
	print("Enter 'quit' to end the program.")
	poll = input("Please tell me. Why do you like programming? ")

	if poll == 'quit':
		break
	else:
		with open(filename, 'a') as file_object:
			file_object.write(f"- {poll}\n")