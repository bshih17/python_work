filename = 'learning_python.txt'

# Read the entire file and print.
# read() makes a long string.
with open(filename) as file_object:
	print(file_object.read())

# Loop over the file object and print.
# readlines() makes a list of the lines.
# Print each line in the list.
print()

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())

# Store the lines in a list, work with them outside the with block, and print.
# readlines() makes a list of the lines.
# Combine all lines in the list into one string.
print()

with open(filename) as file_object:
	lines = file_object.readlines()

info_string = ''
for line in lines:
	info_string += f"{line.strip()} "

print(info_string.rstrip())