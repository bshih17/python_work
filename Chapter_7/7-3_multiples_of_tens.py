number = input("Enter a number to find out if it is a multiple of 10: ")
number = int(number)

if number % 10 == 0:
	print(f"Yes, {number} is a multiple of 10.")
else:
	print(f"No, {number} is not a multiple of 10.")