prompt = "Enter 'quit' to end the program."
prompt += "\nWhat topping would you like to add? "
toppings = []

while True:
	topping = input(prompt)

	if topping == 'quit':
		print(f"You have ordered a pizza with:")
		
		for topping in toppings:
			print(topping)	
				
		break

	toppings.append(topping)

	print(f"Ok, I'll add {topping}.\n")