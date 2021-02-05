# remove() removes an element only once
pets = ['dogs', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# remove all cats from pets
while 'cat' in pets:
	pets.remove('cat')

print(pets)