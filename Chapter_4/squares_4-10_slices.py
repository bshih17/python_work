# testing
print(2**3)
print(range(1,11))

# one way
integers = list(range(1,11))
for integer in integers:
	print(integer**2)

# book solution kinda (turns out to pop up later), more concise
squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

# actual book solution
squares = []
for value in range(1,11):
	square = value **2
	squares.append(square)

print(squares)

# list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)

# 4-10 Slices
print("\nThe first three items in the list are:")
print(squares[:3])

print("Four items from the middle of the list are:")
print(squares[3:7])

print("The last three items in the list are:")
print(squares[-3:])