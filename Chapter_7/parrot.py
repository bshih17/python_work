# the argument of the input is the prompt that appears
# the function assigns the input to the variable
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# using a while loop so that the program continues until you quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

# using a flag to end a program if the flag became false
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)