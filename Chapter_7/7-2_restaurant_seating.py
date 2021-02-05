people = input(f"Welcome to Cristo's Cafe! How many people are in your group? ")
people = int(people)

if people <= 0:
	print(f"You can't have {people} people...")
elif people > 8:
	print("Sorry, we don't have a table ready right now. The wait is 20 minutes.")
else:
	print("Great! Your table is ready. Please follow me.")