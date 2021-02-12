# 9-13 Dice
from random import randint

class Die:
	"""Simulate a die roll."""

	def __init__(self, sides=6):
		"""Initiate the die."""
		self.sides = sides

	def roll_die(self):
		"""Roll the die."""
		self.roll = randint(1, self.sides)
		

# 6-sided die
# How do I save the number for every roll?
die6 = Die()
rolls = []

for number in range (1,11):
	die6.roll_die()
	rolls.append(die6.roll)

print(f"10 rolls for a {die6.sides}-sided die: {rolls}")

# 10-sided die
die10 = Die(10)
rolls = []

for number in range (1,11):
	die10.roll_die()
	rolls.append(die10.roll)

print(f"\n10 rolls for a {die10.sides}-sided die: {rolls}")

# 20-sided die
die20 = Die(20)
rolls = []

for number in range (1,11):
	die20.roll_die()
	rolls.append(die20.roll)

print(f"\n10 rolls for a {die20.sides}-sided die: {rolls}")