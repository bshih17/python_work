dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

# You can't modify a tuple, but you can redefine it.
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)