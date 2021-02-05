# 6-3 Glossary
glossary = {
	'string': 'a series of characters, anything in quotes',
	'whitespace': 'any nonprinting character, such as spaces, tabs, and end-of-line symbols',
	'float': 'a decimal',
	'slice': 'a specific group of items in a list',
	'tuple': 'an immutable list',
	'Boolean': 'either true or false',
	'dictionary': 'a collection of key-value pairs',
}

print("The Glossary/Dictionary of Python Terms:\n")
for term in glossary:
	definition = glossary[term]
	print(f"{term.title()}: \n\t{definition}")

# 6-4 Glossary 2
# append to a dictionary by defining a new key to have a value
glossary['set'] = 'a collection in which each item must be unique'

print("\nThe Glossary/Dictionary of Python Terms:\n")
# sorted() works for a dictionary
for term, definition in sorted(glossary.items()):
	print(f"{term.title()}: \n\t{definition}")
