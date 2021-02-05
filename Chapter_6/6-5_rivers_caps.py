articles = ['a', 'an', 'the']
prepositions = ['of']
conjunctions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
apc = articles + prepositions + conjunctions

rivers = {
	'nile': 'egypt',
	'mississippi': 'the united states of america',
	'huang he': 'china'
}
# Where are the spaces?
print(f"Where are the spaces in {rivers['mississippi']}?")
usa = rivers['mississippi']
for i in range(0,len(usa)):
	if usa[i] == ' ':
		print(i)

for river, country in rivers.items():
# How do I take the string 'the united states of america' and break it up into 5 strings?
# string[x] = character in position x of string
	print("\nITERATION:")
	# Create these here, so that they can be modified during the for loop.
	# These must be placed here, so that they will be reset for each item in the dictionary.
	x = 0
	current_country = country + ' '
	current_title = ''

	print(f"Current country: {current_country}; Length of current country: {len(current_country)}")
	# go through each character in current_country from beginning to the end
	for i in range(0,len(current_country)):
		if current_country[i] == ' ':
			# slices starts at x+1 (letter after space), stops before i (space), thus ending with i-1
			# 1st iteration (of finding the space) slices the 1st word
			word = current_country[x:i]
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

	print(f"Title capitalization: {current_title.strip()}")
		

	
	print(f"The {river.title()} runs through {current_title.strip()}.")