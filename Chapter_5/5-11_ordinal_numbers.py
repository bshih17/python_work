numbers = []
for value in range(1,10):
	numbers.append(value)

print(f"Numbers from 1 to 9: {numbers}")

print("Ordinal numbers:")
for number in numbers:
	if number == 1:
		print(f"{number}st")
	elif number == 2:
		print(f"{number}nd")
	elif number == 3:
		print(f"{number}rd")
	else:
		print(f"{number}th")
