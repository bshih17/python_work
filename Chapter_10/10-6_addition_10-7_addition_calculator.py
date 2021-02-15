print("Enter 'q' to quit.")
print("This program adds 2 numbers together.")

while True:
	first_number = input("\nEnter the first number: ")
	if first_number == 'q':
		break

	try:
		first_number = int(first_number)
	except:
		print("That is not a number!")
		continue

	second_number = input("Enter the second number: ")
	if second_number == 'q':
		break

	try:
		second_number = int(second_number)
	except:
		print("That is not a number!")
		continue
	else:
		print(first_number + second_number)