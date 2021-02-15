filenames = 'cats.txt', 'dogs.txt', 'birds.txt'

for filename in filenames:
	try:
		with open(filename, 'r') as f:
			content = f.read()
			print(content)

	except:
		pass