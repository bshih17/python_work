filename = 'learning_python.txt'

# Read the entire file and print.
# read() makes a long string.
with open(filename) as file_object:
	entire_file = file_object.read()
	print(entire_file.replace('Python', 'C'))

# Loop over the file object and print.
# readlines() makes a list of the lines.
# Print each line in the list.
print()

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	line = line.rstrip()
	print(line.replace('Python', 'C'))

# Store the lines in a list, work with them outside the with block, and print.
# readlines() makes a list of the lines.
# Combine all lines in the list into one string.
print()

with open(filename) as file_object:
	lines = file_object.readlines()

info_string = ''
for line in lines:
	info_string += f"{line.strip()} "

info_string = info_string.rstrip()

print(info_string.replace('Python', 'C'))