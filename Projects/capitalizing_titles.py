# Add more if necessary.
articles = ['a', 'an', 'the']
prepositions = ['of']
conjunctions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
apc = articles + prepositions + conjunctions

country = 'ThE uNiTeD sTaTeS oF aMeRiCa'

# Define x to be used later. x will be replaced multiple times.
x = 0
current_title = ''

# Add a space to the end of country, so that the last word can be sliced.
country = country.lower() + ' '

# position 0 is t, position 28 is space
print(f"Country: {country}; Length of country: {len(country)}; characters go from 0 to {len(country)-1}")
for i in range(0,len(country)):
	if country[i] == ' ':
		# slices starts at x+1 (letter after space), stops before i (space), thus ending with i-1
		# 1st iteration (of finding the space) slices the 1st word
		word = country[x:i]
		# to slice from the letter after the space, that would i+1
		# NOW redefine x so that during the 2nd iteration (of finding the space), it will start slice from the 1st letter of 2nd word
		x = i+1

		# adding capitalization, adding space
		if word not in apc:
			title_word = word.title() + ' '
		else:
			title_word = word + ' '

		# ADDING to current title, NOT REPLACING
		current_title = current_title + title_word

current_title = current_title.strip()

print(current_title)
print(f"We live in {current_title}.")