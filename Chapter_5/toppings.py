requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies!")

# testing multiple conditions
# this will not work if pepperoni and extra cheese are on elif
# because elif ("else if") is only considered if the if condition is false
# since all of them are if, all of them will be tested
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("Finished making your pizza!\n")

# checking for special items
# this is more concise than using if statements for each element
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")

print("Finished making your pizza!\n")

# if the pizzeria runs out of green peppers
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we've run out of green peppers for now.")
	else:
		print(f"Adding {requested_topping}.")

print("Finished making your pizza!\n")

# checking that a list is not empty
# Python will check if requested_toppings has at least 1 element
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("Finished making your pizza!\n")
else:
	print("Are you sure you want a plain pizza, sir?\n")

# using multiple lists
# if a customer wants a topping that's not available
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple','extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping} now")
	else:
		print(f"Sorry sir, we cannot add {requested_topping.title()} to your pizza...")

print(f"Finished making your pizza")



