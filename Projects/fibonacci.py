def check_if_a_in_b(a, b):
	"""Check to see if a is in b."""
	boolean = False

	for i in range(0,len(b)):
		if a == b[i]:
			boolean = True

	return boolean


# This is a program that will tell you if a number is a Fibonacci number or not.

# Fibonacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# F_0 = 0
# F_1 = 1
# F_2 = 1
# F_3 = 2
# F_4 = 3
# F_5 = 5
# F_6 = 8
# F_7 = 13
# F_8 = 21
# F_9 = 34
# F_10 = 55

# F_n = F_n-2 + F_n-1   for   n >= 2 or n > 1

while True:
	number = input("Enter a number to find out if it is a Fibonacci number: ")

	try:
		number = int(number)
	except:
		print("That's not a whole number...\n")
		continue

# Generate a never ending list? no
# Is there a way to test the number to see if it satisfies the recurrence relation? How?
# You could generate a list just big enough to include the inputted number.

	fibonacci_sequence = [0, 1]
	i = 0

	while True:
		# 1st iteration: F_i = F_0 + F_1
		F_i = fibonacci_sequence[i] + fibonacci_sequence[i+1]
		fibonacci_sequence.append(F_i)
		i += 1

		print(fibonacci_sequence)

		if fibonacci_sequence[len(fibonacci_sequence)-1] > number:
			break

	if check_if_a_in_b(number, fibonacci_sequence):
		print(f"\nYes, {number} is a Fibonacci number!\n")
	else:
		print(f"\nNo, {number} is not a Fibonacci number!\n")

