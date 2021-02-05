prompt = "Enter 'quit' to terminate the program."
prompt += "\nWelcome to the movie theater. What is your age? "
age = ''

while age != 'quit':
	age = input(prompt)
	age = int(age)
	
	if age < 3:
		print(f"Your ticket is free because you are {age}.\n")

	elif age >= 3 and age < 12:
		print(f"Your ticket is $10 because you are {age}.\n")

	else:
		print(f"Your ticket is $15 beacuse you are {age}.\n")

