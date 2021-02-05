favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# items() method for key-value pairs
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

# keys() method for keys
print("\nKeys:")
for name in favorite_languages.keys():
	print(name.title())

print("\nPrint more if the friend is in the list:")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# looping through a dictionary's keys in a particular order
print("\nAlphabetically sorted:")
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

# values() method for values
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# sets
print("\nLanguage list with no repeats:")
for language in set(favorite_languages.values()):
	print(language.title())

# 6-6 Polling
people =  [
'bill', 'john', 'son', 'edward', 'amanda', 'amber', 'sophia', 'alexa'
	]

for person in people:
	if person in favorite_languages:
		print(f"Hello?... What are you doing...? You've already taken the poll, {person.title()}... Thanks for responding.")
	else:
		print(f"Hello?????... Take the poll please, {person.upper()}.")


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskel']
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite {len(languages)} languages are:")
	for language in languages:
		print(f"\t{language.title()}")
