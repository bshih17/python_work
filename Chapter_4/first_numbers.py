# range() causes Python to stop counting at 5, so it doesn't get to print it.
for value in range(1,5):
	print(value)

# range() here prints from 0 to 5.
for value in range(6):
	print(value)

numbers = list(range(1,6))
print(numbers)
