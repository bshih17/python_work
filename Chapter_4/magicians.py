# A for loop assigns each element from first to last to magician.
# Everything indented is inside the for loop.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(f"{magician.title()}, that was a great trick!")
	print(f"I can't wait to see your nexxt trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")