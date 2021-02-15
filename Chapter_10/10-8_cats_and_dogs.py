filenames = 'cats.txt', 'dogs.txt', 'birds.txt'

for filename in filenames:
	try:
		with open(filename, encoding='utf-8') as f:
			content = f.read()
			print(content)

	except:
		print(f"Sorry, {filename} does not exist!")