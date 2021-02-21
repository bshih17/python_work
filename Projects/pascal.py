# Generate Pascal's triangle.

def get_median(string):
	"""Gets the median character in a string"""

	# int() rounds down to nearest integer

	if len(string) % 2 == 1:
		median_position = int(len(string)/2)
		median = string[median_position]

		return median

	else:
		position_1 = int(len(string)/2 - 1)
		position_2 = int(len(string)/2)

		median_1 = string[position_1]
		median_2 = string[position_2]

		median = [median_1, median_2]

		return median


print("Pascal's Triangle")

while True:
	total_rows = input("How many rows do you want? (Pascal's Triangle starts with the 0th row) ")

	try:
		total_rows = int(total_rows)
	except:
		print("That's not a whole number...")
		continue

	if total_rows == 0:
		pascal = {0: [1]}
		
		displayed_row = f"0: "

		for number in pascal[0]:
			displayed_row += f"{number}"

		print(displayed_row)

	elif total_rows == 1:
		pascal = {
			0: [1],
			1: [1,1],
			}
		
		for current_row in range(0, total_rows+1):
			displayed_row = f"{current_row}: "

			for number in pascal[current_row]:
				displayed_row += f"{number} "

			print(displayed_row)

	else:
		pascal = {
			0: [1],
			1: [1,1],
			}

		# Even row: odd numbers
		# If 8th row, then 9 numbers
		for current_row in range(2, total_rows+1):
			#        2: 1 2 1
			#       3: 1 3 3 1
			#      4: 1 4 7 4 1
			#     5: 1 5 11 11 5 1
				
			#   6: 1 6 16 22 16 6 1
			#  7: 1 7 22 38 38 22 7 1
			# 8: 1 8 29 60 76 60 29 8 1

			numbers_in_row = []  

			numbers_in_row.append(1)

			# Appending to row 8: 8, 29, 60, ...
			# Positions in row 8: 1, 2, 3, ...
			
			# Get by adding numbers from previous row: (0,1), (1,2), (2,3), ...
			# range(0,7)
			# i = 0,1,2,3,4,5,6
				
			# The issue was I had total_rows, where it should current_row...
			# To make each row, you need the previous row, so you need current_row-1.
			for i in range(0, current_row-1):
				number = pascal[current_row-1][i] + pascal[current_row-1][i+1]
				numbers_in_row.append(number)
			
			numbers_in_row.append(1)

			pascal[current_row] = numbers_in_row

		print(pascal)

		# I don't think you can store multiple lines as a single variable string.
		# So this is a method.
		# Take the dictionary that represents Pascal's Triangle, and display it as the triangle.

#		Not centered

#		for current_row in range(0, total_rows+1):
#			displayed_row = f"{current_row}: "
#		
#			for number in pascal[current_row]:
#				displayed_row += f"{number} "
#
#			print(displayed_row)


		# Centered Pascal's Triangle
		displayed_final_row = ''
		for number in pascal[total_rows]:
			displayed_final_row += f"{number} "

		half_length_final_row = int(len(displayed_final_row)/2)



		for current_row in range(0, total_rows+1):
			displayed_numbers = ''
			
			for number in pascal[current_row]:
				displayed_numbers += f"{number} "

			half_length_displayed_numbers = int(len(displayed_numbers)/2)

			spaces_needed = half_length_final_row - half_length_displayed_numbers
			spaces = ''

			for i in range(0, spaces_needed):
				spaces += " "

			displayed_row = spaces + displayed_numbers
			displayed_row = f"{current_row}: " + spaces + displayed_numbers
			

			print(displayed_row)


			
		
		

