# 9-14 Lottery
from random import randint, choice

lottery_characters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Put 4 random characters into a list.
lucky_characters = []
ticket_length = 3

for number in range(1,ticket_length+1):
	character = choice(lottery_characters)
	lucky_characters.append(character)

# Option 1 for printing
print(f"Any ticket matching these 4 numbers or letters wins $10!     {lucky_characters}")

# Option 2 for printing: turn the list into a string
lucky_combo = f"{lucky_characters[0]}"

for number in range(2,ticket_length+1):
	lucky_combo += f" - {lucky_characters[number-1]}"

print(f"\nIf you got {lucky_combo}, you win $10!")

# 9-15 Lottery Analysis
print("\nLet's analyze this lottery.\n")

my_ticket = []
iteration = 0

while my_ticket != lucky_characters:
	my_ticket = []

	# This for loop generates my 4-character lottery ticket.
	for number in range(1,ticket_length+1):
		character = choice(lottery_characters)
		my_ticket.append(character)
	
	iteration += 1
	print(f"Attempt #{iteration}: {my_ticket}")

	if my_ticket == lucky_characters:
		if iteration == 1:
			print(f"You must be a hacker! You won after {iteration} try!")
		else:
			print(f"You finally won after {iteration} tries!")



